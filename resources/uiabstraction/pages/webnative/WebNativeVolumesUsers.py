__author__ = 'MarceloM Guzman'

import time

from robot.libraries.BuiltIn import BuiltIn
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select

from resources.commons.DriverManager import DriverManager
from resources.commons.GlobalVariables import VOLUME_PATH_KARINA, VOLUME_PATH_RH7WNV, \
    VOLUME_PATH_BUDDY64, VOLUME_PATH_ZBODIKOVA_MINI, VOLUME_PATH_ALL, BROWSER
from resources.libraries.Dictionaries import no_db_volume, no_fpo_volume, wnv_volume
from resources.methods.UIMethods import is_element_present, select_checkbox, unselect_checkbox, \
    accept_alert_before_displayed, click_element_stale, click_element, wait_for_option_selected_in_combo, \
    wait_for_load_page


class WebNativeVolumesUsers(object):
    """
    Page object modeling the structure and operations of the Xinet WebNative Volumes/Users page.
    """
    _driver = None
    _wait = None

    # Selectors
    _system_volumes_link = (By.XPATH, "//a[text()='System Volumes']")
    _new_volume_link = (By.XPATH, "//a[text()='New System Volume']")
    _user_volumes_link = (By.XPATH, "//a[text()='User Volumes']")
    _user_volumes_summary_link = (By.XPATH, "//a[text()='Summary']")
    _new_user_volume_link = (By.XPATH, "//a[text()='New Volume']")
    _video_settings_link = (By.XPATH, "//a[text()='Video Settings']")
    _users_link = (By.XPATH, "//a[text()='Users']")
    _edit_user_link = (By.XPATH, "//a[contains(text(),'Edit User')]")
    _new_user_link = (By.XPATH, "//a[text()='New User']")
    _groups_link = (By.XPATH, "//a[text()='Groups']")
    _new_group_link = (By.XPATH, "//a[text()='New Group']")
    _root_path_link = (By.XPATH, "//a[contains(text(),'Root Path:')]")
    _permissions_link = (By.XPATH, "//a[contains(text(),'Permissions')]")
    _edit_user_permissions_link = (By.XPATH, "//a[contains(text(),'Edit User Permissions')]")
    _video_settings_selected_link = (By.XPATH, "//li[@class='passive selected']/a[.='Video Settings']")
    _plugins_link = (By.XPATH, "//a[text()='Plugins']")

    _message_textbox = (By.XPATH, "//div[@id='messages']/span")
    _volume_name_textbox = (By.NAME, "v_name")
    _username_textbox = (By.NAME, "username")
    _password_textbox = (By.NAME, "password")
    _password_again_textbox = (By.NAME, "password1")
    _group_name_textbox = (By.NAME, "groupname")
    _user_volume_name_textbox = (By.NAME, "uservol0")
    _resolution_description_textbox = "lrDesc"
    _create_folder_textbox = (By.NAME, "newfolder")

    _submit_volume_button = (By.NAME, "vsubmit")
    _submit_update_previews_button = (By.NAME, "submitrebuild")
    _submit_user_volume_button = (By.NAME, "addvolumesubmit0")
    _add_user_button = (By.NAME, "useraddsubmit")
    _add_group_button = (By.NAME, "submitgroupadd")
    _add_button = (By.XPATH, "//input[@value='Add >']")
    _add_resolution_button = (By.NAME, "lowresmovieadd")
    _submit_user_permissions_button = (By.NAME, "permset_submit")
    _submit_edit_user_button = (By.NAME, "editusersubmit")
    _create_folder_button = (By.XPATH, "//button[@type='button' and text()='Create Folder']")
    _submit_plugin_button=(By.NAME,"changeplugins")

    _frame_id = (By.ID, "waFrame")
    _volume_combo = (By.NAME, "editvol")
    _volumes_for_user_combo = (By.XPATH, "//th[contains(text(),'Volumes for')]")
    _root_path_combo = (By.NAME, "subdir")
    _system_web_volume_combo = (By.ID, "volpath0")
    _sub_folder_volume_link = (By.ID, "r_cwd0")
    _download_permissions_combo = (By.ID, "4")
    _user_group_combo = (By.XPATH, "//span[text()='Username']")
    _group_combo = (By.XPATH, "//span[text()='Group Name']")
    _username_combo = (By.ID, "user_name")
    _edit_user_combo = (By.ID, "user0")
    _template_combo = (By.NAME, "template_name")
    _permission_set_combo = (By.NAME, "permset_name")
    _video_encoding_combo = "lrOutputFormat"
    _video_size_combo = "lrWH"
    _video_quality_combo = "lrQuality"
    _video_enabled_combo = "tmpEnabled"
    _i_rotateMode3D_combo = (By.NAME, "i_rotateMode3D")
    _i_movieMode3D_combo = (By.NAME, "i_movieMode3D")
    _select_user_combo = (By.ID, "user0")

    _remove_previews_checkbox = (By.NAME, "v_clearres")
    _enable_db_checkbox = (By.NAME, "v_dbena")
    _show_history_checkbox = (By.ID, "4194304")
    _show_versions_checkbox = (By.ID, "16777216")
    _custom_image_order_checkbox = (By.ID, "262144")
    _file_management_checkbox = (By.ID, "524288")

    _user_successfully_added_span = (By.CSS_SELECTOR, "span")
    _message_displayed_after_click_add_group_span = (By.XPATH, "//div[@id='messages']/span")

    _user_group_name_label = (By.ID, "usergroupopuplabel")
    _primary_group_label = (By.XPATH, "//th[text()='Primary Group:']")
    _user_or_group_has_no_volumes_configured_label = (By.CSS_SELECTOR, "h3")

    _summary_selected = (By.XPATH, "//li[contains(@class,'selected')]/a[text()='Summary']")
    _new_system_volume_selected = (By.XPATH, "//li[contains(@class,'selected')]/a[text()='New System Volume']")
    _plugins_selected = (By.XPATH, "//li[contains(@class,'first last selected')]/a[.='Plugins']")

    _info_table_table = (By.CLASS_NAME, 'infotable')
    _volumes_table = (By.ID, "voltable")

    def __init__(self):
        self._driver = DriverManager().get_instance().get_driver()
        self._wait = DriverManager().get_instance().get_wait()

    def enable_disable_plugin_item(self, plugin_name, user_name, setting_to):
        """
        Enables or disable a plugin according to 'setting_to'value (on/off).
        """
        self.click_plugins_link()
        self.select_user_from_plugins(user_name)
        self.click_plugin_item_radiobutton(plugin_name, setting_to)
        self.click_submit_plugins_button()

    def click_plugin_item_radiobutton(self, plugin_name, setting_to):
        """
        Clicks the plugin item to set to 'off or on' according to 'setting_to value'.
        """
        plugin_item = (By.XPATH, "//th[.='" + plugin_name + "']/following-sibling::td/input[@value='" + setting_to + "']")
        self._wait.until(ec.visibility_of_element_located(plugin_item))
        click_element_stale(self._driver, *plugin_item)

    def click_plugins_link(self):
        """
        Clicks the 'plugins' link.
        """
        self._wait.until(ec.visibility_of_element_located(self._plugins_link))
        click_element_stale(self._driver, *self._plugins_link)
        self._wait.until(ec.visibility_of_element_located(self._plugins_selected))

    def click_system_volumes_link(self):
        """
        Clicks the 'System Volumes' link.
        """
        self._wait.until(ec.visibility_of_element_located(self._system_volumes_link))
        click_element_stale(self._driver, *self._system_volumes_link)
        self._wait.until(ec.visibility_of_element_located(self._summary_selected))

    def click_user_volumes_link(self):
        """
        Clicks the 'User Volumes' link.
        """
        self._wait.until(ec.visibility_of_element_located(self._user_volumes_link))
        click_element_stale(self._driver, *self._user_volumes_link)
        self._wait.until(ec.visibility_of_element_located(self._volumes_for_user_combo))

    def click_summary_link(self):
        """
        Clicks the 'Summary' link.
        """
        self._wait.until(ec.visibility_of_element_located(self._user_volumes_summary_link))
        click_element_stale(self._driver, *self._user_volumes_summary_link)
        self._wait.until(ec.visibility_of_element_located(self._volumes_for_user_combo))

    def click_users_link(self):
        """
        Clicks the 'Users' link.
        """
        self._wait.until(ec.visibility_of_element_located(self._users_link))
        click_element_stale(self._driver, *self._users_link)
        self._wait.until(ec.visibility_of_element_located(self._user_group_combo))

    def click_edit_user_link(self):
        """
        Clicks the 'Edit User' link.
        """
        self._wait.until(ec.visibility_of_element_located(self._edit_user_link))
        click_element_stale(self._driver, *self._edit_user_link)
        self._wait.until(ec.visibility_of_element_located(self._submit_edit_user_button))

    def click_groups_link(self):
        """
        Clicks the 'Groups' link.
        """
        self._wait.until(ec.visibility_of_element_located(self._groups_link))
        click_element_stale(self._driver, *self._groups_link)
        self._wait.until(ec.visibility_of_element_located(self._user_group_name_label))

    def click_video_settings_link(self):
        """
        Clicks the 'Video Settings' link.
        """
        self._wait.until(ec.visibility_of_element_located(self._video_settings_link))
        click_element_stale(self._driver, *self._video_settings_link)
        if not is_element_present(self._driver, *self._video_settings_selected_link):
            self.click_new_system_volume_link()
            click_element_stale(self._driver, *self._video_settings_link)
        self._wait.until(ec.visibility_of_element_located(self._video_settings_selected_link))

    def click_new_system_volume_link(self):
        """
        Clicks the 'New System Volume' link.
        """
        self._wait.until(ec.visibility_of_element_located(self._new_volume_link))
        click_element_stale(self._driver, *self._new_volume_link)
        self._wait.until(ec.visibility_of_element_located(self._new_system_volume_selected))

    def click_new_user_volume_link(self):
        """
        Clicks the 'New Volume' link.
        """
        self._wait.until(ec.visibility_of_element_located(self._new_user_volume_link))
        click_element_stale(self._driver, *self._new_user_volume_link)
        self._wait.until(ec.visibility_of_element_located(self._submit_user_volume_button))

    def click_new_user_link(self):
        """
        Clicks the 'New User' link.
        """
        self._wait.until(ec.visibility_of_element_located(self._new_user_link))
        click_element_stale(self._driver, *self._new_user_link)
        self._wait.until(ec.visibility_of_element_located(self._add_user_button))

    def click_new_group_link(self):
        """
        Clicks the 'New Group' link.
        """
        self._wait.until(ec.visibility_of_element_located(self._new_group_link))
        click_element_stale(self._driver, *self._new_group_link)
        self._wait.until(ec.visibility_of_element_located(self._add_group_button))

    def click_permissions_link(self):
        """
        Clicks the 'Permissions' link.
        """
        self._wait.until(ec.visibility_of_element_located(self._permissions_link))
        click_element_stale(self._driver, *self._permissions_link)
        self._wait.until(ec.visibility_of_element_located(self._user_group_name_label))

    def click_edit_user_permissions_link(self):
        """
        Clicks the 'Edit User Permissions' link.
        """
        self._wait.until(ec.visibility_of_element_located(self._edit_user_permissions_link))
        click_element_stale(self._driver, *self._edit_user_permissions_link)
        self._wait.until(ec.visibility_of_element_located(self._submit_user_permissions_button))

    def click_root_path(self):
        """
        Clicks the 'Root Path' link.
        """
        self._wait.until(ec.visibility_of_element_located(self._root_path_link))
        self._driver.find_element(*self._root_path_link).click()
        self._wait.until(ec.visibility_of_element_located(self._root_path_combo))

    def select_folder_option(self, folder_name):
        """
        Selects the folder option of Volume root path.
        """
        if not is_element_present(self._driver, By.XPATH, "//option[text()='" + folder_name + "']"):
            self.create_new_folder(folder_name)
        else:
            select = Select(self._driver.find_element(*self._root_path_combo))
            select.select_by_visible_text(folder_name)

    def select_folder_option_list(self, folder_name_list):
        """
        Selects a folder of combo box.
        """
        do_cd_up_index = 0
        for folder_list in folder_name_list:
            self.select_folder_option(folder_list)
            folder_href = (By.XPATH, "//a[@href='javascript:do_cd_up(" + str(do_cd_up_index) + ")']")
            self._wait.until(ec.visibility_of_element_located(folder_href))
            do_cd_up_index += 1

    def create_new_folder(self, folder_name):
        """
        Creates a new folder.
        """
        if is_element_present(self._driver, *self._root_path_combo):
            self.select_folder_option("( New Folder )")
        self._driver.find_element(*self._create_folder_textbox).send_keys(folder_name)
        self._driver.find_element(*self._create_folder_button).click()

    def select_volume_root_path(self, server_name, volume_type):
        """
        Selects the Root Path for the volume created.
        """
        if server_name == "karina":
            self.select_folder_option_list(VOLUME_PATH_KARINA)
        elif server_name == "rh7wnv":
            self.select_folder_option_list(VOLUME_PATH_RH7WNV)
        elif server_name == "buddy64":
            self.select_folder_option_list(VOLUME_PATH_BUDDY64)
        elif server_name == "zbodikova-mini":
            self.select_folder_option_list(VOLUME_PATH_ZBODIKOVA_MINI)
        else:
            self.select_folder_option_list(VOLUME_PATH_ALL)
        self.select_folder_option(server_name + "_" + volume_type)

    def unselect_remove_previews(self):
        """
        Unchecks the 'Remove Previews' option.
        """
        unselect_checkbox(self._driver, *self._remove_previews_checkbox)

    def unselect_enable_db(self):
        """
        Unchecks the 'Enable Database' option.
        """
        unselect_checkbox(self._driver, *self._enable_db_checkbox)

    def select_show_history_checkbox(self):
        """
        Checks the 'Show History' option.
        """
        select_checkbox(self._driver, *self._show_history_checkbox)

    def select_show_versions_checkbox(self):
        """
        Checks the 'Show Versions' option.
        """
        select_checkbox(self._driver, *self._show_versions_checkbox)

    def select_custom_image_order_checkbox(self):
        """
        Checks the 'Custom Image Order' option.
        """
        select_checkbox(self._driver, *self._custom_image_order_checkbox)

    def select_file_management_checkbox(self):
        """
        Checks the 'File Management' option.
        """
        select_checkbox(self._driver, *self._file_management_checkbox)

    def _set_value_textbox(self, textbox_selector, value):
        """
        Types any value in a text box.
        """
        self._wait.until(ec.visibility_of_element_located(textbox_selector))
        element = lambda: self._driver.find_element(*textbox_selector)
        element().clear()
        element().click()
        element().send_keys(value)

    def set_volume_name(self, value):
        """
        Sets the 'Volume' value.
        """
        self._set_value_textbox(self._volume_name_textbox, value)

    def set_username_value(self, value):
        """
        Sets the 'Username' value.
        """
        self._set_value_textbox(self._username_textbox, value)

    def set_password_value(self, value):
        """
        Sets the 'Password' value.
        """
        self._set_value_textbox(self._password_textbox, value)

    def set_password_again_value(self, value):
        """
        Sets the 'Password (again)' value.
        """
        self._set_value_textbox(self._password_again_textbox, value)

    def set_group_name_value(self, value):
        """
        Sets the 'Group Name' value.
        """
        self._set_value_textbox(self._group_name_textbox, value)

    def set_user_volume_name(self, value):
        """
        Sets the 'User Volume' value.
        """
        self._set_value_textbox(self._user_volume_name_textbox, value)

    def set_resolution_description(self, row, value):
        """
        Sets the 'Description' value in resolution section.
        """
        description_selector = (By.NAME, self._resolution_description_textbox + str(row))
        self._set_value_textbox(description_selector, value)

    def select_user_from_group_userlist(self, username):
        """
        Selects a user from Users section.
        """
        select = Select(self._driver.find_element_by_name("userList"))
        select.select_by_visible_text(username)

    def select_user_from_edit_user(self, username):
        """
        Selects a user from Edit User section.
        """
        select = Select(self._driver.find_element(*self._edit_user_combo))
        select.select_by_visible_text(username)

    def select_volume_in_video_settings(self, volume_name):
        """
        Selects a Volume from Video Settings section.
        """
        select = Select(self._driver.find_element(*self._volume_combo))
        select.select_by_visible_text(volume_name)
        self._wait.until(ec.visibility_of_element_located(self._submit_update_previews_button))

    def select_system_web_volume(self, volume_name):
        """
        Selects a Volume from Video Settings section.
        """
        web_volume_name = volume_name + " WEB"
        select = Select(self._driver.find_element(*self._system_web_volume_combo))
        select.select_by_visible_text(web_volume_name)
        condition = ec.text_to_be_present_in_element(self._sub_folder_volume_link, volume_name)
        self._wait.until(condition)

    def select_download_permissions_option(self, option):
        """
        Selects an option from Download Permissions section.
        """
        select = Select(self._driver.find_element(*self._download_permissions_combo))
        select.select_by_visible_text(option)

    def select_video_encoding_option(self, row, option):
        """
        Selects an option from Video Encoding section.
        """
        video_encoding_selector = (By.NAME, self._video_encoding_combo + str(row))
        select = Select(self._driver.find_element(*video_encoding_selector))
        select.select_by_visible_text(option)

    def select_video_size_option(self, row, option):
        """
        Selects an option from Video Size section.
        """
        video_size_selector = (By.NAME, self._video_size_combo + str(row))
        select = Select(self._driver.find_element(*video_size_selector))
        select.select_by_visible_text(option)

    def select_video_quality_option(self, row, option):
        """
        Selects an option from Quality section.
        """
        video_quality_selector = (By.NAME, self._video_quality_combo + str(row))
        select = Select(self._driver.find_element(*video_quality_selector))
        select.select_by_visible_text(option)

    def select_username_from_user_permissions(self, username):
        """
        Selects an option from Username section.
        """
        select = Select(self._driver.find_element(*self._username_combo))
        select.select_by_visible_text(username)
        if username == "wnv":
            self._wait.until(ec.visibility_of_element_located(self._primary_group_label))

    def select_template(self, template_name):
        """
        Selects an option from Template section.
        """
        self._wait.until(ec.visibility_of_element_located(self._template_combo))
        select = Select(self._driver.find_element(*self._template_combo))
        select.select_by_visible_text(template_name)
        wait_for_option_selected_in_combo(self._driver, template_name, *self._template_combo)

    def select_permission_set(self, permission_set_name):
        """
        Selects an option from Permission Set section.
        """
        self._wait.until(ec.visibility_of_element_located(self._permission_set_combo))
        select = Select(self._driver.find_element(*self._permission_set_combo))
        select.select_by_visible_text(permission_set_name)
        wait_for_option_selected_in_combo(self._driver, permission_set_name, *self._permission_set_combo)

    def select_user_from_plugins(self, username):
        """
        Selects a user from Plugins section.
        """
        select = Select(self._driver.find_element(*self._select_user_combo))
        select.select_by_visible_text(username)
        wait_for_load_page()
        self._wait.until(ec.visibility_of_element_located(self._primary_group_label))

    def click_submit_button(self, volume_type):
        """
        Clicks the Submit button.
        """
        if BROWSER.lower() != "safari":
            self._driver.find_element(*self._submit_volume_button).click()
            if volume_type != "no_db":
                time.sleep(1)
                self._wait.until(ec.alert_is_present())
        else:
            accept_alert_before_displayed(self._driver)
            self._driver.find_element(*self._submit_volume_button).click()

    def click_submit_user_volume_button(self):
        """
        Clicks the Submit button.
        """
        self._driver.find_element(*self._submit_user_volume_button).click()
        self._wait.until(ec.visibility_of_element_located(self._volumes_for_user_combo))

    def click_submit_plugins_button(self):
        """
        Clicks the submit plugins button.
        """
        self._driver.find_element(*self._submit_plugin_button).click()
        wait_for_load_page()
        self._wait.until(ec.visibility_of_element_located(self._message_displayed_after_click_add_group_span))

    def click_submit_user_permissions_button(self):
        """
        Clicks the Submit User Permissions button.
        """
        self._driver.find_element(*self._submit_user_permissions_button).click()
        self._wait.until(ec.visibility_of_element_located(self._message_textbox))

    def click_submit_edit_user_button(self):
        """
        Clicks the Submit Edit User button.
        """
        self._driver.find_element(*self._submit_edit_user_button).click()
        self._wait.until(ec.visibility_of_element_located(self._message_textbox))

    def click_add_user_button(self):
        """
        Clicks the Add User button.
        """
        self._driver.find_element(*self._add_user_button).click()

    def click_add_button(self, username):
        """
        Clicks the Add button.
        """
        self._driver.find_element(*self._add_button).click()
        new_member_added = By.XPATH, "//option[text()='" + username + "']"
        self._wait.until(ec.visibility_of_element_located(new_member_added))

    def click_add_group_button(self):
        """
        Clicks the Add Group button.
        """
        self._driver.find_element(*self._add_group_button).click()
        self._wait.until(ec.visibility_of_element_located(self._message_displayed_after_click_add_group_span))

    def click_add_resolution_button(self, row_to_wait):
        """
        Clicks the Add Resolution button (+).
        """
        self._wait.until(ec.element_to_be_clickable(self._add_resolution_button))
        click_element(self._driver, self._driver.find_element(*self._add_resolution_button))
        description_selector = (By.NAME, self._resolution_description_textbox + str(row_to_wait))
        self._wait.until(ec.visibility_of_element_located(description_selector))

    def click_submit_and_update_previews_button(self):
        """
        Clicks the Submit And Update Previews button.
        """
        accept_alert_before_displayed(self._driver)
        self._driver.find_element(*self._submit_update_previews_button).click()

    def is_item_displayed_in_combo(self, user_group_name):
        """
        Verifies if an item is displayed in the 'user or group name' combo.
        """
        self._wait.until(ec.visibility_of_element_located(self._user_group_name_label))
        if self.is_user_or_group_displayed_combo():
            self._wait.until(ec.visibility_of_element_located(self._edit_user_combo))
            username_combo_value = (By.XPATH, "//option[@value='" + user_group_name + "']")
            return is_element_present(self._driver, *username_combo_value)
        else:
            return False

    def is_user_or_group_displayed_combo(self):
        """
        Verifies if 'user or group name' combo is displayed.
        """
        return is_element_present(self._driver, *self._edit_user_combo)

    def is_folder_displayed_combo(self, folder_name):
        """
        Verifies if a folder is displayed in the Folders combo
        """
        folder_name_combo_value = (By.XPATH, "//option[text()='" + folder_name + "']")
        return is_element_present(self._driver, *folder_name_combo_value)

    def get_message_displayed(self):
        """
        Get the message displayed.
        """
        return self._driver.find_element(*self._message_textbox).text

    def verify_message_displayed(self, expected_message):
        """
        Verifies if a message is displayed.
        """
        displayed_message = self.get_message_displayed()
        BuiltIn().should_be_equal(displayed_message, expected_message)

    def is_volume_displayed(self, volume_name):
        """
        Returns true if a Volume is displayed.
        """
        parent_page = self._driver.current_window_handle
        try:
            self._wait.until(ec.frame_to_be_available_and_switch_to_it(self._frame_id))
            volume_value = (By.XPATH, "//th[text()='" + volume_name + "']")
            return is_element_present(self._driver, *volume_value)
        finally:
            self._driver.switch_to_window(parent_page)

    def verify_volume_displayed(self, volume_name):
        """
        Verifies if a Volume is displayed.
        """
        BuiltIn().should_be_true(self.is_volume_displayed(volume_name))

    def is_user_volume_displayed(self, username, volume_name):
        """
        Returns true if a User Volume is displayed.
        """
        self.select_user(username)
        self._wait.until(lambda s: s.find_elements(*self._info_table_table) or s.find_element(*self._user_or_group_has_no_volumes_configured_label))
        volume_value = (By.XPATH, "//th[contains(text(),'" + volume_name + "')]")
        return is_element_present(self._driver, *volume_value)

    def verify_user_volume_displayed(self, username, volume_name):
        """
        Verifies if a User Volume is displayed.
        """
        BuiltIn().should_be_true(self.is_user_volume_displayed(username, volume_name))

    def set_system_volume_checkbox_values(self, volume_type):
        """
        Clicks the volume path given in ``volume_type`` argument.
        """
        checkbox_values = None
        if volume_type == "no_db":
            checkbox_values = no_db_volume
        elif volume_type == "no_fpo":
            checkbox_values = no_fpo_volume
        elif volume_type == "wnv":
            checkbox_values = wnv_volume
        for value in checkbox_values.itervalues():
            is_option_displayed = is_element_present(self._driver, *value)
            if is_option_displayed:
                select_checkbox(self._driver, *value)
            elif not is_option_displayed and value[1] == 'v_storeoffice':
                print "The following option is not displayed: Store Office Document Previews."
        if volume_type == "no_db":
            self.unselect_enable_db()
        self.unselect_remove_previews()

    def add_new_system_volume(self, server_name, volume_type):
        """
        Set all values to create a new System Volume.
        """
        if not (self.is_volume_displayed(server_name + "_" + volume_type)):
            parent_page = self._driver.current_window_handle
            self.click_new_system_volume_link()
            self._wait.until(ec.frame_to_be_available_and_switch_to_it(self._frame_id))
            self.click_root_path()
            self.select_volume_root_path(server_name, volume_type)
            self.set_volume_name(server_name + "_" + volume_type)
            self.set_system_volume_checkbox_values(volume_type)
            self.click_submit_button(volume_type)
            if BROWSER.lower() != "safari":
                if volume_type != "no_db":
                    self.accept_and_close_alert()
            self._driver.switch_to_window(parent_page)
            self._wait.until(ec.visibility_of_element_located(self._summary_selected))
        else:
            print "The " + server_name + "_" + volume_type + " volume is already created."

    def add_new_user(self, username, password):
        """
        Set all the values to create a new user.
        """
        if not (self.is_item_displayed_in_combo(username)):
            self.click_new_user_link()
            self.set_username_value(username)
            self.set_password_value(password)
            self.set_password_again_value(password)
            self.click_add_user_button()
            self._wait.until(ec.visibility_of_element_located(self._user_successfully_added_span))
        else:
            print "The " + username + " user is already created."

    def edit_user_password(self, username, password):
        """
        Edits the password value of 'username' user.
        """
        self.click_edit_user_link()
        self.select_user_from_edit_user(username)
        self.set_password_value(password)
        self.set_password_again_value(password)
        self.click_submit_edit_user_button()

    def steps_to_create_group(self, group_name, username):
        """
        Sets required values to add a new group.
        """
        self.click_new_group_link()
        self.set_group_name_value(group_name)
        self.select_user_from_group_userlist(username)
        self.click_add_button(username)
        self.click_add_group_button()

    def add_new_group(self, group_name, username):
        """
        Set all the values to create a new group.
        """
        if self.is_user_or_group_displayed_combo():
            if not (self.is_item_displayed_in_combo(group_name)):
                self.steps_to_create_group(group_name, username)
            else:
                print "The " + group_name + " user is already created."
        else:
            self.steps_to_create_group(group_name, username)

    def add_new_user_volume(self, username, volume_name):
        """
        Set all the values to create a new user volume.
        """
        if not (self.is_user_volume_displayed(username, volume_name)):
            self.click_new_user_volume_link()
            self.select_system_web_volume(volume_name)
            self.set_user_volume_name(volume_name)
            self.select_show_history_checkbox()
            self.select_show_versions_checkbox()
            self.select_custom_image_order_checkbox()
            self.select_file_management_checkbox()
            self.select_download_permissions_option("Download All Files")
            self.click_submit_user_volume_button()
        else:
            print "The " + volume_name + " user volume is already created."

    def select_user(self, username):
        """
        Selects an user of 'Volumes for' combo.
        """
        select = Select(self._driver.find_element(*self._edit_user_combo))
        select.select_by_visible_text(username)
        wait_for_option_selected_in_combo(self._driver, username, *self._edit_user_combo)

    def add_new_video_resolution(self, resolution_list):
        """
        Add a new video resolution if not exists in the given row.
        """
        row = int(resolution_list[4])
        actual_row = row + 2
        if not (is_element_present(self._driver, By.XPATH, "//tr[" + str(actual_row) + "]/td")):
            self.create_new_video_resolution(resolution_list, row)
        else:
            print "The resolution is already created."

    def create_new_video_resolution(self, resolution_list, row):
        """
        Iterate over the list to create a new video resolution.
        """
        self.click_add_resolution_button(row)
        i = iter(resolution_list)
        self.set_resolution_description(row, i.next())
        self.select_video_encoding_option(row, i.next())
        self.select_video_size_option(row, i.next())
        self.select_video_quality_option(row, i.next())

    def configure_video_resolution(self, volume_name, resolution_list, object_name, video_name):
        """
        Configures video resolution.
        """
        parent_page = self._driver.current_window_handle
        try:
            self.click_video_settings_link()
            self._wait.until(ec.frame_to_be_available_and_switch_to_it(self._frame_id))
            self.select_volume_in_video_settings(volume_name)
            for row in resolution_list:
                self.add_new_video_resolution(row)
            self.select_type_of_rotate_in_rotate_around_3D_objects_combo(object_name)
            self.select_type_of_resolution_in_generate_low_resolution_videos_combo(video_name)
            self.click_submit_and_update_previews_button()
            self.verify_3D_options_for_volume(object_name, self._i_rotateMode3D_combo)
            self.verify_3D_options_for_volume(video_name, self._i_movieMode3D_combo)
        finally:
            self._driver.switch_to_window(parent_page)

    def verify_3D_options_for_volume(self, item, combo):
        """
        Verifies in the '3D options for volume' group if an item was selected in combo.
        For example:
                 Verifies if the 'off' item was selected in the 'Rotate around 3D object' combo.   
        """
        self._wait.until(ec.visibility_of_element_located(combo))
        select = Select(self._driver.find_element(*combo))
        selected_option = select.first_selected_option
        if item in selected_option.text:
            BuiltIn().should_be_true('true' in selected_option.get_attribute('selected'))
        else:
            BuiltIn().should_be_true(False)

    def select_type_of_rotate_in_rotate_around_3D_objects_combo(self, object_name):
        """
        Selects a type of rotate in 'Rotate around 3D objects' combo.
        """
        self._wait.until(ec.visibility_of_element_located(self._i_rotateMode3D_combo))
        select = Select(self._driver.find_element(*self._i_rotateMode3D_combo))
        select.select_by_visible_text(object_name)

    def select_type_of_resolution_in_generate_low_resolution_videos_combo(self, video_name):
        """
        Selects a type of resolution in 'Generate low resolution videos' combo.
        """
        self._wait.until(ec.visibility_of_element_located(self._i_movieMode3D_combo))
        select = Select(self._driver.find_element(*self._i_movieMode3D_combo))
        select.select_by_visible_text(video_name)

    def apply_template_permission_to_user(self, username, template_name, permission_set_name):
        """
        Sets all values to apply a template permission over a user.
        """
        self.select_username_from_user_permissions(username)
        self.select_template(template_name)
        self.select_permission_set(permission_set_name)
        self.click_submit_user_permissions_button()

    def submit_and_close_alert(self):
        """
        Clicks the Submit and Update Previews button and close the alert displayed.
        """
        self.click_submit_and_update_previews_button()

    def accept_and_close_alert(self):
        """
        Accepts and closes the alert displayed.
        """
        try:
            alert = self._driver.switch_to_alert()
            alert.accept()
        except NoAlertPresentException:
            print "There is no alert to switch on."
