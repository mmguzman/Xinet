__author__ = 'MarceloM Guzman'

from resources.commons.GlobalVariables import TEMPLATE
from resources.uiabstraction.PageObjectFactory import PageObjectFactory


class LoginSteps:
    """
    Steps definition for Login page object.
    """
    _login = None

    def __init__(self):
        self._login = PageObjectFactory.create_login(TEMPLATE)

    def login_to_portal(self, portal_ip, server_ip, username, password):
        """
        Sets the given credentials and clicks in Sign In button.
        :param portal_ip: IP Address of Portal server.
        :param server_ip: IP Address of Xinet server.
        :param username: user name
        :param password: password
        :return: Home page.
        """
        self._login.login_to_portal(portal_ip, server_ip, username, password)
    
    def login_to_portal_invalid_credentials(self, username, password):
        """
        Sets the credentials and clicks Sign In button and stays in the same page.
        :param username: user name
        :param password: password
        """
        self._login.login_to_portal_invalid_credentials(username, password)

    def verify_if_error_message_is_displayed_in_login_page(self):
        """
        Verifies if an error message is displayed in Login page.
        """
        self._login.verify_if_error_message_is_displayed_in_login_page()
