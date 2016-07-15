__author__ = 'MarceloM Guzman'

import os
from datetime import date, timedelta

from robot.libraries.BuiltIn import BuiltIn
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from resources.methods.DBMethods import get_folder_content
from resources.methods.UIMethods import is_element_present, scroll_down, \
    click_element, wait_for_load_page, move_mouse_to
from resources.uiabstraction.components.widgets.filecontentmodal.FileContentModalMarquee import FileContentModalMarquee
from resources.uiabstraction.components.widgets.foldercontent.FolderContentBase import FolderContentBase


class FolderContentMarquee(FolderContentBase):
    """
    Page object modeling the structure and operations of the Folder Content page for Marquee template.
    """
    # Selectors
    list_view = (By.XPATH, "//div[contains(@class,'list-group-item filebox ')]")
    _dates_section = (By.XPATH, "//div[contains(@class,'table-condensed dates') and @style='margin: 0px; display: block;']")
    _all_files_short_view = (By.XPATH, "//div[@class='thumbnail filebox pull-left']")
    _no_more_items_message = (By.XPATH, "//em[text()='No more items']")
    _upload_message = (By.XPATH, "//h4[contains(text(),'Please enter metadata for this file')]")
    
    _xwnv_date_range_button = (By.XPATH, "//input[@value='xwnv:DateRange']")
    _clear_all_filters_button = (By.XPATH, "//button[contains(text(),'Clear all filters')]")
    _copy_file_button = (By.XPATH, "//button[@class='btn btn-primary copy']")
    _submit_button = (By.XPATH, "//button[@class='btn btn-primary submit']")
    _yes_button = (By.XPATH, "//button[@class='btn btn-primary']")
    _upload_files_button = (By.XPATH, "//div[@class='modal-footer']//button[text()='Upload Files']")
    _dismiss_button = (By.XPATH, "//div[@class='modal-footer']//button[text()='Dismiss']")

    _date_range_picker_start = (By.XPATH, "//input[@name='daterangepicker_start']")
    _date_range_picker_end = (By.XPATH, "//input[@name='daterangepicker_end']")
    _thumbnails_content = (By.ID, "thumbnails")
    _annotations_group = (By.XPATH, "//div[contains(@class,'annotations')]")
    _file_modal = (By.ID, "myModalLabel")
    _required_value_textbox = (By.XPATH, "//dt[contains(text(),'wnv_text_uploader_rq')]/following::input[@type='text']")
    _file_data = (By.NAME, "filedata")
    _play_button = (By.XPATH, "//div[@class='vjs-big-play-button']")

    def __init__(self):
        FolderContentBase.__init__(self, "Marquee")
        self.folder_locator_template = "//div[contains(@data-modaltitle,'%s')]"
        self.short_view_locator_template = (By.XPATH, "//div[@class='thumbnail filebox pull-left']")
        self.file_actions_section_locator_template = (By.XPATH, "//div[contains(@class,'filebuttons') and not(@style='display: none;')]")
        self.action_locator_template = "//div[contains(@class,'filebuttons')]/a[@title='%s']"
        self.file_metadata_info_section_locator_template = (By.XPATH, "//div[contains(@class,'table-condensed keywords') and @style='margin: 0px; display: block;']")
        self.metadata_field_locator_template = "//div[contains(@class,'table-condensed keywords') and @style='margin: 0px; display: block;']/dl/dt[text()='%s']"
        self.element_to_wait_locator_template = (By.XPATH, "//a[@id='addalltobasket']/span")
        self.basket_locator_template = "//a[contains(@data-modaltitle,'%s')]/following-sibling::div/a/span[contains(@class,'cart-in')]"
        self.basket_icon_selected_template = "//a[contains(@data-modaltitle,'%s')]/following-sibling::div/a/span[contains(@class,'cart-out')]"
        self.manage_files_locator_template = "//a[contains(@data-modaltitle,'%s')]/following::div/a[@class='btn btn-link filemanager ']"
        self.cancel_icon_locator_template = "//a[contains(@data-modaltitle,'%s')]/following-sibling::div/a[@class='btn btn-link cancel']"

    def click_xwnvDateRange_button(self):
        """
        Clicks the xwnv:DateRange button
        """
        # self._driver.refresh()  # TODO: Temporal fix until XIN-6051 is fixed
        # wait_for_load_page()
        self._wait.until(ec.visibility_of_element_located(self._xwnv_date_range_button)).click()

    def click_today_button(self):
        """
        Clicks the today button in the calendar
        """
        self._wait.until(ec.element_to_be_clickable(self._today_button)).click()
        self._wait.until(ec.visibility_of_element_located(self._clear_all_filters_button))

    def click_clear_all_filters_button(self):
        """
        Clicks the clear all filters button
        """
        if self._driver.find_element(*self._clear_all_filters_button).is_displayed():
            self._wait.until(ec.element_to_be_clickable(self._clear_all_filters_button)).click()
            wait_for_load_page()
            self._wait.until(ec.invisibility_of_element_located(self._clear_all_filters_button))

    def click_yesterday_button(self):
        """
        Clicks the yesterday button in the calendar
        """
        self._wait.until(ec.element_to_be_clickable(self._yesterday_button)).click()
        self._wait.until(ec.visibility_of_element_located(self._clear_all_filters_button))

    def click_last_7days_button(self):
        """
        Clicks last 7 days button in the calendar
        """
        self._wait.until(ec.element_to_be_clickable(self._last_7days_button)).click()
        self._wait.until(ec.visibility_of_element_located(self._clear_all_filters_button))

    def click_last_30days_button(self):
        """
        Clicks last 30 days button in the calendar
        """
        self._wait.until(ec.element_to_be_clickable(self._last_30days_button)).click()
        self._wait.until(ec.visibility_of_element_located(self._clear_all_filters_button))

    def click_this_month_button(self):
        """
        Clicks this month button in the calendar
        """
        self._wait.until(ec.element_to_be_clickable(self._this_month_button)).click()
        self._wait.until(ec.visibility_of_element_located(self._clear_all_filters_button))

    def click_last_month_button(self):
        """
        Clicks last month button in the calendar
        """
        self._wait.until(ec.element_to_be_clickable(self._last_month_button)).click()
        self._wait.until(ec.visibility_of_element_located(self._clear_all_filters_button))

    def click_custom_range_button(self):
        """
        Clicks custom range button in the calendar
        """
        self._wait.until(ec.element_to_be_clickable(self._custom_range_button)).click()
        today = date.today().strftime('%b/%d/%Y')
        yesterday = (date.today() - timedelta(days=1)).strftime('%b/%d/%Y')
        self.select_date_start_in_calendar(yesterday)
        self.select_date_end_in_calendar(today)
        self.click_apply_button()
        self._wait.until(ec.visibility_of_element_located(self._clear_all_filters_button))

    def click_copy_button(self):
        """
        Clicks the Copy button.
        """
        self._driver.find_element(*self._copy_file_button).click()
        self._wait.until(ec.visibility_of_element_located(self._file_name_textbox))

    def click_submit_button(self):
        """
        Clicks the Copy button to submit the form.
        """
        self._driver.find_element(*self._submit_button).click()
        self._wait.until(ec.invisibility_of_element_located(self._file_modal))

    def click_upload_files_button(self):
        """
        Clicks the Upload Files button.
        """
        self._driver.find_element(*self._upload_files_button).click()
        self._wait.until(ec.visibility_of_element_located(self._dismiss_button))
        self._wait.until(ec.invisibility_of_element_located(self._dismiss_button))
        
    def click_download_high_resolution_button(self, file_name):
        """
        Clicks the Download High Res button.
        :param file_name: The file name on which to click the Download High Res button.
        """
        download_high_res_selector = (By.XPATH, "//div[@class='popover-content']/a[contains(@href,'" + file_name + "')]")
        self._wait.until(ec.visibility_of_element_located(download_high_res_selector))
        click_element(self._driver, self._driver.find_element(*download_high_res_selector))

    def click_yes_button(self):
        """
        Clicks the Yes button.
        """
        self._driver.find_element(*self._yes_button).click()
        self._wait.until(ec.invisibility_of_element_located(self._file_modal))

    def click_copy_icon(self, file_name):
        """
        Clicks the Copy icon.
        :param file_name: The file name on which to click the Copy icon.
        """
        copy_icon_selector = (By.XPATH, "//a[contains(@data-modaltitle,'" + file_name + "')]/following-sibling::div/a[@class='btn btn-link copy ']")
        self._wait.until(ec.visibility_of_element_located(copy_icon_selector), "The Copy icon of " + file_name + " element is not available to be clicked ")
        click_element(self._driver, self._driver.find_element(*copy_icon_selector))
        self._wait.until(ec.visibility_of_element_located(self._file_modal))

    def click_rename_icon(self, file_name):
        """
        Clicks the Rename icon.
        :param file_name: The file name on which to click the Rename icon.
        """
        rename_icon_selector = (By.XPATH, "//a[contains(@data-modaltitle,'" + file_name + "')]/following-sibling::div/a[@class='btn btn-link rename ']")
        self._wait.until(ec.visibility_of_element_located(rename_icon_selector), "The Rename icon of " + file_name + " element is not available to be clicked ")
        click_element(self._driver, self._driver.find_element(*rename_icon_selector))
        self._wait.until(ec.visibility_of_element_located(self._submit_button))

    def click_delete_icon(self, file_name):
        """
        Clicks the Delete icon.
        :param file_name: The file name on which to click the Delete icon.
        """
        delete_icon_selector = (By.XPATH, "//a[contains(@data-modaltitle,'" + file_name + "')]/following-sibling::div/a[@class='btn btn-link trash ']")
        self._wait.until(ec.visibility_of_element_located(delete_icon_selector), "The Delete icon of " + file_name + " element is not available to be clicked ")
        click_element(self._driver, self._driver.find_element(*delete_icon_selector))
        self._wait.until(ec.visibility_of_element_located(self._file_modal))

    def click_download_options_icon(self, file_name):
        """
        Clicks the Download icon.
        :param file_name: The file name on which to click the Download icon.
        """
        download_icon_selector = (By.XPATH, "//a[contains(@data-modaltitle,'" + file_name + "')]/following::span[contains(@class,'glyphicons-download-alt')]")
        try:
            _hover_element = self._driver.find_element_by_xpath("//a[contains(@data-modaltitle,'" + file_name + "')]/following::span[contains(@class,'glyphicons-download-alt')]")
            move_mouse_to(self._driver, _hover_element)
            self._driver.find_element(*download_icon_selector).click()
            self._wait.until(ec.visibility_of_element_located((By.XPATH, "//div/h3[contains(.,'Download Options')]")))
        except (Exception, TimeoutException) as ex:
            print ex
            click_element(self._driver, self._driver.find_element(*download_icon_selector))

    def is_list_view_applied_in_folder_content(self):
        """
        Returns True if the list view mode is applied in the folder content pane, otherwise False.
        """
        return is_element_present(self._driver, *self.list_view)
    
    def verify_if_list_view_is_applied_in_folder_content(self):
        """
        Verifies if the list view mode is applied in the folder content pane.
        """
        BuiltIn().should_be_true(self.is_list_view_applied_in_folder_content())

    # Dates section
    def is_dates_section_displayed_in_file(self, file_name):
        """
        Verifies if the dates section is displayed for a file.
        :param file_name: file name
        :return: True if the Date section is displayed.
        """
        file_date_section = (By.XPATH, "//div[contains(@class,'table-condensed dates') and not(contains(@style,'none'))]/preceding-sibling::div/small[@title='" + file_name + "']")
        return is_element_present(self._driver, *file_date_section)

    def is_dates_section_displayed_in_folder_content(self, folder_path, folder_name):
        """
        Verifies if the dates section is displayed for all files that belongs to a folder in the folder content pane.
        :param folder_path: A list of folders path. e.g. karina_wnv  2015 Bare Bones Test Files  Images
        :param folder_name: Folder name to search in the data base for its content.
        :return: True if the Date section is displayed.
        """
        folder_content_list = get_folder_content(folder_path, folder_name)
        is_displayed = None
        for folder in folder_content_list:
            print folder
            is_displayed = self.is_dates_section_displayed_in_file(folder[0])
            print is_displayed
            if not is_displayed:
                break
        return is_displayed

    def verify_if_dates_section_is_displayed_in_file(self, folder_path, folder_name):
        """
        Verifies if the dates section is displayed for a file.
        :param folder_path: A list of folders path. e.g. karina_wnv  2015 Bare Bones Test Files  Images
        :param folder_name: Folder name to search in the data base for its content.
        """
        BuiltIn().should_be_true(self.is_dates_section_displayed_in_folder_content(folder_path, folder_name))

    def scroll_down_until_page_is_loaded(self):
        """
        Scrolls down until the page is completely loaded (In Short view).
        """
        prior = 0
        while True:
            scroll_down()
            current = len(self._wait.until(ec.presence_of_all_elements_located(self._all_files_short_view)))
            if current == prior:
                return current
            prior = current

    def is_no_more_items_message_displayed(self):
        """
        Verifies if the 'No more items' message is displayed.
        :return: True if displayed otherwise False.
        """
        return is_element_present(self._driver, *self._no_more_items_message)

    def verify_if_no_more_items_message_is_displayed(self):
        """
        Verifies if the 'No more items' message is displayed.
        """
        BuiltIn().should_be_true(self.is_no_more_items_message_displayed())

    def click_view_file(self, file_name):
        """
        Clicks the select file to display the "view file", e.g. rd_Old_Tom_and_Jerry_Open.mpg, 2MonthsAgo.indd
        :param file_name: The file name.
        """
        video_alt = (By.XPATH, "//img[contains(@alt,'" + file_name + "')]")
        file_link = (By.XPATH, "//a[contains(@data-modaltitle,'" + file_name + "')]")
        file_locator = []
        _file_name_image = (By.XPATH, "//div[contains(@id,'details-file')]//img[@alt='" + file_name + "']")
        if is_element_present(self._driver, *video_alt):
            file_locator = video_alt
        elif is_element_present(self._driver, *file_link):
            file_locator = file_link
        self._wait.until(ec.visibility_of_element_located(file_locator))
        click_element(self._driver, self._driver.find_element(*file_locator))
        self._wait.until(ec.visibility_of_element_located(_file_name_image))

    def click_view_video_file(self, video_name):
        """
        Clicks the Video file.
        :param video_name: The file name.
        """
        video_alt = (By.XPATH, "//img[contains(@alt,'" + video_name + "')]")
        file_link = (By.XPATH, "//a[contains(@data-modaltitle,'" + video_name + "')]")
        file_locator = []
        if is_element_present(self._driver, *video_alt):
            file_locator = video_alt
        elif is_element_present(self._driver, *file_link):
            file_locator = file_link
        self._wait.until(ec.visibility_of_element_located(file_locator))
        click_element(self._driver, self._driver.find_element(*file_locator))
        self._wait.until(ec.visibility_of_element_located(self._play_button))

    def set_values_for_xwnvDateRange(self, file_names):
        """
        Sets the dates for xwnv:DateRange with each file. 
        e.g. 2MonthsAgo, 5DaysAgo, LastMonth, Today and Yesterday
        :param file_names: The file names 
        """
        for filename in file_names:
            self.click_view_file(filename)
            modal = FileContentModalMarquee()
            calculated_date = self.calculate_date_according_filename(filename)
            modal.set_date_in_file_content_modal("xwnv:DateRange", calculated_date)
            self._calculated_dates.append(calculated_date)
            modal.click_save_all_button()
            modal.click_close_file_content_modal()

    def set_file_path_upload(self, file_name):
        """
        Sets the path of the file to upload.
        :param file_name: The file name.
        """
        path = os.path.join(os.getcwd(), "downloads", file_name)
        self._driver.find_element(*self._file_data).send_keys(path)
        self._wait.until(ec.visibility_of_element_located(self._upload_message))

    def set_required_value_upload(self, required_value):
        """"
        Set required value to the uploaded file.
        :param required_value: Any value.
        """
        self._driver.find_element(*self._required_value_textbox).clear()
        self._driver.find_element(*self._required_value_textbox).send_keys(required_value)

    def get_date_according_to_the_format_displayed_in_folder_content_page(self, date_without_format):
        """
        Gets the date according to the format displayed in Folder content page, e.g. February 4, 2016.
        Example about a date without format December/04/2015.
        :return: The select date with format month/day/year.
        """
        select_day = self.get_day_without_cero_at_beginning(date_without_format.split('/')[1])
        month = date_without_format.split('/')[0]
        year = date_without_format.split('/')[2]
        select_date = month + " " + select_day + ", " + year
        return select_date
    
    def is_xwnvDateRange_value_displayed(self, filename, calculated_date):
        """
        Verifies if the xwnvDateRange value is displayed according to the file.
        :return: True if xwnvDateRange value is displayed, otherwise False.
        """
        is_displayed = False
        select_date = self.get_date_according_to_the_format_displayed_in_folder_content_page(calculated_date)
        date_to_verify = (By.XPATH, "//div[@data-filename='" + filename + "']/div/div[contains(@class,'table table-condensed')]/dl/dt[text()='xwnv:DateRange']/following-sibling::dd[text()='" + select_date + "']")
        if is_element_present(self._driver, *date_to_verify):
            is_displayed = True
        return is_displayed
    
    def verify_if_xwnvDateRange_value_is_displayed(self, file_names):
        """
        Verifies if the xwnvDateRange value is displayed in each file, 
        e.g. xwnvDateRange value = December 10, 2015 
             file name = 5DaysAgo.indd.
        :param file_names: The file names.
        """
        index = 0
        for filename in file_names:
            BuiltIn().should_be_true(self.is_xwnvDateRange_value_displayed(filename, self._calculated_dates[index]))
            index += 1

    def is_xwnvDateRange_displaying_the_date_according_selected_range(self, selected_range):
        """
        Verify if the xwnvDateRange button is displaying a range of dates according the selected range in the calendar.
        :param selected_range: The selected range in the calendar, e.g Today, Yesterday.
        :return: True if the selected range is displayed, otherwise False.
        """
        is_displayed = False
        xwnv_DateRange_button = (By.XPATH, "//button[text()='xwnv:DateRange: " + self.date_range_calculator(selected_range) + "']")
        if is_element_present(self._driver, *xwnv_DateRange_button):
            is_displayed = True
        return is_displayed
    
    def select_date_start_in_calendar(self, value):
        """
        Selects the date start to custom-range in the calendar.
        :param value: The date start to select.
        """
        selected_month = value.split('/')[0]
        selected_day = self.get_day_without_cero_at_beginning(value.split('/')[1])
        selected_year = value.split('/')[2]
        selected_day_calendar_left = (By.XPATH, "//div[@class='calendar second left']/div/table/tbody/tr/td[@class!='available off' and @class!='available off in-range' and text()='" + selected_day + "']")
        selected_month_calendar_left = (By.XPATH, "//div[@class='calendar second left']/div/table/thead/tr/th[@class='month' and text()='" + selected_month + " " + selected_year + "']")
        if is_element_present(self._driver, *selected_month_calendar_left):
            self._wait.until(ec.element_to_be_clickable(selected_day_calendar_left)).click()
        else:
            next_available_calendar_left = (By.XPATH, "//div[@class='calendar second left']/div/table/thead/tr/th[@class='next available']")
            self._wait.until(ec.element_to_be_clickable(next_available_calendar_left)).click()
            if is_element_present(self._driver, *selected_month_calendar_left):
                    self._wait.until(ec.element_to_be_clickable(selected_day_calendar_left)).click()
            else:
                print "Error when looking for the correct month in calendar left: ", value
    
    def select_date_end_in_calendar(self, value):
        """
        Selects the date end to custom-range in the calendar.
        :param value: The date end to select.
        """
        selected_month = value.split('/')[0]
        selected_day = self.get_day_without_cero_at_beginning(value.split('/')[1])
        selected_year = value.split('/')[2]
        selected_day_calendar_left = (By.XPATH, "//div[@class='calendar first right']/div/table/tbody/tr/td[@class!='available off' and @class!='available off in-range' and text()='" + selected_day + "']")
        selected_month_calendar_left = (By.XPATH, "//div[@class='calendar first right']/div/table/thead/tr/th[@class='month' and text()='" + selected_month + " " + selected_year + "']")
        if is_element_present(self._driver, *selected_month_calendar_left):
            self._wait.until(ec.element_to_be_clickable(selected_day_calendar_left)).click()
        else:
            print "Error when looking for the correct month in calendar right: ", value

    def delete_file(self, file_name):
        """
        Deletes the file.
        :param file_name: The file name to delete.
        """
        self.click_manage_files_icon(file_name)
        self.click_delete_icon(file_name)
        self.click_yes_button()
    
    def is_metadata_value_displayed_in_folder_content(self, filename, expected_metadata):
        """
        Verifies if a metadata value is displayed in folder content.
        :param filename: The file name to select.
        :param expected_metadata: The metadata to verify.
        """
        actual_metadata_value = (By.XPATH, "//div[@data-modaltitle='" + filename + "']/following-sibling::div[@class='text-center']/descendant::dt[.='" + expected_metadata[0] + "']/following-sibling::dd[.='" + expected_metadata[1] + "']")
        return is_element_present(self._driver, *actual_metadata_value)
        
    def click_show_annotations_icon(self, file_name):
        """
        Clicks the Annotations icon.
        :param file_name: The file name.
        """
        _pencil_span = (By.XPATH, "//a[contains(@class,'annotation ') and @data-modaltitle='" + file_name + "']")
        self._wait.until(ec.element_to_be_clickable(_pencil_span))
        click_element(self._driver, self._driver.find_element(*_pencil_span))
        self._wait.until(ec.visibility_of_element_located(self._annotations_group))
