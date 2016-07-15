__author__ = 'MarceloM Guzman'

from selenium.webdriver.common.by import By

from resources.methods.UIMethods import is_element_present
from resources.uiabstraction.components.widgets.breadcrumbs.BreadcrumbsNavigatorExhibit import BreadcrumbsNavigatorExhibit
from resources.uiabstraction.components.widgets.foldercontent.FolderContentExhibit import FolderContentExhibit
from resources.uiabstraction.components.widgets.sidepane.SidePaneNavigatorExhibit import SidePaneNavigatorExhibit
from resources.uiabstraction.pages.home.HomeBase import HomeBase


class HomeExhibit(HomeBase):
    """
    Page object modeling the structure and operations of the Home page for Exhibit template.
    """
    _breadcrumbs_navigator = None

    def __init__(self):
        HomeBase.__init__(self, "Exhibit")
        self._breadcrumbs_navigator = BreadcrumbsNavigatorExhibit()
        self.volumes_displayed_template = "//a[contains(@title,'%s')]"
    
    def select_volume(self, folder_name):
        """
        Clicks the browse folder name given in ``folder_name`` argument.
        :param folder_name: volume name to select.
        """
        if is_element_present(self._driver, By.XPATH, "//a[contains(@title,'" + folder_name + "')]"):
            return SidePaneNavigatorExhibit()

    def back_to_home(self):
        self._breadcrumbs_navigator.click_folder_link_in_breadcrumbs("Top Level")
    
    def _create_folder_content(self):
        return FolderContentExhibit()
