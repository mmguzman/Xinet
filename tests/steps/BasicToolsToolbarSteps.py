__author__ = 'MarceloM Guzman'

from resources.commons.GlobalVariables import TEMPLATE
from resources.uiabstraction.PageObjectFactory import PageObjectFactory


class BasicToolsToolbarSteps:
    """
    Steps definition for Basic Tools toolbar page object.
    """
    _basic_tools_toolbar = None

    def __init__(self):
        self._basic_tools_toolbar = PageObjectFactory.create_basic_tools_toolbar(TEMPLATE)

    def click_user_widget_button(self):
        """
        Clicks the user_widget button.
        """
        self._basic_tools_toolbar.click_user_widget_button()
        return self

    def click_logout_link(self):
        """
        Clicks the Logout link.
        """
        self._basic_tools_toolbar.click_logout_link()
        return self

    def click_home_button(self):
        """
        Clicks the Home button.
        """
        self._basic_tools_toolbar.click_home_button()
        return self

    def click_basket_button(self):
        """
        Clicks the Basket button.
        """
        self._basic_tools_toolbar.click_basket_button()

    def click_upload_button(self):
        """
        Clicks the Upload button.
        """
        self._basic_tools_toolbar.click_upload_button()

    def logout_from_portal(self):
        """
        Logs out from the portal and closes the browser.
        """
        self._basic_tools_toolbar.logout_from_portal()
        return self
