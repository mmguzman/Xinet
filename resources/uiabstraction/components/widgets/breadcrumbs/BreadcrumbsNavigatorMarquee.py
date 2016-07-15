__author__ = 'MarceloM Guzman'

from resources.uiabstraction.components.widgets.breadcrumbs.BreadcrumbsNavigatorBase import BreadcrumbsNavigatorBase
from resources.uiabstraction.components.widgets.foldercontent.FolderContentMarquee import FolderContentMarquee


class BreadcrumbsNavigatorMarquee(BreadcrumbsNavigatorBase):
    """
    Page object modeling the structure and operations of the Breadcrumbs navigator for Marquee template.
    """

    def __init__(self):
        BreadcrumbsNavigatorBase.__init__(self, "Marquee")
        self.folder_locator_template = "//ol[@class='breadcrumb']/li/a[contains(text(),'%s')]"
        
    def _create_folder_content(self):
        return FolderContentMarquee()
