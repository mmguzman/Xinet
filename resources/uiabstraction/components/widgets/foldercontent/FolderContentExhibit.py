__author__ = 'MarceloM Guzman'

import os
from datetime import date, timedelta

from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from resources.methods.UIMethods import is_element_present, get_quantity_of_elements_displayed_on_page, \
    click_element, wait_for_load_page
from resources.uiabstraction.components.widgets.basictoolsbar.BasicToolsToolbarExhibit import BasicToolsToolbarExhibit
from resources.uiabstraction.components.widgets.filecontentmodal.FileContentModalExhibit import FileContentModalExhibit
from resources.uiabstraction.components.widgets.foldercontent.FolderContentBase import FolderContentBase


class FolderContentExhibit(FolderContentBase):
    """
    Page object modeling the structure and operations of the Folder Content page for Exhibit template.
    """
    
    # Selectors
    _icon_view = (By.XPATH, "//div[@id='filelist']/div[@class='preview_outerbox iconview']")
    _long_view = (By.XPATH, "//div[@class='preview_innerbox long' and contains(@style,'height: 116px;')]")
    _page_list_section = (By.XPATH, "//span[@class='pagelist']")
    _element_displayed_short_view_locator = (By.XPATH, "//div[@class='preview_outerbox']")
    _element_displayed_icon_view_locator = (By.XPATH, "//div[@class='preview_outerbox iconview']")
    _filter_tab_active = (By.XPATH, "//li[@id='filtertab' and @class='active']")
    _filters_link = (By.XPATH, "//a/small[text()='Filters']")
    _metadata_flip_button = (By.ID, "metadataflip")
    _go_button = (By.CSS_SELECTOR, "button.btn.btn-default")
    _copy_file_button = (By.XPATH, "//button/span[text()='Copy']")
    _submit_button = (By.XPATH, "//button/span[text()='Submit']")
    _yes_button = (By.XPATH, "//button[@class='btn btn-primary']")
    _upload_file_button = (By.ID, "uploadfileinput0")
    _upload_file_indicator_off = (By.ID, "uploadindicatoroff0")
    _upload_file_indicator_on = (By.ID, "uploadindicatoron0")

    _date_range_link = (By.XPATH, "//a[contains(text(),'Date Range')]")
    _annotation_canvas = (By.ID, "canvasBuffer")
    _date_range_text = (By.XPATH, "//small[text()='xwnv:DateRange']/following::li/descendant::input[contains(@id,'daterange')]")

    _clear_all_filters_link = (By.XPATH, "//a[@title='Clear all filters']")
    _filters_content = (By.XPATH, "//ul[@class='unstyled']")

    _file_modal = (By.ID, "ui-id-1")
    _copy_dialog = (By.XPATH, "//div[@role='dialog' and @aria-describedby='filemgr']")
    _rename_dialog = (By.XPATH, "//div[@role='dialog' and @aria-describedby='fileMgrDialogue']")
    _confirm_delete_label = (By.XPATH, "//span[contains(.,'delete this file?')]")
    _file_manager_table = (By.ID, "filemgrnav")
    _file_list_in_copy_dialog = (By.XPATH, "//div[@id='filemgr']/descendant::div[@id='filelist']")
    _text_annotation_button = (By.ID, "textButton")
    
    def __init__(self):
        FolderContentBase.__init__(self, "Exhibit")
        self.folder_locator_template = "//div[@id='filelist']/descendant::div[@title='%s']"
        self.short_view_locator_template = (By.XPATH, "//div[@class='preview_innerbox short' and @style='height: 116px; width: 240px;']")
        self.file_actions_section_locator_template = (By.XPATH, "//div[@class='fileactions']")
        self.action_locator_template = "//div[@class='fileactions']/a[@title='%s']"
        self.file_metadata_info_section_locator_template = (By.XPATH, "//div[@class='techinfo']")
        self.metadata_field_locator_template = "//div[@class='techinfo']//td[@class='textright' and contains(text(),'%s')]"
        self.element_to_wait_locator_template = (By.ID, "viewtype")
        self.value_locator_template = "//span[@class='pagelist']/a[@class='show_index' and text()='%s']"
        self.basket_locator_template = "//a[contains(@class,'icon_basket') and contains(@name,'%s')]"
        self.basket_icon_selected_template = "//a[(contains(@class,'icon_basket_checked')) and contains(@name,'%s')]"
        self.manage_files_locator_template = "//div[@title='%s']/following::a[@title='Manage Files']"
        self.cancel_icon_locator_template = "//div[@title='%s']/following::a[@title='Cancel']"

    def click_xwnvDateRange_button(self):
        """
        Clicks the xwnv:DateRange button
        """
        self.click_filters_link()
        self._wait.until(ec.visibility_of_element_located(self._date_range_text)).click()

    def click_today_button(self):
        """
        Clicks the today button in the calendar
        """
        self._wait.until(ec.element_to_be_clickable(self._today_button)).click()
        self._wait.until(ec.element_to_be_clickable(self._go_button)).click()
        self._wait.until(ec.visibility_of_element_located(self._clear_all_filters_link))

    def click_clear_all_filters_button(self):
        """
        Clicks the clear all filters button
        """
        if is_element_present(self._driver, *self._clear_all_filters_link):
            self._wait.until(ec.element_to_be_clickable(self._clear_all_filters_link)).click()
            self.wait_for_folder_content_page_loaded()
            self._wait.until(ec.invisibility_of_element_located(self._clear_all_filters_link))

    def click_yesterday_button(self):
        """
        Clicks the yesterday button in the calendar
        """
        self._wait.until(ec.element_to_be_clickable(self._yesterday_button)).click()
        self._wait.until(ec.element_to_be_clickable(self._go_button)).click()
        self._wait.until(ec.visibility_of_element_located(self._clear_all_filters_link))

    def click_last_7days_button(self):
        """
        Clicks last 7 days button in the calendar
        """
        self._wait.until(ec.element_to_be_clickable(self._last_7days_button)).click()
        self._wait.until(ec.element_to_be_clickable(self._go_button)).click()
        self._wait.until(ec.visibility_of_element_located(self._clear_all_filters_link))

    def click_last_30days_button(self):
        """
        Clicks last 30 days button in the calendar
        """
        self._wait.until(ec.element_to_be_clickable(self._last_30days_button)).click()
        self._wait.until(ec.element_to_be_clickable(self._go_button)).click()
        self._wait.until(ec.visibility_of_element_located(self._clear_all_filters_link))

    def click_this_month_button(self):
        """
        Clicks this month button in the calendar
        """
        self._wait.until(ec.element_to_be_clickable(self._this_month_button)).click()
        self._wait.until(ec.element_to_be_clickable(self._go_button)).click()
        self._wait.until(ec.visibility_of_element_located(self._clear_all_filters_link))

    def click_last_month_button(self):
        """
        Clicks last month button in the calendar
        """
        self._wait.until(ec.element_to_be_clickable(self._last_month_button)).click()
        self._wait.until(ec.element_to_be_clickable(self._go_button)).click()
        self._wait.until(ec.visibility_of_element_located(self._clear_all_filters_link))

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
        self._wait.until(ec.element_to_be_clickable(self._go_button)).click()
        self._wait.until(ec.visibility_of_element_located(self._clear_all_filters_link))

    def click_copy_button(self):
        """
        Clicks the Copy button.
        """
        self._wait.until(ec.visibility_of_element_located(self._copy_file_button)).click()
        self._wait.until(ec.visibility_of_element_located(self._file_name_textbox))

    def click_submit_button(self):
        """
        Clicks the Copy button to submit the form.
        """
        self._driver.find_element(*self._submit_button).click()
        self._wait.until(ec.invisibility_of_element_located(self._copy_dialog))
        wait_for_load_page()

    def click_upload_files_button(self):
        """
        Clicks the Upload Files button.
        """
        self._driver.find_element(*self._upload_file_button).click()
        self._wait.until(ec.visibility_of_element_located(self._upload_file_indicator_on))

    def click_submit_button_for_delete_dialog(self):
        """
        Clicks the Copy button to submit the form.
        """
        self._wait.until(ec.visibility_of_element_located(self._confirm_delete_label))
        self._driver.find_element(*self._submit_button).click()
        self._wait.until(ec.invisibility_of_element_located(self._rename_dialog))
        wait_for_load_page()

    def click_download_high_resolution_button(self, file_name):
        """
        Clicks the Download High Res button.
        """
        download_high_res_selector = (By.XPATH, "//div[@title='" + file_name + "']/following::a[@title='Download High-Res']")
        self._wait.until(ec.element_to_be_clickable(download_high_res_selector)).click()

    def click_copy_icon(self, file_name):
        """
        Clicks the Copy icon.
        """
        copy_icon_selector = (By.XPATH, "//div[@title='" + file_name + "']/following::a[contains(@class,'icon_filemgr_copy')]")
        self._wait.until(ec.visibility_of_element_located(copy_icon_selector), "The Copy icon of " + file_name + " element is not available to be clicked ")
        click_element(self._driver, self._driver.find_element(*copy_icon_selector))
        self._wait.until(ec.visibility_of_element_located(self._file_manager_table))
        
    def click_rename_icon(self, file_name):
        """
        Clicks the Rename icon.
        """
        rename_icon_selector = (By.XPATH, "//div[@title='" + file_name + "']/following::a[contains(@class,'icon_filemgr_rename')]")
        self._wait.until(ec.visibility_of_element_located(rename_icon_selector), "The Rename icon of " + file_name + " element is not available to be clicked ")
        click_element(self._driver, self._driver.find_element(*rename_icon_selector))
        self._wait.until(lambda s: s.find_element(*self._rename_dialog).is_displayed())

    def click_delete_icon(self, file_name):
        """
        Clicks the Rename icon.
        """
        delete_icon_selector = (By.XPATH, "//div[@title='" + file_name + "']/following::a[contains(@class,'icon_filemgr_trash')]")
        self._wait.until(ec.visibility_of_element_located(delete_icon_selector), "The Delete icon of " + file_name + " element is not available to be clicked ")
        click_element(self._driver, self._driver.find_element(*delete_icon_selector))
        self._wait.until(lambda s: s.find_element(*self._rename_dialog).is_displayed())

    def is_icon_view_applied_in_folder_content(self):
        """
        Returns True if the icon view mode is applied in the folder content pane, otherwise False.
        """
        return is_element_present(self._driver, *self._icon_view)
    
    def verify_if_icon_view_is_applied_in_folder_content(self):
        """
        Verifies if the icon view mode is applied in the folder content pane.
        """
        BuiltIn().should_be_true(self.is_icon_view_applied_in_folder_content())
    
    def is_long_view_applied_in_folder_content(self):
        """
        Returns True if the long view mode is applied in the folder content pane, otherwise False.
        """
        return is_element_present(self._driver, *self._long_view)

    def verify_if_long_view_is_applied_in_folder_content(self):
        """
        Verifies if the long view mode is applied in the folder content pane.
        """
        BuiltIn().should_be_true(self.is_long_view_applied_in_folder_content())

    def is_page_list_section_displayed_in_folder_content(self):
        """
        Returns true if the page list section is displayed in folder content pane.
        """
        return is_element_present(self._driver, *self._page_list_section)
     
    def verify_if_page_list_section_is_displayed_in_folder_content(self):
        """
        Verifies if the page list section is displayed in folder content pane.
        """
        BuiltIn().should_be_true(self.is_page_list_section_displayed_in_folder_content())
    
    def verify_if_quantity_of_elements_is_displayed(self, quantity_expected, view_type='Short View'):
        """
        Verifies if a quantity of elements is displayed in folder content pane.
        :param quantity_expected: Quantity to be expected.
        :param view_type: Type of view such as Icon view, Short view or Long view.
        """
        if view_type == "Icon View":
            quantity_displayed = get_quantity_of_elements_displayed_on_page(self._driver, *self._element_displayed_icon_view_locator)
        else:
            quantity_displayed = get_quantity_of_elements_displayed_on_page(self._driver, *self._element_displayed_short_view_locator)
        BuiltIn().should_be_equal(quantity_displayed, int(quantity_expected))
    
    def click_link_in_page_list_section(self, value):
        """
        Clicks a link, whether a value or symbol in page list section.
        """
        value_selector = (By.XPATH, self.value_locator_template % value)
        self._driver.find_element(*value_selector).click()
        self.wait_for_folder_content_page_loaded()
        
    def is_link_displayed_in_page_list_section(self, value):
        """
        Verifies if a link whether a value or symbol, is displayed in folder content pane.
        :param value: Value to search.
        :return: True if displayed, otherwise False.
        """
        value_selector = (By.XPATH, self.value_locator_template % value)
        return is_element_present(self._driver, *value_selector)
    
    def verify_if_link_is_displayed_in_page_list_section(self, value):
        """
        Verifies if a link whether a value or symbol, is displayed in folder content pane.
        :param value: Value to search.
        :return: True if displayed, otherwise False.
        """
        BuiltIn().should_be_true(self.is_link_displayed_in_page_list_section(value))

    def verify_if_link_is_not_displayed_in_page_list_section(self, value):
        """
        Verifies if a link whether a value or symbol, is not displayed in folder content pane.
        :param value: Value to search.
        :return: True if not displayed, otherwise False.
        """
        BuiltIn().should_not_be_true(self.is_link_displayed_in_page_list_section(value))
    
    def click_view_file(self, file_name):
        """
        Clicks the select file to display the "view file", e.g. rd_Old_Tom_and_Jerry_Open.mpg, 2MonthsAgo.indd
        :param file_name: The file name.
        """
        video_alt = (By.XPATH, "//img[contains(@alt,'" + file_name + "')]")
        self._wait.until(ec.visibility_of_element_located(video_alt)).click()
        wait_for_load_page()
    
    def set_values_for_xwnvDateRange(self, file_names):
        """
        Sets the dates for xwnv:DateRange with each file. 
        e.g. 2MonthsAgo, 5DaysAgo, LastMonth, Today and Yesterday
        :param file_names: The file names 
        """
        modal = FileContentModalExhibit()
        for filename in file_names:
            self.click_view_file(filename)
            calculated_date = self.calculate_date_according_filename(filename)
            self._wait.until(ec.visibility_of_element_located(self._annotation_canvas))
            click_element(self._driver, self._driver.find_element(*self._metadata_flip_button))
            modal.set_date_in_file_content_modal("xwnv:DateRange", calculated_date)
            modal.click_save_all_button()
            BasicToolsToolbarExhibit().click_folder_link_in_breadcrumbs("Date Range")

    def set_file_path_upload(self, file_name):
        """
        Sets the path of the file to upload.
        :param file_name: The file name.
        """
        path = os.path.join(os.getcwd(), "downloads", file_name)
        self._driver.find_element(*self._upload_file_button).send_keys(path)
        self._wait.until(ec.invisibility_of_element_located(self._upload_file_indicator_off))

    def click_filters_link(self):
        """
        Clicks the filters link.
        """
        self._driver.find_element(*self._filters_link).click()
        self._wait.until(ec.visibility_of_element_located(self._date_range_text))

    def is_xwnvDateRange_displaying_the_date_according_selected_range(self, selected_range):
        """
        Verify if the xwnvDateRange button is displaying a range of dates according to the selected range in the calendar.
        :param selected_range: The selected range in the calendar, e.g Today, Yesterday.
        :return: True if the selected range is displayed, otherwise False.
        """
        is_displayed = False
        xwnv_DateRange_button = (By.XPATH, "//span[text()='xwnv:DateRange: " + self.date_range_calculator(selected_range) + " ']")
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
        selected_day_calendar_left = (By.XPATH, "//div[@class='calendar left']/div/table/tbody/tr/td[@class!='available off' and @class!='available off in-range' and text()='" + selected_day + "']")
        selected_month_calendar_left = (By.XPATH, "//div[@class='calendar left']/div/table/thead/tr/th[@class='month' and text()='" + selected_month + " " + selected_year + "']")
        if is_element_present(self._driver, *selected_month_calendar_left):
            self._wait.until(ec.element_to_be_clickable(selected_day_calendar_left)).click()
        else:
            next_available_calendar_left = (By.XPATH, "//div[@class='calendar left']/div/table/thead/tr/th[@class='next available']")
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
        selected_day_calendar_left = (By.XPATH, "//div[@class='calendar right']/div/table/tbody/tr/td[@class!='available off' and @class!='available off in-range' and text()='" + selected_day + "']")
        selected_month_calendar_left = (By.XPATH, "//div[@class='calendar right']/div/table/thead/tr/th[@class='month' and text()='" + selected_month + " " + selected_year + "']")
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
        self.click_submit_button_for_delete_dialog()
        
    def is_metadata_value_displayed_in_folder_content(self, filename, expected_metadata):
        """
        Verifies if a metadata value is displayed in folder content.
        :param filename: The file name to select.
        :param expected_metadata: The metadata to verify.
        """
        if expected_metadata[2] == "combo":
            actual_metadata_value = (By.XPATH, "//div[contains(@title,'" + filename + "')]/../following::div[@class='techinfo']/descendant::td[.='" + expected_metadata[0] + "']/following-sibling::td/descendant::option[@selected='selected' and @value='" + expected_metadata[1] + "']")
        elif expected_metadata[2] == "text":
            actual_metadata_value = (By.XPATH, "//div[contains(@title,'" + filename + "')]/../following::div[@class='techinfo']/descendant::td[.='" + expected_metadata[0] + "']/following-sibling::td/input[@value='" + expected_metadata[1] + "']")
        return is_element_present(self._driver, *actual_metadata_value)
    
    def click_show_annotations_icon(self, file_name):
        """
        Clicks the Show Annotations icon.
        :param file_name: The file name.
        """
        pencil_button = (By.XPATH, "//a[contains(@class,'annotation') and contains(@href,'" + file_name + "')]")
        self._wait.until(ec.element_to_be_clickable(pencil_button)).click()
        wait_for_load_page()
        self._wait.until(ec.visibility_of_element_located(self._text_annotation_button))
