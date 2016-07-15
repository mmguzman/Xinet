__author__ = 'Edmundo Cossio'

from resources.uiabstraction.PageObjectFactory import PageObjectFactory


class PortalAdminAuthenticationSteps:
    """
    Steps definition for Login page object.
    """
    _portal_admin_authentication = None

    def __init__(self):
        self._portal_admin_authentication = PageObjectFactory.create_portal_admin_authentication()

    def add_new_site(self, portal_ip, portal_admin_password, server_ip, template):
        """
        Adds a new site.
        """
        self._portal_admin_authentication.add_new_site(portal_ip, portal_admin_password, server_ip, template)
