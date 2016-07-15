__author__ = 'MarceloM Guzman'

import os

from robot.libraries.BuiltIn import BuiltIn
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

from resources.commons.DriverManager import DriverManager
from resources.commons.GlobalVariables import DOWNLOAD_PATH
from resources.libraries.Utils import wait_until_file_is_downloaded, wait_until_file_is_created, \
    is_file_present_in_directory, extract_file
from resources.methods.UIMethods import get_quantity_of_elements_displayed_on_page, select_checkbox, \
    is_element_present, click_element, wait_for_load_page


class BasketBase(object):
    """
    Page object modeling the structure and operations of the Basket page.
    """
    _driver = None
    _wait = None

    # Selectors
    _apply_keywords_button = (By.NAME, "process")
    _close_batch_report_button = (By.XPATH, "//span[.='Close']")
    _download_button = (By.ID, "download")

    _keywords_updated_text = (By.XPATH, "//div[text()='All keywords were successfully updated.']")
    _archive_name_textbox = (By.ID, "archName")
    _batch_archive_name_textbox = (By.ID, "_archivename_")

    _convert_file_format_checkbox = (By.ID, "_DOformat_")

    _text_popup_combobox = (By.XPATH, "//th[contains(text(),'wnv_text_popup') and not(contains(text(),'wnv_text_popup_'))]/following::select")
    _select_format_combobox = (By.NAME, "_formatselect_")
    _available_keywords_title = (By.XPATH, "//div[@id='report_content']/descendant::th[.='Available keywords']")

    def __init__(self, theme):
        self._driver = DriverManager().get_instance().get_driver()
        self._wait = DriverManager().get_instance().get_wait()
        self.theme = theme

    def click_clear_basket_link(self):
        """
        Clicks Clear Basket link.
        """
        return self

    def click_batch_keyword_apply_link(self):
        """
        Clicks Batch Keyword Apply link.
        """
        return self

    def click_download_archive_of_fpos_link(self):
        """
        Clicks Download Archive of FPOs link.
        """
        return self

    def click_batch_image_order_link(self):
        """
        Clicks Batch Image Order link.
        """
        return self

    def click_apply_keywords_button(self):
        """
        Clicks the Apply Keywords button.
        """
        self._driver.find_element(*self._apply_keywords_button).click()
        self._wait.until(ec.invisibility_of_element_located(self._apply_keywords_button))

    def click_download_button(self):
        """
        Clicks the Download button.
        """
        return self

    def click_download_batch_button(self):
        """
        Clicks the Download button in Batch Image Order section.
        """
        try:
            click_element(self._driver, self._driver.find_element(*self._apply_keywords_button))
            self._wait.until(ec.invisibility_of_element_located(self._apply_keywords_button))
        except TimeoutException:
            self._driver.find_element(*self._apply_keywords_button).click()
            self._wait.until(ec.invisibility_of_element_located(self._apply_keywords_button))

    def click_close_batch_report_dialog_button(self):
        """
        Clicks close modal content button
        """
        return self
    
    def click_batch_report_link(self):
        """
        Clicks Batch report link.
        """
        return self
    
    def click_generate_batch_report_button(self):
        """
        Clicks Generate Batch Report button.
        """
        return self

    def close_apply_keyword_modal(self):
        """
        Click the 'x' button to  close the keyword modal.
        """
        return self

    def close_batch_report(self):
        """
        Clicks Close button in batch report.
        """
        parent_page = self._driver.current_window_handle
        try:
            self._driver.switch_to_window(self._driver.window_handles[-1])
            self._wait.until(ec.visibility_of_element_located(self._close_batch_report_button)).click()
        finally:
            self._driver.switch_to_window(parent_page)

    def select_report_preview_option(self, report_name):
        """
        Selects the report preview option.
        :param report_name: Type of report to select.
        """
        return self

    def select_metadata_checkbox(self, metadata_name):
        """
        Checks the metadata option.
        :param metadata_name: The metadata name to select.
        """
        metadata_checkbox = (By.XPATH, "//th[contains(text(),'" + metadata_name + "')]/input[@type='checkbox']")
        self._wait.until(ec.element_to_be_clickable(metadata_checkbox))
        if metadata_name == "wnv_text":
            metadata_checkbox = (By.XPATH, "//th[contains(text(),'" + metadata_name + "') and not(contains(text(),'" + metadata_name + "_'))]/input[@type='checkbox']")
        elif metadata_name == "wnv_text_popup":
            metadata_checkbox = (By.XPATH, "//th[contains(text(),'" + metadata_name + "') and not(contains(text(),'" + metadata_name + "_'))]/input[@type='checkbox']")
        select_checkbox(self._driver, *metadata_checkbox)

    def select_show_annotations_checkbox(self, show_type):
        """
        Checks the show keywords or annotations according to type of show.
        :param show_type: The type of show to check (keywords or annotations)
        """
        return self

    def _select_date(self, date_list):
        """
        Selects the date in the combo boxes.
        :param date_list: A list containing the date to select, e.g. December  21  2012.
        """
        row = 1
        for date in date_list:
            date_selector = (By.XPATH, "//th[contains(text(),'wnv_date')]/input[@type='checkbox']/following::select[" + str(row) + " ]")
            select = Select(self._driver.find_element(*date_selector))
            select.select_by_visible_text(date)
            row += 1

    def _select_text_popup(self, value):
        """
        Selects the text_popup value.
        :param value: Value to select.
        """
        select = Select(self._driver.find_element(*self._text_popup_combobox))
        select.select_by_visible_text(value)

    def _set_text(self, text_type, text, combo_value):
        """
        Sets the text and combo values according the text type.
        :param text_type: Metadata type.
        :param text: Text value to type.
        """
        if text_type == "wnv_text":
            _text_box_selector = (By.XPATH, "//th[contains(text(),'" + text_type + "') and not(contains(text(),'wnv_text_'))]/input[@type='checkbox']/following::input[@type='text']")
            _combo_box_selector = (By.XPATH, "//th[contains(text(),'" + text_type + "') and not(contains(text(),'wnv_text_'))]/input[@type='checkbox']/following::select")
        else:
            _text_box_selector = (By.XPATH, "//th[contains(text(),'" + text_type + "')]/input[@type='checkbox']/following::input[@type='text']")
            _combo_box_selector = (By.XPATH, "//th[contains(text(),'" + text_type + "')]/input[@type='checkbox']/following::select")
        self._driver.find_element(*_text_box_selector).clear()
        self._driver.find_element(*_text_box_selector).send_keys(text)
        Select(self._driver.find_element(*_combo_box_selector)).select_by_visible_text(combo_value)

    def _select_boolean_checkbox(self, boolean):
        """
        Checks the boolean value.
        :param boolean: Boolean value: True or False.
        """
        if boolean:
            self._driver.find_element_by_xpath("//input[contains(@name,'checkboxkeyword')]").click()

    def select_convert_file_format_checkbox(self):
        """
        Checks the Convert File Format option.
        """
        select_checkbox(self._driver, *self._convert_file_format_checkbox)
        self._wait.until(ec.visibility_of_element_located(self._select_format_combobox))

    def select_format_option(self, format_name):
        """
        Select the Format option.
        :param format_name: The format to select.
        """
        select = Select(self._driver.find_element(*self._select_format_combobox))
        select.select_by_visible_text(format_name)

    def set_archive_name(self, archive_name):
        """
        Sets the download archive name.
        :param archive_name: The name of the archive.
        """
        self._driver.find_element(*self._archive_name_textbox).clear()
        self._driver.find_element(*self._archive_name_textbox).send_keys(archive_name)

    def set_batch_archive_name(self, archive_name):
        """
        Sets the Batch Image Order archive name.
        :param archive_name: The name of the batch archive.
        """
        self._driver.find_element(*self._batch_archive_name_textbox).clear()
        self._driver.find_element(*self._batch_archive_name_textbox).send_keys(archive_name)

    def set_metadata_default_values(self, default_data_field_list_values):
        """
        Sets the metadata values by default.
        :param default_data_field_list_values: A list of MD values to set in the batchapply.
        """
        self.click_batch_keyword_apply_link()
        self.apply_keyword_to_fields_list(default_data_field_list_values)
        self.click_apply_keywords_button()
        self.click_clear_basket_link()

    def apply_keyword_to_fields_list(self, metadata_list):
        """
        Applies keyword values to a metadata list.
        :param metadata_list: List of metadata list values, e.g.
                            @{wnv_text} =  wnv_text  five_text  Replace
                            @{wnv_text_popup} =  wnv_text_popup  kiwi
                            @{data_field_list} =  ${wnv_text}  ${wnv_text_popup}
        """
        for metadata in metadata_list:
            i = iter(metadata)
            field = i.next()
            self.select_metadata_checkbox(field)
            if field == "wnv_text":
                self._set_text(field, i.next(), i.next())
            elif field == "wnv_text_popup":
                self._select_text_popup(i.next())
            elif field == "wnv_date":
                self._select_date(i.next())
            elif field == "wnv_text_xmp":
                self._set_text(field, i.next(), i.next())
            elif field == "wnv_int":
                self._set_text(field, i.next(), i.next())
            elif field == "wnv_bool":
                self._select_boolean_checkbox(i.next())
            elif field == "wnv_float":
                self._set_text(field, i.next(), i.next())
            elif field == "wnv_text_accent":
                self._set_text(field, i.next(), i.next())
            elif field == "Author":
                self._set_text(field, i.next(), i.next())

    def download_archive_of_fpos(self, archive_name):
        """
        Actions to perform a Download archive of FPOs.
        :param archive_name: The name of the archive to download.
        """
        self.click_download_archive_of_fpos_link()
        self.set_archive_name(archive_name)
        self.click_download_button()

    def download_batch_image_order(self, batch_name, format_name):
        """
        Actions to perform a Batch Image Order download.
        :param batch_name: The batch name.
        :param format_name: The format to select.
        """
        self.click_batch_image_order_link()
        self.set_batch_archive_name(batch_name)
        self.select_convert_file_format_checkbox()
        self.select_format_option(format_name)
        self.click_download_batch_button()

    def is_keywords_updated_message_displayed(self):
        """
        Verifies if the keywords message update is displayed.
        :return: True if displayed, otherwise False.
        """
        return is_element_present(self._driver, *self._keywords_updated_text)

    def verify_if_keywords_updated_message_is_displayed(self):
        """
        Assertion to verify if the keywords message update is displayed.
        :return: True if displayed, otherwise False.
        """
        BuiltIn().should_be_true(self.is_keywords_updated_message_displayed())

    def get_basket_elements(self):
        """
        Gets the total quantity of elements added to the Basket.
        :return: The quantity of elements displayed.
        """
        basket_elements_selector = (By.XPATH, self.basket_elements_template)
        return get_quantity_of_elements_displayed_on_page(self._driver, *basket_elements_selector)

    def verify_if_basket_is_empty(self):
        """
        Verifies if the Basket is empty (Elements displayed equals to 0).
        """
        BuiltIn().should_be_equal(self.get_basket_elements(), int(0))

    def is_keyword_value_displayed(self, keyword_value):
        """
        Verifies if the keyword value is displayed.
        :param keyword_value: The keyword value.
        :return: True if displayed, otherwise False.
        """
        return self

    def is_keyword_value_displayed_in_collection(self, keyword_list):
        """
        Verifies if the keyword value is displayed in collection page.
        :param keyword_list: A list of keyword values.
        :return: True if displayed, otherwise False.
        """
        return self

    def is_keyword_value_list_displayed_in_collection(self, keyword_list):
        """
        Verifies if a list of keyword values is displayed in collection page.
        :param keyword_list: A list of keyword values.
        :return: True if displayed, otherwise False.
        """
        return self

    def verify_if_keyword_list_value_is_displayed_in_collection(self, keyword_list):
        """
        Assertion to verify if a list of keyword values is displayed in collection page.
        :param keyword_list: A list of keyword values.
        :return: True if displayed, otherwise False.
        """
        BuiltIn().should_be_true(self.is_keyword_value_list_displayed_in_collection(keyword_list))

    def verify_if_keyword_value_is_displayed_in_collection(self, keyword_list):
        """
        Assertion to verify if the keyword value is displayed in collection page.
        :param keyword_list: A list of keyword values.
        :return: True if displayed, otherwise False.
        """
        BuiltIn().should_be_true(self.is_keyword_value_displayed_in_collection(keyword_list))

    def wait_until_file_is_created(self, file_name):
        """
        Waits until a file is created in a directory.
        :param file_name: The file name to wait.
        """
        file_path = os.path.join(DOWNLOAD_PATH, file_name)
        wait_until_file_is_created(file_path)
        wait_until_file_is_downloaded(file_path)

    def verify_if_annotation_is_displayed_in_batch_report(self, expected_annotation_batch_report):
        """
        Verifies if annotation is displayed in batch report.
        """
        BuiltIn().should_be_true(self.is_annotation_displayed_in_batch_report(expected_annotation_batch_report))
        
    def verify_if_metadata_values_are_displayed_in_batch_report(self, expected_metadata_list, file_name):
        """
        Verifies if metadata value is displayed in batch report
        """
        for expected_metadata in expected_metadata_list:
            BuiltIn().should_be_true(self.is_metadata_value_displayed_in_batch_report(expected_metadata, file_name))

    def is_annotation_displayed_in_batch_report(self, expected_annotation_batch_report):
        """
        Verifies if annotation is displayed in batch report.
        """
        # is_displayed = False
        expected_annotation = (By.XPATH, "//tr[contains(.,'" + expected_annotation_batch_report + "')]/../../../following-sibling::div[@id='report_annotations']")
        parent_page = self._driver.current_window_handle
        try:
            self._driver.switch_to_window(self._driver.window_handles[-1])
            wait_for_load_page()
            self._wait.until(ec.visibility_of_element_located(self._available_keywords_title))
            is_displayed = is_element_present(self._driver, *expected_annotation)
        finally:
            self._driver.switch_to_window(parent_page)
        return is_displayed

    def is_metadata_value_displayed_in_batch_report(self, expected_metadata_batch_report, file_name):
        """
        Verifies if metadata value is displayed in batch report
        """
        # is_displayed = False
        expected_metadata = (By.XPATH, "//th[contains(.,'" + file_name +"')]/../../../following-sibling::table[@class='datatables']/descendant::td[.='" + expected_metadata_batch_report[0] + "']/following-sibling::td[.='" + expected_metadata_batch_report[1] + "']")
        parent_page = self._driver.current_window_handle
        try:
            self._driver.switch_to_window(self._driver.window_handles[-1])
            wait_for_load_page()
            self._wait.until(ec.visibility_of_element_located(self._available_keywords_title))
            is_displayed = is_element_present(self._driver, *expected_metadata)
        finally:
            self._driver.switch_to_window(parent_page)
        return is_displayed

    def verify_if_a_file_is_downloaded(self, file_name):
        """
        Assertion to verify if the file is downloaded from Collection.
        :param file_name: The file name to verify.
        """
        file_path = os.path.join(DOWNLOAD_PATH, file_name)
        BuiltIn().should_be_true(is_file_present_in_directory(file_path))

    def extract_file(self, file_name):
        """
        Extract all the files from a compressed file.
        :param file_name: The file name to extract.
        """
        file_path = os.path.join(DOWNLOAD_PATH, file_name)
        extract_file(file_path)

    def verify_if_file_list_extracted_is_displayed(self, file_list):
        """
        Assertion to verify if the list of extracted files is displayed.
        :param file_list: A list of files to verify its presence.
        """
        for file_name in file_list:
            self.verify_if_a_file_is_downloaded(file_name)
