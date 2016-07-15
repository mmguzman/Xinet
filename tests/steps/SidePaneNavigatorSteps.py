__author__ = 'MarceloM Guzman'

from resources.commons.GlobalVariables import TEMPLATE
from resources.uiabstraction.PageObjectFactory import PageObjectFactory


class SidePaneNavigatorSteps:
    """
    Steps definition for SidePaneNavigator page object.
    """
    _side_pane_navigator = None

    def __init__(self):
        self._side_pane_navigator = PageObjectFactory.create_side_pane_navigator(TEMPLATE)

    def click_folder_link_in_side_pane(self, folder_name):
        """
        Clicks the folder name given in ``folder_name`` argument.
        """
        self._side_pane_navigator.click_folder_link(folder_name)
        return self

    def click_folder_link_by_path_in_side_pane(self, folder_path):
        """
        Clicks the folder path given in ``folder_path`` argument.
        """
        self._side_pane_navigator.click_folder_link_by_path(folder_path)
        return self

    def expand_folder_in_side_pane(self, folder_name):
        """
        Expands the folder given in ``folder_name`` argument.
        """
        self._side_pane_navigator.expand_folder(folder_name)
        return self

    def expand_folder_by_path_in_side_pane(self, folder_path):
        """
        Expands the folder path given in ``folder_path`` argument.
        """
        self._side_pane_navigator.expand_folder_by_path(folder_path)
        return self

    def scroll_and_expand_folder_by_path(self, folder_path):
        """
        Scrolls and expands the folder path given in ``folder_path`` argument.
        :param folder_path: A list of folders path. e.g. karina_wnv  2015 Bare Bones Test Files  Images
        """
        self._side_pane_navigator.scroll_and_expand_folder_by_path(folder_path)

    def collapse_folder_in_side_pane(self, folder_name):
        """
        Collapses the folder given in ``folder_name`` argument.
        """
        self._side_pane_navigator.collapse_folder(folder_name)
        return self

    def is_folder_revealed_under_parent_folder_in_side_pane(self, folder_name):
        """
        Returns True if the folder given in ``folder_name`` argument is revealed below the parent folder
        in the side pane, otherwise False.
        """
        return self._side_pane_navigator.is_folder_revealed_under_parent_folder(folder_name)

    def is_folder_content_revealed_under_parent_folder_in_side_pane(self, folder_path, folder_name):
        """
        Returns True if all the folders and files that belongs to a folder are revealed
        below the parent folder in the side pane, otherwise False.
        The folder is identified by the given ``folder_path`` and ``folder_name`` arguments.
        """
        return self._side_pane_navigator.is_folder_content_revealed_under_parent_folder(folder_path, folder_name)

    def verify_if_folder_content_is_revealed_under_parent_folder_in_side_pane(self, folder_path, folder_name):
        """
        Verifies if all the folders and files that belongs to a folder are revealed
        below the parent folder in the side pane.
        The folder is identified by the given ``folder_path`` and ``folder_name`` arguments.
        """
        return self._side_pane_navigator.verify_if_folder_content_is_revealed_under_parent_folder(folder_path, folder_name)

    def verify_if_folder_content_is_revealed_under_parent_folder_in_side_pane_only_folders(self, folder_path, folder_name):
        """
        Verifies if all the folders that belongs to a folder are revealed below the parent folder 
        in the side pane.
        The folder is identified by the given ``folder_path`` and ``folder_name`` arguments.
        """
        return self._side_pane_navigator.verify_if_folder_content_is_revealed_under_parent_folder_only_folders(folder_path, folder_name)
    
    def verify_if_folder_content_is_not_revealed_under_parent_folder_in_side_pane(self, folder_path, folder_name):
        """
        Verifies if the folders and files that belongs to a folder are not revealed
        below the parent folder in the side pane.
        The folder is identified by the given ``folder_path`` and ``folder_name`` arguments.
        """
        return self._side_pane_navigator.verify_if_folder_content_is_not_revealed_under_parent_folder(folder_path, folder_name)

    def is_folder_link_selected_in_side_pane(self, folder_name):
        """
        Returns True if the folder name given in ``folder_name`` argument is selected in the side pane,
        otherwise False.
        """
        return self._side_pane_navigator.is_folder_link_selected(folder_name)

    def verify_if_folder_link_is_selected_in_side_pane(self, folder_name):
        """
        Verifies if the folder name given in ``folder_name`` argument is selected in the side pane.
        """
        return self._side_pane_navigator.verify_if_folder_link_is_selected(folder_name)
    
    def click_navigator_link(self):
        """
        Clicks the navigator link.
        """
        self._side_pane_navigator.click_navigator_link()
