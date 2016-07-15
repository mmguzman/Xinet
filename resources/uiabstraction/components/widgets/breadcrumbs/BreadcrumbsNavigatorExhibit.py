__author__ = 'MarceloM Guzman'

from selenium.webdriver.common.by import By

from resources.methods.UIMethods import accept_alert_and_leave_page
from resources.uiabstraction.components.widgets.breadcrumbs.BreadcrumbsNavigatorBase import BreadcrumbsNavigatorBase
from resources.uiabstraction.components.widgets.foldercontent.FolderContentExhibit import FolderContentExhibit


class BreadcrumbsNavigatorExhibit(BreadcrumbsNavigatorBase):
    """
    Page object modeling the structure and operations of the Breadcrumbs navigator for Exhibit template.
    """

    def __init__(self):
        BreadcrumbsNavigatorBase.__init__(self, "Exhibit")
        self.folder_locator_template = "//div[@id='navcrumbs']/a[contains(text(),'%s')]"

    def _create_folder_content(self):
        return FolderContentExhibit()

    def click_folder_link_in_breadcrumbs_and_close_alert(self, folder_name):
        """
        Clicks the folder name link given in folder_name argument and close alert related with "leave this page?"
        """
        folder_name_selector = (By.XPATH, self.folder_locator_template % folder_name)
        # This alert is displayed with Chrome and FF browsers (Used in XNT-67: DetailsViewMetadataHistory.txt)
        accept_alert_and_leave_page(self._driver)
        self._driver.find_element(*folder_name_selector).click()
        self._folder_content.wait_for_folder_content_page_loaded()
