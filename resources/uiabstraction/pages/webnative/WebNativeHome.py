__author__ = 'MarceloM Guzman'

import os
import platform
import shutil

from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select

from resources.commons.DriverManager import DriverManager
from resources.commons.GlobalVariables import BROWSER, CHROME_PATH
from resources.methods.UIMethods import wait_for_load_page, click_element_stale, \
    accept_alert_before_displayed, is_element_present
from resources.uiabstraction.pages.webnative.WebNativeDatabase import WebNativeDatabase
from resources.uiabstraction.pages.webnative.WebNativeLogging import WebNativeLogging
from resources.uiabstraction.pages.webnative.WebNativePrintHotFolder import WebNativePrintHotFolder
from resources.uiabstraction.pages.webnative.WebNativeVolumesUsers import WebNativeVolumesUsers


class WebNativeHome(object):
    """
    Page object modeling the structure and operations of the Xinet WebNative Home page.
    """
    _driver = None
    _wait = None   

    # Selectors
    _xinet_image = (By.XPATH, "//img[@alt='WebNative']")
    _volumes_users_link = (By.XPATH, "//a[text()='Volumes/Users']")
    _database_link = (By.XPATH, "//a[text()='Database']")
    _print_hot_folder_link = (By.XPATH, "//a[text()='Print/Hot Folder']")
    _encoding_link = By.XPATH, "//a[text()='Encoding']"
    _actual_selected_link = (By.XPATH, "//li[contains(@class,'selected')]")
    _logging_link = (By.XPATH, "//a[text()='Logging']")
    _status_link = (By.XPATH, "//a[text()='Status']")
    
    _frame_id = (By.ID, "waFrame")
    _database_table_id = (By.ID, "wform")
    _clear_browser_data_commit_id = (By.ID, 'clear-browser-data-commit')
    
    _server_info = (By.XPATH, "//th[text()='Server Info']")
    _xinet_service_and_or_daemon = (By.XPATH, "//th[text()='Xinet Service and/or Daemon']")
    _summary_selected = (By.XPATH, "//li[contains(@class,'selected')]/a[text()='Summary']")

    _admin_selected = (By.XPATH, "//li[contains(@class,'selected')]/a[text()='Admin']")
    _system_volumes_selected = (By.XPATH, "//li[contains(@class,'selected')]/a[text()='System Volumes']")
    _queue_status_selected = (By.XPATH, "//li[contains(@class,'selected')]/a[text()='Queue Status']")
    _status_selected = (By.XPATH, "//li[contains(@class,'selected')]/a[text()='Status']")
    
    _frame_clear_browser_data = (By.XPATH, "//iframe[@src='chrome://settings-frame/clearBrowserData']")

    _name_combo = (By.NAME, 'enc')

    _submit_set_selected_encoding_button = (By.NAME, "submit")
    
    def __init__(self):
        self._driver = DriverManager().get_instance().get_driver()
        self._wait = DriverManager().get_instance().get_wait()

    def _open_webnative(self, url):
        """
        Opens the browser with Xinet Portal.
        """
        self._driver.get(url)
        self._wait.until(ec.visibility_of_element_located(self._xinet_image))

    def login_to_webnative(self, server_ip, username, password):
        """
        Sets the given credentials and logs in to WebNative administration.
        """
        xinet_webnative_url = "http://" + username + ":" + password + "@" + server_ip + "/webnative/listdir/"
        self._driver.get(xinet_webnative_url)
        wait_for_load_page()

    def close_browser(self):
        """
        Closes the browser.
        """
        self._driver.quit()
    
    def click_volumes_users_link(self):
        """
        Clicks the 'Volumes/Users' link.
        """
        self._wait.until(ec.visibility_of_element_located(self._database_link))
        click_element_stale(self._driver, *self._volumes_users_link)
        self._wait.until(ec.visibility_of_element_located(self._system_volumes_selected))
        return WebNativeVolumesUsers()
    
    def click_database_link(self):
        """
        Clicks the 'Database' link.
        """
        self._wait.until(ec.visibility_of_element_located(self._database_link))
        click_element_stale(self._driver, *self._database_link)
        if not is_element_present(self._driver, *self._server_info):
            volumes_users = WebNativeVolumesUsers()
            volumes_users.click_user_volumes_link()
            click_element_stale(self._driver, *self._database_link)
        self._wait.until(ec.visibility_of_element_located(self._admin_selected))
        return WebNativeDatabase()
    
    def click_print_hot_folder(self):
        """
        Clicks the 'Print/Hot Folder' link.
        """
        self._wait.until(ec.visibility_of_element_located(self._print_hot_folder_link))
        click_element_stale(self._driver, *self._print_hot_folder_link)
        self._wait.until(ec.visibility_of_element_located(self._queue_status_selected))
        return WebNativePrintHotFolder()
    
    def clear_browsing_data(self):
        """
        Clears the browser data if the navigator is Chrome and MAC OS.
        """
        if BROWSER.lower() == "chrome" and platform.system() == "Darwin":
            default_folder_path = CHROME_PATH + '/Default'
            if os.path.exists(default_folder_path):
                os.chdir(CHROME_PATH)
                shutil.rmtree('Default')
            else:
                print 'Default Folder does not exists...'

    def select_language_encoding(self, language_type):
        """
        Selects the language encoding.
        """
        self._wait.until(ec.visibility_of_element_located(self._actual_selected_link))
        if self._driver.find_element(*self._actual_selected_link).text == 'License':
            select = Select(self._driver.find_element(*self._name_combo))
            select.select_by_visible_text(language_type)
            if BROWSER.lower() != "safari":
                click_element_stale(self._driver, *self._submit_set_selected_encoding_button)
                self._wait.until(ec.alert_is_present())
                self.accept_and_close_alert()
            else:
                accept_alert_before_displayed(self._driver)
                click_element_stale(self._driver, *self._submit_set_selected_encoding_button)
            wait_for_load_page()
    
    def accept_and_close_alert(self):
        """
        Accepts and closes the alert displayed.
        """
        try:
            alert = self._driver.switch_to_alert()
            alert.accept()
        except NoAlertPresentException:
            print "There is no alert to switch on."
    
    def click_logging_link(self):
        """
        Clicks the 'Logging' link.
        """
        self._wait.until(ec.visibility_of_element_located(self._logging_link))
        click_element_stale(self._driver, *self._logging_link)
        if is_element_present(self._driver, *self._summary_selected):
            volumes_users = WebNativeVolumesUsers()
            volumes_users.click_user_volumes_link()
            click_element_stale(self._driver, *self._logging_link)
        self._wait.until(ec.visibility_of_element_located(self._status_selected))
        return WebNativeLogging()
