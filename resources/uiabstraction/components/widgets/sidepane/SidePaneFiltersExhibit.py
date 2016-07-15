__author__ = 'Edmundo Cossio'

from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from resources.uiabstraction.components.widgets.foldercontent.FolderContentExhibit import FolderContentExhibit
from resources.uiabstraction.components.widgets.sidepane.SidePaneFiltersBase import SidePaneFiltersBase
from resources.uiabstraction.components.widgets.sidepane.SidePaneNavigatorExhibit import SidePaneNavigatorExhibit


class SidePaneFiltersExhibit(SidePaneFiltersBase):
    """
    Page object modeling the structure and operations of the Side Pane filters for Exhibit template.
    """

    # Selectors
    _2nd_range_in_filters = (By.XPATH, "//li/descendant::small[contains(.,'xwnv:facet_')]/../../following-sibling::li/descendant::ul[@class='facets_ul']/li[2]/descendant::small")
    _filters_link = (By.XPATH, "//a/small[text()='Filters']")
    _file_list = (By.ID, "filelist")
    
    def __init__(self):
        SidePaneFiltersBase.__init__(self, "Exhibit")
    
    def verify_if_metadata_is_configured_according_to_bucket_size(self, expected_range):
        """
        Verifies if the metadata is configured according to bucket size(e.g. auto mode)
        :param expected_range: The expected range.
        """
        actual_2nd_range_in_filters = self._driver.find_element(*self._2nd_range_in_filters).text
        BuiltIn().should_be_true(expected_range in actual_2nd_range_in_filters)
        SidePaneNavigatorExhibit().click_navigator_link()
    
    def verify_if_file_is_displayed_in_folder_content(self, file_name):
        """
        Verify if file is displayed in folder content.
        :param file_name: The file.
        """
        BuiltIn().should_be_true(FolderContentExhibit().is_file_displayed_in_folder_content(file_name))
    
    def is_expected_range_displayed_in_filters(self, expected_range):
        """
        Verify if expected range is displayed in filters tab.
        :param expected_range: The expected range.
        """
        for count_id in range(1, 6):
            range_locator = (By.XPATH, "//li/descendant::small[contains(.,'xwnv:facet_')]/../../following-sibling::li/descendant::ul[@class='facets_ul']/li[" + str(count_id) + "]/descendant::small")
            actual_range_in_filters = self._driver.find_element(*range_locator).text
            if expected_range in actual_range_in_filters:
                return True
        return False
    
    def verify_if_expected_range_is_displayed_in_filters(self, expected_range):
        """
        Verify if expected range is displayed in filters tab.
        :param expected_range: The expected range.
        """
        BuiltIn().should_be_true(self.is_expected_range_displayed_in_filters(expected_range))
    
    def verify_there_is_one_range_for_file_list(self, files):
        """
        Verifies if there is one range for file list into a folder(e.g. Big-Integer Folder)
        :param files:The list of files into a folder.
        """
        for file_name in files:
            self.verify_if_file_is_displayed_in_folder_content(file_name)
            self.verify_if_expected_range_is_displayed_in_filters(self.get_individual_range_expected(file_name))
    
    def expand_filters_link_in_side_pane(self):
        """
        Expands the filters link in side pane.
        """
        self._wait.until(ec.element_to_be_clickable(self._filters_link)).click()
        self._wait.until(ec.visibility_of_element_located(self._file_list))
    
    def verify_if_range_is_displayed_in_filters_tab_according_to_bucket_size(self, range_expected_in_filters):
        """
        Verifies if a range is displayed in filters tab according to bucket size
        :param range_expected_in_filters: The range expected in the Filters tab.
        """
        BuiltIn().should_be_true(range_expected_in_filters in self._driver.find_element(*self._2nd_range_in_filters).text)
    
    def type_file_name_in_filters(self, file_name):
        """
        Types a file name in the filters tab according to the data field (e.g. file name=16.indd and data field=Integer).
        :param file_name: The file name.
        """
        self._wait.until(ec.visibility_of_element_located(self._data_field_text))
        self._driver.find_element(*self._data_field_text).clear()
        self._driver.find_element(*self._data_field_text).send_keys(file_name)
    
    def click_go_in_filters(self):
        """
        Clicks go in the filters tab.
        """
        self._wait.until(ec.element_to_be_clickable(self._go_button)).click()
        self._wait.until(ec.visibility_of_element_located(self._file_list))
