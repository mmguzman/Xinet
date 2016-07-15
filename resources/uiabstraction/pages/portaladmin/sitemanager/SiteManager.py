__author__ = 'Edmundo Cossio'

from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from resources.commons.DriverManager import DriverManager
from resources.methods.UIMethods import is_element_present
from resources.uiabstraction.pages.portaladmin.sitemanager.AddSite import AddSite


class SiteManager(object):
    """
    Page object modeling the structure and operations of the Site Manager page.
    """
    _driver = None
    _wait = None
    
    # Selectors
    _add_site_link = (By.LINK_TEXT, "Add Site")
    _site_summary_tab = (By.LINK_TEXT, "Site Summary")
    _create_new_site_header = (By.XPATH, "//td[text()='Create a new site']")
    _site_name_header = (By.XPATH, "//th[text()='Site Name']")
    _delete_site = (By.XPATH, "//td[text()='Delete Site']")
    _site_delete_text = (By.XPATH, "//input[@name='siteDeleteForce']")
    _submit_button = (By.XPATH, "//input[@name='siteDelete']")
    _delete_message = (By.XPATH, "//span[contains(text(),'deleted')]")
    
    def __init__(self):
        self._driver = DriverManager().get_instance().get_driver()
        self._wait = DriverManager().get_instance().get_wait()
    
    def click_add_site_link(self):
        """
        Clicks 'Add Site' link
        """
        self._wait.until(ec.visibility_of_element_located(self._add_site_link))
        self._driver.find_element(*self._add_site_link).click()
        self._wait.until(ec.visibility_of_element_located(self._create_new_site_header))
        return AddSite()
    
    def is_already_displayed_in_sites_list(self, server_ip, template_name):
        """
        Verifies if a site is displayed in the Site list.
        """
        self._wait.until(ec.visibility_of_element_located(self._site_name_header))
        site_name = server_ip.split(".")[3] + 'robot' + template_name
        site_to_find = (By.XPATH, "//td[text()='" + site_name + "']")
        return is_element_present(self._driver, *site_to_find)
    
    def click_remove_button(self, site_name):
        """
        Clicks remove button.
        :param site_name: The site name.
        """
        remove_button_icon = (By.XPATH, "//a[contains(@href,'" + site_name + "')]/img[@alt='Delete']")
        self._wait.until(ec.element_to_be_clickable(remove_button_icon)).click()
    
    def set_confirmation_text(self, value):
        """
        Sets a value in the confirmation text.
        :param value: The value to set.
        """
        self._wait.until(ec.visibility_of_element_located(self._delete_site))
        self._driver.find_element(*self._site_delete_text).clear()
        self._driver.find_element(*self._site_delete_text).send_keys(value)
    
    def click_submit_button(self):
        """
        Clicks submit button.
        """
        self._wait.until(ec.element_to_be_clickable(self._submit_button)).click()
        self._wait.until(ec.visibility_of_element_located(self._delete_message))

    def is_removed_site_successfully_message_displayed(self, site_name):
        """
        Verifies if the 'Removed site successfully' message is displayed.
        :param site_name: The site name.
        """
        removed_site_message = (By.XPATH, "//span[contains(text(),'" + site_name + " * deleted from system.')]")
        return is_element_present(self._driver, *removed_site_message)
        
    def verify_if_removed_site_successfully_message_is_displayed(self, site_name):
        """
        Verifies if the 'Removed site successfully' message is displayed.
        :param site_name: The site name.
        """
        BuiltIn().should_be_true(self.is_removed_site_successfully_message_displayed(site_name))
    
    def remove_site(self, server_ip, template_name):
        """
        Removes the site created.
        :param server_ip: The server ip.
        :param template_name: The template name.
        """
        site_name = server_ip.split(".")[3] + 'robot' + template_name
        self.click_remove_button(site_name)
        self.set_confirmation_text('yes')
        self.click_submit_button()
        self.verify_if_removed_site_successfully_message_is_displayed(site_name)
