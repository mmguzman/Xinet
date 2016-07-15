__author__ = 'MarceloM Guzman'

from resources.commons.GlobalVariables import TEMPLATE
from resources.uiabstraction.PageObjectFactory import PageObjectFactory


class FolderContentSteps:
    """
    Steps definition for Folder Content page object.
    """
    _folder_content = None

    def __init__(self):
        self._folder_content = PageObjectFactory.create_folder_content(TEMPLATE)

    def get_page_title(self):
        """
        Gets the title of the page.
        """
        return self._folder_content.get_page_title()

    def is_folder_displayed_in_folder_content(self, folder_name):
        """
        Verifies if a folder given in ``folder_name`` is displayed in folder content.
        :param folder_name: folder name.
        :return: True if a folder name is displayed, otherwise False.
        """
        return self._folder_content.is_folder_displayed_in_folder_content(folder_name)

    def is_folder_content_displayed_in_folder_content(self, folder_path, folder_name):
        """
        Returns True if all the folders and files that belongs to a folder are displayed
        in the folder content pane, otherwise False.
        The folder is identified by the given ``folder_path`` and ``folder_name`` arguments.
        """
        return self._folder_content.is_folder_content_displayed_in_folder_content(folder_path, folder_name)

    def verify_if_folder_content_is_displayed_in_folder_content(self, folder_path, folder_name):
        """
        Verifies if all the folders and files that belongs to a folder are displayed in the folder content pane.
        The folder is identified by the given ``folder_path`` and ``folder_name`` arguments.
        """
        return self._folder_content.verify_if_folder_content_is_displayed_in_folder_content(folder_path, folder_name)

    def verify_if_folder_content_is_not_displayed_in_folder_content(self, folder_path, folder_name):
        """
        Verifies if the folders and files that belongs to a folder are not displayed in the folder content pane.
        The folder is identified by the given ``folder_path`` and ``folder_name`` arguments.
        """
        return self._folder_content.verify_if_folder_content_is_not_displayed_in_folder_content(folder_path, folder_name)

    def is_file_displayed_in_folder_content(self, file_name):
        """
        Verifies if a file is displayed in folder content.
        :param file_name: The file name to verify.
        """
        return self._folder_content.is_file_displayed_in_folder_content(file_name)

    def is_icon_view_applied_in_folder_content(self):
        """
        Returns True if the icon view mode is applied in the folder content pane, otherwise False.
        """
        return self._folder_content.is_icon_view_applied_in_folder_content()

    def verify_if_icon_view_is_applied_in_folder_content(self):
        """
        Verifies if the icon view mode is applied in the folder content pane.
        """
        return self._folder_content.verify_if_icon_view_is_applied_in_folder_content()

    def is_short_view_applied_in_folder_content(self):
        """
        Returns True if the short view mode is applied in the folder content pane, otherwise False.
        """
        return self._folder_content.is_short_view_applied_in_folder_content()

    def verify_if_short_view_is_applied_in_folder_content(self):
        """
        Verifies if the short view mode is applied in the folder content pane.
        """
        return self._folder_content.is_short_view_applied_in_folder_content()

    def is_list_view_applied_in_folder_content(self):
        """
        Returns True if the list view mode is applied in the folder content pane, otherwise False.
        """
        return self._folder_content.is_list_view_applied_in_folder_content()

    def verify_if_list_view_is_applied_in_folder_content(self):
        """
        Verifies if the list view mode is applied in the folder content pane.
        """
        return self._folder_content.verify_if_list_view_is_applied_in_folder_content()

    def is_long_view_applied_in_folder_content(self):
        """
        Returns True if the long view mode is applied in the folder content pane, otherwise False.
        """
        return self._folder_content.is_long_view_applied_in_folder_content()

    def verify_if_long_view_is_applied_in_folder_content(self):
        """
        Verifies if the long view mode is applied in the folder content pane.
        """
        return self._folder_content.verify_if_long_view_is_applied_in_folder_content()

    def verify_if_no_more_items_message_is_displayed(self):
        """
        Verifies if the 'No more items' message is displayed.
        """
        self._folder_content.verify_if_no_more_items_message_is_displayed()

    # Dates section
    def verify_if_dates_section_is_displayed_in_file(self, folder_path, folder_name):
        """
        Verifies if the dates section is displayed for a file.
        """
        return self._folder_content.verify_if_dates_section_is_displayed_in_file(folder_path, folder_name)

    # File Actions section
    def is_file_actions_section_displayed_under_folder_in_folder_content(self):
        """
        Returns True if the section for the file actions icons is displayed below the folder or file
        in the folder content pane, otherwise False.
        """
        return self._folder_content.is_file_actions_section_displayed_under_folder_in_folder_content()

    def verify_if_file_actions_section_is_not_displayed_under_folder_in_folder_content(self):
        """
        Verifies if the section for the file actions icons is not displayed below the folder or file
        in the folder content pane.
        """
        return self._folder_content.verify_if_file_actions_section_is_not_displayed_under_folder_in_folder_content()

    def is_file_action_displayed_under_folder_in_folder_content(self, action_name):
        """
        Returns True if the file action icon given in ``action_name`` argument is displayed below the folder or file
        in the folder content pane, otherwise False.
        """
        return self._folder_content.is_file_action_displayed_under_folder_in_folder_content(action_name)

    def verify_if_file_action_is_displayed_under_folder_in_folder_content(self, action_name):
        """
        Verifies if the file action icon given in ``action_name`` argument is displayed below the folder or file
        in the folder content pane.
        """
        return self._folder_content.verify_if_file_action_is_displayed_under_folder_in_folder_content(action_name)

    def is_file_action_list_displayed_under_folder_in_folder_content(self, actions_list):
        """
        Returns True if the list of file actions icons given in ``action_list`` argument is displayed
        below the folder or file in the folder content pane, otherwise False.
        """
        return self._folder_content.is_file_action_list_displayed_under_folder_in_folder_content(actions_list)

    def verify_if_file_action_list_is_displayed_under_folder_in_folder_content(self, actions_list):
        """
        Verifies if the list of file actions icons given in ``action_list`` argument is displayed
        below the folder or file in the folder content pane.
        """
        return self._folder_content.verify_if_file_action_list_is_displayed_under_folder_in_folder_content(actions_list)

    def verify_if_file_action_list_is_not_displayed_under_folder_in_folder_content(self, actions_list):
        """
        Verifies if the list of file actions icons given in ``action_list`` argument is not displayed
        below the folder or file in the folder content pane.
        """
        return self._folder_content.verify_if_file_action_list_is_not_displayed_under_folder_in_folder_content(actions_list)
    
    # MetaData section
    def is_file_metadata_section_displayed_under_folder_in_folder_content(self):
        """
        Returns True if the section for the file metadata info is displayed below the folder or file
        in the folder content pane, otherwise False.
        """
        return self._folder_content.is_file_metadata_section_displayed_under_folder_in_folder_content()

    def verify_if_file_metadata_section_is_not_displayed_under_folder_in_folder_content(self):
        """
        Verifies if the section for the file metadata info is not displayed below the folder or file
        in the folder content pane.
        """
        return self._folder_content.verify_if_file_metadata_section_is_not_displayed_under_folder_in_folder_content()

    def is_file_metadata_field_displayed_under_folder_in_folder_content(self, metadata_name):
        """
        Returns True if the file metadata given in ``metadata_name`` is displayed below the folder or file
        in the folder content pane, otherwise False.
        """
        return self._folder_content.is_file_metadata_field_displayed_under_folder_in_folder_content(metadata_name)

    def verify_if_file_metadata_field_is_displayed_under_folder_in_folder_content(self, metadata_name):
        """
        Verifies if the file metadata given in ``metadata_name`` is displayed below the folder or file
        in the folder content pane.
        """
        self._folder_content.verify_if_file_metadata_field_is_displayed_under_folder_in_folder_content(metadata_name)

    def is_file_metadata_list_displayed_under_folder_in_folder_content(self, metadata_list):
        """
        Returns True if the list of metadata given in ``metadata_list`` argument is displayed
        below the folder or file in the folder content pane, otherwise False.;
        """
        return self._folder_content.is_file_metadata_list_displayed_under_folder_in_folder_content(metadata_list)

    def verify_if_file_metadata_list_is_displayed_under_folder_in_folder_content(self, metadata_list):
        """
        Verifies if the list of metadata given in ``metadata_list`` argument is displayed
        below the folder or file in the folder content pane.
        """
        self._folder_content.verify_if_file_metadata_list_is_displayed_under_folder_in_folder_content(metadata_list)

    # Page List section
    def click_link_in_page_list_section(self, value):
        """
        Clicks a link, whether a value or symbol in page list section.
        """
        self._folder_content.click_link_in_page_list_section(value)
        
    def is_page_list_section_displayed_in_folder_content(self):
        """
        Returns true if the page list section is displayed in folder content pane.
        """
        self._folder_content.is_page_list_section_displayed_in_folder_content()
        
    def verify_if_page_list_section_is_displayed_in_folder_content(self):
        """
        Verifies if the page list section is displayed in folder content pane.
        """
        self._folder_content.verify_if_page_list_section_is_displayed_in_folder_content()
        
    def verify_if_quantity_of_elements_is_displayed(self, quantity_expected, view_type='Short View'):
        """
        Verifies if a quantity of elements is displayed in folder content pane when selecting a view.
        :param quantity_expected: Quantity of elements expected.
        :param view_type: Type of view: Icon, Short or Long.
        """
        self._folder_content.verify_if_quantity_of_elements_is_displayed(quantity_expected, view_type)
    
    def is_link_displayed_in_page_list_section(self, value):
        """
        Returns true if a link, whether a value or symbol, is displayed in folder content pane.
        """
        self._folder_content.is_link_displayed_in_page_list_section(value)
        
    def verify_if_link_is_displayed_in_page_list_section(self, value):
        """
        Verifies if a link, whether a number or symbol, is displayed in folder content pane.
        """
        self._folder_content.verify_if_link_is_displayed_in_page_list_section(value)
        
    def verify_if_link_is_not_displayed_in_page_list_section(self, value):
        """
        Verifies if a link, whether a number or symbol, is not displayed in folder content pane.
        """
        self._folder_content.verify_if_link_is_not_displayed_in_page_list_section(value)
        
    def wait_for_folder_content_page_loaded(self):
        """
        Waits until the the folder content page is loaded.
        """
        self._folder_content.wait_for_folder_content_page_loaded()

    def scroll_down_until_page_is_loaded(self):
        """
        Scrolls down until the page is completely loaded (In Short view).
        """
        self._folder_content.scroll_down_until_page_is_loaded()
    
    def click_add_to_basket_icon(self, file_name):
        """
        Clicks the Add to basket icon.
        :param file_name: File name to select.
        """
        self._folder_content.click_add_to_basket_icon(file_name)

    def add_list_to_basket(self, file_list):
        """
        Add a list of files to the basket.
        :param file_list: The list of files to be added to the basket.
        """
        self._folder_content.add_list_to_basket(file_list)
    
    def click_view_file(self, file_name):
        """
        Clicks the select file to display the "view file", e.g. rd_Old_Tom_and_Jerry_Open.mpg, 2MonthsAgo.indd
        :param file_name: The file name.
        """
        self._folder_content.click_view_file(file_name)

    def click_view_video_file(self, file_name):
        """
        Clicks the select file to display the "view file", e.g. rd_Old_Tom_and_Jerry_Open.mpg, 2MonthsAgo.indd
        :param file_name: The file name.
        """
        self._folder_content.click_view_video_file(file_name)

    def set_values_for_xwnvDateRange(self, file_names):
        """
        Sets the dates for xwnv:DateRange with each file. 
        e.g. 2MonthsAgo, 5DaysAgo, LastMonth, Today and Yesterday
        :param file_names: The file names
        """
        self._folder_content.set_values_for_xwnvDateRange(file_names)
    
    def verify_if_xwnvDateRange_value_is_displayed(self, file_names):
        """
        Verifies if the xwnvDateRange value is displayed in each file, 
        e.g. xwnvDateRange value = December 10, 2015 
             file name = 5DaysAgo.indd.
        :param file_names: The file names.
        """
        self._folder_content.verify_if_xwnvDateRange_value_is_displayed(file_names)
    
    def click_xwnvDateRange_button(self):
        """
        Clicks the xwnv:DateRange button
        """
        self._folder_content.click_xwnvDateRange_button()
    
    def click_today_button(self):
        """
        Clicks the today button in the calendar
        """
        self._folder_content.click_today_button()
    
    def verify_if_files_are_displayed_according_to_selected_range(self, expected_files, selected_date_rage=None):
        """
        Verifies if files are displayed according to the selected range
        e.g. Today (range) - should just be displayed a file 'Today.indd' 
        """
        self._folder_content.verify_if_files_are_displayed_according_to_selected_range(expected_files, selected_date_rage)
    
    def verify_if_xwnvDateRange_is_displaying_dates_according_selected_range(self, selected_range):
        """
        Verify if the xwnvDateRange button is displaying a range of dates according to the selected range in the calendar.
        e.g. xwnv:DateRange: 02/06/2016 - 02/06/2016
        """
        self._folder_content.verify_if_xwnvDateRange_is_displaying_dates_according_selected_range(selected_range)
        
    def click_clear_all_filters_button(self):
        """
        Clicks the clear all filters button
        """
        self._folder_content.click_clear_all_filters_button()
    
    def click_yesterday_button(self):
        """
        Clicks the yesterday button in the calendar
        """
        self._folder_content.click_yesterday_button()
    
    def click_last_7days_button(self):
        """
        Clicks last 7 days button in the calendar
        """
        self._folder_content.click_last_7days_button()
    
    def click_last_30days_button(self):
        """
        Clicks last 30 days button in the calendar
        """
        self._folder_content.click_last_30days_button()
        
    def click_this_month_button(self):
        """
        Clicks this month button in the calendar
        """
        self._folder_content.click_this_month_button()
    
    def click_last_month_button(self):
        """
        Clicks last month button in the calendar
        """
        self._folder_content.click_last_month_button()
    
    def click_custom_range_button(self):
        """
        Clicks custom range button in the calendar
        """
        self._folder_content.click_custom_range_button()
    
    def verify_if_file_is_displayed_according_to_value_set(self, file_name):
        """
         Verifies if the file is displayed in folder content according to value set in Filters tab.
        :param file_name: File name.
        """
        self._folder_content.verify_if_file_is_displayed_according_to_value_set(file_name)

    def verify_if_file_is_displayed_in_folder_content(self, file_name):
        """
        Verifies if a file is displayed in Folder Content pane.
        :param file_name: The file name to verify.
        :return: True if displayed, otherwise False.
        """
        self._folder_content.verify_if_file_is_displayed_in_folder_content(file_name)

    def verify_if_file_is_not_displayed_in_folder_content(self, file_name):
        """
        Verifies if a file is not displayed in Folder Content pane.
        :param file_name: The file name to verify.
        :return: True if not displayed, otherwise False.
        """
        self._folder_content.verify_if_file_is_not_displayed_in_folder_content(file_name)

    def copy_file_folder_content(self, file_name, file_name_copied):
        """
        Copies a file and set a new name.
        :param file_name:  The file name to copy.
        :param file_name_copied: The new file name.
        """
        self._folder_content.copy_file_folder_content(file_name, file_name_copied)

    def rename_file(self, file_name, file_name_renamed):
        """
        Renames the file with a new name.
        :param file_name: The file name to rename.
        :param file_name_renamed: The new file name.
        """
        self._folder_content.rename_file(file_name, file_name_renamed)

    def download_file(self, file_name):
        """
        Downloads the file.
        :param file_name: The file name to download.
        """
        self._folder_content.download_file(file_name)

    def delete_file(self, file_name):
        """
        Deletes the file.
        :param file_name: The file name to delete.
        """
        self._folder_content.delete_file(file_name)

    def wait_until_file_is_copied(self, file_name):
        """
        Waits until the file appears in the Folder Content section.
        :param file_name:
        """
        self._folder_content.wait_until_file_is_copied(file_name)

    def upload_file(self, file_path, required_value="test"):
        """
        Uploads a file to the application.
        :param file_path: The path of the file to upload.
        :param required_value: Any value to fill on Required field.
        """
        self._folder_content.upload_file(file_path, required_value)
    
    def generate_random_file_name(self, file_extension=""):
        """
        Generates a random file name.
        :param file_extension: The extension of file name to create. 
        """
        return self._folder_content.generate_random_file_name(file_extension)
    
    def click_show_annotations_icon(self, file_name):
        """
        Clicks the Annotations icon.
        :param file_name: The file name.
        """
        self._folder_content.click_show_annotations_icon(file_name)
    
    def verify_if_metadata_value_is_displayed_in_folder_content(self, filename, expected_metadata):
        """
        Verifies if metadata value is displayed in folder content.
        :param filename: The file name to select.
        :param expected_metadata: The metadata to verify.
        """
        self._folder_content.verify_if_metadata_value_is_displayed_in_folder_content(filename, expected_metadata)
