__author__ = 'Edmundo Cossio'

from robot.libraries.BuiltIn import BuiltIn
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select

from resources.commons.GlobalVariables import BROWSER
from resources.methods.UIMethods import is_element_present, wait_for_load_page, \
    click_element, accept_alert_before_displayed, move_mouse_to
from resources.uiabstraction.components.widgets.filecontentmodal.FileContentModalBase import FileContentModalBase
from resources.uiabstraction.components.widgets.foldercontent.FolderContentBase import FolderContentBase


class FileContentModalExhibit(FileContentModalBase):
    """
    Page object modeling the structure and operations of the File Content Modal page for Exhibit template.
    """
    
    # Selectors
    _close_button = (By.XPATH, "//button[text()='Close']")
    _info_toolbar_button_stream = (By.ID, "info_toolbar_button_stream")
    _save_changes_button = (By.XPATH, "//a[@class='savebutton btn btn-mini btn-primary']/span[text()='Save Changes']")
    _flag_button = (By.ID, "rectButton")
    _flag_selected_button = (By.XPATH, "//div[@id='rectButton' and contains(@class,'selected')]")
    _delete_button = (By.XPATH, "//a[@title='Delete']")
    _create_new_version_button = (By.XPATH, "//span[.='Create New Version']")
    _text_button = (By.ID, "textButton")
    _add_button = (By.XPATH, "//form[@class='XinetCanvasText_inputForm']/div/input[@value='Ok']")
    _comment_buttons = (By.XPATH, "//div[@class='XinetCanvasText_buttons']")
    _cancel_button = (By.XPATH, "//a[@class ='cancelbutton btn btn-small'] / span[.='Cancel']")
    _stamp_button = (By.ID, "stampButton")
    _rectangle_button = (By.XPATH, "//img[@alt='annotation' and  contains(@src,'rect.gif')]")
    _stamp_selected_button = (By.XPATH, "//div[@id='stampButton' and contains(@class,'selected')]")
    _rectangle_selected_button = (By.XPATH, "//div[@id='rectButton' and contains(@class,'selected')]")
    _back_button = (By.XPATH, "//a[@class ='backbutton btn btn-mini'] / span[.='Back']")
    _back_to_file_button = (By.XPATH, "//a/span[text()='Back']")

    _play_progress = (By.CLASS_NAME, "vjs-play-progress")
    _changes_successfully_saved = (By.XPATH, "//div[@id='saveOKMsg' and contains(text(),'Changes were successfully saved')]")

    _wnv_text_panel = (By.ID, "metadatapanel")
    _annotation_panel = (By.XPATH, "//div[@id='controlstrip' and contains(@style,'-300px;')]")
    _pages_files_panel = (By.XPATH, "//div[@class='detailsheading' and contains(.,'Pages')]")
    _linked_files_panel = (By.XPATH, "//div[@class='detailsheading' and contains(.,'Linked Files')]")
    _control_panel = (By.ID, "info_controlpanel")

    _stamp_displayed_pane = (By.XPATH, "//div[@id='stampPaneTemplate' and @class='panelListItemMenu optionpane ']")
    _compare_link = (By.XPATH, "//a[@id='inspectorOpenButton']")

    _file_preview_image = (By.XPATH, "//li[contains(@class,'listopen')]/descendant::div[contains(@class,'filepreview')]")
    _details_view_image = (By.XPATH, "//div[@id='annotationCanvas']/descendant::canvas")

    _select_label = (By.XPATH, "//span[.='Adjustment/Select']")
    _containing_documents_label = (By.XPATH, "//div[@id='containersdetails']/div[contains(.,'Containing')]")
    _datetime_last_activity_label = (By.XPATH, "//div[@id='historyinfopanel']/descendant::li[1]/descendant::div[@class='panelListItemMenu ']/div")

    _annotation_tab = (By.XPATH, "//div[@id='annotateflip' and contains(@class,'active')]")
    _version_tab = (By.XPATH, "//div[@id='versionsflip' and contains(@class,'active')]")
    _containing_tab = (By.XPATH, "//div[@id='containersflip' and contains(@class,'active')]")
    _metadata_tab = (By.ID, "metadataflip")
    _metadata_active_tab = (By.XPATH, "//div[@id='metadataflip' and contains(@class,'active')]")
    _linked_tab = (By.XPATH, "//div[@id='linkedfilesflip' and contains(@class,'active')]")
    _history_tab = (By.XPATH, "//div[@id='fileinfoflip' and contains(@class,'active')]")
    _pages_tab = (By.XPATH, "//div[@id='pagesflip' and contains(@class,'active')]")

    _containing_item = (By.XPATH, "//li[contains(@class,'listclosed')]/div[contains(@id,'containerpreview')]/div")
    _actual_history_item = (By.XPATH, "//li[@class='listclosed panelListItemExpandable']/descendant::strong")
    _history_item_collapsed = (By.XPATH, "//li[contains(@class,'listclosed panelListItemExpandable')]")
    _activity_item_collapsed = (By.XPATH, "//li[contains(@class,'listopen')]")
    _view_file = (By.XPATH, "//a[@title='View file']")
    _linked_list = (By.XPATH, "//div[@id='linkedfilespanel']/descendant::div[@class='detailssubpanel']")
    _history_list = (By.XPATH, "//div[@class='detailsheading' and contains(.,'Detailed History')]")
    _comment_text = (By.XPATH, "//form[@class='XinetCanvasText_inputForm']/div/textarea")

    _default_preview_checkbox = (By.ID, "markpreferredtoggle")
    _canvas_details_view = (By.XPATH, "//div[@id='annotationCanvas']/descendant::canvas")
    _tools_section = (By.XPATH, "//div[@class='detailsheading']")
    _metadata_changed_link_opened = (By.XPATH, "//div/ul/li[contains(@class,'listopen')]/div/div/strong[contains(.,'Metadata Changed')]")
    _metadata_changed_link_closed = (By.XPATH, "//div/ul/li[contains(@class,'listclosed')]/div/div/strong[contains(.,'Metadata Changed')]")

    def __init__(self):
        FileContentModalBase.__init__(self, "Exhibit")
        self.keyword_value = "//form/div/div[contains(text(),'%s')]/following-sibling::div/select/option[@selected='selected' and @label='%s']"
    
    def play_video(self):
        """
        Plays video
        """
        self._wait.until(ec.element_to_be_clickable(self._info_toolbar_button_stream)).click()
    
    def is_video_reproduced(self):
        """
        Verifies if video is reproduced.
        :return: True if video was reproduced, otherwise False.
        """
        if BROWSER.lower() == "chrome":
            action_stream_file = (By.ID, "previewbox")
            self._wait.until(ec.visibility_of_element_located(action_stream_file))
        elif BROWSER.lower() == "ie":
            action_stream_file = (By.ID, "WMVpreviewbox")
            self._wait.until(lambda s: s.find_element(*action_stream_file))
        else:
            action_stream_file = (By.XPATH, "//video/source[contains(@src,'streamfile')]")
            self._wait.until(ec.invisibility_of_element_located(action_stream_file))
        if is_element_present(self._driver, *action_stream_file):
            is_reproduced = True
        else:
            is_reproduced = False
        return is_reproduced
    
    def verify_if_the_selected_video_is_reproduced(self):
        """
        Verifies if a Volume is displayed.
        """
        BuiltIn().should_be_true(self.is_video_reproduced())
    
    def set_date_in_file_content_modal(self, metadata_name, select_date):
        """
        Sets date in the file content modal page.
        :param metadata_name:The metadata name.
        :param select_date: The date value (month/day/year) to set, e.g. February/11/2016
        """
        metadata_label = (By.XPATH, "//div[contains(text(),'" + metadata_name + "')]")
        month_combo = (By.XPATH, "//div[contains(text(),'" + metadata_name + "')]/../div/select[@class='datefield  form-control']")
        month_id = self._driver.find_element(*month_combo).get_attribute("id")
        day_combo = (By.ID, month_id.replace("[1]", "[2]"))
        year_combo = (By.ID, month_id.replace("[1]", "[0]"))
        select_day = FolderContentBase("Exhibit").get_day_without_cero_at_beginning(select_date.split('/')[1])
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
        try:
            click_element(self._driver, self._driver.find_element(*self._save_changes_button))
            self._wait.until(ec.visibility_of_element_located(self._changes_successfully_saved))
        except NoSuchElementException:
            print "The  Save All button is not visible."
    
    def click_metadata_tab(self):
        """
        Clicks the metadata tab
        """
        self._wait.until(ec.visibility_of_element_located(self._metadata_active_tab))
        self._driver.find_element(*self._metadata_tab).click()
        self._wait.until(ec.visibility_of_element_located(self._wnv_text_panel))
    
    def is_keyword_value_displayed(self, keyword):
        """
        Verifies if the keyword value is displayed.
        :param keyword: The keyword to verify.
        :return: True if displayed, otherwise False.
        """
        keyword_value_text = (By.XPATH, "//form/div/div[contains(text(),'" + keyword[0] + "')]/following-sibling::div/input[@value='" + keyword[1] + "']")
        return is_element_present(self._driver, *keyword_value_text)
    
    def set_textbox_in_file_content_modal(self, keyword):
        """
        Sets textbox in file content modal.
        :param keyword: The keyword to set.
        """
        keyword_value_text = (By.XPATH, "//div[@class='keywordname' and contains(.,'" + keyword[0] + "')]/following-sibling::div/input")
        self._wait.until(ec.visibility_of_element_located(keyword_value_text))
        element = self._driver.find_element(*keyword_value_text)
        element.clear()
        element.send_keys(keyword[1])
    
    def set_combobox_keyword_file_content_modal(self, keyword):
        """
        Sets combobox in file content modal.
        :param keyword: The keyword to set.
        """
        keyword_value_text = (By.XPATH, "//form/div/div[contains(text(),'" + keyword[0] + "')]/following-sibling::div/select")
        self._wait.until(ec.visibility_of_element_located(keyword_value_text))
        try:
            Select(self._driver.find_element(*keyword_value_text)).select_by_visible_text(keyword[1])
        except NoSuchElementException as stale:
                print "Problem:" + str(stale)
    
    def click_versions_tab(self):
        """
        Clicks the Versions tab.
        """
        try:
            self._wait.until(ec.visibility_of_element_located(self._version_tab))
            self._driver.find_element(*self._version_tab).click()
            self._wait.until(ec.visibility_of_element_located(self._create_new_version_button))
        except NoSuchElementException:
            print "The 'Versions' tab is already selected."
    
    def click_create_new_version_button(self):
        """
        Clicks Create New Version button.
        """
        self._driver.find_element(*self._create_new_version_button).click()
        self._wait.until(ec.invisibility_of_element_located(self._create_new_version_button))
        self._wait.until(ec.visibility_of_element_located(self._version_tab))

    def click_promote_version(self, row):
        """
        Clicks promote version button to make it the working version.
        :param row: The row where the Version is present.
        """
        version = (By.XPATH, "//li[" + row + "]//a[@class='_img_pad button_container icon_promote ']")
        self._driver.find_element(*version).click()
        self._wait.until(ec.invisibility_of_element_located(self._create_new_version_button))
        self._wait.until(ec.visibility_of_element_located(self._tools_section))

    def is_version_displayed_in_list(self, version_name):
        """
        Verifies if new version is displayed in list.
        :param version_name: The name of new version created.
        :return: True if displayed, otherwise False.
        """
        _expected_version = (By.XPATH, "//li[contains(@class,'listclosed')]/div[contains(.,'" + version_name + "')]")
        return is_element_present(self._driver, *_expected_version)
    
    def select_version(self, version_name):
        """
        Clicks the select version.
        :param version_name: The version name.
        """
        version_item_collapsed = (By.XPATH, "//li[contains(@class,'listclosed')]/div[contains(.,'" + version_name + "')]")
        self._wait.until(ec.element_to_be_clickable(version_item_collapsed)).click()
        self._wait.until(ec.visibility_of_element_located(self._file_preview_image))
    
    def is_selected_version_displayed_in_file_content_modal(self, version_name):
        """
        Verifies if selected version is displayed in file content modal.
        :param version_name: The version name.
        :return: True if displayed, otherwise False.
        """
        _expected_version = (By.XPATH, "//div[@id='annotationCanvas']/img[contains(@src,'" + version_name + "')]")
        return is_element_present(self._driver, *_expected_version)
    
    def click_back_to_file_content_modal_button(self):
        """
        Clicks back file content modal.
        """
        self._wait.until(ec.invisibility_of_element_located(self._changes_successfully_saved))
        click_element(self._driver, self._driver.find_element(*self._back_button))
        self._wait.until(ec.invisibility_of_element_located(self._annotation_panel))

    def click_delete_version_button(self):
        """
        Clicks back file content modal.
        """
        accept_alert_before_displayed(self._driver)
        self._wait.until(ec.element_to_be_clickable(self._delete_button)).click()
        wait_for_load_page()
        self._wait.until(ec.visibility_of_element_located(self._version_tab))
    
    def click_flag_button(self):
        """
        Clicks the Flag button.
        """
        self._wait.until(ec.invisibility_of_element_located(self._flag_selected_button))
        self._driver.find_element(*self._flag_button).click()
        self._wait.until(ec.visibility_of_element_located(self._flag_selected_button))
    
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
        self._wait.until(ec.visibility_of_element_located(self._annotation_tab)).click()
        self._wait.until(ec.visibility_of_element_located(self._select_label))
    
    def is_annotation_item_displayed_in_annotation_list(self, expected_result):
        """
        Verifies if annotation item is displayed in Annotation list
        :param expected_result: The expected result regarding annotation (Flag, Stamp, Comment,etc)
        :return: True if displayed, otherwise False.
        """
        flag_in_annotation = (By.XPATH, "//ul[@id='annotationList']/descendant::div[.='" + expected_result[1] + "']")
        return is_element_present(self._driver, *flag_in_annotation)
    
    def click_containing_tab(self):
        """
        Clicks the containing tab.
        """
        self._wait.until(ec.visibility_of_element_located(self._containing_tab)).click()
        self._wait.until(ec.visibility_of_element_located(self._containing_documents_label))
    
    def click_file_in_containing_list(self):
        """
        Clicks file in Containing list.
        """
        self._wait.until(ec.visibility_of_element_located(self._containing_item)).click()
        self._wait.until(ec.visibility_of_element_located(self._view_file))
    
    def is_file_content_modal_displayed(self, file_name):
        """
        Verifies if file content modal is displayed when clicking file.
        :param file_name: The file name.
        :return: True if displayed, otherwise False.
        """
        self._wait.until(ec.visibility_of_element_located(self._annotation_tab))
        _expected_version = (By.XPATH, "//div[@id='annotationCanvas']/img[contains(@src,'" + file_name + "')]")
        return is_element_present(self._driver, *_expected_version)
    
    def is_annotation_displayed_in_file_content_modal(self, annotation_type):
        """
        Verifies if annotation type is displayed in file content modal.
        :param annotation_type: The annotation type.
        :return: True if displayed, otherwise False.
        """
        _annotation_button = (By.XPATH, "//span[.='"+annotation_type+"']") 
        return is_element_present(self._driver, *_annotation_button)
    
    def click_linked_tab(self):
        """
        Clicks the linked tab.
        """
        self._wait.until(ec.visibility_of_element_located(self._linked_tab)).click()
        self._wait.until(ec.visibility_of_element_located(self._linked_files_panel))
    
    def click_file_linked(self, file_name):
        """
        Clicks file linked.
        :param file_name: The file name.
        """
        view_file = (By.XPATH, "//img[@alt='"+file_name+"']")
        self._wait.until(ec.visibility_of_element_located(self._linked_list))
        self._driver.find_element(*self.get_image_of_linked_list(file_name)).click()
        self._wait.until(ec.visibility_of_element_located(view_file))
    
    def get_image_of_linked_list(self, file_name):
        """
        Gets image of linked list.
        :param file_name: The file name.
        """
        index = 1
        row = "//div[@id='linkedfilespanel']/descendant::div[@class='detailssubpanel']/ul/li[%s]/div/div"
        linked_item_selector = (By.XPATH, row % str(index))
        element = self._driver.find_element(*linked_item_selector)
        while not(file_name in element.text):
            index += 1
            linked_item_selector = (By.XPATH, row % str(index))
            try:
                element = self._driver.find_element(*linked_item_selector)
            except NoSuchElementException:
                print "The element was not found: ", file_name
                break
        return linked_item_selector
    
    def click_text_button(self):
        """
        Clicks text button.
        """
        self._wait.until(ec.visibility_of_element_located(self._text_button)).click()
    
    def set_user_comment(self, comment):
        """
        Sets new user comment.
        :param new comment: The new comment to set.
        """
        self._wait.until(ec.visibility_of_element_located(self._comment_text))
        element = self._driver.find_element(*self._comment_text)
        element.clear()
        element.send_keys(comment)
    
    def click_add_button(self):
        """
        Clicks add button.
        """
        self._wait.until(ec.element_to_be_clickable(self._add_button)).click()
        self._wait.until(ec.invisibility_of_element_located(self._comment_buttons))
    
    def is_comment_displayed_in_annotation_list(self, expected_result):
        """
        Verifies if comment is displayed in annotation list
        :param expected_result: The comment to verify.
        :return: True if displayed, otherwise False.
        """
        new_annotation = (By.XPATH, "//li[contains(@id,'annotationlist_new')]/descendant::div[contains(@class,'item') and contains(.,'" + expected_result + "')]")
        return is_element_present(self._driver, *new_annotation)
    
    def delete_comment(self, comment):
        """
        Deletes comment created.
        :param comment: The comment to delete.
        """
        comment_to_delete = (By.XPATH, "//li[contains(@id,'list_new')]/descendant::div[contains(@class,'item') and contains(.,'" + comment + "')]/following::div[contains(@class,'trash')]")
        if is_element_present(self._driver, *comment_to_delete):
            accept_alert_before_displayed(self._driver)
            self._wait.until(ec.element_to_be_clickable(comment_to_delete)).click()
            self._wait.until(ec.invisibility_of_element_located(comment_to_delete))
    
    def click_cancel_button(self):
        """
        Clicks cancel button.
        """
        self._wait.until(ec.visibility_of_element_located(self._cancel_button))
        click_element(self._driver, self._driver.find_element(*self._cancel_button))
    
    def click_stamp_button(self):
        """
        Clicks stamp button
        """
        try:
            self._driver.find_element(*self._stamp_button).click()
            self._wait.until(ec.visibility_of_element_located(self._stamp_selected_button))
        except NoSuchElementException:
            print"The Stamp button is not displayed."
    
    def click_stamp_item_button(self, stamp_selected):
        """
        Clicks stamp item button.
        :param stamp_selected: The stamp selected i.e. Expired
        """
        stamp_selected_button = (By.XPATH, "//div[@id='MviewStampList']/descendant::div[contains(@class,'Selected')]/img[@name='" + stamp_selected + "']")
        stamp_button = (By.NAME, stamp_selected)
        if is_element_present(self._driver, *self._stamp_displayed_pane):
            self._driver.find_element(*stamp_button).click()
            self._wait.until(ec.visibility_of_element_located(stamp_selected_button))
    
    def click_rectangle_button(self):
        """
        Clicks rectangle button.
        """
        if not is_element_present(self._driver, *self._rectangle_selected_button):
            self._wait.until(ec.visibility_of_element_located(self._rectangle_button)).click()
            self._wait.until(ec.visibility_of_element_located(self._rectangle_selected_button))
    
    def click_history_tab(self):
        """
        Clicks the history tab.
        """
        self._wait.until(ec.visibility_of_element_located(self._history_tab)).click()
        self._wait.until(ec.visibility_of_element_located(self._history_list))
    
    def click_recent_activity_in_history_list(self):
        """
        Clicks recent activity in history list
        """
        if is_element_present(self._driver, *self._history_item_collapsed):
            self._wait.until(ec.element_to_be_clickable(self._history_item_collapsed)).click()
            self._wait.until(ec.visibility_of_element_located(self._activity_item_collapsed))

    def click_metadata_changed_link(self):
        """
        Clicks Metadata Changed link in history list.
        """
        try:
            self._driver.find_element(*self._metadata_changed_link_closed).click()
            self._wait.until(ec.visibility_of_element_located(self._metadata_changed_link_opened))
        except NoSuchElementException:
            print "The Metadata Changed section is already opened."

    def is_metadata_changed_value_displayed(self, metadata_value):
        """
        Returns True if the metadata updated value is displayed, otherwise False.
        :param metadata_value: The value to verify.
        """
        return is_element_present(self._driver, By.XPATH, "//div/ul/li[contains(@class,'listopen')]//div/div[contains(., '" + metadata_value + "')]")

    def click_back_button(self):
        """
        Clicks back button in file content modal.
        """
        if is_element_present(self._driver, *self._back_button):
            click_element(self._driver, self._driver.find_element(*self._back_button))

    def click_back_to_file_button(self):
        """
        Clicks the Back button to return to File.
        """
        self._driver.find_element(*self._back_to_file_button).click()
        self._wait.until(ec.visibility_of_element_located(self._control_panel))

    def click_page_number_image(self, page_number, file_name):
        """
        Click page number in Details view.
        :param page_number: The number of page to select.
        :param file_name: The file name.
        """
        select_page = (By.XPATH, "//div[@id='spreadpreview" + page_number + "']/descendant::img")
        preview_file = (By.XPATH, "//div[@id='spreadcell" + page_number + "' and contains(@class,'previewhighlight')]")
        self._wait.until(ec.element_to_be_clickable(select_page)).click()
        wait_for_load_page()
        self._wait.until(ec.visibility_of_element_located(preview_file))
    
    def is_selected_page_loaded_in_file_content_modal(self, page_number):
        """
        Verifies if selected page is loaded in file content modal.
        :param page_number: The number of page selected.
        """
        preview_file = (By.XPATH, "//div[@id='spreadcell" + page_number + "' and contains(@class,'previewhighlight')]")
        return is_element_present(self._driver, *preview_file)
    
    def select_default_page_in_pages_tab(self, page_number):
        """
        Selects page by default in pages tab.
        :param page_number: The number of page to select.
        """
        cancel_button = (By.XPATH, "//div[@id='pagesdetails']/descendant::span[.='Cancel']")
        preview_file = (By.XPATH, "//div[@id='spreadcell" + page_number + "' and contains(@class,'previewhighlight')]")
        if not is_element_present(self._driver, *preview_file):
            self.click_page_number_image(page_number, None)
            self._wait.until(ec.element_to_be_clickable(self._default_preview_checkbox)).click()
            self._wait.until(ec.visibility_of_element_located(cancel_button))
    
    def is_selected_page_displayed_in_folder_content(self, expected_result):
        """
        Verifies if selected page is displayed in folder content.
        :param expected_result: The page to be displayed.
        """
        selected_page = (By.XPATH, "//div[@class='detailsheading' and contains(.,'Page " + expected_result[0] + " selected')]")
        return is_element_present(self._driver, *selected_page)
    
    def click_pages_tab(self):
        """
        Clicks pages tab.
        """
        self._wait.until(ec.visibility_of_element_located(self._pages_tab)).click()
        self._wait.until(ec.visibility_of_element_located(self._pages_files_panel))
