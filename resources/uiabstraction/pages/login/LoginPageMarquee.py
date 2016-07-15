__author__ = 'MarceloM Guzman'

from resources.uiabstraction.pages.home.HomeMarquee import HomeMarquee
from resources.uiabstraction.pages.login.LoginPageBase import LoginPageBase


class LoginPageMarquee(LoginPageBase):
    """
    Page object modeling the structure and operations of the Portal LoginPageBase page for Marquee template.
    """
    def __init__(self):
        LoginPageBase.__init__(self, "robotMarquee")
        self.page_title = "Welcome to Marquee"
        self.error_message_template = "//div[@class='alert alert-danger']"
    
    def _home_page(self):
        """
        Gets the HomeMarquee page returned after login.
        """
        return HomeMarquee()
