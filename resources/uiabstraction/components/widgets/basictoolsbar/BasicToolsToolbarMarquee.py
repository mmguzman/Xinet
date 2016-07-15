__author__ = 'MarceloM Guzman'

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from resources.methods.UIMethods import is_element_present, click_element
from resources.uiabstraction.components.widgets.basictoolsbar.BasicToolsToolbarBase import BasicToolsToolbarBase
from resources.uiabstraction.components.widgets.basket.BasketMarquee import BasketMarquee


class BasicToolsToolbarMarquee(BasicToolsToolbarBase):
    """
    Page object modeling the structure and operations of the Basic Tools Toolbar page for Marquee template.
    """

    # Selectors
    _user_widget_button = (By.ID, "userwidget-addon1")
    _home_button = (By.XPATH, "//span[@class='glyphicons glyphicons-home']")
    _logout_button = (By.XPATH, "//span[@class='glyphicons glyphicons-exit']")
    _upload_button = (By.XPATH, "//span[@class='glyphicons glyphicons-cloud-upload']")
    _volumes_container = (By.XPATH, "//div[@class='volume pull-left']")
    _sign_in_button = (By.XPATH, "//button[@type='submit']")

    _file_modal = (By.ID, "myModalLabel")

    def __init__(self):
        BasicToolsToolbarBase.__init__(self, "Marquee")
        self.basket_button_locator_template = (By.XPATH, "//span[@class='glyphicons glyphicons-shopping-cart']")
        self.collection_pane_selected_template = (By.ID, "pluginspanel")

    def click_user_widget_button(self):
        """
        Clicks the user_widget button.
        """
        self._driver.find_element(*self._user_widget_button).click()
        self._wait.until(ec.visibility_of_element_located(self._logout_button), "The Logout link is not displayed")
    
    def click_logout_link(self):
        """
        Clicks the Logout link.
        """
        if self.is_home_page_displayed():
            self.click_user_widget_button()
            self._driver.find_element(*self._logout_button).click()
            self._wait.until(ec.visibility_of_element_located(self._sign_in_button))
    
    def click_home_button(self):
        """
        Clicks the Home button.
        """
        click_element(self._driver, self._driver.find_element(*self._home_button))
        self._wait.until(ec.visibility_of_element_located(self._volumes_container), "The Volumes container is not displayed")

    def click_upload_button(self):
        """
        Clicks the Upload button.
        """
        click_element(self._driver, self._driver.find_element(*self._upload_button))
        self._wait.until(ec.visibility_of_element_located(self._file_modal), "The Upload container is not displayed")

    def is_home_page_displayed(self):
        """
        Verifies if the Home button is displayed
        :return: True if displayed, otherwise False.
        """
        return is_element_present(self._driver, *self._home_button)

    def _basket_page(self):
        """
        Gets the Basket page returned.
        """
        return BasketMarquee()
