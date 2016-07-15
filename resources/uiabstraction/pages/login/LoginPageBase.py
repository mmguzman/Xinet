__author__ = 'MarceloM Guzman'

from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from resources.commons.DriverManager import DriverManager
from resources.methods.UIMethods import is_element_present


class LoginPageBase(object):
    """
    Page object modeling the structure and operations of the Portal LoginPageBase page.
    """
    _driver = None
    _wait = None

    # Selectors
    _username_input = (By.NAME, "username")
    _password_input = (By.NAME, "password")
    _sign_in_button = (By.XPATH, "//button[@type='submit']")
    _xinet_image = (By.XPATH, "//img[@alt='WebNative']")

    def __init__(self, theme):
        self._driver = DriverManager().get_instance().get_driver()
        self._wait = DriverManager().get_instance().get_wait()
        self.theme = theme

    def open_url(self, url):
        """
        Opens the browser with Xinet Portal.
        :param url: URL of the Xinet server.
        """
        self._driver.get(url)
        return self

    def _set_username(self, username):
        """
        Sets the User Name.
        """
        self._driver.find_element(*self._username_input).clear()
        self._driver.find_element(*self._username_input).send_keys(username)
        return self

    def _set_password(self, password):
        """
        Sets the User Password.
        """
        self._driver.find_element(*self._password_input).clear()
        self._driver.find_element(*self._password_input).send_keys(password)
        return self

    def set_user_credentials(self, username, password):
        """
        Sets user name and password values.
        :param username: User name.
        :param password: Password.
        """
        self._set_username(username)
        self._set_password(password)

    def _click_sign_in_button(self):
        """
        Clicks the Sign In button.
        """
        self._driver.find_element(*self._sign_in_button).click()
        self._wait.until(ec.title_contains(self.page_title), "The page does not contain the " + self.page_title + " title.")
        return self

    def _click_sign_in_button_error(self):
        """
        Clicks the Sign In button.
        """
        self._driver.find_element(*self._sign_in_button).click()
        return self

    def login_to_portal(self, portal_ip, server_ip, username, password):
        """
        Sets the given credentials and clicks in Sign In button.
        :param portal_ip: IP Address of Portal server.
        :param server_ip: IP Address of Xinet server.
        :param username: user name
        :param password: password
        :return: Home page.
        """
        xinet_site_url = "http://" + portal_ip + "/" + server_ip.split(".")[3] + self.theme.lower()
        self.open_url(xinet_site_url)
        if is_element_present(self._driver, *self._username_input):
            self.set_user_credentials(username, password)
            self._click_sign_in_button()
        return self._home_page()
    
    def login_to_portal_invalid_credentials(self, username, password):
        """
        Sets the credentials and clicks Sign In button.
        :param username: user name
        :param password: password
        """
        self.set_user_credentials(username, password)
        self._click_sign_in_button_error()

    def _home_page(self):
        """
        Gets the Home page returned after login.
        """
        raise NotImplementedError()

    def is_error_displayed_login_page(self):
        """
        Verifies if an error is displayed in Login page.
        :return: Returns True if the error is displayed.
        """
        error_message_selector = (By.XPATH, self.error_message_template)
        return is_element_present(self._driver, *error_message_selector)

    def verify_if_error_message_is_displayed_in_login_page(self):
        """
        Verifies if an error message is displayed in Login page.
        """
        BuiltIn().should_be_true(self.is_error_displayed_login_page())
