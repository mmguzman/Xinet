__author__ = 'MarceloM Guzman'

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from resources.methods.UIMethods import move_mouse_to, click_element
from resources.uiabstraction.components.widgets.basictoolsbar.BasicToolsToolbarMarquee import BasicToolsToolbarMarquee
from resources.uiabstraction.components.widgets.foldercontent.FolderContentMarquee import FolderContentMarquee
from resources.uiabstraction.components.widgets.sidepane.SidePaneNavigatorMarquee import SidePaneNavigatorMarquee
from resources.uiabstraction.pages.home.HomeBase import HomeBase


class HomeMarquee(HomeBase):
    """
    Page object modeling the structure and operations of the Home page for Marquee template.
    """
    _basic_tools_toolbar = None

    # Selectors
    _main_container = (By.ID, "main")
    
    def __init__(self):
        HomeBase.__init__(self, "Marquee")
        self._basic_tools_toolbar = BasicToolsToolbarMarquee()
        self.volumes_displayed_template = "//div[@class='caption text-center']/small[contains(text(),'%s')]"

    def select_volume(self, folder_name):
        """
        Clicks the browse folder name given in ``folder_name`` argument.
        :param folder_name: volume name to select.
        """
        try:
            self._wait.until(ec.visibility_of_element_located(self._main_container), "The main container is not displayed")
            _hover_element = self._driver.find_element_by_xpath("//div/small[contains(text(),'" + folder_name + "')]")
            _browse_element = self._driver.find_element_by_xpath("//div/small[contains(text(),'" + folder_name + "')]/../preceding-sibling::div/div/span[contains(@class,'folder-open')]")
            move_mouse_to(self._driver, _hover_element)
            click_element(self._driver, _browse_element)
            self._folder_content.wait_for_folder_content_page_loaded()
        except NoSuchElementException:
            return SidePaneNavigatorMarquee()

    def back_to_home(self):
        self._basic_tools_toolbar.click_home_button()
    
    def _create_folder_content(self):
        return FolderContentMarquee()
