__author__ = 'Edmundo Cossio'

from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from resources.commons.DriverManager import DriverManager
from resources.libraries.Dictionaries import request_queue
from resources.methods.UIMethods import click_element_stale


class WebNativeLogging(object):
    """
    Page object modeling the structure and operations of the Xinet WebNative Logging page.
    """
    _driver = None
    _wait = None

    # Selectors
    _preview_generation_link = (By.XPATH, "//a[text()='Preview Generation']")
    _request_queue = (By.XPATH, "//th[text()='Request Queue']")
    _frame_id = (By.ID, "waFrame")
    _pending_selected_link = (By.XPATH, "//div[@id='page-nav']/descendant::li[@class='selected']/a[.='Pending']")

    def __init__(self):
        self._driver = DriverManager().get_instance().get_driver()
        self._wait = DriverManager().get_instance().get_wait()

    def click_preview_generation_link(self):
        """
        Clicks the 'Preview Generation' link.
        """
        click_element_stale(self._driver, *self._preview_generation_link)
        self._wait.until(ec.visibility_of_element_located(self._pending_selected_link))
        
    def are_request_queue_values_displayed(self, request_queue_name, processing=0, waiting=0, holding=0):
        """
        Are request queue values displayed in the list with corrected values for processing, waiting, holding
        :param request_queue_name: Request queue name to verify in the 'Request Queue' list in Preview Generation.
        :param processing: Process value.
        :param waiting: Wait value.
        :param holding: Hold value.
        :return: True if displayed, otherwise False. 
        """
        selected_item = (By.XPATH, "//td[text()='" + request_queue_name + "']")
        processing_cell = (By.ID, "rve_proc" + request_queue[request_queue_name] + "")
        waiting_cell = (By.ID, "rve_wait" + request_queue[request_queue_name] + "")
        holding_cell = (By.ID, "rve_hold" + request_queue[request_queue_name] + "")
        parent_page = self._driver.current_window_handle
        try:
            self._wait.until(ec.frame_to_be_available_and_switch_to_it(self._frame_id))
            self._wait.until(lambda s: s.find_element(*selected_item).is_displayed())
            actual_processing = self._driver.find_element(*processing_cell).text
            actual_waiting = self._driver.find_element(*waiting_cell).text
            actual_holding = self._driver.find_element(*holding_cell).text
            if actual_processing == processing and actual_waiting == waiting and actual_holding == holding:
                are_displayed = True
            else:
                are_displayed = False
        finally:
            self._driver.switch_to_window(parent_page)
        return are_displayed

    def verify_if_the_request_queue_name_is_displayed_in_the_request_queue_list(self, request_queue_name, processing=0, waiting=0, holding=0):
        """
        Verify if the request queue name is displayed with corrected values for processing, waiting, holding in the request-queue list.
        :param request_queue_name: Request queue name to verify in the 'Request Queue' list in Preview Generation.
        :param processing: Process value.
        :param waiting: Wait value.
        :param holding: Hold value.
        """
        BuiltIn().should_be_true(self.are_request_queue_values_displayed(request_queue_name, processing, waiting, holding))
