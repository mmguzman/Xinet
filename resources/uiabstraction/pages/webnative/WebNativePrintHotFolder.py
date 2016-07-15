__author__ = 'MarceloM Guzman'

import time

from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select

from resources.commons.DriverManager import DriverManager
from resources.commons.GlobalVariables import PATH_TO_HOT_FOLDER_VOLUME_PATH_KARINA, \
    PATH_TO_HOT_FOLDER_VOLUME_PATH_RH7WNV, PATH_TO_HOT_FOLDER_VOLUME_PATH_BUDDY64, PATH_TO_HOT_FOLDER_VOLUME_PATH_ALL, \
    PATH_TO_HOT_FOLDER_ZBODIKOVA_MINI, OUTPUT_FOLDER_PATH_KARINA, OUTPUT_FOLDER_PATH_RH7WNV, \
    OUTPUT_FOLDER_PATH_BUDDY64, OUTPUT_FOLDER_PATH_ALL, OUTPUT_FOLDER_PATH_ZBODIKOVA_MINI
from resources.methods.UIMethods import is_element_present, click_element_stale, click_element


class WebNativePrintHotFolder(object):
    """
    Page object modeling the structure and operations of the Xinet WebNative Print/Hot Folder page.
    """
    _driver = None
    _wait = None
    
    # Selectors
    _print_queues_link = (By.XPATH, "//a[text()='Print Queues']")
    _new_queue_link = (By.XPATH, "//a[text()='New Queue']")
    _hot_folders_link = (By.XPATH, "//a[text()='Hot Folders']")
    _make_new_hot_folder_link = (By.XPATH, "//a[text()='Make New Hot Folder']")
    _summary_link = (By.XPATH, "//a[text()='Summary']")
    
    _frame_id = (By.ID, "waFrame")
    _path_to_hot_folder_table_id = (By.ID, "hotlisttable")
    
    _print_area = (By.ID, "prtarea")
    
    _print_queue_combo = (By.NAME, "i0_0")
    _select_printer_combo = (By.NAME, "i1_0")
    _select_output_folder_combo = (By.NAME, "subdir2_0")
    _path_to_hot_folder_combo = (By.NAME, "subdir")
    _spool_to_print_queue_combo = (By.NAME, "pqueue")
    
    _next_button = (By.NAME, "next")
    _create_new_queue_button = (By.XPATH, "//input[@value='Create New Queue']")
    _submit_button = (By.NAME, "doedit")
    _submit_hot_folder_button = (By.NAME, "save")
    _delete_button = (By.XPATH, "//input[@value='Delete']")
    _create_folder_button = (By.XPATH, "//button[@type='button' and text()='Create Folder']")
    
    _print_queue_name_textbox = (By.NAME, "i3_1")
    _create_folder_textbox = (By.NAME, "newfolder")
    _create_output_folder_textbox = (By.NAME, "newfolder2_0")

    _summary_selected = (By.XPATH, "//li[contains(@class,'selected')]/a[text()='Summary']")
    
    _unique_print_queue_name_label = (By.XPATH, "//span[text()='Unique print queue name:']")
    
    def __init__(self):
        self._driver = DriverManager().get_instance().get_driver()
        self._wait = DriverManager().get_instance().get_wait()
    
    def click_print_queues_link(self):
        """
        Clicks the 'Print Queues' link.
        """
        self._wait.until(ec.visibility_of_element_located(self._print_queues_link))
        click_element_stale(self._driver, *self._print_queues_link)
        self._wait.until(ec.visibility_of_element_located(self._print_queues_link))
        
    def click_new_queue_link(self):
        """
        Clicks the 'New Queue' link
        """
        self._wait.until(ec.visibility_of_element_located(self._new_queue_link))
        click_element_stale(self._driver, *self._new_queue_link)
        self._wait.until(ec.visibility_of_element_located(self._frame_id))
        
    def click_make_new_hot_folder_link(self):
        """
        Clicks the 'Make New Hot Folder' link
        """
        self._wait.until(ec.visibility_of_element_located(self._make_new_hot_folder_link))
        click_element_stale(self._driver, *self._make_new_hot_folder_link)
        self._wait.until(ec.visibility_of_element_located(self._frame_id))
        
    def click_hot_folders_link(self):
        """
        Clicks the 'Hot Folders' link
        """
        self._wait.until(ec.visibility_of_element_located(self._hot_folders_link))
        click_element_stale(self._driver, *self._hot_folders_link)
        self._wait.until(ec.visibility_of_element_located(self._frame_id))
        
    def click_summary_link(self):
        """
        Clicks the 'Summary' link
        """
        self._wait.until(ec.visibility_of_element_located(self._summary_link))
        click_element_stale(self._driver, *self._summary_link)
        self._wait.until(ec.visibility_of_element_located(self._frame_id))
        
    def select_type_of_print_queue(self, print_queue_type):
        """
        Selects the type of Print Queue.
        """
        select = Select(self._driver.find_element(*self._print_queue_combo))
        select.select_by_visible_text(print_queue_type)
        self._wait.until(ec.visibility_of_element_located(self._select_printer_combo))
        
    def select_printer_or_subtype(self, printer_sub_type):
        """
        Selects the Printer (or Subtype).
        """
        select = Select(self._driver.find_element(*self._select_printer_combo))
        select.select_by_visible_text(printer_sub_type)
        self._wait.until(ec.visibility_of_element_located(self._select_output_folder_combo))
        
    def select_spool_to_print_queue(self, queue_name):
        """
        Selects the Spool To Print Queue.
        """
        select = Select(self._driver.find_element(*self._spool_to_print_queue_combo))
        select.select_by_visible_text(queue_name)

    def select_output_folder_option(self, folder_name):
        """
        Selects the folder option of Output root path.
        """
        if not is_element_present(self._driver, By.XPATH, "//option[text()='" + folder_name + "']"):
            self.create_new_output_folder(folder_name)
        else:
            select = Select(self._driver.find_element(*self._select_output_folder_combo))
            select.select_by_visible_text(folder_name)

    def select_hot_folder_option(self, folder_name):
        """
        Selects the folder option of Hot folder root path.
        """
        if not is_element_present(self._driver, By.XPATH, "//option[text()='" + folder_name + "']"):
            self.create_hot_folder(folder_name)
        else:
            select = Select(self._driver.find_element(*self._path_to_hot_folder_combo))
            select.select_by_visible_text(folder_name)

    def select_output_folder_option_list(self, output_folder_name_list):
        """
        Selects a folder of Output combobox.
        """
        do_cd_up_index = 0
        for folder_list in output_folder_name_list:
            self.select_output_folder_option(folder_list)
            folder_href = (By.XPATH, "//a[@href='javascript:do_cd_up(2,0," + str(do_cd_up_index) + ")']")
            self._wait.until(ec.visibility_of_element_located(folder_href))
            do_cd_up_index += 1

    def select_hot_folder_option_list(self, path_to_hot_folder_list):
        """
        Selects a folder of Path To Hot Folder combobox.
        """
        do_cd_up_index = 0
        for folder_list in path_to_hot_folder_list:
            self.select_hot_folder_option(folder_list)
            time.sleep(1)
            folder_href = (By.XPATH, "//a[@href='javascript:do_cd_up(" + str(do_cd_up_index) + ")']")
            self._wait.until(ec.visibility_of_element_located(folder_href))
            do_cd_up_index += 1

    def create_new_output_folder(self, folder_name):
        """
        Creates a new Output folder.
        """
        if is_element_present(self._driver, *self._select_output_folder_combo):
            self.select_output_folder_option("( New Folder )")
        self._driver.find_element(*self._create_output_folder_textbox).send_keys(folder_name)
        self._driver.find_element(*self._create_folder_button).click()

    def create_hot_folder(self, folder_name):
        """
        Creates a new Hot folder.
        """
        if is_element_present(self._driver, *self._path_to_hot_folder_combo):
            self.select_hot_folder_option("( New Folder )")
        self._driver.find_element(*self._create_folder_textbox).send_keys(folder_name)
        self._driver.find_element(*self._create_folder_button).click()

    def select_output_folder(self, server_name):
        """
        Selects the Output folder.
        """
        if server_name == "karina":
            self.select_output_folder_option_list(OUTPUT_FOLDER_PATH_KARINA)
        elif server_name == "rh7wnv":
            self.select_output_folder_option_list(OUTPUT_FOLDER_PATH_RH7WNV)
        elif server_name == "buddy64":
            self.select_output_folder_option_list(OUTPUT_FOLDER_PATH_BUDDY64)
        elif server_name == "zbodikova-mini":
            self.select_output_folder_option_list(OUTPUT_FOLDER_PATH_ZBODIKOVA_MINI)
        else:
            self.select_output_folder_option_list(OUTPUT_FOLDER_PATH_ALL)

    def select_hot_folder(self, server_name):
        """
        Selects the Path To Hot Folder.
        """
        if server_name == "karina":
            self.select_hot_folder_option_list(PATH_TO_HOT_FOLDER_VOLUME_PATH_KARINA)
        elif server_name == "rh7wnv":
            self.select_hot_folder_option_list(PATH_TO_HOT_FOLDER_VOLUME_PATH_RH7WNV)
        elif server_name == "buddy64":
            self.select_hot_folder_option_list(PATH_TO_HOT_FOLDER_VOLUME_PATH_BUDDY64)
        elif server_name == "zbodikova-mini":
            self.select_hot_folder_option_list(PATH_TO_HOT_FOLDER_ZBODIKOVA_MINI)
        else:
            self.select_hot_folder_option_list(PATH_TO_HOT_FOLDER_VOLUME_PATH_ALL)

    def click_next_button(self):
        """
        Clicks the Next button.
        """
        self._driver.find_element(*self._next_button).click()
        self._wait.until(ec.visibility_of_element_located(self._print_queue_name_textbox))
        
    def click_create_new_queue_button(self):
        """
        Clicks the Create New Queue button
        """
        click_element(self._driver, self._driver.find_element(*self._create_new_queue_button))
        self._wait.until(ec.invisibility_of_element_located(self._create_new_queue_button))

    def click_submit_button(self):
        """
        Clicks the Submit button.
        """
        self._driver.find_element(*self._submit_button).click()
        self._wait.until(ec.visibility_of_element_located(self._print_area))
        
    def click_submit_hot_folder_button(self):
        """
        Clicks the Submit hot folder button.
        """
        self._driver.find_element(*self._submit_hot_folder_button).click()
        self._wait.until(ec.invisibility_of_element_located(self._submit_hot_folder_button))
        
    def click_delete_icon(self, queue_name):
        """
        Clicks the 'Delete' icon according queue name.
        """
        delete_icon = (By.NAME, "rmqq_" + queue_name)
        self._driver.find_element(*delete_icon).click()
        self._wait.until(ec.visibility_of_element_located(self._delete_button))
        
    def click_delete_button(self):
        """
        Clicks the 'Delete' button.
        """
        self._driver.find_element(*self._delete_button).click()
        self._wait.until(ec.invisibility_of_element_located(self._delete_button))
        
    def set_queue_name_textbox(self, queue_name):
        """
        Sets the Queue name.
        """
        self._wait.until(ec.visibility_of_element_located(self._print_queue_name_textbox))
        element = lambda: self._driver.find_element(*self._print_queue_name_textbox)
        element().clear()
        element().click()
        element().send_keys(queue_name)

    def is_pdf_ir_queue_displayed(self, queue_name):
        """
        Returns true if a PDF IR queue is displayed.
        """
        self._wait.until(ec.visibility_of_element_located(self._summary_selected))
        parent_page = self._driver.current_window_handle
        try:
            self._wait.until(ec.frame_to_be_available_and_switch_to_it(self._frame_id))
            queue_value = (By.XPATH, "//td[text()='" + queue_name + "']")
            return is_element_present(self._driver, *queue_value)
        finally:
            self._driver.switch_to_window(parent_page)
    
    def verify_if_pdf_ir_queue_displayed(self, queue_name):
        """
        Verifies if a PDF IR queue is displayed.
        """
        BuiltIn().should_be_true(self.is_pdf_ir_queue_displayed(queue_name))
        
    def verify_if_pdf_ir_queue_is_not_displayed(self, queue_name):
        """
        Verifies if a PDF IR queue is not displayed.
        """
        BuiltIn().should_not_be_true(self.is_pdf_ir_queue_displayed(queue_name))
        
    def get_hot_folder_path(self, server_name):
        """
        Gets the path of the Hot Folder.
        """
        global hot_folder_path
        
        if server_name == "karina":
            hot_folder_path = '/'.join(PATH_TO_HOT_FOLDER_VOLUME_PATH_KARINA)
        elif server_name == "rh7wnv":
            hot_folder_path = '/'.join(PATH_TO_HOT_FOLDER_VOLUME_PATH_RH7WNV)
        elif server_name == "buddy64":
            hot_folder_path = '/'.join(PATH_TO_HOT_FOLDER_VOLUME_PATH_BUDDY64)
        elif server_name == "zbodikova-mini":
            hot_folder_path = '/'.join(PATH_TO_HOT_FOLDER_ZBODIKOVA_MINI)
        else:
            hot_folder_path = '/'.join(PATH_TO_HOT_FOLDER_VOLUME_PATH_ALL)
        return hot_folder_path

    def is_hot_folder_displayed(self, server_name):
        """
        Returns true if a Hot Folder is displayed.
        """
        parent_page = self._driver.current_window_handle
        try:
            self._wait.until(ec.frame_to_be_available_and_switch_to_it(self._frame_id))
            hot_folder_dir = self.get_hot_folder_path(server_name)
            hot_folder_value = (By.XPATH, "//a[contains(text(),'" + hot_folder_dir + "')]")
            return is_element_present(self._driver, *hot_folder_value)
        finally:
            self._driver.switch_to_window(parent_page)

    def get_print_queue_name(self, row):
        """
        Gets the name of the print queue according its position.
        """
        parent_page = self._driver.current_window_handle
        try:
            self._wait.until(ec.frame_to_be_available_and_switch_to_it(self._frame_id))
            return self._driver.find_element((By.XPATH, "//tr[" + str(row + 1) + "]/td")).text
        finally:
            self._driver.switch_to_window(parent_page)
            
    def verify_if_hot_folder_displayed(self, server_name):
        """
        Verifies if a Hot Folder is displayed.
        """
        BuiltIn().should_be_true(self.is_hot_folder_displayed(server_name))
    
    def add_new_pdf_ir_queue(self, server_name, queue_name, print_queue_type, printer_sub_type):
        """
        Sets all values to create a new PDF IR queue.
        """
        if not (self.is_pdf_ir_queue_displayed(queue_name)):
            parent_page = self._driver.current_window_handle
            try:
                self.click_new_queue_link()
                self._wait.until(ec.frame_to_be_available_and_switch_to_it(self._frame_id))
                self.select_type_of_print_queue(print_queue_type)
                self.select_printer_or_subtype(printer_sub_type)
                self.select_output_folder(server_name)
                self.click_next_button()
                self.set_queue_name_textbox(queue_name)
                self.click_create_new_queue_button()
                self.click_submit_button()
            finally:
                self._driver.switch_to_window(parent_page)
        else:
            print "The " + queue_name + " queue is already created."
    
    def create_new_hot_folder(self, server_name, queue_name):
        """
        Sets all values to create a new Hot Folder.
        """
        if not (self.is_hot_folder_displayed(server_name)):
            parent_page = self._driver.current_window_handle
            try:
                self.click_make_new_hot_folder_link()
                self._wait.until(ec.frame_to_be_available_and_switch_to_it(self._frame_id))
                self.select_hot_folder(server_name)
                self.select_spool_to_print_queue(queue_name)
                self.click_submit_hot_folder_button()
            finally:
                self._driver.switch_to_window(parent_page)
        else:
            print "The hot folder for " + queue_name + " queue is already created."
    
    def delete_print_queue(self, print_queue_name):
        """
        Deletes a print queue.
        """
        if self.is_pdf_ir_queue_displayed(print_queue_name):
            parent_page = self._driver.current_window_handle
            self._wait.until(ec.frame_to_be_available_and_switch_to_it(self._frame_id))
            self.click_delete_icon(print_queue_name)
            self.click_delete_button()
            self._driver.switch_to_window(parent_page)
        else:
            print "The " + print_queue_name + " is not present."
