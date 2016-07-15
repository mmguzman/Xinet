__author__ = 'MarceloM Guzman'

from calendar import monthrange
from datetime import date, timedelta

from dateutil.relativedelta import relativedelta
from robot.libraries.BuiltIn import BuiltIn
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from resources.commons.DriverManager import DriverManager
from resources.methods.DBMethods import get_folder_content
from resources.methods.UIMethods import is_element_present, wait_for_load_page, click_element, \
    get_random_name


class FolderContentBase(object):
    """
    Page object modeling the structure and operations of the Folder Content page.
    """
    _driver = None
    _wait = None
    _calculated_dates = []

    # Selectors
    _video_alt_img = (By.XPATH, "//img[@alt='2MonthsAgo.indd']")
    _apply_button = (By.XPATH, "//button[text()='Apply']")
    _date_range_base = "//li[text()='%s']"
    _file_name_textbox = (By.NAME, "newname")

    def __init__(self, theme):
        self._driver = DriverManager().get_instance().get_driver()
        self._wait = DriverManager().get_instance().get_wait()
        self.theme = theme
        self._today_button = (By.XPATH, self._date_range_base % 'Today')
        self._yesterday_button = (By.XPATH, self._date_range_base % 'Yesterday')
        self._last_7days_button = (By.XPATH, self._date_range_base % 'Last 7 days')
        self._last_30days_button = (By.XPATH, self._date_range_base % 'Last 30 days')
        self._this_month_button = (By.XPATH, self._date_range_base % 'This Month')
        self._last_month_button = (By.XPATH, self._date_range_base % 'Last Month')
        self._custom_range_button = (By.XPATH, self._date_range_base % 'Custom Range')

    def get_page_title(self):
        """
        Gets the title of the page.
        """
        return self._driver.title

    def click_xwnvDateRange_button(self):
        """
        Clicks the xwnv:DateRange button
        """
        return self

    def click_today_button(self):
        """
        Clicks the today button in the calendar
        """
        return self

    def click_clear_all_filters_button(self):
        """
        Clicks the clear all filters button
        """
        return self

    def click_yesterday_button(self):
        """
        Clicks the yesterday button in the calendar
        """
        return self

    def click_last_7days_button(self):
        """
        Clicks last 7 days button in the calendar
        """
        return self

    def click_last_30days_button(self):
        """
        Clicks last 30 days button in the calendar
        """
        return self

    def click_this_month_button(self):
        """
        Clicks this month button in the calendar
        """
        return self

    def click_last_month_button(self):
        """
        Clicks last month button in the calendar
        """
        return self

    def click_custom_range_button(self):
        """
        Clicks custom range button in the calendar
        """
        return self

    def click_apply_button(self):
        """
        Clicks the Apply button in the calendar
        """
        self._wait.until(ec.element_to_be_clickable(self._apply_button)).click()

    def click_submit_button(self):
        """
        Clicks the Copy button to submit the form.
        """
        return self

    def click_upload_files_button(self):
        """
        Clicks the Upload Files button.
        """
        return self

    def click_add_to_basket_icon(self, file_name):
        """
        Clicks the Add to basket icon.
        :param file_name: File name to select.
        """
        add_to_basket_selector = (By.XPATH, self.basket_locator_template % file_name)
        basket_icon_selected_selector = (By.XPATH, self.basket_icon_selected_template % file_name)
        # self._wait.until(ec.visibility_of_element_located(add_to_basket_selector), "The " + file_name + " element is not available to be clicked ")
        click_element(self._driver, self._driver.find_element(*add_to_basket_selector))
        self._wait.until(ec.visibility_of_element_located(basket_icon_selected_selector))

    def click_manage_files_icon(self, file_name):
        """
        Clicks the Manage Files icon.
        """
        manage_files_selector = (By.XPATH, self.manage_files_locator_template % file_name)
        cancel_icon_selector = (By.XPATH, self.cancel_icon_locator_template % file_name)
        self._wait.until(ec.visibility_of_element_located(manage_files_selector), "The Manage Files icon of " + file_name + " element is not available to be clicked ")
        click_element(self._driver, self._driver.find_element(*manage_files_selector))
        self._wait.until(ec.visibility_of_element_located(cancel_icon_selector))

    def click_copy_icon(self, file_name):
        """
        Clicks the Copy icon.
        :param file_name: The file name on which to click the Copy icon.
        """
        return self

    def click_rename_icon(self, file_name):
        """
        Clicks the Rename icon.
        :param file_name: The file name on which to click the Rename icon.
        """
        return self

    def click_download_options_icon(self, file_name):
        """
        Clicks the Download icon.
        :param file_name: The file name on which to click the Download icon.
        """
        return self

    def click_delete_icon(self, file_name):
        """
        Clicks the Delete icon.
        :param file_name: The file name on which to click the Delete icon.
        """
        return self

    def click_show_annotations_icon(self, file_name):
        """
        Clicks the Annotations icon.
        :param file_name: The file name.
        """
        return self

    def click_copy_button(self):
        """
        Clicks the Copy button
        """
        return self

    def click_download_high_resolution_button(self, file_name):
        """
        Clicks the Download High Res button.
        :param file_name: The file name on which to click the Download High Res button.
        """
        return self

    def click_yes_button(self):
        """
        Clicks the Yes button.
        """
        return self

    def click_view_file(self, file_name):
        """
        Clicks the select file to display the "view file", e.g. rd_Old_Tom_and_Jerry_Open.mpg, 2MonthsAgo.indd
        :param file_name: The file name.
        """
        return self

    def click_view_video_file(self, video_name):
        """
        Clicks the Video file.
        :param video_name: The file name.
        """
        return self

    def set_values_for_xwnvDateRange(self, file_names):
        """
        Sets the dates for xwnv:DateRange with each file.
        e.g. 2MonthsAgo, 5DaysAgo, LastMonth, Today and Yesterday
        :param file_names: The file names
        """
        return self

    def set_file_name(self, file_name):
        """
        Sets the file name
        :param file_name: The file name.
        """
        self._driver.find_element(*self._file_name_textbox).clear()
        self._driver.find_element(*self._file_name_textbox).send_keys(file_name)

    def set_file_path_upload(self, file_name):
        """
        Sets the path of the file to upload.
        :param file_name: The file name.
        """
        return self

    def set_required_value_upload(self, required_value):
        """
        Set required value to the uploaded file.
        :param required_value: Any value.
        """
        return self

    def select_date_start_in_calendar(self, value):
        """
        Selects the date start to custom-range in the calendar.
        :param value: The date start to select.
        """
        return self

    def select_date_end_in_calendar(self, value):
        """
        Selects the date end to custom-range in the calendar.
        :param value: The date end to select.
        """
        return self

    def get_day_without_cero_at_beginning(self, day):
        """
        Gets the day without zero at beginning of the word e.g. from 02 to 2
        :return: The day.
        """
        if day[0] == "0":
            day = day[1]
        return day

    def add_list_to_basket(self, file_list):
        """
        Add a list of files to the basket.
        :param file_list: The list of files to be added to the basket.
        """
        for file_name in file_list:
            self.click_add_to_basket_icon(file_name)

    def is_folder_displayed_in_folder_content(self, folder_name):
        """
        Verifies if a folder is displayed in folder content.
        :param folder_name: Folder name.
        :return: True if a folder name is displayed, otherwise False.
        """
        folder_name_selector = (By.XPATH, self.folder_locator_template % folder_name)
        return is_element_present(self._driver, *folder_name_selector)

    def verify_if_file_is_displayed_according_to_value_set(self, file_name):
        """
        Verifies if the file is displayed in folder content according to value set in Filters tab.
        :param file_name: File name.
        """
        BuiltIn().should_be_true(self.is_folder_displayed_in_folder_content(file_name))

    def is_folder_content_displayed_in_folder_content(self, folder_path, folder_name):
        """
        Verifies if all folder and files that belongs to a folder are displayed in the folder content pane.
        :param folder_path: A list of folders path. e.g. karina_wnv  2015 Bare Bones Test Files  Images
        :param folder_name: Folder name to search in the data base for its content.
        :return: True if the content is displayed, otherwise False.
        """
        folder_content_list = get_folder_content(folder_path, folder_name)
        is_displayed = None
        for folder in folder_content_list:
            print folder
            is_displayed = self.is_folder_displayed_in_folder_content(folder[0])
            if not is_displayed:
                break
        return is_displayed

    def verify_if_folder_content_is_displayed_in_folder_content(self, folder_path, folder_name):
        """
        Verifies if all folder and files that belongs to a folder are displayed in the folder content pane.
        :param folder_path: A list of folders path. e.g. karina_wnv  2015 Bare Bones Test Files  Images
        :param folder_name: Folder name to search in the data base for its content.
        :return: True if the content is displayed, otherwise False.
        """
        BuiltIn().should_be_true(self.is_folder_content_displayed_in_folder_content(folder_path, folder_name))

    def verify_if_folder_content_is_not_displayed_in_folder_content(self, folder_path, folder_name):
        """
        Verifies if all folder and files that belongs to a folder are not displayed in the folder content pane.
        :param folder_path: A list of folders path. e.g. karina_wnv  2015 Bare Bones Test Files  Images
        :param folder_name: Folder name to search in the data base for its content.
        :return: True if the content is displayed, otherwise False.
        """
        BuiltIn().should_not_be_true(self.is_folder_content_displayed_in_folder_content(folder_path, folder_name))

    def is_icon_view_applied_in_folder_content(self):
        """
        Returns True if the icon view mode is applied in the folder content pane, otherwise False.
        """
        return self

    def verify_if_icon_view_is_applied_in_folder_content(self):
        """
        Verifies if the icon view mode is applied in the folder content pane.
        """
        BuiltIn().should_be_true(self.is_icon_view_applied_in_folder_content())

    def is_short_view_applied_in_folder_content(self):
        """
        Returns True if the short view mode is applied in the folder content pane, otherwise False.
        """
        return is_element_present(self._driver, *self.short_view_locator_template)

    def verify_if_short_view_is_applied_in_folder_content(self):
        """
        Verifies if the short view mode is applied in the folder content pane.
        """
        BuiltIn().should_be_true(self.is_short_view_applied_in_folder_content())

    def is_list_view_applied_in_folder_content(self):
        """
        Returns True if the list view mode is applied in the folder content pane, otherwise False.
        """
        return self

    def verify_if_list_view_is_applied_in_folder_content(self):
        """
        Verifies if the list view mode is applied in the folder content pane.
        """
        return self

    def is_long_view_applied_in_folder_content(self):
        """
        Returns True if the long view mode is applied in the folder content pane, otherwise False.
        """
        return self

    def verify_if_long_view_is_applied_in_folder_content(self):
        """
        Verifies if the long view mode is applied in the folder content pane.
        """
        return self

    # File Actions section
    def is_file_actions_section_displayed_under_folder_in_folder_content(self):
        """
        Returns True if the section for the file actions icons is displayed below the folder or file
        in the folder content pane, otherwise False.
        """
        return is_element_present(self._driver, *self.file_actions_section_locator_template)

    def verify_if_file_actions_section_is_not_displayed_under_folder_in_folder_content(self):
        """
        Verifies if the section for the file actions icons is not displayed below the folder or file
        in the folder content pane.
        """
        BuiltIn().should_not_be_true(self.is_file_actions_section_displayed_under_folder_in_folder_content())

    def is_file_action_displayed_under_folder_in_folder_content(self, action_name):
        """
        Verifies if the file action icon given in ``action_name`` argument is displayed below the folder or file
        in the folder content pane.
        :param action_name:  Action name to search.
        :return: Returns True if is displayed, otherwise False.
        """
        action_name_selector = (By.XPATH, self.action_locator_template % action_name)
        try:  # TODO - Remove try-except block when Add to collection option is completely updated.
            if self.theme == "Exhibit":
                return is_element_present(self._driver, *action_name_selector)
            else:
                return self._driver.find_element(*action_name_selector).is_displayed()
        except NoSuchElementException:
                print "The " + action_name_selector[1] + " locator was not found."
                return False

    def verify_if_file_action_is_displayed_under_folder_in_folder_content(self, action_name):
        """
        Verifies if the file action icon given in ``action_name`` argument is displayed below the folder or file
        in the folder content pane.
        :param action_name:  Action name to search.
        :return: Returns True if is displayed, otherwise False.
        """
        BuiltIn().should_be_true(self.is_file_action_displayed_under_folder_in_folder_content(action_name))

    def is_file_action_list_displayed_under_folder_in_folder_content(self, actions_list):
        """
        Verifies if the list of file actions icons given in ``action_list`` argument is displayed
        below the folder or file in the folder content pane
        :param actions_list:  List of actions to search.
        :return: Returns True if is displayed, otherwise False.
        """
        # TODO - Remove if blocks when Add to collection option is completely updated.
        is_displayed = None
        for action in actions_list:
            is_displayed = self.is_file_action_displayed_under_folder_in_folder_content(action)
            if not is_displayed and action == "Add to basket":
                is_displayed = self.is_file_action_displayed_under_folder_in_folder_content("Add to collection")
            if not is_displayed and action == "Add to basket":
                is_displayed = self.is_file_action_displayed_under_folder_in_folder_content("")
            if not is_displayed:
                break
        return is_displayed

    def verify_if_file_action_list_is_displayed_under_folder_in_folder_content(self, actions_list):
        """
        Verifies if the list of file actions icons given in ``action_list`` argument is displayed
        below the folder or file in the folder content pane
        :param actions_list:  List of actions to search.
        :return: Returns True if is displayed, otherwise False.
        """
        BuiltIn().should_be_true(self.is_file_action_list_displayed_under_folder_in_folder_content(actions_list))

    def verify_if_file_action_list_is_not_displayed_under_folder_in_folder_content(self, actions_list):
        """
        Verifies if the list of file actions icons given in ``action_list`` argument is not displayed
        below the folder or file in the folder content pane
        :param actions_list:  List of actions to search.
        :return: Returns True if is displayed, otherwise False.
        """
        BuiltIn().should_not_be_true(self.is_file_action_list_displayed_under_folder_in_folder_content(actions_list))

    # MetaData section
    def is_file_metadata_section_displayed_under_folder_in_folder_content(self):
        """
        Returns True if the section for the file metadata info is displayed below the folder or file
        in the folder content pane, otherwise False.
        """
        return is_element_present(self._driver, *self.file_metadata_info_section_locator_template)

    def verify_if_file_metadata_section_is_not_displayed_under_folder_in_folder_content(self):
        """
        Verifies if the section for the file metadata info is not displayed below the folder or file
        in the folder content pane.
        """
        BuiltIn().should_not_be_true(self.is_file_metadata_section_displayed_under_folder_in_folder_content())

    def is_file_metadata_field_displayed_under_folder_in_folder_content(self, metadata_name):
        """
        Verifies if the file metadata given in ``metadata_name`` is displayed below the folder or file
        in the folder content pane
        :param metadata_name: Metadata name.
        :return: True if is displayed, otherwise False.
        """
        metadata_name_selector = (By.XPATH, self.metadata_field_locator_template % metadata_name)
        return is_element_present(self._driver, *metadata_name_selector)

    def verify_if_file_metadata_field_is_displayed_under_folder_in_folder_content(self, metadata_name):
        """
        Verifies if the file metadata given in ``metadata_name`` is displayed below the folder or file
        in the folder content pane
        :param metadata_name: Metadata name.
        :return: True if is displayed, otherwise False.
        """
        BuiltIn().should_be_true(self.is_file_metadata_field_displayed_under_folder_in_folder_content(metadata_name))

    def is_file_metadata_list_displayed_under_folder_in_folder_content(self, metadata_list):
        """
        Verifies if the list of metadata given in ``metadata_list`` is displayed below the folder or file
        in the folder content pane
        :param metadata_list: List of metadata files.
        :return: True if is displayed, otherwise False.
        """
        is_displayed = None
        for metadata in metadata_list:
            is_displayed = self.is_file_metadata_field_displayed_under_folder_in_folder_content(metadata)
            if not is_displayed:
                break
        return is_displayed

    def verify_if_file_metadata_list_is_displayed_under_folder_in_folder_content(self, metadata_list):
        """
        Verifies if the list of metadata given in ``metadata_list`` is displayed below the folder or file
        in the folder content pane
        :param metadata_list: List of metadata files.
        :return: True if is displayed, otherwise False.
        """
        BuiltIn().should_be_true(self.is_file_metadata_list_displayed_under_folder_in_folder_content(metadata_list))

    def wait_for_folder_content_page_loaded(self):
        """
        Waits until the the folder content page is loaded.
        """
        wait_for_load_page()
        self._wait.until(lambda s: s.find_element(*self.element_to_wait_locator_template))

    def calculate_date_according_filename(self, filename):
        """
        Calculates the date according to the file name. 
        :return: The calculated date with format: month/day/year.
        """
        date_calculator = {"2MonthsAgo.indd": date.today() - relativedelta(months=2),
                           "5DaysAgo.indd": date.today() - timedelta(days=5),
                           "LastMonth.indd": date.today() - relativedelta(months=1),
                           "Today.indd": date.today(),
                           "Yesterday.indd": date.today() - timedelta(days=1)}
        calculated_date = date_calculator[filename]
        return calculated_date.strftime('%B/%d/%Y')

    def date_range_calculator(self, selected_range):
        """
        The date range calculator allows to get ranges according to
        the options in the calendar, e.g. Today, Yesterday.
        :return selected_range: The selected range.
        """
        today = date.today().strftime('%m/%d/%Y')
        yesterday = (date.today() - timedelta(days=1)).strftime('%m/%d/%Y')
        last_7days = (date.today() - timedelta(days=6)).strftime('%m/%d/%Y')
        last_30days = (date.today() - timedelta(days=29)).strftime('%m/%d/%Y')

        days_passed = date.today().day - 1
        days_left = monthrange(date.today().year, date.today().month)[1] - date.today().day
        this_date_start = (date.today() - timedelta(days=days_passed)).strftime('%m/%d/%Y')
        this_date_end = (date.today() + timedelta(days=days_left)).strftime('%m/%d/%Y')

        last_date_start = ((date.today() - timedelta(days=days_passed)) - relativedelta(months=1)).strftime('%m/%d/%Y')
        last_date_end = (date.today() - timedelta(days=date.today().day)).strftime('%m/%d/%Y')

        date_range_calculator = {"Today_range": today + " - " + today,
                                 "Yesterday_range": yesterday + " - " + yesterday,
                                 "Last_7days_range": last_7days + " - " + today,
                                 "Last_30days_range": last_30days + " - " + today,
                                 "This_Month_range": this_date_start + " - " + this_date_end,
                                 "Last_Month_range": last_date_start + " - " + last_date_end,
                                 "Custom_range": yesterday + " - " + today
                                 }
        return date_range_calculator[selected_range]

    def verify_if_xwnvDateRange_value_is_displayed(self, file_names):
        """
        Verifies if the xwnvDateRange value is displayed in each file,
        e.g. xwnvDateRange value = December 10, 2015
             file name = 5DaysAgo.indd.
        :param file_names: The file names.
        """
        return self

    def is_file_displayed_in_folder_content(self, file_name):
        """
        Verifies if a file is displayed in folder content.
        """
        video_alt = (By.XPATH, "//img[@alt='" + file_name + "']")
        file_link = (By.XPATH, "//a[@data-modaltitle='" + file_name + "']")
        return is_element_present(self._driver, *video_alt) or is_element_present(self._driver, *file_link)

    def verify_if_files_are_displayed_according_to_selected_range(self, expected_files, selected_date_range=None):
        """
        Verifies if files are displayed according to the selected range
        e.g. Today (range) - should just be displayed a file 'Today.indd' 
        """
        for filename in expected_files:
            if selected_date_range == "This Month" and filename == "5DaysAgo.indd":
                if date.today().day >= 6:
                    BuiltIn().should_be_true(self.is_file_displayed_in_folder_content(filename))
            elif selected_date_range == "This Month" and filename == "Yesterday.indd":
                if date.today().day >= 2:
                    BuiltIn().should_be_true(self.is_file_displayed_in_folder_content(filename))
            else:
                BuiltIn().should_be_true(self.is_file_displayed_in_folder_content(filename))

    def verify_if_xwnvDateRange_is_displaying_dates_according_selected_range(self, selected_range):
        """
        Verifies if the xwnvDateRange button is displaying a range of dates according to selected range in the calendar.
        e.g. xwnv:DateRange: 02/06/2016 - 02/06/2016
        """
        BuiltIn().should_be_true(self.is_xwnvDateRange_displaying_the_date_according_selected_range(selected_range))

    def verify_if_file_is_displayed_in_folder_content(self, file_name):
        """
        Verifies if a file is displayed in Folder Content pane.
        :param file_name: The file name to verify.
        :return: True if displayed, otherwise False.
        """
        BuiltIn().should_be_true(self.is_file_displayed_in_folder_content(file_name))

    def verify_if_file_is_not_displayed_in_folder_content(self, file_name):
        """
        Verifies if a file is not displayed in Folder Content pane.
        :param file_name: The file name to verify.
        :return: True if not displayed, otherwise False.
        """
        BuiltIn().should_not_be_true(self.is_file_displayed_in_folder_content(file_name))

    def wait_until_file_is_copied(self, file_name):
        """
        Waits until the file appears in the Folder Content section.
        :param file_name: The file name to wait.
        """
        count = 0
        while count < 10 and not self.is_file_displayed_in_folder_content(file_name):
            self._driver.refresh()
            self.wait_for_folder_content_page_loaded()
            count += 1

    def copy_file_folder_content(self, file_name, file_name_copied):
        """
        Copies a file and set a new name.
        :param file_name:  The file name to copy.
        :param file_name_copied: The new file name.
        """
        if self.is_file_displayed_in_folder_content(file_name_copied):
            self.delete_file(file_name_copied)
        self.click_manage_files_icon(file_name)
        self.click_copy_icon(file_name)
        self.click_copy_button()
        self.set_file_name(file_name_copied)
        self.click_submit_button()

    def rename_file(self, file_name, file_name_renamed):
        """
        Renames the file with a new name.
        :param file_name: The file name to rename.
        :param file_name_renamed: The new file name.
        """
        if self.is_file_displayed_in_folder_content(file_name_renamed):
            self.delete_file(file_name_renamed)
        self.click_manage_files_icon(file_name)
        self.click_rename_icon(file_name)
        self.set_file_name(file_name_renamed)
        self.click_submit_button()

    def download_file(self, file_name):
        """
        Downloads the file.
        :param file_name: The file name to download.
        """
        self.click_download_options_icon(file_name)
        self.click_download_high_resolution_button(file_name)

    def delete_file(self, file_name):
        """
        Deletes the file.
        :param file_name: The file name to delete.
        """
        return self

    def is_metadata_value_displayed_in_folder_content(self, filename, expected_metadata):
        """
        Verifies if a metadata value is displayed in folder content.
        :param filename: The file name to select.
        :param expected_metadata: The metadata to verify.
        """
        return self

    def verify_if_metadata_value_is_displayed_in_folder_content(self, filename, expected_metadata):
        """
        Verifies if metadata value is displayed in folder content.
        :param filename: The file name to select.
        :param expected_metadata: The metadata to verify.
        """
        BuiltIn().should_be_true(self.is_metadata_value_displayed_in_folder_content(filename, expected_metadata))
    
    def generate_random_file_name(self, file_extension):
        """
        Generates a random file name.
        :param file_extension: The extension of file name to create. 
        :return: A random name.
        """
        return "auto" + get_random_name() + str(file_extension)

    def upload_file(self, file_name, required_value):
        """"
        Steps to upload a file.
        :param file_name: The file name to upload.
        :param required_value: Any value to fill on 'wnv_text_uploader_rq' field.
        """
        self.set_file_path_upload(file_name)
        self.set_required_value_upload(required_value)
        self.click_upload_files_button()
        wait_for_load_page()
