__author__ = 'MarceloM Guzman'

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from resources.methods.UIMethods import is_element_present, click_element
from resources.uiabstraction.components.widgets.fileactionstoolbar.FileActionsToolbarBase import FileActionsToolbarBase
from resources.uiabstraction.components.widgets.foldercontent.FolderContentMarquee import FolderContentMarquee


class FileActionsToolbarMarquee(FileActionsToolbarBase):
    """
    Page object modeling the structure and operations of the File Actions Toolbar page for Marquee template.
    """

    # Selectors
    _short_view_mode = (By.XPATH, "//button[@type='button' and @class='btn btn-default short']")
    _short_view_mode_selected = (By.XPATH, "//button[@class='btn btn-default short active']")
    _list_view_mode = (By.XPATH, "//button[@type='button' and @class='btn btn-default list']")
    _list_view_mode_selected = (By.XPATH, "//button[@class='btn btn-default list active']")
    _actions_button = (By.XPATH, "//button[@type='button' and @class='btn btn-default toggle buttons']")
    _actions_button_selected = (By.XPATH, "//button[@class='btn btn-default toggle buttons active']")
    _dates_button = (By.XPATH, "//button[@type='button' and @class='btn btn-default toggle dates']")
    _dates_button_selected = (By.XPATH, "//button[@class='btn btn-default toggle dates active']")
    _details_button = (By.XPATH, "//span/button[contains(@class,'keywords')]")

    def __init__(self):
        """
        Constructor
        """
        FileActionsToolbarBase.__init__(self, "Marquee")
        
    def select_short_view_mode_in_toolbar(self):
        """
        Selects the Short View mode.
        """
        try:
            self._driver.find_element(*self._short_view_mode).click()
            self._wait.until(ec.visibility_of_element_located(self._short_view_mode_selected))
            self._folder_content.wait_for_folder_content_page_loaded()
        except NoSuchElementException:
            print "The 'Short View'  mode is already selected."

    def select_list_view_mode_in_toolbar(self):
        """
        Selects the List View mode.
        """
        try:
            self._wait.until(ec.element_to_be_clickable(self._list_view_mode))
            self._driver.find_element(*self._list_view_mode).click()
            self._wait.until(ec.visibility_of_element_located(self._list_view_mode_selected))
            while not is_element_present(self._driver, *FolderContentMarquee().list_view):
                self._driver.find_element(*self._list_view_mode_selected).click()
                self._folder_content.wait_for_folder_content_page_loaded()
        except Exception as ex:
            print ex  # TODO: Delete these lines after XIN-6081 is fixed
            self._driver.find_element(*self._list_view_mode_selected).click()
            self._folder_content.wait_for_folder_content_page_loaded()
            while not is_element_present(self._driver, *FolderContentMarquee().list_view):
                self._driver.find_element(*self._list_view_mode_selected).click()
                self._folder_content.wait_for_folder_content_page_loaded()
                print "The 'List View'  mode is already selected."

    def select_actions_button_in_toolbar(self):
        """
        Selects the Actions button.
        """
        try:
            self._driver.find_element(*self._actions_button).click()
            self._wait.until(ec.visibility_of_element_located(self._actions_button_selected))
            self._folder_content.wait_for_folder_content_page_loaded()
        except NoSuchElementException:
            print "The 'Actions' button is already selected."
    
    def select_dates_button_in_toolbar(self):
        """
        Selects the Dates button.
        """
        try:
            self._driver.find_element(*self._dates_button).click()
            self._wait.until(ec.visibility_of_element_located(self._dates_button_selected))
            self._folder_content.wait_for_folder_content_page_loaded()
        except NoSuchElementException:
            print "The 'Dates' button is already selected."

    def select_details_button_in_toolbar(self):
        """
        Selects the Details button.
        """
        try:
            if is_element_present(self._driver, *self._details_button):
                click_element(self._driver, self._driver.find_element(*self._details_button))
        except NoSuchElementException:
                print "The 'Details' button is already selected."
    
    def _create_folder_content(self):
        return FolderContentMarquee()
