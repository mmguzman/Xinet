__author__ = 'MarceloM Guzman'

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from resources.methods.UIMethods import is_element_present, click_element, scroll_click_element
from resources.uiabstraction.components.widgets.foldercontent.FolderContentExhibit import FolderContentExhibit
from resources.uiabstraction.components.widgets.sidepane.SidePaneNavigatorBase import SidePaneNavigatorBase


class SidePaneNavigatorExhibit(SidePaneNavigatorBase):
    """
    Page object modeling the structure and operations of the Side Pane navigator for Exhibit template.
    """

    # Selectors
    _navigator_link = (By.XPATH, "//li[@id='navigatortab' and @class='']/a/small[.='Navigator']")
    _navigator_table = (By.XPATH, "//form[@id='navigator_table']")

    def __init__(self):
        SidePaneNavigatorBase.__init__(self, "Exhibit")
        self.folder_locator_template = "//a[contains(@title,'%s')]"
        self.is_folder_revealed_locator_template = "//ul[@id='navlist']/descendant::a[@class='filename' and @title='%s']"
        self.folder_breadcrumbs_template = "//div[@id='navcrumbs']/a[contains(text(),'%s')]"
    
    def expand_folder(self, folder_name):
        """
        Expands the folder given in ``folder_name`` argument.
        """
        down_arrow_selector = (By.XPATH, "//a[contains(@title,'" + folder_name + "')]/preceding-sibling::a[@title='Open']")
        up_arrow_selector = (By.XPATH, "//a[@title='" + folder_name + "']/preceding-sibling::a[@title='Close']")
        try:
            self._wait.until(ec.element_to_be_clickable(down_arrow_selector))
            click_element(self._driver, self._driver.find_element(*down_arrow_selector))
            self._wait.until(ec.visibility_of_element_located(up_arrow_selector))
            self._folder_content.wait_for_folder_content_page_loaded()
            if not is_element_present(self._driver, *up_arrow_selector):
                click_element(self._driver, self._driver.find_element(*down_arrow_selector))
                self._wait.until(ec.visibility_of_element_located(up_arrow_selector))
                self._folder_content.wait_for_folder_content_page_loaded()
        except NoSuchElementException:
            print "The " + folder_name + " folder is already expanded."

    def scroll_and_expand_folder(self, folder_name):
        """
        Scrolls until find the ``folder_name`` and expands the folder given in ``folder_name`` argument.
        :param folder_name: The folder to expand.
        """
        down_arrow_selector = (By.XPATH, "//a[contains(@title,'" + folder_name + "')]/preceding-sibling::a[@title='Open']")
        up_arrow_selector = (By.XPATH, "//a[@title='" + folder_name + "']/preceding-sibling::a[@title='Close']")
        try:
            self._wait.until(ec.element_to_be_clickable(down_arrow_selector))
            scroll_click_element(self._driver, self._driver.find_element(*down_arrow_selector))
            self._wait.until(ec.visibility_of_element_located(up_arrow_selector))
            self._folder_content.wait_for_folder_content_page_loaded()
        except NoSuchElementException:
            print "The " + folder_name + " folder is already expanded."

    def collapse_folder(self, folder_name):
        """
        Collapses the folder given in ``folder_name`` argument.
        """
        right_arrow_selector = (By.XPATH, "//a[@title='" + folder_name + "']/preceding-sibling::a[@title='Open']")
        try:
            up_arrow_selector = (By.XPATH, "//a[@title='" + folder_name + "']/preceding-sibling::a[@title='Close']")
            self._wait.until(ec.element_to_be_clickable(up_arrow_selector))
            click_element(self._driver, self._driver.find_element(*up_arrow_selector))
            self._wait.until(ec.visibility_of_element_located(right_arrow_selector))
            self._folder_content.wait_for_folder_content_page_loaded()
            if not is_element_present(self._driver, *right_arrow_selector):
                click_element(self._driver, self._driver.find_element(*up_arrow_selector))
                self._wait.until(ec.visibility_of_element_located(right_arrow_selector))
                self._folder_content.wait_for_folder_content_page_loaded()
        except (NoSuchElementException, TimeoutException):
            print "The " + folder_name + " folder is already collapsed."
    
    def _create_folder_content(self):
        return FolderContentExhibit()
    
    def click_navigator_link(self):
        """
        Clicks the navigator link.
        """
        if is_element_present(self._driver, *self._navigator_link):
            self._driver.find_element(*self._navigator_link).click()
            self._wait.until(ec.visibility_of_element_located(self._navigator_table))
