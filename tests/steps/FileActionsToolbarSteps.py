__author__ = 'MarceloM Guzman'

from resources.commons.GlobalVariables import TEMPLATE
from resources.uiabstraction.PageObjectFactory import PageObjectFactory

class FileActionsToolbarSteps:
    """
    Steps definition for FileActionsToolbar page object.
    """
    _file_actions_toolbar = None

    def __init__(self):
        self._file_actions_toolbar = PageObjectFactory.create_file_actions_toolbar(TEMPLATE)

    def click_view_mode(self):
        """
        Clicks the View icon.
        """
        self._file_actions_toolbar.click_view_mode()

    def select_icon_view_mode_in_toolbar(self):
        """
        Selects the Icon View mode.
        """
        self._file_actions_toolbar.select_icon_view_mode_in_toolbar()

    def select_short_view_mode_in_toolbar(self):
        """
        Selects the Short View mode.
        """
        self._file_actions_toolbar.select_short_view_mode_in_toolbar()

    def select_list_view_mode_in_toolbar(self):
        """
        Selects the List View mode. (Marquee template)
        """
        self._file_actions_toolbar.select_list_view_mode_in_toolbar()

    def select_long_view_mode_in_toolbar(self):
        """
        Selects the Long View mode. (Exhibit template)
        """
        self._file_actions_toolbar.select_long_view_mode_in_toolbar()

    def select_actions_button_in_toolbar(self):
        """
        Selects the Actions button.
        """
        self._file_actions_toolbar.select_actions_button_in_toolbar()

    def select_dates_button_in_toolbar(self):
        """
        Selects the Dates button.
        """
        self._file_actions_toolbar.select_dates_button_in_toolbar()

    def select_details_button_in_toolbar(self):
        """
        Selects the Details button.
        """
        self._file_actions_toolbar.select_details_button_in_toolbar()

    def select_images_quantity_in_toolbar(self, quantity):
        """
        Select the images quantity in 'Display per page' combo box
        """
        self._file_actions_toolbar.select_images_quantity_in_toolbar(quantity)
