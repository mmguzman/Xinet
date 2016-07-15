__author__ = 'MarceloM Guzman'

from resources.uiabstraction.PageObjectFactory import PageObjectFactory


class WebNativeVolumesUsersSteps:
    """
    Steps definition for WebNative Volumes/Users page object.
    """
    _webnative_volumes_users = None

    def __init__(self):
        self._webnative_volumes_users = PageObjectFactory.create_webnative_volumes_users()

    def click_system_volumes_link(self):
        """
        Clicks the 'System Volumes' link.
        """
        self._webnative_volumes_users.click_system_volumes_link()

    def click_user_volumes_link(self):
        """
        Clicks the 'User Volumes' link.
        """
        self._webnative_volumes_users.click_user_volumes_link()
        
    def click_summary_link(self):
        """
        Clicks the 'Summary' link.
        """
        self._webnative_volumes_users.click_summary_link()
        
    def click_users_link(self):
        """
        Clicks the 'Users' link.
        """
        self._webnative_volumes_users.click_users_link()
        
    def click_groups_link(self):
        """
        Clicks the 'Groups' link.
        """
        self._webnative_volumes_users.click_groups_link()
        
    def click_new_system_volume_link(self):
        """
        Clicks the 'New System Volume' link.
        """
        self._webnative_volumes_users.click_new_system_volume_link()
        
    def click_new_user_link(self):
        """
        Clicks the 'New User' link.
        """
        self._webnative_volumes_users.click_new_user_link()
    
    def click_video_settings_link(self):
        """
        Clicks the 'Video Settings' link.
        """
        self._webnative_volumes_users.click_video_settings_link()
        
    def click_permissions_link(self):
        """
        Clicks the 'Permissions' link.
        """
        self._webnative_volumes_users.click_permissions_link()
        
    def click_edit_user_permissions_link(self):
        """
        Clicks the 'Edit User Permissions' link.
        """
        self._webnative_volumes_users.click_edit_user_permissions_link()
        
    def click_add_user_button(self):
        """
        Clicks the Add User button.
        """
        self._webnative_volumes_users.click_add_user_button()
    
    def is_item_displayed_in_combo(self, user_group_name):
        """
        Verifies if an item is displayed in the 'user or group name' combo.
        """
        return self._webnative_volumes_users.is_item_displayed_in_combo(user_group_name)
    
    def is_volume_displayed(self, volume_name):
        """
        Returns true if a Volume is displayed.
        """
        return self._webnative_volumes_users.is_volume_displayed(volume_name)
    
    def is_user_volume_displayed(self, username, volume_name):
        """
        Returns true if a User Volume is displayed.
        """
        return self._webnative_volumes_users.is_user_volume_displayed(username, volume_name)
        
    def verify_user_volume_displayed(self, username, volume_name):
        """
        Verifies if a User Volume is displayed.
        """
        self._webnative_volumes_users.verify_user_volume_displayed(username, volume_name)
        
    def edit_user_password(self, username, password):
        """
        Edits the password value of 'username' user.
        """
        self._webnative_volumes_users.edit_user_password(username, password)
        
    def add_new_user(self, username, password):
        """
        Set all the values to create a new User.
        """
        self._webnative_volumes_users.add_new_user(username, password)
        
    def add_new_group(self, username, groupname):
        """
        Set all the values to create a new Group.
        """
        self._webnative_volumes_users.add_new_group(username, groupname)
    
    def add_new_system_volume(self, volume_name, volume_type):
        """
        Set all values to create a new System Volume
        """
        self._webnative_volumes_users.add_new_system_volume(volume_name, volume_type)

    def add_new_user_volume(self, username, volume_name):
        """
        Set all the values to create a new User Volume.
        """
        self._webnative_volumes_users.add_new_user_volume(username, volume_name)
        
    def select_volume_in_video_settings(self, volume_name):
        """
        Selects a Volume from Video Settings section.
        """
        self._webnative_volumes_users.select_volume_in_video_settings(volume_name)
        
    def add_new_video_resolution(self, resolution_list):
        """
        Iterate over the list to create a new video resolution.
        """
        self._webnative_volumes_users.add_new_video_resolution(resolution_list)
        
    def configure_video_resolution(self, volume_name, resolution_list, object_name, video_name):
        """
        Configures the video resolution.
        """
        self._webnative_volumes_users.configure_video_resolution(volume_name, resolution_list, object_name, video_name)
        
    def apply_template_permission_to_user(self, username, template_name, permission_set_name):
        """
        Sets all values to apply a template permission over a user.
        """
        self._webnative_volumes_users.apply_template_permission_to_user(username, template_name, permission_set_name)
        
    def submit_and_close_alert(self):
        """
        Clicks the Submit and Update Previews button and close the alert displayed.
        """
        self._webnative_volumes_users.submit_and_close_alert()
        
    def verify_message_displayed(self, expected_message):
        """
        Verifies if a message is displayed according user creation.
        """
        self._webnative_volumes_users.verify_message_displayed(expected_message)
        
    def verify_volume_displayed(self, volume_name):
        """
        Verifies if a Volume is displayed.
        """
        self._webnative_volumes_users.verify_volume_displayed(volume_name)
    
    def enable_disable_plugin_item(self, plugin_name, user_name, setting_to):
        """
        Enables or disable a plugin according to 'setting_to'value (on/off).
        """
        self._webnative_volumes_users.enable_disable_plugin_item(plugin_name, user_name, setting_to)
