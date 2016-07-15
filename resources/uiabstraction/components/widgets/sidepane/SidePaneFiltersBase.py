__author__ = 'Edmundo Cossio'

from selenium.webdriver.common.by import By

from resources.commons.DriverManager import DriverManager
from resources.methods.UIMethods import is_element_present


class SidePaneFiltersBase(object):
    """
    Page object modeling the structure and operations of the Side Pane filters.
    """
    _driver = None
    _wait = None
    
    # Selectors
    _data_field_text = (By.XPATH, "//input[@type='number']")
    _go_button = (By.XPATH, "//input[@type='number']/following-sibling::button[@class='btn btn-default']")

    def __init__(self, theme):
        self._driver = DriverManager().get_instance().get_driver()
        self._wait = DriverManager().get_instance().get_wait()
        self.theme = theme
    
    def verify_if_metadata_is_configured_according_to_bucket_size(self, expected_range):
        """
        Verifies if the metadata is configured according to bucket size(e.g. auto mode)
        :param expected_range: The expected range.
        """
        return self
    
    def verify_there_is_one_range_for_file_list(self, files):
        """
        Verifies if there is one range for file list into a folder(e.g. Big-Integer Folder)
        :param files: The list of files into a folder.
        """
        return self
    
    def expand_filters_link_in_side_pane(self):
        """
        Expands the filters link in side pane.
        """
        return self
    
    def verify_if_range_is_displayed_in_filters_tab_according_to_bucket_size(self, range_expected_in_filters):
        """
        Verifies if a range is displayed in filters tab according to bucket size
        :param range_expected_in_filters: The range expected in the Filters tab.
        """
        return self
    
    def type_file_name_in_filters(self, file_name):
        """
        Types a file name in the filters tab according to data field (e.g. file name=16.indd and data field=Integer).
        :param file_name: The file name.
        """
        return self
    
    def click_go_in_filters(self):
        """
        Clicks go in the filters tab.
        """
        return self
        
    def is_range_according_to_bucket_size_configured(self, range_to_verify):
        """
        Verifies if the range is according to bucket size configured (e.g. bucket size = 'auto mode').
        :param range_to_verify: The range to verify.
        :return: True if displayed, otherwise False.
        """
        if is_element_present(self._driver, *range_to_verify):
            return True
        return False
    
    def get_individual_range_expected(self, file_name):
        """
        Gets the individual range expected according to the file.
        :param file_name: The file.
        :return: An individual range.
        """
        expected_range = file_name.split(".indd")[0]
        if expected_range.startswith("-."):
            expected_range = expected_range.replace("-.", "-0.")
        return expected_range
    
    def collapse_filters_link_in_side_pane(self):
        """
        Collapses the filters link in side pane.
        """
        return self
    
    def expand_folder_for_xwnvfacet(self, data_field):
        """
        Expands folder for xwnv Facet in the filters tab.
        :param data_field: The data field e.g. Integer.
        """
        return self
