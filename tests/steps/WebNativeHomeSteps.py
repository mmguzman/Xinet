__author__ = 'MarceloM Guzman'

from resources.uiabstraction.PageObjectFactory import PageObjectFactory


class WebNativeHomeSteps:
    """
    Steps definition for WebNative page object.
    """
    _webnative_home = None

    def __init__(self):
        self._webnative_home = PageObjectFactory.create_webnative_home()

    def login_to_webnative(self, server_ip, username, password):
        """
        Sets the given credentials and logs in to WebNative administration.
        """
        self._webnative_home.login_to_webnative(server_ip, username, password)
        
    def click_volumes_users_link(self):
        """
        Clicks the 'Volumes/Users' link.
        """
        self._webnative_home.click_volumes_users_link()
        
    def click_database_link(self):
        """
        Clicks the 'Database' link.
        """
        self._webnative_home.click_database_link()
        
    def click_print_hot_folder(self):
        """
        Clicks the 'Print/Hot Folder' link.
        """
        self._webnative_home.click_print_hot_folder()
        
    def close_browser(self):
        """
        Closes the browser.
        """
        self._webnative_home.close_browser()
    
    def fill_credentials(self, username, password):
        """
        Sets username and password.
        """
        self._webnative_home.fill_credentials(username, password)
    
    def clear_browsing_data(self):
        """
        Clears the browser data if the navigator is chrome.
        """
        self._webnative_home.clear_browsing_data()

    def select_language_encoding(self, language_type):
        """
         Selects the language encoding.
        """
        self._webnative_home.select_language_encoding(language_type)
    
    def click_logging_link(self):
        """
        Clicks the 'Logging' link.
        """
        self._webnative_home.click_logging_link()
