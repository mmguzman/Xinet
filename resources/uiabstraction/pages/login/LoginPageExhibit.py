__author__ = 'MarceloM Guzman'

from resources.uiabstraction.pages.home.HomeExhibit import HomeExhibit
from resources.uiabstraction.pages.login.LoginPageBase import LoginPageBase


class LoginPageExhibit(LoginPageBase):
    """
    Page object modeling the structure and operations of the Portal LoginPageBase page for Exhibit template.
    """
    def __init__(self):
        LoginPageBase.__init__(self, "robotExhibit")
        self.page_title = "Available Volumes"
        self.error_message_template = "//div[@class='errormsg']"

    def _home_page(self):
        """
        Gets the Home page returned after login.
        """
        return HomeExhibit()
