__author__ = 'MarceloM Guzman'

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from resources.commons.DriverManager import DriverManager
from resources.methods.UIMethods import is_element_present
from resources.uiabstraction.pages.login import LoginPageBase
from resources.uiabstraction.pages.portaladmin.PortalAdminHome import PortalAdminHome


class PortalAdminAuthentication:
    """
    Page object modeling the structure and operations of the Portal Administration page.
    """
    _driver = None
    _wait = None

    # Selectors
    _password_input = (By.NAME, "password")
    _server_textbox = (By.NAME, "WNHOSTNAME")
    _port_textbox = (By.NAME, "WNHOSTPORT")
    _submit_button = (By.XPATH, "//input[@value='Submit']")
    _site_manager_link = (By.LINK_TEXT, "Site Manager")

    def __init__(self):
        self._driver = DriverManager().get_instance().get_driver()
        self._wait = DriverManager().get_instance().get_wait()

    def _set_password(self, password):
        """
        Sets the User Password.
        """
        self._driver.find_element(*self._password_input).clear()
        self._driver.find_element(*self._password_input).send_keys(password)

    def _click_submit_button(self):
        """
        Clicks the Submit button.
        """
        self._driver.find_element(*self._submit_button).click()

    def login_to_portal_administration(self, portal_ip, server_ip, password):
        """
        Sets the given credentials and clicks in Sign In button.
        Returns the Portal Admin Home page.
        """
        portal_admin_url = "http://" + portal_ip + "/PORTALADMIN"
        login = LoginPageBase.LoginPageBase(self)
        login.open_url(portal_admin_url)
        self.configure_server_values(server_ip)
        self._set_password(password)
        self._click_submit_button()
        self._wait.until(ec.visibility_of_element_located(self._site_manager_link))
        return PortalAdminHome()

    def set_server_address(self, server_ip):
        """
        Sets the Xinet server default value.
        :param server_ip: The server ip address.
        """
        self._driver.find_element(*self._server_textbox).clear()
        self._driver.find_element(*self._server_textbox).send_keys(server_ip)

    def set_port_number(self, port_number):
        """
        Sets the Port default value.
        :param port_number: The port number.
        """
        self._driver.find_element(*self._port_textbox).clear()
        self._driver.find_element(*self._port_textbox).send_keys(port_number)

    def configure_server_values(self, server_ip, port=80):
        """
        Configures Xinet default server and port.
        :param server_ip: The server ip address.
        :param port: The port number.
        """
        if is_element_present(self._driver, *self._server_textbox):
            self.set_server_address(server_ip)
            self.set_port_number(port)

    def add_new_site(self, portal_ip, portal_admin_password, server_ip, template):
        """
        Set values to add a new site.
        """
        portal_admin_home_page = self.login_to_portal_administration(portal_ip, server_ip, portal_admin_password)
        site_manager = portal_admin_home_page.click_site_manager_link()
        site_already_created = site_manager.is_already_displayed_in_sites_list(server_ip, template)
        if site_already_created:
            site_manager.remove_site(server_ip, template)
        add_site = site_manager.click_add_site_link()
        configuration = add_site.create_new_site(server_ip, template)
        configuration.set_server_host(server_ip)
        configuration.click_submit_button()
        configuration.verify_if_the_changes_saved_message_is_displayed()
