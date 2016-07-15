__author__ = 'Edmundo Cossio'

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from resources.commons.DriverManager import DriverManager
from resources.uiabstraction.pages.portaladmin.sitemanager.SiteManager import SiteManager


class PortalAdminHome(object):
    """
    Page object modeling the structure and operations of the Portal Admin Home page.
    """
    _driver = None
    _wait = None
    
    # Selectors
    _site_manager_link = (By.LINK_TEXT, "Site Manager")
    _site_name_header = (By.XPATH, "//th[text()='Site Name']")
    
    def __init__(self):
        self._driver = DriverManager().get_instance().get_driver()
        self._wait = DriverManager().get_instance().get_wait()
    
    def click_site_manager_link(self):
        """
        Clicks 'Site Manager' link
        """
        self._wait.until(ec.visibility_of_element_located(self._site_manager_link))
        self._driver.find_element(*self._site_manager_link).click()
        self._wait.until(ec.visibility_of_element_located(self._site_name_header))
        return SiteManager()
