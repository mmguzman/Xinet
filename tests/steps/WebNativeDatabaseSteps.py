__author__ = 'MarceloM Guzman'

from resources.uiabstraction.PageObjectFactory import PageObjectFactory


class WebNativeDatabaseSteps:
    """
    Steps definition for WebNative Database page object.
    """
    _webnative_database = None

    def __init__(self):
        self._webnative_database = PageObjectFactory.create_webnative_database()

    def click_data_fields_link(self):
        """
        Clicks the Data Fields link.
        """
        self._webnative_database.click_data_fields_link()
        
    def click_templates_link(self):
        """
        Clicks the Templates link.
        """
        self._webnative_database.click_templates_link()
        
    def click_permission_sets_link(self):
        """
        Clicks the Permission Sets link.
        """
        self._webnative_database.click_permission_sets_link()
        
    def click_admin_link(self):
        """
        Clicks the Admin link.
        """
        self._webnative_database.click_admin_link()
        
    def click_searching_link(self):
        """
        Clicks the Searching link.
        """
        self._webnative_database.click_searching_link()
        
    def click_backup_link(self):
        """
        Clicks the Backup link.
        """
        self._webnative_database.click_backup_link()
        
    def add_new_field(self, name, fieldtype, save_xmp_packet, facet):
        """
        Set all values to create a new field according 'fieldtype'.
        """
        self._webnative_database.add_new_field(name, fieldtype)
        
    def click_new_template_link(self):
        """
        Clicks the New Template link.
        """
        self._webnative_database.click_new_template_link()
        
    def click_new_permission_set_link(self):
        """
        Clicks the New Permission Set link.
        """
        self._webnative_database.click_new_permission_set_link()
        
    def create_new_field(self, name, field_type, save_xmp_packet, facet, facet_values, popup_list, popup_values, date_format, integer_type, decimal_digits):
        """
         Adds and verifies if a field was added.
        """
        self._webnative_database.create_new_field(name, field_type, save_xmp_packet, facet, facet_values, popup_list, popup_values, date_format, integer_type, decimal_digits)

    def update_data_field(self, data_field_name):
        """
        Sets values to update a data field
        """
        self._webnative_database.update_data_field(data_field_name)

    def add_new_template(self, template_name, data_field_list):
        """
        Sets all the values to create a new template.
        """
        self._webnative_database.add_new_template(template_name, data_field_list)
       
    def add_new_permission_set(self, template_name, permission_set_name, data_field_list):
        """
        Sets all values to create a new permission set.
        """
        self._webnative_database.add_new_permission_set(template_name, permission_set_name, data_field_list)
    
    def set_backup_folder_to_venture_backups(self, server_name):
        """
        Sets all values to set backup to venture_backups directory.
        """
        self._webnative_database.set_backup_folder_to_venture_backups(server_name)
        
    def is_template_displayed_combo(self, template_name):
        """
        Verifies if a Template is displayed in the Templates combo
        """
        return self._webnative_database.is_template_displayed_combo(template_name)
    
    def is_permission_set_displayed(self, permission_set_name):
        """
        Verifies if a Permission Set is displayed in Permission Sets section.
        """
        return self._webnative_database.is_permission_set_displayed(permission_set_name)
        
    def is_db_backup_displayed(self, server_name):
        """
        Returns true if a DB Backup is displayed.
        """
        return self._webnative_database.is_db_backup_displayed(server_name)
        
    def is_solr_db_created(self):
        """
        Verifies if Solr DB is already created.
        """
        return self._webnative_database.is_solr_db_created()
        
    def create_solr_db(self):
        """
        Creates a Solr DB.
        """
        self._webnative_database.create_solr_db()
        
    def verify_message_displayed(self, expected_message):
        """
        Verifies if a message is displayed.
        """
        self._webnative_database.verify_message_displayed(expected_message)
        
    def verify_if_db_backup_is_displayed(self, server_name):
        """
        Verifies if a DB Backup is displayed.
        """
        self._webnative_database.verify_if_db_backup_is_displayed(server_name)
        
    def verify_if_solr_db_is_created(self):
        """
        Verifies if a Hot Folder is displayed. (If the 'Enabled' message is displayed, it is already created.)
        """
        self._webnative_database.verify_if_solr_db_is_created()
    
    def click_edit_fields_link(self):
        """
        Clicks the 'edit fields' link.
        """
        self._webnative_database.click_edit_fields_link()
        
    def change_facet_type(self, data_field_name, value, bucket_size=None):
        """
        Changes the facet type according to the data field name selected.
        :param data_field_name: The data field name.
        :param value: The value to update.
        :param bucket_size: The bucket size.
        """
        self._webnative_database.change_facet_type(data_field_name, value, bucket_size)
    
    def set_default_values_facet(self, metadata_list):
        """
        Sets values by default for facet(e.g. Integer, Float-2dec)
        :param metadata_list: The list of metadatas.
        """
        self._webnative_database.set_default_values_facet(metadata_list)

    def set_default_built_in_facets_values(self):
        """
        Set the default Built-in facets values.
        """
        self._webnative_database.set_default_built_in_facets_values()
