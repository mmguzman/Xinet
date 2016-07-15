__author__ = 'MarceloM Guzman'

import time

from robot.libraries.BuiltIn import BuiltIn
from selenium.common.exceptions import NoAlertPresentException, \
    NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

from resources.commons.DriverManager import DriverManager
from resources.commons.GlobalVariables import BACKUP_DIRECTORY_PATH_KARINA, \
    BACKUP_DIRECTORY_PATH_RH7WNV, BACKUP_DIRECTORY_PATH_BUDDY64, BACKUP_DIRECTORY_PATH_ALL, \
    BACKUP_DIRECTORY_PATH_ZBODIKOVA_MINI, BROWSER, DEFAULT_BUILT_IN_FACETS
from resources.libraries.Dictionaries import field_type, perm_set_checkbox, \
    facet_metadata
from resources.methods.UIMethods import select_checkbox, is_element_present, \
    accept_alert_before_displayed, click_element_stale, found_window, wait_for_load_page, click_element


class WebNativeDatabase(object):
    """
    Page object modeling the structure and operations of the Xinet WebNative Database page.
    """
    _driver = None
    _wait = None

    # Selectors
    _data_fields_link = (By.XPATH, "//a[text()='Data Fields']")
    _templates_link = (By.XPATH, "//a[text()='Templates']")
    _permission_sets_link = (By.XPATH, "//a[text()='Permission Sets']")
    _new_template_link = (By.XPATH, "//a[text()='New Template']")
    _new_field_link = (By.XPATH, "//a[text()='New Field']")
    _new_permission_set_link = (By.XPATH, "//a[text()='New Permission Set']")
    _admin_link = (By.XPATH, "//a[text()='Admin']")
    _searching_link = (By.XPATH, "//a[text()='Searching']")
    _backup_link = (By.XPATH, "//a[text()='Backup']")
    _new_backup_directory_link = (By.XPATH, "//a[contains(text(),'New Backup Directory')]")
    _summary_link = (By.XPATH, "//a[text()='Summary']")
    _edit_fields_link = (By.XPATH, "//a[text()='Edit Fields']")

    _data_field_set_combo = (By.NAME, "keywordset_id")
    _field_type_combo = (By.ID, "keyword_newtype")
    _display_format_combo = (By.ID, "field_disp")
    _integer_type_combo = (By.ID, "field_btyp")
    _facet_type_combo = (By.XPATH, "//span[@id='facetdata']/select")
    _bucket_size_combo = (By.NAME, "keyword_frange")
    _templates_combo = (By.NAME, "template_name")
    _add_data_field_combo = (By.ID, "keyword_name")
    _metadata_fields_table = (By.XPATH, "//tr[4]/th")
    _folder_path_combo = (By.NAME, "subdir")
    _select_data_field_combo = (By.NAME, "keyword_name")
    _select_face_type_combo = (By.XPATH, "//select[contains(@onchange,'facetchange')]")

    _field_name_textbox = (By.NAME, "keyword_newname")
    _template_name_textbox = (By.NAME, "template_namenew")
    _message_textbox = (By.XPATH, "//div[@id='messages']/span")
    _popup_value_textbox = (By.NAME, "value_newvalue")
    _decimal_digits_textbox = (By.NAME, "field_prec")
    _permission_set_textbox = (By.NAME, "permset_newname")
    _create_folder_textbox = (By.NAME, "newfolder")

    _maximum_length_text = (By.XPATH, "//th[contains(text(),'Maximum Length')]")
    _integer_type_text = (By.XPATH, "//th[contains(text(),'Integer Type')]")
    _total_digits_text = (By.XPATH, "//th[contains(text(),'Total Digits')]")
    _display_format_text = (By.XPATH, "//th[contains(text(),'Display Format')]")
    _display_type_text = (By.XPATH, "//th[contains(text(),'Display Type')]")
    _templates_text = (By.XPATH, "//th[text()='Templates']")
    _solr_searching_text = (By.XPATH, "//th[contains(text(),'Solr Searching (Portal Only)')]")
    _solr_db_enabled_text = (By.XPATH, "//b[text()='Enabled']")

    _backup_save_settings_button = (By.NAME, 'backupsavesettings')
    _save_button = (By.NAME, "keyword_submit")
    _add_and_edit_button = (By.NAME, "keyword_submitandedit")
    _add_data_field_values_button = (By.NAME, "valueadd")
    _add_field_button = (By.ID, "addfield")
    _save_template_button = (By.NAME, "templatecreate")
    _add_permission_set_button = (By.NAME, "permset_submit")
    _refresh_now_button = (By.XPATH, "//input[@value='Refresh Now']")
    _create_solr_db_button = (By.XPATH, "//input[@value='Create Solr DB']")
    _move_solr_db_button = (By.XPATH, "//input[@value='Move Solr DB']")
    _edit_backup_button = (By.NAME, "choosebackupdir")
    _set_directory_button = (By.NAME, "newdirsubmit")
    _close_button = (By.XPATH, "//input[@value='Close']")
    _create_folder_button = (By.XPATH, "//button[@type='button' and text()='Create Folder']")
    _save_changes_button = (By.NAME, "solrbuiltinf")

    _use_custom_values_radio_button = (By.NAME, "value_usecurrent")
    _use_current_values_radio_button = (By.XPATH, "(//input[@name='value_usecurrent'])[2]")

    _save_into_xmp_packet_checkbox = (By.ID, "keyword_xmpwrite")
    _save_into_xmp_packet_edit_checkbox = (By.NAME, "keyword_xmpeditable")
    _facet_checkbox = (By.NAME, "keyword_facet")

    _summary_selected = (By.XPATH, "//li[contains(@class,'selected')]/a[text()='Summary']")
    _new_field_selected = (By.XPATH, "//li[contains(@class,'selected')]/a[text()='New Field']")

    _data_field_set_label = (By.XPATH, "//th[contains(text(),'Data Field Set:')]")

    _updating_em = (By.XPATH, "//em[text()='Updating...')]")
    _data_field_updated_span = (By.XPATH, "//div[@id='messages']/span[contains(text(),'Data Field')]")
    _changes_saved_span = (By.XPATH, "//div[@id='messages']/span[contains(text(),'Changes were successfully saved')]")

    def __init__(self):
        self._driver = DriverManager().get_instance().get_driver()
        self._wait = DriverManager().get_instance().get_wait()

    def click_data_fields_link(self):
        """
        Clicks the 'Data Fields' link.
        """
        self._wait.until(ec.visibility_of_element_located(self._data_fields_link))
        click_element_stale(self._driver, *self._data_fields_link)
        self._wait.until(ec.visibility_of_element_located(self._new_field_link))

    def click_templates_link(self):
        """
        Clicks the 'Templates' link.
        """
        self._wait.until(ec.visibility_of_element_located(self._templates_link))
        click_element_stale(self._driver, *self._templates_link)
        self._wait.until(ec.visibility_of_element_located(self._new_template_link))

    def click_permission_sets_link(self):
        """
        Clicks the 'Permission Sets' link.
        """
        self._wait.until(ec.visibility_of_element_located(self._permission_sets_link))
        click_element_stale(self._driver, *self._permission_sets_link)
        self._wait.until(ec.visibility_of_element_located(self._new_permission_set_link))

    def click_new_template_link(self):
        """
        Clicks the 'New Template' link.
        """
        self._wait.until(ec.visibility_of_element_located(self._new_template_link))
        click_element_stale(self._driver, *self._new_template_link)
        self._wait.until(ec.visibility_of_element_located(self._template_name_textbox))

    def click_admin_link(self):
        """
        Clicks the 'Admin' link.
        """
        self._wait.until(ec.visibility_of_element_located(self._admin_link))
        click_element_stale(self._driver, *self._admin_link)
        self._wait.until(ec.visibility_of_element_located(self._refresh_now_button))

    def click_searching_link(self):
        """
        Clicks the 'Searching' link.
        """
        self._wait.until(ec.visibility_of_element_located(self._searching_link))
        click_element_stale(self._driver, *self._searching_link)
        self._wait.until(ec.visibility_of_element_located(self._solr_searching_text))

    def click_backup_link(self):
        """
        Clicks the 'Backup' link.
        """
        self._wait.until(ec.visibility_of_element_located(self._backup_link))
        click_element_stale(self._driver, *self._backup_link)
        self._wait.until(ec.visibility_of_element_located(self._edit_backup_button))

    def click_new_field_link(self):
        """
        Clicks the 'New Field' link.
        """
        self._wait.until(ec.visibility_of_element_located(self._new_field_link))
        self._driver.find_element(*self._new_field_link).click()
        self._wait.until(ec.visibility_of_element_located(self._field_name_textbox))

    def click_new_permission_set_link(self):
        """
        Clicks the 'New Permission Set' link.
        """
        self._wait.until(ec.visibility_of_element_located(self._new_permission_set_link))
        click_element_stale(self._driver, *self._new_permission_set_link)
        self._wait.until(ec.visibility_of_element_located(self._templates_combo))

    def click_new_backup_directory_link(self):
        """
        Clicks the 'New Backup Directory' link.
        """
        self._wait.until(ec.visibility_of_element_located(self._set_directory_button))
        if is_element_present(self._driver, *self._new_backup_directory_link):
            click_element_stale(self._driver, *self._new_backup_directory_link)
            time.sleep(1)
        else:
            print 'false: click_new_backup_directory_link'

    def click_edit_field_image_button(self, data_field_name):
        """
        Clicks the edit image button of a data field
        """
        data_field = (By.XPATH, "//tr/th[contains(text(),'" + data_field_name + "')]/following-sibling::td/input[@value='Modify']")
        click_element_stale(self._driver, *data_field)
        self._wait.until(ec.visibility_of_element_located(self._save_button))

    def set_template_name(self, template_name):
        """
        Sets the template name.
        """
        self._wait.until(ec.visibility_of_element_located(self._template_name_textbox))
        element = lambda: self._driver.find_element(*self._template_name_textbox)
        element().clear()
        element().send_keys(template_name)

    def set_field_name(self, field_name):
        """
        Sets the field name.
        """
        self._wait.until(ec.visibility_of_element_located(self._field_name_textbox))
        element = lambda: self._driver.find_element(*self._field_name_textbox)
        element().clear()
        element().click()
        element().send_keys(field_name)

    def set_popup_value(self, field_name):
        """
        Sets the popup value.
        """
        self._wait.until(ec.visibility_of_element_located(self._popup_value_textbox))
        element = lambda: self._driver.find_element(*self._popup_value_textbox)
        element().clear()
        element().send_keys(field_name)

    def set_permission_set_name(self, permission_set_name):
        """
        Sets the Permission Set value.
        """
        element = lambda: self._driver.find_element(*self._permission_set_textbox)
        element().clear()
        element().send_keys(permission_set_name)

    def set_decimal_digits_value(self, field_name):
        """
        Sets the Decimal Digits value.
        """
        element = lambda: self._driver.find_element(*self._decimal_digits_textbox)
        element().clear()
        element().send_keys(field_name)

    def select_field_type_combo(self, fieldtype):
        """
        Selects the Field Type option.
        """
        self._wait.until(ec.visibility_of_element_located(self._field_type_combo))
        select = Select(self._driver.find_element(*self._field_type_combo))
        select.select_by_visible_text(fieldtype)
        if fieldtype == field_type.get('text'):
            self._wait.until(ec.visibility_of_element_located(self._maximum_length_text))
        elif fieldtype == field_type.get('integer'):
            self._wait.until(ec.visibility_of_element_located(self._integer_type_text))
        elif fieldtype == field_type.get('float'):
            self._wait.until(ec.visibility_of_element_located(self._total_digits_text))
        elif fieldtype == field_type.get('date'):
            self._wait.until(ec.visibility_of_element_located(self._display_format_text))
        elif fieldtype == field_type.get('boolean'):
            self._wait.until(ec.visibility_of_element_located(self._display_type_text))

    def select_display_format_combo(self, display_format):
        """
        Selects the Display Format option.
        """
        select = Select(self._driver.find_element(*self._display_format_combo))
        select.select_by_visible_text(display_format)

    def select_add_data_field_combo(self, data_field):
        """
        Selects a field from Add Data Field option.
        """
        select = Select(self._driver.find_element(*self._add_data_field_combo))
        try:
            select.select_by_visible_text(data_field)
        except NoSuchElementException:
            new_data_field = data_field.replace("*", "")
            select.select_by_visible_text(new_data_field)
        # Note:
        # The (.148) server is  displaying 'Byline' without '*', but another servers are displaying 'Byline*'
        # This behavior allows that the '13 Make a new wnv tmpl template'TC failed.
        # select = Select(self._driver.find_element(*self._add_data_field_combo))
        # select.select_by_visible_text(data_field)
    
    def select_data_field_combo(self, data_field):
        """
        Selects a data field of combo box.
        :param data_field: The data field.
        """
        select = Select(self._driver.find_element(*self._select_data_field_combo))
        select.select_by_visible_text(data_field)
        data_field_selector = (By.XPATH, "//input[@value='" + data_field + "']")
        self._wait.until(ec.visibility_of_element_located(data_field_selector))
    
    def select_facet_type_combo(self, value):
        """
        Selects a face type of combo box.
        :param value: The value (e.g.range).
        """
        select = Select(self._driver.find_element(*self._select_face_type_combo))
        select.select_by_visible_text(value)
    
    def click_save_edit_fields_button(self):
        """
        Clicks the save edit fields button.
        """
        self._driver.find_element(*self._save_button).click()
        self._wait.until(ec.visibility_of_element_located(self._data_field_updated_span))
        
    def change_facet_type(self, data_field_name, value, bucket_size=None):
        """
        Changes the facet type according to the data field name selected.
        :param data_field_name: The data field name.
        :param value: The value to update.
        :param bucket_size: The bucket size.
        """
        self.select_data_field_combo(facet_metadata[data_field_name])
        self.select_facet_type_combo(value)
        if bucket_size != None:
            self._wait.until(ec.visibility_of_element_located(self._bucket_size_combo))
            self.select_bucket_size_combo(bucket_size)
        self.click_save_edit_fields_button()
    
    def set_default_values_facet(self, metadata_list):
        """
        Sets values by default for facet(e.g. Integer, Float-2dec)
        :param metadata_list: The list of metadatas.
        """
        self.click_data_fields_link()
        self.click_edit_fields_link()
        for metadata in metadata_list:
            self.change_facet_type(metadata[0], metadata[1], metadata[2])
    
    def select_bucket_size_combo(self, bucket_size):
        """
        Selects a bucket size of combo box.
        :param bucket_size: The bucket size (e.g. auto mode).
        """
        select = Select(self._driver.find_element(*self._bucket_size_combo))
        select.select_by_visible_text(bucket_size)

    def select_integer_type_combo(self, integer_type):
        """
        Selects the Integer Type option.
        """
        select = Select(self._driver.find_element(*self._integer_type_combo))
        select.select_by_visible_text(integer_type)

    def select_template_combo(self, template_name):
        """
        Selects the Integer Type option.
        """
        select = Select(self._driver.find_element(*self._templates_combo))
        select.select_by_visible_text(template_name)
        self._wait.until(ec.visibility_of_element_located(self._metadata_fields_table))

    def select_folder_option(self, folder_name):
        """
        Selects the folder option of backup root path.
        """
        if not is_element_present(self._driver, By.XPATH, "//option[text()='" + folder_name + "']"):
            self.create_new_folder(folder_name)
        else:
            select = Select(self._driver.find_element(*self._folder_path_combo))
            select.select_by_visible_text(folder_name)

    def select_folder_option_list(self, output_folder_name_list):
        """
        Selects folders from a folder list.
        """
        do_cd_up_index = 0
        for folder_list in output_folder_name_list:
            self.select_folder_option(folder_list)
            folder_href = (By.XPATH, "//a[@href='javascript:do_cd_up(" + str(do_cd_up_index) + ")']")
            self._wait.until(ec.visibility_of_element_located(folder_href))
            do_cd_up_index += 1

    def create_new_folder(self, folder_name):
        """
        Creates a new folder.
        """
        if is_element_present(self._driver, *self._folder_path_combo):
            self.select_folder_option("( New Folder )")
        self._driver.find_element(*self._create_folder_textbox).send_keys(folder_name)
        self._driver.find_element(*self._create_folder_button).click()

    def select_backup_directory_path(self, server_name):
        """
        Selects the Backup Directory folder.
        """
        if server_name == "karina":
            self.select_folder_option_list(BACKUP_DIRECTORY_PATH_KARINA)
        elif server_name == "rh7wnv":
            self.select_folder_option_list(BACKUP_DIRECTORY_PATH_RH7WNV)
        elif server_name == "buddy64":
            self.select_folder_option_list(BACKUP_DIRECTORY_PATH_BUDDY64)
        elif server_name == "zbodikova-mini":
            self.select_folder_option_list(BACKUP_DIRECTORY_PATH_ZBODIKOVA_MINI)
        else:
            self.select_folder_option_list(BACKUP_DIRECTORY_PATH_ALL)

    def get_message_displayed(self):
        """
        Gets the message displayed after create a new field.
        """
        self._wait.until(ec.visibility_of_element_located(self._message_textbox))
        return self._driver.find_element(*self._message_textbox).text

    def click_save_button(self):
        """
        Clicks the Save button
        """
        accept_alert_before_displayed(self._driver)
        click_element(self._driver, self._driver.find_element(*self._save_button))
        self._wait.until(ec.visibility_of_element_located(self._message_textbox))

    def click_add_and_edit_button(self):
        """
        Clicks the Add and Edit button.
        """
        self._driver.find_element(*self._add_and_edit_button).click()
        self._wait.until(ec.visibility_of_element_located(self._add_data_field_values_button))

    def click_add_popup_value_button(self):
        """
        Clicks the Add popup value button.
        """
        self._driver.find_element(*self._add_data_field_values_button).click()
        wait_for_load_page()
        time.sleep(2)

    def click_add_field_button(self, data_field):
        """
        Clicks the Add button to add a new data field.
        """
        if data_field == "Byline*":
            data_field = "Byline"
        data_field_added = (By.XPATH, "//th[contains(text(),'" + data_field + "')]")
        self._driver.find_element(*self._add_field_button).click()
        self._wait.until(ec.visibility_of_element_located(data_field_added))

    def click_save_template_button(self):
        """
        Clicks the Save template button.
        """
        accept_alert_before_displayed(self._driver)
        self._driver.find_element(*self._save_template_button).click()

    def click_add_permission_set_button(self):
        """
        Clicks the Save template button.
        """
        self._driver.find_element(*self._add_permission_set_button).click()
        self._wait.until(ec.visibility_of_element_located(self._message_textbox))

    def click_create_solr_db_button(self):
        """
        Clicks the Create Solr DB button.
        """
        self._driver.find_element(*self._create_solr_db_button).click()
        self._wait.until(ec.visibility_of_element_located(self._solr_db_enabled_text))

    def click_edit_backup_button(self):
        """
        Clicks the Edit backup button.
        """
        self._wait.until(ec.visibility_of_element_located(self._edit_backup_button))
        self._driver.find_element(*self._edit_backup_button).click()
        time.sleep(3)

    def click_set_directory_button(self):
        """
        Clicks the Set Directory button.
        """
        self._wait.until(ec.visibility_of_element_located(self._set_directory_button))
        if BROWSER.lower() != "safari":
            self._driver.find_element(*self._set_directory_button).click()
            time.sleep(1)
            self._wait.until(ec.alert_is_present())
            self.accept_and_close_alert()
        else:
            accept_alert_before_displayed(self._driver)
            self._driver.find_element(*self._set_directory_button).click()

    def click_close_button(self):
        """
        Clicks the Close button.
        """
        self._wait.until(ec.visibility_of_element_located(self._close_button))
        self._driver.find_element(*self._close_button).click()

    def click_radio_button(self, data_field, button_type):
        """
        Clicks the radio button next to the data field added.
        Button type parameters are: 1=Locked , 2=Popup,  3=Edit.
        """
        if data_field == "Byline*":
            data_field = "Byline"
        field = (By.XPATH, "//th[contains(text(),'" + data_field + "')]/following-sibling::td/input[@type='radio' and @value='" + button_type + "']")
        self._driver.find_element(*field).click()

    def click_use_custom_values_radio_button(self):
        """
        Clicks the 'Use Custom Values' radio button.
        """
        self._wait.until(ec.visibility_of_element_located(self._use_custom_values_radio_button))
        self._driver.find_element(*self._use_custom_values_radio_button).click()

    def click_use_current_values_radio_button(self):
        """
        Clicks the 'Use Current Values' radio button.
        """
        self._wait.until(ec.visibility_of_element_located(self._use_current_values_radio_button))
        self._driver.find_element(*self._use_current_values_radio_button).click()

    def click_save_changes_button(self):
        """
        Clicks the Save Changes button.
        """
        self._driver.find_element(*self._save_changes_button).click()
        self._wait.until(ec.visibility_of_element_located(self._changes_saved_span))

    def select_permission_set_checkbox(self, data_field, checkbox_type):
        """
        Clicks the checkbox next to the data field added.
        Checkbox type parameters are: visible, searchable, browse, enabled, required, push required, editable, popup, locked.
        """
        global checkbox
        if checkbox_type == "visible":
            checkbox = perm_set_checkbox.get("visible")
        if checkbox_type == "searchable":
            checkbox = perm_set_checkbox.get("searchable")
        if checkbox_type == "browse":
            checkbox = perm_set_checkbox.get("browse")
        if checkbox_type == "enabled":
            checkbox = perm_set_checkbox.get("enabled")
        if checkbox_type == "required":
            checkbox = perm_set_checkbox.get("required")
        if checkbox_type == "push required":
            checkbox = perm_set_checkbox.get("push required")
        if checkbox_type == "editable":
            checkbox = perm_set_checkbox.get("editable")
        if checkbox_type == "popup":
            checkbox = perm_set_checkbox.get("popup")
        if checkbox_type == "locked":
            checkbox = perm_set_checkbox.get("locked")
        data_field = (By.XPATH, "//th[text()='" + data_field + "']/following::input[@type='checkbox' and contains(@name,'" + checkbox + "')]")
        select_checkbox(self._driver, *data_field)

    def select_save_into_xmp_packet_checkbox(self):
        """
        Checks the Save Into XMP Packet checkbox.
        """
        select_checkbox(self._driver, *self._save_into_xmp_packet_checkbox)

    def select_save_into_xmp_packet_edit_checkbox(self):
        """
        Checks the Save Into XMP Packet checkbox when editing a data field.
        """
        if not (self._driver.find_element(*self._save_into_xmp_packet_edit_checkbox)).is_selected():
            select_checkbox(self._driver, *self._save_into_xmp_packet_edit_checkbox)

    def select_facet_checkbox(self):
        """
        Checks the Facet checkbox.
        """
        select_checkbox(self._driver, *self._facet_checkbox)

    def select_built_in_facet(self, built_in_facet_name):
        """
        Checks the Built-in checkbox according the ``built_in_facet_name`` argument.
        :param built_in_facet_name: The Built-in facet name.
        :return:
        """
        built_in_selector = (By.XPATH, "//th[contains(text(),'" + built_in_facet_name + "')]/input[@type='checkbox']")
        select_checkbox(self._driver, *built_in_selector)

    def set_default_built_in_facets_values(self):
        """
        Set the default Built-in facets values.
        """
        from resources.uiabstraction.pages.webnative import WebNativeHome
        web_native_home = WebNativeHome.WebNativeHome()
        web_native_home.click_database_link()
        self.click_searching_link()
        for built_in_facet in DEFAULT_BUILT_IN_FACETS:
            self.select_built_in_facet(built_in_facet)
        self.click_save_changes_button()

    def is_data_field_displayed(self, data_field_name):
        """
        Returns true if a Data Field is displayed.
        """
        data_field_value = (By.XPATH, "//th[contains(text(),'" + data_field_name + "')]")
        return is_element_present(self._driver, *data_field_value)

    def is_template_displayed_combo(self, template_name):
        """
        Verifies if a Template is displayed in the Templates combo
        """
        template_combo_value = (By.XPATH, "//option[@value='" + template_name + "']")
        return is_element_present(self._driver, *template_combo_value)

    def is_permission_set_displayed(self, permission_set_name):
        """
        Verifies if a Permission Set is displayed in Permission Sets section.
        """
        self._wait.until(ec.visibility_of_element_located(self._templates_text))
        permission_set_value = (By.XPATH, "//a[text()='" + permission_set_name + "']")
        return is_element_present(self._driver, *permission_set_value)

    def is_solr_db_created(self):
        """
        Verifies if Solr DB is already created.
        """
        return is_element_present(self._driver, *self._solr_db_enabled_text)

    def is_db_backup_displayed(self, server_name):
        """
        Returns true if a DB Backup is displayed.
        """
        db_backup_dir = self.get_db_backup_path(server_name)
        db_backup_value = (By.XPATH, "//span[contains(text(),'" + db_backup_dir + "')]")
        return is_element_present(self._driver, *db_backup_value)

    def verify_if_db_backup_is_displayed(self, server_name):
        """
        Verifies if a DB Backup is displayed.
        """
        BuiltIn().should_be_true(self.is_db_backup_displayed(server_name))

    def get_db_backup_path(self, server_name):
        """
        Gets the path of the DB Backup.
        """
        global db_backup_path

        if server_name == "karina":
            db_backup_path = '/'.join(BACKUP_DIRECTORY_PATH_KARINA)
        elif server_name == "rh7wnv":
            db_backup_path = '/'.join(BACKUP_DIRECTORY_PATH_RH7WNV)
        elif server_name == "buddy64":
            db_backup_path = '/'.join(BACKUP_DIRECTORY_PATH_BUDDY64)
        elif server_name == "zbodikova-mini":
            db_backup_path = '/'.join(BACKUP_DIRECTORY_PATH_ZBODIKOVA_MINI)
        else:
            db_backup_path = '/'.join(BACKUP_DIRECTORY_PATH_ALL)
        return db_backup_path

    def verify_if_solr_db_is_created(self):
        """
        Verifies if a Hot Folder is displayed. (If the 'Enabled' message is displayed, it is already created.)
        """
        BuiltIn().should_be_true(self.is_solr_db_created)

    def verify_message_displayed(self, expected_message):
        """
        Verifies if a message is displayed.
        """
        displayed_message = self.get_message_displayed()
        BuiltIn().should_be_equal(displayed_message, expected_message)

    def add_new_field(self, name, fieldtype, save_xmp_packet, facet, facet_values, popup_list, popup_values, date_format, integer_type, decimal_digits):
        """
        Set all values to create a new field according 'fieldtype'.
        """
        self.click_new_field_link()
        self.set_field_name(name)
        self.select_field_type_combo(fieldtype)
        if save_xmp_packet == True:
            self.select_save_into_xmp_packet_checkbox()

        if facet == True:
            self.select_facet_checkbox()

        if facet_values != None:
            i = iter(facet_values)
            self.select_facet_type_combo(i.next())
            self.select_bucket_size_combo(i.next())

        if popup_list != None:
            self.click_add_and_edit_button()
            for i in popup_list:
                if len(i) > 0:
                    self.set_popup_value(i)
                    self.click_add_popup_value_button()
                    popup_value = (By.XPATH, "//option[@value='" + i + "']")
                    self._wait.until(ec.visibility_of_element_located(popup_value))

        if popup_values != None:
            if popup_values == True:
                self.click_use_custom_values_radio_button()
            else:
                self.click_use_current_values_radio_button()

        if date_format != None:
            self.select_display_format_combo(date_format)

        if integer_type != None:
            self.select_integer_type_combo(integer_type)

        if decimal_digits != None:
            self.set_decimal_digits_value(decimal_digits)

    def create_new_field(self, name, field_type, save_xmp_packet, facet, facet_values, popup_list, popup_values, date_format, integer_type, decimal_digits):
        """
         Adds and verifies if a field was added.
        """
        self.verify_if_data_fields_summary_link_is_displayed()
        if not (self.is_data_field_displayed(name)):
            self.add_new_field(name, field_type, save_xmp_packet, facet, facet_values, popup_list, popup_values, date_format, integer_type, decimal_digits)
            self.click_save_button()
            if popup_list == None:
                self.verify_message_displayed("Keyword " + name + " successfully added.")
            else:
                self.verify_message_displayed("Data Field " + name + " successfully updated.")
        else:
            print "The " + name + " data field is already created."

    def update_data_field(self, data_field_name):
        """
        Sets values to update a data field
        """
        self.click_edit_field_image_button(data_field_name)
        self.select_save_into_xmp_packet_edit_checkbox()
        self.click_save_button()

    def add_new_template(self, template_name, data_field_list):
        """
        Sets all values to create a new template.
        """
        if not (self.is_template_displayed_combo(template_name)):
            self.click_new_template_link()
            self.set_template_name(template_name)
            for data_field in data_field_list:
                i = iter(data_field)
                field = i.next()
                self.select_add_data_field_combo(field)
                self.click_add_field_button(field)
                self.click_radio_button(field, i.next())
            self.click_save_and_close_alert()
        else:
            print "The " + template_name + " template is already created."

    def add_new_permission_set(self, template_name, permission_set_name, data_field_list):
        """
        Sets all values to create a new permission set.
        """
        if not (self.is_permission_set_displayed(permission_set_name)):
            self.click_new_permission_set_link()
            self.select_template_combo(template_name)
            self.set_permission_set_name(permission_set_name)
            for data_field in data_field_list:
                i = iter(data_field)
                field = i.next()
                self.select_permission_set_checkbox(field, i.next())
                self.select_permission_set_checkbox(field, i.next())
                self.select_permission_set_checkbox(field, i.next())
            self.click_add_permission_set_button()
        else:
            print "The " + permission_set_name + " permission set is already created."

    def set_backup_folder_to_venture_backups(self, server_name):
        """
        Sets all values to set backup to venture_backups directory.
        """
        if not (self.is_db_backup_displayed(server_name)):
            parent_page = self._driver.current_window_handle
            try:
                self.click_edit_backup_button()
                self._wait.until(found_window("dbmgrWindow"))
                self.click_new_backup_directory_link()
                self.select_backup_directory_path(server_name)
                self.click_set_directory_button()
            finally:
                self._driver.switch_to_window(parent_page)
                self._wait.until(ec.invisibility_of_element_located(self._updating_em))
        else:
            print "The backup is already created."

    def create_solr_db(self):
        """
        Creates a Solr DB.
        """
        if not (self.is_solr_db_created()):
            self.click_create_solr_db_button()
        else:
            print "The Solr DB is already created."

    def click_save_and_close_alert(self):
        """
        Clicks the Save button and close the alert displayed.
        """
        self.click_save_template_button()

    def accept_and_close_alert(self):
        """
        Accepts and closes the alert displayed.
        """
        try:
            alert = self._driver.switch_to_alert()
            alert.accept()
        except NoAlertPresentException:
            print "There is no alert to switch on."

    def verify_if_data_fields_summary_link_is_displayed(self):
        """
        Verifies if  the 'Summary link' is displayed
        """
        if not (is_element_present(self._driver, *self._summary_selected)):
            self._driver.find_element(*self._summary_link).click()
            self._wait.until(ec.visibility_of_element_located(self._summary_selected))
    
    def click_edit_fields_link(self):
        """
        Clicks the 'edit fields' link.
        """
        self._wait.until(ec.visibility_of_element_located(self._edit_fields_link))
        self._driver.find_element(*self._edit_fields_link).click()
        self._wait.until(ec.visibility_of_element_located(self._data_field_set_combo))
