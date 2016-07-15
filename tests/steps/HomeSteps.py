__author__ = 'MarceloM Guzman'

from resources.commons.GlobalVariables import TEMPLATE
from resources.uiabstraction.PageObjectFactory import PageObjectFactory


class HomeSteps:
    """
    Steps definition for Home page object.
    """
    _home = None

    def __init__(self):
        self._home = PageObjectFactory.create_home(TEMPLATE)

    def select_volume(self, folder_name):
        """
        Clicks the browse folder name given in ``folder_name`` argument.
        :param folder_name: volume name to select.
        """
        self._home.select_volume(folder_name)
        
    def back_to_home(self):
        """
        Returns to Home page
        """
        self._home.back_to_home()

    def verify_if_volume_is_displayed(self, volume_name):
        """
        Verifies if a volume is displayed.
        :param volume_name: volume name to select.
        """
        self._home.verify_if_volume_is_displayed(volume_name)
