__author__ = 'Edmundo Cossio'

from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By

from resources.commons.DriverManager import DriverManager
from resources.methods.UIMethods import is_element_present


class FileContentModalBase(object):
    """
    Page object modeling the structure and operations of the File Content Modal page.
    """
    _driver = None
    _wait = None
    
    # Selectors
    _user_comment_textbox = (By.XPATH, "//li[contains(@id,'annotationlist_new')]/descendant::textarea")

    def __init__(self, theme):
        self._driver = DriverManager().get_instance().get_driver()
        self._wait = DriverManager().get_instance().get_wait()
        self.theme = theme
    
    def click_close_file_content_modal(self):
        """
        Clicks the Close button.
        """
        return self
     
    def click_save_all_button(self):
        """
        Clicks the Save All button in the file content modal page.
        """
        return self

    def click_create_new_version_button(self):
        """
        Clicks create new version button.
        """
        return self
    
    def select_version(self, version_name):
        """
        Clicks the select version.
        :param version_name: The version name.
        """
        return self

    def click_promote_version(self, row):
        """
        Clicks promote version button to make it the working version.
        :param row: The row where the Version is present.
        """
        return self

    def click_close_file_button(self):
        """
        Clicks the Close button to close the file.
        :return:
        """

    def click_back_to_file_content_modal_button(self):
        """
        Clicks back file content modal.
        """
        return self
    
    def click_delete_version_button(self):
        """
        Clicks delete version button
        """
        return self
    
    def click_right_arrow_in_file_content_modal(self):
        """
        Clicks arrow right in file content modal.
        """
        return self
    
    def click_flag_button(self):
        """
        Clicks the Flag button.
        """
        return self

    def click_show_annotations_button(self):
        """
        Clicks the annotations button.
        """
        return self

    def click_text_button(self):
        """
        Clicks text button
        """
        return self

    def click_add_button(self):
        """
        Clicks add button.
        """
        return self

    def click_cancel_button(self):
        """
        Clicks cancel button.
        """
        return self

    def click_stamp_button(self):
        """
        Clicks stamp button
        """
        return self

    def click_stamp_item_button(self, stamp_selected):
        """
        Clicks stamp item button.
        :param stamp_selected: The stamp selected i.e. Expired
        """
        return self

    def click_rectangle_button(self):
        """
        Clicks rectangle button.
        """
        return self

    def click_image_on_preview(self):
        """
        Clicks image on preview to display a new annotation type.
        """
        return self

    def click_back_button(self):
        """
        Clicks back button in file content modal.
        """
        return self

    def click_back_to_file_button(self):
        """
        Clicks the Back button to return to File.
        """
        return self

    def click_metadata_tab(self):
        """
        Clicks the metadata tab.
        """
        return self

    def click_versions_tab(self):
        """
        Clicks the versions tab.
        """
        return self

    def click_linked_tab(self):
        """
        Clicks the linked tab.
        """
        return self

    def click_containing_tab(self):
        """
        Clicks the containing tab.
        """
        return self

    def click_comments_tab(self):
        """
        Clicks comments tab.
        """
        return self

    def click_history_tab(self):
        """
        Clicks the history tab.
        """
        return self

    def click_pages_tab(self):
        """
        Clicks pages tab.
        """
        return self

    def click_file_in_containing_list(self):
        """
        Clicks file in Containing list.
        """
        return self
    
    def click_file_linked(self, file_name):
        """
        Clicks file linked.
        :param file_name: The file name.
        """
        return self

    def click_recent_activity_in_history_list(self):
        """
        Clicks recent activity in history_list
        """
        return self

    def click_metadata_changed_link(self):
        """
        Clicks Metadata Changed link in history list.
        """
        return self

    def click_page_number_image(self, page_number, file_name):
        """
        Click page number in Details view.
        :param page_number: The number of page to select.
        :param file_name: The file name.
        """
        return self

    def delete_version(self, version_name):
        """
        Deletes the created version.
        :param version_name: The version name to delete. 
        """
        self.click_versions_tab()
        if self.theme.lower() == 'exhibit':
            self.select_version(version_name)
        self.click_delete_version_button()
        self.click_close_file_content_modal()

    def is_keyword_value_displayed(self, keyword):
        """
        Verifies if the keyword value is displayed.
        :param keyword: The keyword to verify.
        :return: True if displayed, otherwise False.
        """
        return self

    def is_keyword_value_list_displayed_in_file_content_modal(self, keyword_list):
        """
        Verifies if a list of keyword values is displayed in file content modal page.
        :param keyword_list: A list of keyword values.
        :return: True if displayed, otherwise False.
        """
        is_displayed = None
        for folder in keyword_list:
            if "date" in folder[0]:
                is_displayed = self.is_keyword_date_value_displayed(folder)
            else:
                is_displayed = self.is_keyword_value_displayed(folder)
            if not is_displayed:
                break
        return is_displayed
    
    def is_annotation_item_displayed_on_canvas(self, annotation_item):
        """
        Verifies if annotation item is displayed on canvas.
        :param annotation_item : The annotation item to find in the image (annotations: Flag, Comment, etc).
        :return: True if displayed, otherwise False.
        """
        annotation_in_canvas = (By.XPATH, "//div[@id='annotationCanvas']/descendant::div[@class='XinetCanvasObject' and contains(@style,'visible')]/div[.='" + annotation_item[1] + "']")
        print annotation_in_canvas
        return is_element_present(self._driver, *annotation_in_canvas)
    
    def select_default_page_in_pages_tab(self, number_of_page):
        """
        Selects page by default in pages tab.
        :param number_of_page: The number of page to select.
        """
        return self
    
    def set_metadata_textbox_in_file_content_modal(self, value):
        """
        Sets textbox in file content modal regarding metadata
        :param value: The metadata value.
        """
        self.click_metadata_tab()
        self.set_textbox_in_file_content_modal(value)
        self.click_save_all_button()
        self.click_back_button()
        self.click_close_file_content_modal()
    
    def set_user_comment(self, comment):
        """
        Sets new user comment.
        :param comment: The new comment to set.
        """
        return self
    
    def set_annotation_note(self, note):
        """
        Sets note for annotation.
        :param note: The note to set in the annotation.
        """
        self._driver.find_element(*self._user_comment_textbox).clear()
        self._driver.find_element(*self._user_comment_textbox).send_keys(note)
    
    def play_video(self):
        """
        Plays video
        """
        return self
    
    def set_textbox_in_file_content_modal(self, keyword):
        """
        Sets textbox in file content modal.
        :param keyword: The keyword to set.
        """
        return self
    
    def set_combobox_keyword_file_content_modal(self, keyword):
        """
        Sets combobox in file content modal.
        :param keyword: The keyword to set.
        """
        return self
    
    def create_annotation(self, note, annotation_item):
        """
        Creates note for annotation.
        """
        self.click_right_arrow_in_file_content_modal()
        if annotation_item[0].lower() in 'flag':
            self.click_flag_button()
        elif annotation_item[0].lower() == 'stamp':
            self.click_stamp_button()
            self.click_stamp_item_button(annotation_item[1])
        elif annotation_item[0].lower() == 'rectangle':
            self.click_rectangle_button()
        self.click_image_on_preview()
        self.set_annotation_note(note)
        self.click_save_all_button()
        self.click_back_to_file_content_modal_button()
    
    def delete_comment(self, comment):
        """
        Deletes comment created.
        :param comment: The comment to delete.
        """
        return self
    
    def delete_user_comment(self, comment_to_delete):
        """
        Deletes user comment created.
        :param comment_to_delete: The comment to delete in file content modal.
        """
        if self.theme.lower() == 'marquee':
            self.click_back_to_file_content_modal_button()
            self.click_comments_tab()
        self.delete_comment(comment_to_delete)
        if self.theme.lower() == 'exhibit':
            self.click_cancel_button()
    
    def verify_if_metadata_values_are_displayed_in_file_content_modal(self, keyword_list): 
        """
        Verifies if metadatas entered in batchapply are displayed in file content modal.
        :param keyword_list: A list of keyword values.
        :return: True if displayed, otherwise False.
        """
        BuiltIn().should_be_true(self.is_keyword_value_list_displayed_in_file_content_modal(keyword_list))

    def is_version_displayed_in_list(self, version_name):
        """
        Verifies if new version is displayed in list.
        :param version_name: The name of new version created.
        :return: True if displayed, otherwise False.
        """
        return self

    def verify_if_version_is_displayed_in_list(self, version_name):
        """
        Verifies if new version is displayed in list.
        :param version_name: The name of new version created.
        """
        BuiltIn().should_be_true(self.is_version_displayed_in_list(version_name))

    def is_selected_version_displayed_in_file_content_modal(self, version_name):
        """
        Verifies if selected version is displayed in file content modal.
        :param version_name: The version name.
        :return: True if displayed, otherwise False.
        """
        return self

    def verify_if_selected_version_is_displayed_in_file_content_modal(self, version_name): 
        """
        Verifies if selected version is displayed in file content modal.
        :param version_name: The version name.
        """
        BuiltIn().should_be_true(self.is_selected_version_displayed_in_file_content_modal(version_name))
    
    def verify_if_annotation_item_is_displayed_on_canvas(self, annotation_item):
        """
        Verifies if annotation item is displayed on canvas.
        :param annotation_item : The annotation item to find in the image (annotations: Flag, Comment, etc).
        """
        BuiltIn().should_be_true(self.is_annotation_item_displayed_on_canvas(annotation_item))

    def verify_if_annotation_item_is_not_displayed_on_canvas(self, annotation_item):
        """
        Verifies if annotation item is displayed on canvas.
        :param annotation_item : The annotation item to find in the image (annotations: Flag, Comment, etc).
        """
        BuiltIn().should_not_be_true(self.is_annotation_item_displayed_on_canvas(annotation_item))

    def is_annotation_item_displayed_in_annotation_list(self, expected_result):
        """
        Verifies if annotation item is displayed in Annotation list
        :param expected_result: The expected result regarding annotation (Flag, Stamp, Comment,etc)
        :return: True if displayed, otherwise False.
        """
        return self

    def verify_if_annotation_item_is_displayed_in_annotation_list(self, expected_result):
        """
        Verifies if annotation item is displayed in Annotation list
        :param expected_result: The expected result regarding annotation (Flag, Stamp, Comment,etc)  
        """
        BuiltIn().should_be_true(self.is_annotation_item_displayed_in_annotation_list(expected_result))

    def is_file_content_modal_displayed(self, file_name):
        """
        Verifies if file content modal is displayed when clicking file.
        :param file_name: The file name.
        :return: True if displayed, otherwise False.
        """
        return self

    def verify_if_file_content_modal_is_displayed(self, file_name): 
        """
        Verifies if file content modal is displayed when clicking file.
        :param file_name: The file name.
        """
        BuiltIn().should_be_true(self.is_file_content_modal_displayed(file_name))

    def is_annotation_displayed_in_file_content_modal(self, annotation_type):
        """
        Verifies if annotation type is displayed in file content modal.
        :param annotation_type: The annotation type.
        :return: True if displayed, otherwise False.
        """
        return self

    def verify_if_annotation_type_is_displayed_in_file_content_modal(self, annotation_type):
        """
        Verifies if annotation type is displayed in file content modal.
        :param annotation_type: The annotation type.
        """
        BuiltIn().should_be_true(self.is_annotation_displayed_in_file_content_modal(annotation_type))

    def is_comment_displayed_in_annotation_list(self, expected_result):
        """
        Verifies if comment is displayed in annotation list
        :param expected_result: The comment to verify.
        :return: True if displayed, otherwise False.
        """
        return self

    def verify_if_comment_is_displayed_in_annotation_list(self, expected_comment):
        """
        Verifies if comment is displayed in annotation list
        :param expected_comment: The comment to verify.
        """
        BuiltIn().should_be_true(self.is_comment_displayed_in_annotation_list(expected_comment))

    def is_metadata_changed_value_displayed(self, metadata_value):
        """
        Returns True if the metadata updated value is displayed, otherwise False.
        :param metadata_value: The value to verify.
        """
        return self

    def verify_if_metadata_changed_value_is_displayed_in_history_list(self, metadata_value):
        """
        Verifies if the metadata updated value is displayed in History list.
        :param metadata_value: The value to verify.
        """
        BuiltIn().should_be_true(self.is_metadata_changed_value_displayed(metadata_value))

    def is_selected_page_loaded_in_file_content_modal(self, page_number):
        """
        Verifies if selected page is loaded in file content modal.
        :param page_number: The number of page selected.
        """
        return self

    def verify_if_selected_page_is_loaded_in_file_content_modal(self, page_number):
        """
        Verifies if selected page is loaded in file content modal.
        :param page_number: The number of page selected.
        """
        BuiltIn().should_be_true(self.is_selected_page_loaded_in_file_content_modal(page_number))

    def is_selected_page_displayed_in_folder_content(self, expected_result):
        """
        Verifies if selected page is displayed in folder content.
        :param expected_result: The page to be displayed.
        """
        return self

    def verify_if_selected_page_is_displayed_in_folder_content(self, expected_result):
        """
        Verifies if selected page is displayed in folder content.
        :param expected_result: The page to be displayed.
        """
        BuiltIn().should_be_true(self.is_selected_page_displayed_in_folder_content(expected_result))
    
    def is_keyword_date_value_displayed(self, keyword):
        """
        Verifies if the keyword value is displayed.
        :param keyword: The keyword value.
        :return: True if displayed, otherwise False.
        """
        is_displayed = None
        for i in range(0, 3):
            keyword_value_text = (By.XPATH, self.keyword_value % (keyword[0], keyword[1][i]))
            is_displayed = is_element_present(self._driver, *keyword_value_text)
            if not is_displayed:
                break
        return is_displayed

    def verify_if_zoom_is_modified(self, initial_percent):
        """
        Verifies if zoom is modified.
        """
        return self

    def wait_until_file_is_loaded_in_file_content_modal(self, file_name):
        """
        Waits until the file is load in the File Content modal section.
        :param file_name: The file name to wait.
        """
        return self
