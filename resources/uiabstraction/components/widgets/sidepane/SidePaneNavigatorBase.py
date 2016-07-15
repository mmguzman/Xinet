__author__ = 'MarceloM Guzman'

import time

from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from resources.commons.DriverManager import DriverManager
from resources.methods.DBMethods import get_folder_content
from resources.methods.UIMethods import is_element_present, click_element


class SidePaneNavigatorBase(object):
    """
    Page object modeling the structure and operations of the Side Pane navigator.
    """
    _driver = None
    _wait = None
    _folder_content = None

    def __init__(self, theme):
        self._driver = DriverManager().get_instance().get_driver()
        self._wait = DriverManager().get_instance().get_wait()
        self.theme = theme
        self._folder_content = self._create_folder_content()

    def click_folder_link(self, folder_name):
        """
        Clicks the folder name given in ``folder_name`` argument.
        """
        folder_name_selector = (By.XPATH, self.folder_locator_template % folder_name)
        # self._wait.until(ec.visibility_of_element_located(folder_name_selector), "The " + folder_name + " folder is not available to be clicked")
        self._wait.until(ec.element_to_be_clickable(folder_name_selector), "The " + folder_name + " folder is not available to be clicked")
        click_element(self._driver, self._driver.find_element(*folder_name_selector))
        folder_breadcrumbs_selector = (By.XPATH, self.folder_breadcrumbs_template % folder_name)
        self._folder_content.wait_for_folder_content_page_loaded()
        time.sleep(3)
        self._wait.until(ec.visibility_of_element_located(folder_breadcrumbs_selector))

    def click_folder_link_by_path(self, folder_path):
        """
        Clicks the folder path given in ``folder_path`` argument.
        """
        for folder in folder_path:
            self.click_folder_link(folder)

    def expand_folder(self, folder_name):
        """
        Expands the folder given in ``folder_name`` argument.
        """
        return self
    
    def expand_folder_by_path(self, folder_path):
        """
        Expands the folder path given in ``folder_path`` argument.
        :param folder_path: A list of folders path. e.g. karina_wnv  2015 Bare Bones Test Files  Images
        """
        for folder in folder_path:
            self.expand_folder(folder)

    def scroll_and_expand_folder(self, folder_name):
        """
        Scrolls until find the ``folder_name`` and expands the folder given in ``folder_name`` argument.
        :param folder_name: The folder to expand.
        """
        return self

    def scroll_and_expand_folder_by_path(self, folder_path):
        """
        Scrolls and expands the folder path given in ``folder_path`` argument.
        """
        for folder in folder_path:
            self.scroll_and_expand_folder(folder)

    def collapse_folder(self, folder_name):
        """
        Collapses the folder given in ``folder_name`` argument.
        """
        return self
    
    def is_folder_revealed_under_parent_folder(self, folder_name):
        """
        Returns True if the folder given in ``folder_name`` argument is revealed below the parent folder
        in the side pane, otherwise False.
        """
        folder_name_selector = (By.XPATH, self.is_folder_revealed_locator_template % folder_name)
        return is_element_present(self._driver, *folder_name_selector)
    
    def is_folder_content_revealed_under_parent_folder(self, folder_path, folder_name):
        """
        Returns True if all the folders and files that belongs to a folder are revealed
        below the parent folder in the side pane, otherwise False.
        The folder is identified by the given ``folder_path`` and ``folder_name`` arguments.
        """
        folder_content_list = get_folder_content(folder_path, folder_name)
        is_revealed = None
        
        for folder in folder_content_list:
            is_revealed = self.is_folder_revealed_under_parent_folder(folder[0])
            if not is_revealed:
                break
        return is_revealed
    
    def is_folder_content_revealed_under_parent_folder_only_folders(self, folder_path, folder_name):
        """
        Returns True if all the folders and files that belongs to a folder are revealed
        below the parent folder in the side pane, otherwise False.
        The folder is identified by the given ``folder_path`` and ``folder_name`` arguments.
        """
        folder_content_list = get_folder_content(folder_path, folder_name)
        is_revealed = None
        for folder in folder_content_list:
            length = len(folder[0])
            if length > 4:
                if folder[0][-4] != ".":  # Verifying if the element is a file (has a suffix)
                    is_revealed = self.is_folder_revealed_under_parent_folder(folder[0])
                    if not is_revealed:
                        break
            else:
                    is_revealed = self.is_folder_revealed_under_parent_folder(folder[0])
                    if not is_revealed:
                        break
        return is_revealed
    
    def verify_if_folder_content_is_revealed_under_parent_folder(self, folder_path, folder_name):
        """
        Verifies if all the folders and files that belongs to a folder are revealed
        below the parent folder in the side pane.
        The folder is identified by the given ``folder_path`` and ``folder_name`` arguments.
        """
        BuiltIn().should_be_true(self.is_folder_content_revealed_under_parent_folder(folder_path, folder_name))
        
    def verify_if_folder_content_is_not_revealed_under_parent_folder(self, folder_path, folder_name):
        """
        Verifies if the folders and files that belongs to a folder are not revealed
        below the parent folder in the side pane.
        The folder is identified by the given ``folder_path`` and ``folder_name`` arguments.
        """
        BuiltIn().should_not_be_true(self.is_folder_content_revealed_under_parent_folder(folder_path, folder_name))
        
    def verify_if_folder_content_is_revealed_under_parent_folder_only_folders(self, folder_path, folder_name):
        """
        Verifies if all the folders that belongs to a folder are revealed below the parent folder 
        in the side pane.
        The folder is identified by the given ``folder_path`` and ``folder_name`` arguments.
        """
        BuiltIn().should_be_true(self.is_folder_content_revealed_under_parent_folder_only_folders(folder_path, folder_name))
        
    def is_folder_link_selected(self, folder_name):
        """
        Returns True if the folder name given in ``folder_name`` argument is selected in the side pane,
        otherwise False.
        """
        folder_name_selector = (By.XPATH, "//li[@id='navigator_selected']/a[@class='filename' and contains(@title,'" + folder_name + "')]")
        return is_element_present(self._driver, *folder_name_selector)
    
    def verify_if_folder_link_is_selected(self, folder_name):
        """
        Verifies if the folder name given in ``folder_name`` argument is selected in the side pane.
        """
        BuiltIn().should_be_true(self.is_folder_link_selected(folder_name))

    def _create_folder_content(self):
        raise NotImplementedError()
    
    def click_navigator_link(self):
        """
        Clicks the navigator link.
        """
        return self
