__author__ = 'MarceloM Guzman'

from resources.commons.DriverManager import DriverManager


class FileActionsToolbarBase(object):
    """
    Page object modeling the structure and operations of the File Actions Toolbar page.
    """
    _driver = None
    _wait = None
    _folder_content = None

    def __init__(self, theme):
        self._driver = DriverManager().get_instance().get_driver()
        self._wait = DriverManager().get_instance().get_wait()
        self.theme = theme
        self._folder_content = self._create_folder_content()
        
    def click_view_mode(self):
        """
        Clicks the View icon.
        """
        return self
    
    def select_icon_view_mode_in_toolbar(self):
        """
        Selects the Icon View mode.
        """
        return self
    
    def select_short_view_mode_in_toolbar(self):
        """
        Selects the Short View mode.
        """
        return self

    def select_list_view_mode_in_toolbar(self):
        """
        Selects the List View mode.
        """
        return self
    
    def select_long_view_mode_in_toolbar(self):
        """
        Selects the Long View mode.
        """
        return self
    
    def select_actions_button_in_toolbar(self):
        """
        Selects the Actions button.
        """
        return self
    
    def select_dates_button_in_toolbar(self):
        """
        Selects the Dates button.
        """
        return self
    
    def select_details_button_in_toolbar(self):
        """
        Selects the Details button.
        """
        return self
    
    def _create_folder_content(self):
        raise NotImplementedError()
