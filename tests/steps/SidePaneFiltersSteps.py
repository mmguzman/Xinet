__author__ = 'Edmundo Cossio'

from resources.commons.GlobalVariables import TEMPLATE
from resources.uiabstraction.PageObjectFactory import PageObjectFactory


class SidePaneFiltersSteps:
    """
    Steps definition for SidePaneFilters page object.
    """
    _side_pane_filters = None

    def __init__(self):
        self._side_pane_filters = PageObjectFactory.create_side_pane_filters(TEMPLATE)
        
    def verify_if_metadata_is_configured_according_to_bucket_size(self, expected_range):
        """
        Verifies if the metadata is configured according to bucket size(e.g. auto mode)
        :param expected_range: The expected range.
        """
        self._side_pane_filters.verify_if_metadata_is_configured_according_to_bucket_size(expected_range)
    
    def verify_that_there_is_one_range_for_file_list(self, files):
        """
        Verifies if there is one range for file list into a folder(e.g. Big-Integer Folder)
        :param files:The list of files into a folder.
        """
        self._side_pane_filters.verify_there_is_one_range_for_file_list(files)
        
    def type_file_name_in_filters(self, file_name):
        """
        Types a file name in the filters tab according to data field (e.g. file name=16.indd and data field=Integer).
        :param file_name: The file name.
        """
        self._side_pane_filters.type_file_name_in_filters(file_name)

    def verify_if_range_is_displayed_in_filters_tab_according_to_bucket_size(self, range_expected_in_filters):
        """
        Verifies if a range is displayed in filters tab according to bucket size
        :param range_expected_in_filters: The range expected in the Filters tab.
        """
        self._side_pane_filters.verify_if_range_is_displayed_in_filters_tab_according_to_bucket_size(range_expected_in_filters)
    
    def expand_filters_link_in_side_pane(self):
        """
        Expands the filters link.
        """
        self._side_pane_filters.expand_filters_link_in_side_pane()
        
    def collapse_filters_link_in_side_pane(self):
        """
        Collapses the filters link in side pane.
        """
        self._side_pane_filters.collapse_filters_link_in_side_pane()
    
    def click_go_in_filters(self):
        """
        Clicks go in the filters tab.
        """
        self._side_pane_filters.click_go_in_filters()
    
    def expand_folder_for_xwnvfacet(self, data_field):
        """
        Expands folder for xwnv Facet in the filters tab.
        :param data_field: The data field e.g. Integer.
        """
        self._side_pane_filters.expand_folder_for_xwnvfacet(data_field)
