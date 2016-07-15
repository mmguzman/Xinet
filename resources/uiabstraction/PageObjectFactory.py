__author__ = 'MarceloM Guzman'

from resources.uiabstraction.components.widgets.basictoolsbar.BasicToolsToolbarExhibit import BasicToolsToolbarExhibit
from resources.uiabstraction.components.widgets.basictoolsbar.BasicToolsToolbarMarquee import BasicToolsToolbarMarquee
from resources.uiabstraction.components.widgets.basket.BasketExhibit import BasketExhibit
from resources.uiabstraction.components.widgets.basket.BasketMarquee import BasketMarquee
from resources.uiabstraction.components.widgets.breadcrumbs.BreadcrumbsNavigatorExhibit import BreadcrumbsNavigatorExhibit
from resources.uiabstraction.components.widgets.breadcrumbs.BreadcrumbsNavigatorMarquee import BreadcrumbsNavigatorMarquee
from resources.uiabstraction.components.widgets.fileactionstoolbar.FileActionsToolbarExhibit import FileActionsToolbarExhibit
from resources.uiabstraction.components.widgets.fileactionstoolbar.FileActionsToolbarMarquee import FileActionsToolbarMarquee
from resources.uiabstraction.components.widgets.filecontentmodal.FileContentModalExhibit import FileContentModalExhibit
from resources.uiabstraction.components.widgets.filecontentmodal.FileContentModalMarquee import FileContentModalMarquee
from resources.uiabstraction.components.widgets.foldercontent.FolderContentExhibit import FolderContentExhibit
from resources.uiabstraction.components.widgets.foldercontent.FolderContentMarquee import FolderContentMarquee
from resources.uiabstraction.components.widgets.sidepane.SidePaneFiltersExhibit import SidePaneFiltersExhibit
from resources.uiabstraction.components.widgets.sidepane.SidePaneFiltersMarquee import SidePaneFiltersMarquee
from resources.uiabstraction.components.widgets.sidepane.SidePaneNavigatorExhibit import SidePaneNavigatorExhibit
from resources.uiabstraction.components.widgets.sidepane.SidePaneNavigatorMarquee import SidePaneNavigatorMarquee
from resources.uiabstraction.pages.home.HomeExhibit import HomeExhibit
from resources.uiabstraction.pages.home.HomeMarquee import HomeMarquee
from resources.uiabstraction.pages.login.LoginPageExhibit import LoginPageExhibit
from resources.uiabstraction.pages.login.LoginPageMarquee import LoginPageMarquee
from resources.uiabstraction.pages.portaladmin.PortalAdminAuthentication import PortalAdminAuthentication
from resources.uiabstraction.pages.portaladmin.PortalAdminHome import PortalAdminHome
from resources.uiabstraction.pages.portaladmin.sitemanager.AddSite import AddSite
from resources.uiabstraction.pages.portaladmin.sitemanager.EditSiteConfiguration import EditSiteConfiguration
from resources.uiabstraction.pages.portaladmin.sitemanager.SiteManager import SiteManager
from resources.uiabstraction.pages.webnative.WebNativeDatabase import WebNativeDatabase
from resources.uiabstraction.pages.webnative.WebNativeHome import WebNativeHome
from resources.uiabstraction.pages.webnative.WebNativeLogging import WebNativeLogging
from resources.uiabstraction.pages.webnative.WebNativePrintHotFolder import WebNativePrintHotFolder
from resources.uiabstraction.pages.webnative.WebNativeVolumesUsers import WebNativeVolumesUsers


class PageObjectFactory(object):
    """
    Class responsible to design a page implementation according template.
    """

    @classmethod
    def create_side_pane_navigator(cls, look_and_feel):
        if look_and_feel.lower() == "marquee":
            return SidePaneNavigatorMarquee()
        else:
            return SidePaneNavigatorExhibit()
    
    @classmethod
    def create_side_pane_filters(cls, look_and_feel):
        if look_and_feel.lower() == "marquee":
            return SidePaneFiltersMarquee()
        else:
            return SidePaneFiltersExhibit()
        
    @classmethod
    def create_basic_tools_toolbar(cls, look_and_feel):
        if look_and_feel.lower() == "marquee":
            return BasicToolsToolbarMarquee()
        else:
            return BasicToolsToolbarExhibit()
    
    @classmethod
    def create_breadcrumbs_navigator(cls, look_and_feel):
        if look_and_feel.lower() == "marquee":
            return BreadcrumbsNavigatorMarquee()
        else:
            return BreadcrumbsNavigatorExhibit()
        
    @classmethod
    def create_file_actions_toolbar(cls, look_and_feel):
        if look_and_feel.lower() == "marquee":
            return FileActionsToolbarMarquee()
        else:
            return FileActionsToolbarExhibit()
        
    @classmethod
    def create_folder_content(cls, look_and_feel):
        if look_and_feel.lower() == "marquee":
            return FolderContentMarquee()
        else:
            return FolderContentExhibit()
    
    @classmethod
    def create_login(cls, look_and_feel):
        if look_and_feel.lower() == "marquee":
            return LoginPageMarquee()
        else:
            return LoginPageExhibit()
        
    @classmethod
    def create_home(cls, look_and_feel):
        if look_and_feel.lower() == "marquee":
            return HomeMarquee()
        else:
            return HomeExhibit()

    @classmethod
    def create_basket(cls, look_and_feel):
        if look_and_feel.lower() == "marquee":
            return BasketMarquee()
        else:
            return BasketExhibit()

    @classmethod
    def create_webnative_home(cls):
        return WebNativeHome()

    @classmethod
    def create_webnative_volumes_users(cls):
        return WebNativeVolumesUsers()
    
    @classmethod
    def create_webnative_database(cls):
        return WebNativeDatabase()
    
    @classmethod
    def create_webnative_print_hot_folder(cls):
        return WebNativePrintHotFolder()
    
    @classmethod
    def create_portal_admin_authentication(cls):
        return PortalAdminAuthentication()
    
    @classmethod
    def create_portal_admin_home(cls):
        return PortalAdminHome()
    
    @classmethod
    def create_site_manager(cls):
        return SiteManager()
    
    @classmethod
    def create_add_site(cls):
        return AddSite()
    
    @classmethod
    def create_edit_site_configuration(cls):
        return EditSiteConfiguration()

    @classmethod
    def create_webnative_logging(cls):
        return WebNativeLogging()
    
    @classmethod
    def create_dialog_content(cls, look_and_feel):
        if look_and_feel.lower() == "marquee":
            return FileContentModalMarquee()
        else:
            return FileContentModalExhibit()
