__author__ = 'Edmundo Cossio'

import time

from robot.libraries.BuiltIn import BuiltIn
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

from resources.methods.UIMethods import is_element_present, \
    accept_alert_before_displayed, move_mouse_to, click_element
from resources.uiabstraction.components.widgets.filecontentmodal.FileContentModalBase import FileContentModalBase
from resources.uiabstraction.components.widgets.foldercontent.FolderContentBase import FolderContentBase


class FileContentModalMarquee(FileContentModalBase):
    """
    Page object modeling the structure and operations of the File Content Modal page for Marquee template.
    """
    
    # Selectors
    _close_button = (By.XPATH, "//button[@class='btn btn-default' and text()='Close']")
    _save_all_button = (By.XPATH, "//button[contains(.,'Save All')]")
    _versions_button = (By.XPATH, "//button[text()='Create New Version']")
    _back_button = (By.XPATH, "//button[text()='Back']")
    _delete_button = (By.XPATH, "//button[@title='Delete']")
    _flag_button = (By.XPATH, "//button[@data-stamp='Flagged']")
    _flag_active_button = (By.XPATH, "//button[contains(@class,'active') and @data-stamp='Flagged']")
    _stamp_button = (By.XPATH, "//button[@title='Stamp']")
    _stamp_active_button = (By.XPATH, "//button[@aria-expanded='true' and @title='Stamp']")
    _stamp_inactive_button = (By.XPATH, "//button[@aria-expanded='false' and @title='Stamp']")
    _rectangle_button = (By.XPATH, "//button[@title='Rectangle']")
    _rectangle_active_button = (By.XPATH, "//button[contains(@class,'active') and @title='Rectangle']")
    _add_button = (By.XPATH, "//input[@name='comment']/following-sibling::span/button")
    _x_button = (By.XPATH, "//button[@class='close']")
    _close_file_button = (By.ID, "inspectorCloseButton")
    
    _play_video = (By.XPATH, "//div[@aria-label='play video']")
    _play_progress = (By.CLASS_NAME, "vjs-play-progress")
    _changes_successfully_saved_message = (By.XPATH, "//em[contains(text(),'Changes were successfully saved')]")

    _versions_tab = (By.LINK_TEXT, "Versions")
    _metadata_tab = (By.LINK_TEXT, "Metadata")
    _containing_tab = (By.LINK_TEXT, "Containing")
    _comments_tab = (By.LINK_TEXT, "Comments")
    _pages_tab = (By.LINK_TEXT, "Pages")
    _history_tab = (By.LINK_TEXT, "History")
    _linked_tab = (By.LINK_TEXT, "Linked")
    _containing_list = (By.XPATH, "//div[contains(@class,'containing')]")
    _comments_list = (By.XPATH, "//div[contains(@class,'comments')]")
    _history_list = (By.XPATH, "//div[contains(@class,'history') and contains(@style,'block;')]")
    _linked_list = (By.XPATH, "//div[@class='list-group content linked']")
    _pages_list = (By.XPATH, "//div[contains(@class,'content pages')]")
    _wnv_text_label = (By.XPATH, "//label[.='wnv_text']")
    _success_delete_group = (By.XPATH, "//div[@class='btn-group btn-group-sm pull-right']")
    _annotations_group = (By.XPATH, "//div[contains(@class,'group-justified')]")
    _annotation_hidden = (By.XPATH, "//div[@id='toolspanel' and @class='small']")
    _right_arrow = (By.XPATH, "//button/span[contains(@class,'glyphicons-chevron-right')]")
    _left_arrow = (By.XPATH, "//button/span[contains(@class,'glyphicons-chevron-left')]")
    _annotation_displayed = (By.XPATH, "//div[@id='toolspanel' and @class='']")
    _pencil_span = (By.XPATH, "//a/span[contains(@class,'glyphicons-pencil')]")
    _containing_item = (By.XPATH, "//div[contains(@class,'list-group content containing')]/a")
    _user_comment_textbox = (By.XPATH, "//input[@name='comment']")
    _comment_added = (By.XPATH, "//ul[@class='annotationlist list-unstyled']/descendant::li[contains(@id,'commentlist')]")
    _annotations_container = (By.XPATH, "//div[@class='annotations']")
    _actual_position_slider = (By.XPATH, "//div[@class='slider-handle round' and contains(@style,'left: 0%;')]")
    _actual_percent_tooltip = (By.XPATH, "//div[@class='tooltip top']/descendant::div[contains(@class,'tooltip-inner')]")
    _canvas_details_view = (By.XPATH, "//div[@id='annotationCanvas']/descendant::canvas")
    _slider_horizontal = (By.XPATH, "//div[@class='middlecontrols']")
    _slider_handle_round = (By.XPATH, "//div[@class='slider-handle round']")
    _details_view_content = (By.ID, "details-info")
    _actual_percent_label = (By.XPATH, "//div[@class='tooltip-inner']")
    _inspector_canvas = (By.ID, "inspectorCanvas")
    _annotation_canvas = (By.ID, "annotationCanvas")

    def __init__(self):
        FileContentModalBase.__init__(self, "Marquee")
        self.keyword_value = "//label[text()='%s']/../following-sibling::td/select/option[@selected ='selected' and @label='%s']"
    
    def click_close_file_content_modal(self):
        """
        Clicks the Close button.
        """
        try:
            self._wait.until(ec.element_to_be_clickable(self._close_button))
            self._driver.find_element(*self._close_button).click()
            self._wait.until(ec.invisibility_of_element_located(self._details_view_content))
        except NoSuchElementException:
            print "The close button is not displayed."
    
    def play_video(self):
        """
        Plays video
        """
        self._wait.until(ec.element_to_be_clickable(self._play_video)).click()
    
    def is_video_reproduced(self):
        """
        Verify if video is reproduced.
        :return: True if video was reproduced, otherwise False.
        """
        is_reproduced = False
        for i in range(10):
            actual_progress = self._driver.find_element(*self._play_progress).get_attribute("style")
            if actual_progress >= "width: 3.00%;":
                is_reproduced = True 
                break
            else:
                time.sleep(1)
        return is_reproduced
    
    def verify_if_the_selected_video_is_reproduced(self):
        """
        Verifies if the selected video is reproduced.
        """
        BuiltIn().should_be_true(self.is_video_reproduced())
    
    def set_date_in_file_content_modal(self, metadata_name, select_date):
        """
        Set date in the file content modal page.
        :param metadata_name:The metadata name.
        :param select_date: The date value (month/day/year) to set, e.g. February/11/2016
        """
        metadata_label = (By.XPATH, "//label[text()='" + metadata_name + "']")
        month_combo = (By.XPATH, "//label[text()='" + metadata_name + "']/../following-sibling::td/select[@class='datefield  form-control']")
        month_id = self._driver.find_element(*month_combo).get_attribute("id")
        day_combo = (By.ID, month_id.replace("[1]", "[2]"))
        year_combo = (By.ID, month_id.replace("[1]", "[0]"))
        select_day = FolderContentBase("Marquee").get_day_without_cero_at_beginning(select_date.split('/')[1])
        if is_element_present(self._driver, *metadata_label):
            try:
                Select(self._driver.find_element(*month_combo)).select_by_visible_text(select_date.split('/')[0])
                Select(self._driver.find_element(*day_combo)).select_by_visible_text(select_day)
                Select(self._driver.find_element(*year_combo)).select_by_visible_text(select_date.split('/')[2])
            except NoSuchElementException as stale:
                print "Problem:" + str(stale)
     
    def click_save_all_button(self):
        """
        Clicks the Save All button in the file content modal page.
        """
        self._wait.until(ec.element_to_be_clickable(self._save_all_button)).click()
        self._wait.until(ec.visibility_of_element_located(self._changes_successfully_saved_message))
    
    def click_metadata_tab(self):
        """
        Clicks the metadata tab.
        """
        self._wait.until(ec.element_to_be_clickable(self._metadata_tab)).click()
        self._wait.until(ec.visibility_of_element_located(self._wnv_text_label))
    
    def is_keyword_value_displayed(self, keyword):
        """
        Verifies if the keyword value is displayed.
        :param keyword: The keyword to verify.
        :return: True if displayed, otherwise False.
        """
        keyword_value_text = (By.XPATH, "//label[text()='"+keyword[0]+"']/../following-sibling::td/input[@value='" + keyword[1] + "']")
        return is_element_present(self._driver, *keyword_value_text)
    
    def set_textbox_in_file_content_modal(self, keyword):
        """
        Sets textbox in file content modal.
        :param keyword: The keyword to set.
        """
        keyword_value_text = (By.XPATH, "//label[text()='" + keyword[0] + "']/../following-sibling::td/input")
        self._wait.until(ec.visibility_of_element_located(keyword_value_text))
        element = self._driver.find_element(*keyword_value_text)
        element.clear()
        element.send_keys(keyword[1])
    
    def set_combobox_keyword_file_content_modal(self, keyword):
        """
        Sets combobox in file content modal.
        :param keyword: The keyword to set.
        """
        keyword_value_text = (By.XPATH, "//label[text()='" + keyword[0] + "']/../following-sibling::td/select")
        self._wait.until(ec.visibility_of_element_located(keyword_value_text))
        try:
            Select(self._driver.find_element(*keyword_value_text)).select_by_visible_text(keyword[1])
        except NoSuchElementException as stale:
                print "Problem:" + str(stale)
    
    def click_versions_tab(self):
        """
        Clicks the versions tab.
        """
        try:
            self._wait.until(ec.element_to_be_clickable(self._versions_tab)).click()
            self._wait.until(ec.visibility_of_element_located(self._versions_button))
        except NoSuchElementException:
            print "The 'versions' tab is already selected."
    
    def click_create_new_version_button(self):
        """
        Clicks create new version button.
        """
        self._wait.until(ec.element_to_be_clickable(self._versions_button)).click()
        self._wait.until(ec.visibility_of_element_located(self._delete_button))

    def click_promote_version(self, row):
        """
        Clicks promote version button to make it the working version.
        :param row: The row where the Version is present.
        """
        accept_alert_before_displayed(self._driver)
        version = (By.XPATH, "//div[@id='details-info']//div[" + row + "]/button[@class='btn btn-success trash ']")
        version_disabled = (By.XPATH, "//div[@id='details-info']//div[" + row + "]/button[@class='btn btn-success trash  btn-warning' and @disabled='']")
        self._driver.find_element(*version).click()
        self._wait.until(ec.invisibility_of_element_located(version_disabled))

    def click_close_file_button(self):
        """
        Clicks the Close button to close the file.
        :return:
        """
        self._driver.find_element(*self._close_file_button).click()
        self._wait.until(ec.invisibility_of_element_located(self._inspector_canvas))

    def is_version_displayed_in_list(self, version_name):
        """
        Verifies if new version is displayed in list.
        :param version_name: The name of new version created.
        :return: True if displayed, otherwise False.
        """
        expected_version = (By.XPATH, "//h5[contains(.,'" + version_name + "')]")
        return is_element_present(self._driver, *expected_version)
    
    def select_version(self, version_name):
        """
        Clicks the select version.
        :param version_name: The version name.
        """
        _select_version = (By.XPATH, "//h5[contains(.,'"+version_name+"')]")
        _image = (By.XPATH, "//h5[contains(.,'" + version_name + "')]/../following-sibling::a")
        self._wait.until(ec.element_to_be_clickable(_select_version)).click()
        self._wait.until(ec.visibility_of_element_located(_image))
    
    def is_selected_version_displayed_in_file_content_modal(self, version_name):
        """
        Verifies if selected version is displayed in file content modal.
        :param version_name: The version name.
        :return: True if displayed, otherwise False.
        """
        selected_version = (By.XPATH, "//select[@id='inspectorPreviewSelect']/option[contains(.,'" + version_name + "')]")
        return is_element_present(self._driver, *selected_version)
    
    def click_back_to_file_content_modal_button(self):
        """
        Clicks back file content modal.
        """
        try:
            self._wait.until(ec.visibility_of_element_located(self._back_button))
            self._driver.find_element(*self._back_button).click()
            self._wait.until(ec.invisibility_of_element_located(self._back_button))
        except NoSuchElementException:
            print "The Back button is not displayed."
    
    def click_delete_version_button(self):
        """
        Clicks back file content modal.
        """
        accept_alert_before_displayed(self._driver)
        self._wait.until(ec.element_to_be_clickable(self._delete_button)).click()
        self._wait.until(ec.invisibility_of_element_located(self._success_delete_group))
    
    def click_right_arrow_in_file_content_modal(self):
        """
        Clicks arrow right in file content modal.
        """
        try:
            if is_element_present(self._driver, *self._right_arrow):
                click_element(self._driver, self._driver.find_element(*self._right_arrow))
                self._wait.until(ec.visibility_of_element_located(self._left_arrow))
        except NoSuchElementException:
            print "The right arrow is already selected."
    
    def click_flag_button(self):
        """
        Clicks the Flag button.
        """
        if not is_element_present(self._driver, *self._flag_active_button):
            self._driver.find_element(*self._flag_button).click()
            self._wait.until(ec.visibility_of_element_located(self._flag_active_button))
    
    def click_image_on_preview(self):
        """
        Clicks image on preview to display a new annotation type.
        """
        self._wait.until(ec.visibility_of_element_located(self._canvas_details_view))
        image_indd = self._driver.find_element(*self._canvas_details_view)
        move_mouse_to(self._driver, image_indd)
        image_indd.click()
    
    def click_show_annotations_button(self):
        """
        Clicks the annotations button.
        """
        self._wait.until(ec.element_to_be_clickable(self._pencil_span))
        # self._driver.find_element(*self._pencil_span).click()
        click_element(self._driver, self._driver.find_element(*self._pencil_span))
        self._wait.until(ec.visibility_of_element_located(self._slider_handle_round))
    
    def is_annotation_item_displayed_in_annotation_list(self, expected_result):
        """
        Verifies if annotation item is displayed in Annotation list
        :param expected_result: The expected result regarding annotation (Flag, Stamp, Comment,etc)
        :return: True if displayed, otherwise False.
        """
        flag_in_annotation = (By.XPATH, "//ul[@class='annotationlist list-unstyled']/descendant::div[.='" + expected_result[1] + "']")
        return is_element_present(self._driver, *flag_in_annotation)
    
    def click_containing_tab(self):
        """
        Clicks the containing tab.
        """
        self._wait.until(ec.element_to_be_clickable(self._containing_tab)).click()
        self._wait.until(ec.visibility_of_element_located(self._containing_list))
    
    def click_file_in_containing_list(self):
        """
        Selects file in Containing list.
        """
        self._wait.until(ec.element_to_be_clickable(self._containing_item)).click()
        self._wait.until(ec.visibility_of_element_located(self._containing_list))
    
    def is_file_content_modal_displayed(self, file_name):
        """
        Verifies if file content modal is displayed with selected file.
        :param file_name: The file name.
        :return: True if displayed, otherwise False.
        """
        image_indd = (By.XPATH, "//div[contains(@id,'details')]/descendant::img[contains(@src,'" + file_name + "')]")
        return is_element_present(self._driver, *image_indd)
    
    def is_annotation_displayed_in_file_content_modal(self, annotation_type):
        """
        Verifies if annotation type is displayed in file content modal.
        :param annotation_type: The annotation type.
        :return: True if displayed, otherwise False.
        """
        _annotation_button = (By.XPATH, "//button[@title='" + annotation_type + "']")
        return is_element_present(self._driver, *_annotation_button)
    
    def click_linked_tab(self):
        """
        Clicks the linked tab.
        """
        self._wait.until(ec.element_to_be_clickable(self._linked_tab)).click()
        self._wait.until(ec.visibility_of_element_located(self._linked_list))
    
    def click_file_linked(self, file_name):
        """
        Clicks file linked.
        :param file_name: The file name.
        """
        view_file = (By.XPATH, "//img[@alt='" + file_name + "']")
        self._wait.until(ec.visibility_of_element_located(self.get_image_of_linked_list(file_name))).click()
        self._wait.until(ec.visibility_of_element_located(view_file))
    
    def get_image_of_linked_list(self, file_name):
        """
        Gets image of linked list.
        :param file_name: The file name.
        """
        row = "//div[@id='details-info']/div[4]/a[%s]/h4"
        index = 1
        linked_item_selector = (By.XPATH, row % str(index))
        self._wait.until(ec.visibility_of_element_located(linked_item_selector))
        while True:
            linked_item_selector = (By.XPATH, row % str(index))
            try:
                element = self._driver.find_element(*linked_item_selector)
            except NoSuchElementException:
                print "The element was not found: ", file_name
                break
            if file_name in element.text:
                return linked_item_selector
            else:
                index += 1
    
    def set_user_comment(self, comment):
        """
        Sets a user comment.
        :param comment: The comment to set.
        """
        self._driver.find_element(*self._user_comment_textbox).clear()
        self._driver.find_element(*self._user_comment_textbox).send_keys(comment)
    
    def click_add_button(self):
        """
        Clicks add button.
        """
        self._wait.until(ec.element_to_be_clickable(self._add_button)).click()
        self._wait.until(ec.presence_of_element_located(self._comment_added))
    
    def is_comment_displayed_in_annotation_list(self, expected_result):
        """
        Verifies if comment is displayed in annotation list
        :param expected_result: The comment to verify.
        :return: True if displayed, otherwise False.
        """
        comment = (By.XPATH, "//ul[@class='annotationlist list-unstyled']/descendant::span[.='" + expected_result + "']")
        return is_element_present(self._driver, *comment)
    
    def delete_comment(self, comment):
        """
        Deletes comment created.
        :param comment: The comment to delete.
        """
        comment = (By.XPATH, "//a[contains(@class,'addcomment')]/preceding::p[contains(.,'" + comment + "')]/preceding-sibling::h5/preceding-sibling::button")
        if is_element_present(self._driver, *comment):
            self._wait.until(ec.element_to_be_clickable(comment)).click()
            self._wait.until(ec.invisibility_of_element_located(comment))
    
    def click_comments_tab(self):
        """
        Clicks comments tab.
        """
        if is_element_present(self._driver, *self._comments_tab):
            self._wait.until(ec.element_to_be_clickable(self._comments_tab)).click()
            self._wait.until(ec.visibility_of_element_located(self._comments_list))
    
    def click_stamp_button(self):
        """
        Clicks stamp button
        """
        if not is_element_present(self._driver, *self._stamp_active_button):
            self._wait.until(ec.visibility_of_element_located(self._stamp_button)).click()
            self._wait.until(ec.visibility_of_element_located(self._stamp_active_button))
    
    def click_stamp_item_button(self, stamp_selected):
        """
        Clicks stamp item button.
        :param stamp_selected: The stamp selected i.e. Expired
        """
        stamp_selected_button = (By.XPATH, "//img[@alt='" + stamp_selected + "']")
        if is_element_present(self._driver, *self._stamp_active_button):
            self._driver.find_element(*stamp_selected_button).click()
            self._wait.until(ec.visibility_of_element_located(self._stamp_inactive_button))
    
    def click_rectangle_button(self):
        """
        Clicks rectangle button.
        """
        if not is_element_present(self._driver, *self._rectangle_active_button):
            self._wait.until(ec.visibility_of_element_located(self._rectangle_button)).click()
            self._wait.until(ec.visibility_of_element_located(self._rectangle_active_button))
    
    def click_history_tab(self):
        """
        Clicks the history tab.
        """
        self._wait.until(ec.element_to_be_clickable(self._history_tab)).click()
        self._wait.until(ec.visibility_of_element_located(self._history_list))
    
    def is_metadata_changed_value_displayed(self, expected_metadata):
        """
        Verifies if updated metadata matches with recent activity in history list.
        :param expected_metadata: The expected recent activity in history list.
        """
        activity = (By.XPATH, "//h5[.='Metadata Changed']/following-sibling::p[contains(.,'" + expected_metadata + "')]")
        return is_element_present(self._driver, *activity)
    
    def click_page_number_image(self, page_number, file_name):
        """
        Click page number in Details view.
        :param page_number: The number of page to select.
        :param file_name: The file name.
        """
        select_page = (By.XPATH, "(//img[@alt='" + file_name + "'])[" + page_number + "]")
        self._wait.until(ec.element_to_be_clickable(select_page)).click()
        self._wait.until(ec.visibility_of_element_located(self._annotations_container))
    
    def is_selected_page_loaded_in_file_content_modal(self, page_number):
        """
        Verifies if selected page is loaded in file content modal.
        :param page_number: The number of page selected.
        """
        return is_element_present(self._driver, *self._annotations_container)
    
    def select_default_page_in_pages_tab(self, number_of_page):
        """
        Selects page by default in pages tab.
        :param number_of_page: The number of page to select.
        """
        current_spread_button = (By.XPATH, "//span[.='" + number_of_page + "']/following-sibling::span/a")
        self._wait.until(ec.element_to_be_clickable(current_spread_button)).click()
        self._wait.until(ec.visibility_of_element_located(self._changes_successfully_saved_message))
    
    def is_selected_page_displayed_in_folder_content(self, expected_result):
        """
        Verifies if selected page is displayed in folder content.
        :param expected_result: The page to be displayed.
        """
        selected_file = (By.XPATH, "//span[contains(.,'" + expected_result + "')]")
        return is_element_present(self._driver, *selected_file)
    
    def click_x_button_in_file_content_modal(self):
        """
        Clicks x button to close the file content modal.
        """
        self._wait.until(ec.element_to_be_clickable(self._x_button)).click()
        self._wait.until(ec.invisibility_of_element_located(self._back_button))
    
    def click_pages_tab(self):
        """
        Clicks pages tab.
        """
        self._wait.until(ec.element_to_be_clickable(self._pages_tab)).click()
        self._wait.until(ec.visibility_of_element_located(self._pages_list))
    
    def move_zoom_round_slider(self):
        """
        Moves the slider round to the middle in slider horizontal.
        """
        self._wait.until(ec.visibility_of_element_located(self._slider_handle_round))
        image = self._driver.find_element(*self._slider_horizontal)
        move_mouse_to(self._driver, image)
        initial_percent = self._driver.find_element(*self._actual_percent_label).text
        image.click()
        image.click()
        return initial_percent

    def verify_if_zoom_is_modified(self, initial_percent):
        """
        Verifies if zoom is modified.
        """
        BuiltIn().should_be_true(self.is_zoom_modified(initial_percent))
    
    def is_zoom_modified(self, initial_percent):
        """
        Returns True if zoom is modified, otherwise False.
        """
        actual_percent = self._driver.find_element(*self._actual_percent_label).text
        if int(actual_percent.replace("%", "")) > int(initial_percent.replace("%", "")):
            return True
        return False

    def wait_until_file_is_loaded_in_file_content_modal(self, file_name):
        """
        Waits until the file is load in the File Content modal section.
        :param file_name: The file name to wait.
        """
        count = 0
        file_content_modal_title = (By.XPATH, "//h4[@id='myModalLabel' and .='" + file_name + "']")
        while count < 10 and not is_element_present(self._driver, *file_content_modal_title):
            time.sleep(1)
            count += 1
