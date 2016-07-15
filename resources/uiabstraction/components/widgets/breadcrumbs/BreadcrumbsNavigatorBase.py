__author__ = 'MarceloM Guzman'

from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By

from resources.commons.DriverManager import DriverManager
from resources.methods.UIMethods import is_element_present


class BreadcrumbsNavigatorBase(object):
    """
    Page object modeling the structure and operations of the Breadcrumbs navigator.
    """
    _driver = None
    _wait = None
    _folder_content = None

    def __init__(self, theme):
        self._driver = DriverManager().get_instance().get_driver()
        self._wait = DriverManager().get_instance().get_wait()
        self.theme = theme
        self._folder_content = self._create_folder_content()

    def click_folder_link_in_breadcrumbs(self, folder_name):
        """
        Clicks the folder name link given in ``folder_name`` argument.
        """
        if folder_name == 'Return to Browse' and self.theme.lower() == "marquee":
            folder_name_selector = (By.XPATH, "//a[@title='"+folder_name+"']")
        else:
            folder_name_selector = (By.XPATH, self.folder_locator_template % folder_name)
        self._driver.find_element(*folder_name_selector).click()
        self._folder_content.wait_for_folder_content_page_loaded()

    def is_folder_link_displayed_in_breadcrumbs(self, folder_name):
        """
        Returns True if the folder name link given in ``folder_name`` is displayed in Breadcrumbs, otherwise False.
        """
        folder_name_selector = (By.XPATH, self.folder_locator_template % folder_name)
        return is_element_present(self._driver, *folder_name_selector)
    
    def verify_if_folder_link_is_displayed_in_breadcrumbs(self, folder_name):
        """
        Verifies if the folder name link given in ``folder_name`` is displayed in Breadcrumbs.
        """
        BuiltIn().should_be_true(self.is_folder_link_displayed_in_breadcrumbs(folder_name))

    def verify_if_folder_link_is_not_displayed_in_breadcrumbs(self, folder_name):
        """
        Verifies if the folder name link given in ``folder_name`` is displayed in Breadcrumbs.
        """
        BuiltIn().should_not_be_true(self.is_folder_link_displayed_in_breadcrumbs(folder_name))
        
    def _create_folder_content(self):
        raise NotImplementedError()
