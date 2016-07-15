__author__ = 'MarceloM Guzman'

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from resources.methods.UIMethods import is_element_present, click_element
from resources.uiabstraction.components.widgets.basictoolsbar.BasicToolsToolbarBase import BasicToolsToolbarBase
from resources.uiabstraction.components.widgets.basket.BasketExhibit import BasketExhibit


class BasicToolsToolbarExhibit(BasicToolsToolbarBase):
    """
    Page object modeling the structure and operations of the Basic Tools Toolbar page for Exhibit template.
    """

    # Selectors
    _logout_button = (By.XPATH, "//a[contains(@title,'Logout')]")
    _upload_button = (By.XPATH, "//a[@title='Upload Files']")
    _upload_file_indicator = (By.ID, "uploadindicatoroff0")
    _top_level_link = (By.XPATH, "//a[contains(@title,'Top Level')]")
    _file_list = (By.ID, "filelist")

    def __init__(self):
        BasicToolsToolbarBase.__init__(self, "Exhibit")
        self.basket_button_locator_template = (By.XPATH, "//a[@title='Show Basket']")
        self.collection_pane_selected_template = (By.ID, "clearbasket")
        
    def click_logout_link(self):
        """
        Clicks the Logout link.
        """
        if self.is_home_page_displayed():
            self._driver.find_element(*self._logout_button).click()
            self._wait.until(ec.invisibility_of_element_located(self._logout_button))

    def click_upload_button(self):
        """
        Clicks the Upload button.
        """
        click_element(self._driver, self._driver.find_element(*self._upload_button))
        self._wait.until(ec.visibility_of_element_located(self._upload_file_indicator), "The Upload container is not displayed")

    def is_home_page_displayed(self):
        """
        Verifies if the Home page is displayed.
        :return: True if displayed, otherwise False.
        """
        return is_element_present(self._driver, *self._top_level_link)

    def _basket_page(self):
        """
        Gets the Basket page returned.
        """
        return BasketExhibit()
    
    def click_folder_link_in_breadcrumbs(self, folder_name):
        """
        Clicks the folder name link given in ``folder_name`` argument.
        :param folder_name: The link name to select on Breadcrumbs, e.g. 2015 Bare Bones Test Files.
        """
        select_link = (By.XPATH, "//a[text()='" + folder_name + "']")
        self._wait.until(ec.element_to_be_clickable(select_link))
        click_element(self._driver, self._driver.find_element(*select_link))
        self._wait.until(ec.visibility_of_element_located(self._file_list))
