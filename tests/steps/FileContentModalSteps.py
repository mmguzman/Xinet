__author__ = 'Edmundo Cossio'

from resources.commons.GlobalVariables import TEMPLATE
from resources.uiabstraction.PageObjectFactory import PageObjectFactory


class FileContentModalSteps:
    """
    Steps definition for File Content Modal object.
    """
    _file_content_modal = None

    def __init__(self):
        self._file_content_modal = PageObjectFactory.create_dialog_content(TEMPLATE)

    def click_close_file_content_modal(self):
        """
        Clicks the Close button.
        """
        self._file_content_modal.click_close_file_content_modal()
    
    def play_video(self):
        """
        Plays video
        """
        self._file_content_modal.play_video()
    
    def verify_if_the_selected_video_is_reproduced(self):
        """
        Verifies if the selected video is reproduced.
        """
        self._file_content_modal.verify_if_the_selected_video_is_reproduced()
    
    def click_metadata_tab(self):
        """
        Clicks the metadata tab.
        """
        self._file_content_modal.click_metadata_tab()
    
    def verify_if_metadata_values_are_displayed_in_file_content_modal(self, keyword_list): 
        """
        verify_if_metadata_values_entered_in_batchapply_are_displayed_in_file_content_modal
        :param keyword_list: A list of keyword values.
        :return: True if displayed, otherwise False.
        """
        self._file_content_modal.verify_if_metadata_values_are_displayed_in_file_content_modal(keyword_list)
    
    def set_textbox_in_file_content_modal(self, keyword):
        """
        Sets textbox in file content modal.
        :param keyword: The keyword to set.
        """
        self._file_content_modal.set_textbox_in_file_content_modal(keyword)
    
    def set_combobox_keyword_file_content_modal(self, keyword):
        """
        Sets combobox in file content modal.
        :param keyword: The keyword to set.
        """
        self._file_content_modal.set_combobox_keyword_file_content_modal(keyword)
    
    def click_save_all_button(self):
        """
        Clicks the Save All button in the file content modal.
        """
        self._file_content_modal.click_save_all_button()
    
    def click_versions_tab(self):
        """
        Clicks the versions tab.
        """
        self._file_content_modal.click_versions_tab()
    
    def click_create_new_version_button(self):
        """
        Clicks create new version button.
        """
        self._file_content_modal.click_create_new_version_button()

    def click_close_file_button(self):
        """
        Clicks the Close button to close the file.
        :return:
        """
        self._file_content_modal.click_close_file_button()

    def verify_if_version_is_displayed_in_list(self, version_name):
        """
        Verifies if new version is dislayed in list.
        :param version_name: The name of new version created.
        """
        self._file_content_modal.verify_if_version_is_displayed_in_list(version_name)
    
    def verify_if_selected_version_is_displayed_in_file_content_modal(self, version_name): 
        """
        Verifies if selected version is displayed in file content modal.
        :param version_name: The version name.
        """
        self._file_content_modal.verify_if_selected_version_is_displayed_in_file_content_modal(version_name)
    
    def click_back_to_file_content_modal_button(self):
        """
        Clicks back file content modal.
        """
        self._file_content_modal.click_back_to_file_content_modal_button()

    def click_back_to_file_button(self):
        """
        Clicks the Back button to return to File.
        """
        self._file_content_modal.click_back_to_file_button()

    def click_delete_version_button(self):
        """
        Clicks back file content modal.
        """
        self._file_content_modal.click_delete_version_button()
    
    def select_version(self, version_name):
        """
        Clicks the select version.
        :param version_name: The version name.
        """
        self._file_content_modal.select_version(version_name)
    
    def click_right_arrow_in_file_content_modal(self):
        """
        Clicks arrow right in file content modal.
        """
        self._file_content_modal.click_right_arrow_in_file_content_modal()
    
    def click_flag_button(self):
        """
        Clicks the Flag button.
        """
        self._file_content_modal.click_flag_button()
        
    def click_image_on_preview(self):
        """
        Clicks image on preview to display a new annotation type.
        """
        self._file_content_modal.click_image_on_preview()
    
    def set_annotation_note(self, note):
        """
        Sets note for annotation.
        :param note: The note set for annotation.
        """
        self._file_content_modal.set_annotation_note(note)
    
    def click_show_annotations_button(self):
        """
        Clicks the annotations button.
        """
        self._file_content_modal.click_show_annotations_button()

    def delete_version(self, version_name):
        """
        Deletes the created version.
        :param version_name: The version name to delete. 
        """
        self._file_content_modal.delete_version(version_name)
    
    def verify_if_annotation_item_is_displayed_on_canvas(self, annotation_item):
        """
        Verifies if annotation item is displayed on canvas.
        :param annotation_item : The annotation item to find in the image (annotations: Flag, Comment, etc).
        """
        self._file_content_modal.verify_if_annotation_item_is_displayed_on_canvas(annotation_item)

    def verify_if_annotation_item_is_not_displayed_on_canvas(self, annotation_item):
        """
        Verifies if annotation item is displayed on canvas.
        :param annotation_item : The annotation item to find in the image (annotations: Flag, Comment, etc).
        """
        self._file_content_modal.verify_if_annotation_item_is_not_displayed_on_canvas(annotation_item)

    def verify_if_annotation_item_is_displayed_in_annotation_list(self, expected_result):
        """
        Verifies if annotation item is displayed in Annotation list
        :param expected_result: The expected result regarding annotation (Flag, Stamp, Comment,etc)
        """
        self._file_content_modal.verify_if_annotation_item_is_displayed_in_annotation_list(expected_result)
    
    def click_containing_tab(self):
        """
        Clicks the containing tab.
        """
        self._file_content_modal.click_containing_tab()
    
    def verify_if_file_content_modal_is_displayed(self, file_name): 
        """
        Verifies if file content modal is displayed when clicking file.
        :param file_name: The file name.
        """
        self._file_content_modal.verify_if_file_content_modal_is_displayed(file_name)
    
    def verify_if_annotation_type_is_displayed_in_file_content_modal(self, annotation_type):
        """
        Verifies if annotation type is displayed in file content modal.
        :param annotation_type: The annotation type.
        """
        self._file_content_modal.verify_if_annotation_type_is_displayed_in_file_content_modal(annotation_type)
    
    def click_file_in_containing_list(self):
        """
        Clicks file in Containing list.
        """
        self._file_content_modal.click_file_in_containing_list()
    
    def click_linked_tab(self):
        """
        Clicks the linked tab.
        """
        self._file_content_modal.click_linked_tab()
    
    def click_file_linked(self, file_name):
        """
        Clicks file linked.
        :param file_name: The file name.
        """
        self._file_content_modal.click_file_linked(file_name)
    
    def click_text_button(self):
        """
        Clicks text button.
        """
        self._file_content_modal.click_text_button()
    
    def set_user_comment(self, comment):
        """
        Sets new user comment.
        :param comment: The new comment to set.
        """
        self._file_content_modal.set_user_comment(comment)
    
    def click_add_button(self):
        """
        Clicks add button.
        """
        self._file_content_modal.click_add_button()
    
    def verify_if_comment_is_displayed_in_annotation_list(self, expected_comment):
        """
        Verifies if comment is displayed in annotation list
        :param expected_comment: The comment to verify.
        """
        self._file_content_modal.verify_if_comment_is_displayed_in_annotation_list(expected_comment)
    
    def delete_user_comment(self, comment_to_delete):
        """
        Deletes user comment created.
        :param comment_to_delete: The comment to delete in file content modal.
        """
        self._file_content_modal.delete_user_comment(comment_to_delete)
    
    def delete_comment(self, comment):
        """
        Deletes comment created.
        :param comment: The comment to delete.
        """
        self._file_content_modal.delete_comment(comment)
    
    def click_cancel_button(self):
        """
        Clicks cancel button.
        """
        self._file_content_modal.click_cancel_button()
    
    def click_comments_tab(self):
        """
        Clicks comments tab.
        """
        self._file_content_modal.click_comments_tab()
    
    def click_stamp_button(self):
        """
        Clicks stamp button
        """
        self._file_content_modal.click_stamp_button()
    
    def click_stamp_item_button(self, stamp_selected):
        """
        Clicks stamp item button.
        :param stamp_selected: The stamp selected i.e. Expired
        """
        self._file_content_modal.click_stamp_item_button(stamp_selected)
    
    def click_rectangle_button(self):
        """
        Clicks rectangle button.
        """
        self._file_content_modal.click_rectangle_button()
    
    def click_history_tab(self):
        """
        Clicks the history tab.
        """
        self._file_content_modal.click_history_tab()
    
    def click_recent_activity_in_history_list(self):
        """
        clicks recent activity in history list
        """
        self._file_content_modal.click_recent_activity_in_history_list()

    def click_metadata_changed_link(self):
        """

        :return:
        """
        self._file_content_modal.click_metadata_changed_link()

    def set_metadata_textbox_in_file_content_modal(self, value):
        """
        Sets textbox in file content modal regarding metadata
        :param value: The metadata value.
        """
        self._file_content_modal.set_metadata_textbox_in_file_content_modal(value)
    
    def click_back_button(self):
        """
        Clicks back button in file content modal.
        """
        self._file_content_modal.click_back_button()
    
    def verify_if_metadata_matches_recent_activity_in_history_list(self, expected_recent_activity):
        """
        Verifies if metadata matches with recent activity in history list.
        :param expected_recent_activity: The expected recent activity in history list.
        """
        self._file_content_modal.verify_if_metadata_matches_recent_activity_in_history_list(expected_recent_activity)

    def verify_if_metadata_changed_value_is_displayed_in_history_list(self, metadata_value):
        """

        :param metadata_value:
        :return:
        """
        self._file_content_modal.verify_if_metadata_changed_value_is_displayed_in_history_list(metadata_value)

    def click_page_number_image(self, page_number, file_name):
        """
        Click page number in Details view.
        :param page_number: The number of page to select.
        :param file_name: The file name.
        """
        self._file_content_modal.click_page_number_image(page_number, file_name)
    
    def verify_if_selected_page_is_loaded_in_file_content_modal(self, number_of_page):
        """
        Verifies if selected page is loaded in file content modal.
        :param number_of_page: The number of page selected.
        """
        self._file_content_modal.verify_if_selected_page_is_loaded_in_file_content_modal(number_of_page)
    
    def select_default_page_in_pages_tab(self, number_of_page):
        """
        Selects page by default in pages tab.
        :param number_of_page: The number of page to select.
        """
        self._file_content_modal.select_default_page_in_pages_tab(number_of_page)
    
    def click_x_button_in_file_content_modal(self):
        """
        Clicks x button to close the file content modal.
        """
        self._file_content_modal.click_x_button_in_file_content_modal()
    
    def click_pages_tab(self):
        """
        Clicks pages tab.
        """
        self._file_content_modal.click_pages_tab()

    def click_promote_version(self, row):
        """
        Clicks promote version button to make it the working version.
        :param row:
        """
        self._file_content_modal.click_promote_version(row)

    def verify_if_selected_page_is_displayed_in_folder_content(self, expected_result):
        """
        Verifies if selected page is displayed in folder content.
        :param expected_result: The page to be displayed.
        """
        self._file_content_modal.verify_if_selected_page_is_displayed_in_folder_content(expected_result)
    
    def create_annotation(self, note, annotation_item):
        """
        Creates note for annotation.
        """
        self._file_content_modal.create_annotation(note, annotation_item)
    
    def move_zoom_round_slider(self):
        """
        Moves the slider round to the middle in slider horizontal. 
        """
        return self._file_content_modal.move_zoom_round_slider()
    
    def verify_if_zoom_is_modified(self, initial_percent):
        """
        Verifies if zoom is modified.
        """
        self._file_content_modal.verify_if_zoom_is_modified(initial_percent)
    
    def wait_until_file_is_loaded_in_file_content_modal(self, file_name):
        """
        Waits until the file is load in the File Content modal section.
        :param file_name: The file name to wait.
        """
        self._file_content_modal.wait_until_file_is_loaded_in_file_content_modal(file_name)
