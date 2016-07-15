__author__ = 'MarceloM Guzman'

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select

from resources.methods.UIMethods import is_element_present
from resources.uiabstraction.components.widgets.fileactionstoolbar.FileActionsToolbarBase import FileActionsToolbarBase
from resources.uiabstraction.components.widgets.foldercontent.FolderContentExhibit import FolderContentExhibit


class FileActionsToolbarExhibit(FileActionsToolbarBase):
    """
    Page object modeling the structure and operations of the File Actions Toolbar page for Exhibit template.
    """
    # Selectors
    _view_mode = (By.XPATH, "//a[@title='View']")
    _view_options = (By.ID, "viewoptions")
    _icon_view_mode = (By.XPATH, "//a[@title='Icon View']")
    _short_view_mode = (By.XPATH, "//a[@title='Short View']")
    _long_view_mode = (By.XPATH, "//a[@title='Long View']")
    _options_button = (By.XPATH, "//a[@title='Options']")
    _tools_options = (By.ID, "toolsoptions")
    _display_per_page_combo_box = (By.XPATH, "//select[@name='show_rows']")
    
    _icon_view_selected = (By.XPATH, "//a[contains(@class,'icon_icon_view_on')]")
    _short_view_selected = (By.XPATH, "//a[contains(@class,'icon_short_view_on')]")
    _long_view_selected = (By.XPATH, "//a[contains(@class,'icon_long_view_on')]")
    
    _tech_info = (By.XPATH, "//div[@class='techinfo']")
    
    def __init__(self):
        FileActionsToolbarBase.__init__(self, "Exhibit")

    def click_view_mode(self):
        """
        Clicks the View icon.
        """
        try:
            self._driver.find_element(*self._view_mode).click()
            self._wait.until(ec.element_to_be_clickable(self._view_options))
        except Exception as e:
            print "Problem:" + str(e)
            self._driver.find_element(*self._view_mode).click()
            self._wait.until(ec.element_to_be_clickable(self._view_options))
    
    def click_icon_view_mode(self):
        """
        Clicks the Icon view. 
        """
        self._driver.find_element(*self._icon_view_mode).click()
        self._folder_content.wait_for_folder_content_page_loaded()
    
    def select_icon_view_mode_in_toolbar(self):
        """
        Selects the Icon View mode.
        """
        self._wait.until(ec.element_to_be_clickable(self._view_mode))
        if not is_element_present(self._driver, *self._icon_view_selected):
            self.click_view_mode()
            self.click_icon_view_mode()
            if not is_element_present(self._driver, *self._icon_view_selected):
                self.click_view_mode()
                self.click_icon_view_mode()
     
    def click_short_view_mode(self):
        """
        Clicks the short view.
        """
        try:
            self._driver.find_element(*self._short_view_mode).click()
            self._folder_content.wait_for_folder_content_page_loaded()
        except Exception as e:
            print "Problem:" + str(e)
            self._driver.find_element(*self._short_view_mode).click()
            self._folder_content.wait_for_folder_content_page_loaded()
        
    def select_short_view_mode_in_toolbar(self):
        """
        Selects the Short View mode.
        """
        self._wait.until(ec.element_to_be_clickable(self._view_mode))
        if not is_element_present(self._driver, *self._short_view_selected):
            self.click_view_mode()
            self.click_short_view_mode()
            if not is_element_present(self._driver, *self._short_view_selected):
                self.click_view_mode()
                self.click_short_view_mode()
    
    def click_long_view_mode(self):
        """
        Clicks the long view mode
        """
        self._driver.find_element(*self._long_view_mode).click()
        self._folder_content.wait_for_folder_content_page_loaded()
        self._wait.until(ec.visibility_of_element_located(self._tech_info))
    
    def select_long_view_mode_in_toolbar(self):
        """
        Selects the Long View mode.
        """
        self._wait.until(ec.element_to_be_clickable(self._view_mode))
        if not is_element_present(self._driver, *self._long_view_selected):
            self.click_view_mode()
            self.click_long_view_mode()
            if not is_element_present(self._driver, *self._long_view_selected):
                self.click_view_mode()
                self.click_long_view_mode()
    
    def click_options_button(self):
        """
        Clicks the Options button.
        """
        self._wait.until(ec.element_to_be_clickable(self._options_button))
        element = lambda: self._driver.find_element(*self._options_button)
        element().click()
        self._wait.until(ec.element_to_be_clickable(self._tools_options))
        if not self._driver.find_element(*self._tools_options).is_displayed():
            element().click()
            self._wait.until(ec.element_to_be_clickable(self._tools_options))
    
    def select_images_quantity_in_toolbar(self, quantity):
        """
        Select the images quantity in 'Display per page' combo box
        """
        self.click_options_button()
        Select(self._driver.find_element(*self._display_per_page_combo_box)).select_by_visible_text(quantity + " Images")
        try:
            self._wait.until(ec.invisibility_of_element_located(self._tools_options))
        except Exception as e:
            print "Problem type:Exception \nArgs: " + str(e)
        self._folder_content.wait_for_folder_content_page_loaded()
    
    def _create_folder_content(self):
        return FolderContentExhibit()
