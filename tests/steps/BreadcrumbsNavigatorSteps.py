__author__ = 'MarceloM Guzman'

from resources.commons.GlobalVariables import TEMPLATE
from resources.uiabstraction.PageObjectFactory import PageObjectFactory


class BreadcrumbsNavigatorSteps:
    """
    Steps definition for Breadcrumbs page object.
    """
    _breadcrumbs_navigator = None

    def __init__(self):
        self._breadcrumbs_navigator = PageObjectFactory.create_breadcrumbs_navigator(TEMPLATE)

    def click_folder_link_in_breadcrumbs(self, folder_name):
        """
        Clicks the folder name link given in ``folder_name`` argument.
        """
        self._breadcrumbs_navigator.click_folder_link_in_breadcrumbs(folder_name)
        return self

    def click_folder_link_in_breadcrumbs_and_close_alert(self, folder_name):
        """
        Clicks the folder name link given in folder_name argument and close alert related with "leave this page?"
        """
        self._breadcrumbs_navigator.click_folder_link_in_breadcrumbs_and_close_alert(folder_name)

    def is_folder_link_displayed_in_breadcrumbs(self, folder_name):
        """
        Returns True if the folder name link given in ``folder_name`` is displayed in Breadcrumbs, otherwise False.
        """
        return self._breadcrumbs_navigator.is_folder_link_displayed_in_breadcrumbs(folder_name)

    def verify_if_folder_link_is_displayed_in_breadcrumbs(self, folder_name):
        """
        Verifies if the folder name link given in ``folder_name`` is displayed in Breadcrumbs.
        """
        self._breadcrumbs_navigator.verify_if_folder_link_is_displayed_in_breadcrumbs(folder_name)

    def verify_if_folder_link_is_not_displayed_in_breadcrumbs(self, folder_name):
        """
        Verifies if the folder name link given in ``folder_name`` is displayed in Breadcrumbs.
        """
        self._breadcrumbs_navigator.verify_if_folder_link_is_not_displayed_in_breadcrumbs(folder_name)
