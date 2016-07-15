__author__ = 'Edmundo Cossio'

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

from resources.commons.DriverManager import DriverManager
from resources.uiabstraction.pages.portaladmin.sitemanager.EditSiteConfiguration import EditSiteConfiguration


class AddSite(object):
    """
    Page object modeling the structure and operations of the Add Site page.
    """
    _driver = None
    _wait = None
    
    # Selectors
    _site_name_input = (By.NAME, "SITENAME")
    _submit_volume_button = (By.NAME, "siteSetup")
    _templates_dropdown = (By.NAME, "TEMPLATES")
    _create_new_site_header = (By.XPATH, "//td[text()='Create a new site']")
    
    def __init__(self):
        self._driver = DriverManager().get_instance().get_driver()
        self._wait = DriverManager().get_instance().get_wait()
        
    def create_new_site(self, server_ip, template_name):
        """
        Creates a new site
        Returns Edit Site Configuration page
        """
        self._wait.until(ec.visibility_of_element_located(self._create_new_site_header))
        site_name = server_ip.split(".")[3] + 'robot' + template_name
        self._set_site_name(site_name)
        self._select_item_of_template_list(template_name)
        self._click_submit_button()
        created_site_header = (By.XPATH, "//td[text()='Site: " + site_name + "']")
        self._wait.until(ec.visibility_of_element_located(created_site_header))
        return EditSiteConfiguration()

    def _set_site_name(self, name):
        """
        Sets the Site name.
        """
        self._driver.find_element(*self._site_name_input).send_keys(name)

    def _click_submit_button(self):
        """
        Clicks the Submit button.
        """
        self._driver.find_element(*self._submit_volume_button).click()
    
    def _select_item_of_template_list(self, item_name):
        """
        Selects an item (Exhibit/Marquee) of templates drop-down
        """
        template_set_dropdown = Select(self._driver.find_element(*self._templates_dropdown))
        template_set_dropdown.select_by_visible_text(item_name.capitalize())
