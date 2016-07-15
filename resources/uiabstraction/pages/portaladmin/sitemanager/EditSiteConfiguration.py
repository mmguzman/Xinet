__author__ = 'Edmundo Cossio'

from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from resources.commons.DriverManager import DriverManager


class EditSiteConfiguration(object):
    """
    Page object modeling the structure and operations of the Edit Site Configuration page.
    """
    _driver = None
    _wait = None
    
    # Selectors
    _submit_button = (By.NAME, "siteChange")
    _address_input = (By.NAME, "WNHOSTNAME[]")
    _port_input = (By.NAME, "WNHOSTPORT[]")
    
    _changes_saved_span = (By.XPATH, "//span[text()='* Changes saved']")
    
    def __init__(self):
        self._driver = DriverManager().get_instance().get_driver()
        self._wait = DriverManager().get_instance().get_wait()

    def set_server_host(self, address, port=80):
        """
        Sets the server host with address and port.
        """
        self._driver.find_element(*self._address_input).clear()
        self._driver.find_element(*self._address_input).send_keys(address)
        self._driver.find_element(*self._port_input).clear()
        self._driver.find_element(*self._port_input).send_keys(port)

    def click_submit_button(self):
        """
        Clicks Submit button.
        """
        self._driver.find_element(*self._submit_button).click()
        self._wait.until(ec.visibility_of_element_located(self._changes_saved_span))
        
    def verify_if_the_changes_saved_message_is_displayed(self):
        """
        Verifies if the '* Changes saved' message is displayed.
        """
        is_message_displayed = self._driver.find_element(*self._changes_saved_span).is_displayed()
        BuiltIn().should_be_true(is_message_displayed)
