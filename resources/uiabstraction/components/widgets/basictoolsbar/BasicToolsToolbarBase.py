__author__ = 'MarceloM Guzman'

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from resources.commons.DriverManager import DriverManager
from resources.methods.UIMethods import wait_for_load_page


class BasicToolsToolbarBase(object):
    """
    Page object modeling the structure and operations of the Basic Tools Toolbar page.
    """
    _driver = None
    _wait = None

    # Selectors
    _sign_in_button = (By.XPATH, "//button[@type='submit']")
    
    def __init__(self, theme):
        self._driver = DriverManager().get_instance().get_driver()
        self._wait = DriverManager().get_instance().get_wait()
        self.theme = theme
        
    def click_user_widget_button(self):
        """
        Clicks the user_widget button.
        """
        return self
    
    def click_home_button(self):
        """
        Clicks the Home button.
        """
        return self
    
    def click_logout_link(self):
        """
        Clicks the Logout link.
        """
        return self

    def click_basket_button(self):
        """
        Clicks the Basket button.
        """
        basket_button_selector = self.basket_button_locator_template
        collection_pane_displayed_selector = self.collection_pane_selected_template
        self._wait.until(ec.visibility_of_element_located(basket_button_selector), "The Basket button is not available to be clicked")
        self._driver.find_element(*basket_button_selector).click()
        wait_for_load_page()
        self._wait.until(ec.visibility_of_element_located(collection_pane_displayed_selector), "The Collection pane is not displayed")
        return self._basket_page()

    def click_upload_button(self):
        """
        Clicks the Upload button.
        """
        return self

    def logout_from_portal(self):
        """
        Logs out from the portal and closes the browser.
        """
        try:
            self.click_logout_link()
        except NoSuchElementException:
            print "The 'Logout' link is not displayed."
        finally:
            self._driver.quit()

    def is_home_page_displayed(self):
        """
        Verifies if the Home button is displayed
        """
        return self

    def _basket_page(self):
        """
        Gets the Basket page returned.
        """
        raise NotImplementedError()
