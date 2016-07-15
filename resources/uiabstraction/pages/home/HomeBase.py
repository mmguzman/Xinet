__author__ = 'MarceloM Guzman'

from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By

from resources.commons.DriverManager import DriverManager
from resources.methods.UIMethods import is_element_present


class HomeBase(object):
    """
    Page object modeling the structure and operations of the Home page.
    """
    _driver = None
    _wait = None
    _folder_content = None

    def __init__(self, theme):
        self._driver = DriverManager().get_instance().get_driver()
        self._wait = DriverManager().get_instance().get_wait()
        self.theme = theme
        self._folder_content = self._create_folder_content()
    
    def select_volume(self, folder_name):
        """
        Clicks the browse folder name given in ``folder_name`` argument.
        :param folder_name: volume name to select.
        """
        return self

    def is_volume_displayed(self, volume_name):
        """
        Verifies if a volume is displayed.
        :param volume_name: volume name.
        :return: True if the volume is displayed.
        """
        volumes_displayed_selector = (By.XPATH, self.volumes_displayed_template % volume_name)
        return is_element_present(self._driver, *volumes_displayed_selector)

    def verify_if_volume_is_displayed(self, volume_name):
        """
        Verifies if a volume is displayed.
        :param volume_name: volume name.
        """
        BuiltIn().should_be_true(self.is_volume_displayed(volume_name))

    def back_to_home(self):
        return self
    
    def _create_folder_content(self):
        raise NotImplementedError()
