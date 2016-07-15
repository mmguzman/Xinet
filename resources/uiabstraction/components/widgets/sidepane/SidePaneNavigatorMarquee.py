__author__ = 'MarceloM Guzman'

import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from resources.methods.UIMethods import click_element, scroll_click_element
from resources.uiabstraction.components.widgets.foldercontent.FolderContentMarquee import FolderContentMarquee
from resources.uiabstraction.components.widgets.sidepane.SidePaneNavigatorBase import SidePaneNavigatorBase


class SidePaneNavigatorMarquee(SidePaneNavigatorBase):
    """
    Page object modeling the structure and operations of the Side Pane navigator for Marquee template.
    """

    def __init__(self):
        SidePaneNavigatorBase.__init__(self, "Marquee")
        self.folder_locator_template = "//a/span[starts-with(text(),'%s')]"
        self.is_folder_revealed_locator_template = "//a/span[contains(text(),'%s')]"
        self.folder_breadcrumbs_template = "//ol[@class='breadcrumb']/li/a[contains(text(),'%s')]"

    def expand_folder(self, folder_name):
        """
        Expands the folder given in ``folder_name`` argument.
        """
        down_arrow_selector = (By.XPATH, "//a/span[contains(text(),'" + folder_name + "')]/preceding-sibling::span[contains(@class,'chevron-right')]")
        up_arrow_selector = (By.XPATH, "//a/span[contains(text(),'" + folder_name + "')]/preceding-sibling::span[contains(@class,'chevron-down')]")
        try:
            element = lambda: self._driver.find_element(*down_arrow_selector)
            element().click()
            self._wait.until(ec.visibility_of_element_located(up_arrow_selector))
            time.sleep(4)
        except NoSuchElementException:
            print "The " + folder_name + " folder is already expanded."

    def scroll_and_expand_folder(self, folder_name):
        """
        Scrolls until find the ``folder_name`` and expands the folder given in ``folder_name`` argument.
        :param folder_name: The folder to expand.
        """
        down_arrow_selector = (By.XPATH, "//a/span[contains(text(),'" + folder_name + "')]/preceding-sibling::span[contains(@class,'chevron-right')]")
        up_arrow_selector = (By.XPATH, "//a/span[contains(text(),'" + folder_name + "')]/preceding-sibling::span[contains(@class,'chevron-down')]")
        try:
            scroll_click_element(self._driver, self._driver.find_element(*down_arrow_selector))
            self._wait.until(ec.visibility_of_element_located(up_arrow_selector))
            time.sleep(4)
        except NoSuchElementException:
            print "The " + folder_name + " folder is already expanded."

    def collapse_folder(self, folder_name):
        """
        Collapses the folder given in ``folder_name`` argument.
        """
        try:
            up_arrow_selector = (By.XPATH, "//a/span[contains(text(),'" + folder_name + "')]/preceding-sibling::span[contains(@class,'chevron-down')]")
            down_arrow_selector = (By.XPATH, "//a/span[contains(text(),'" + folder_name + "')]/preceding-sibling::span[contains(@class,'chevron-right')]")
            click_element(self._driver, self._driver.find_element(*up_arrow_selector))
            self._wait.until(ec.visibility_of_element_located(down_arrow_selector))
            self._folder_content.wait_for_folder_content_page_loaded()
        except (NoSuchElementException, TimeoutException):
            print "The " + folder_name + " folder is already collapsed."
        return self
    
    def _create_folder_content(self):
        return FolderContentMarquee()
