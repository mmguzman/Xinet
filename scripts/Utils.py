__author__ = 'MarceloM Guzman'

import sys
import fileinput
import os

XINET_WEBNATIVE_ADM_INSTALL_DIR = '/var/adm/webnative/'
XINET_APPLETALK_ADM_INSTALL_DIR = '/var/adm/appletalk/'
XINET_WEBNATIVE_ETC_INSTALL_DIR = '/usr/etc/webnative/'
XINET_APPLETALK_ETC_INSTALL_DIR = '/usr/etc/appletalk/'
CUSTOM_INSTALLER_FILE = '/var/buildbot/XinetPath'
PORTAL_INSTALL_DIR = '/usr/etc/portal/'
WN_HOSTNAME = "$WNHOSTNAME  =  '';"


def is_directory_present(directory_path):
    """
    Verifies if a directory is present.
    """
    return os.path.exists(directory_path)


def is_file_present(file_path):
    """
    Verifies if a file is present.
    """
    return os.path.isfile(file_path)


def is_custom_installer_file_present():
    """
    Verifies if the XinetPath custom file is present on buildslave.
    """
    if is_file_present(CUSTOM_INSTALLER_FILE):
        print "yes"
    else:
        print "no"


def is_server_installed():
    """
    Verifies if Xinet server is installed.
    """
    if (is_directory_present(XINET_WEBNATIVE_ADM_INSTALL_DIR) or
            is_directory_present(XINET_APPLETALK_ADM_INSTALL_DIR) or
            is_directory_present(XINET_WEBNATIVE_ETC_INSTALL_DIR) or
            is_directory_present(XINET_APPLETALK_ETC_INSTALL_DIR)):
        print "yes"
    else:
        print "no"


def is_portal_installed():
    """
    Verifies if Portal server is installed.
    """
    if is_directory_present(PORTAL_INSTALL_DIR):
        print "yes"
    else:
        print "no"


def search_string_in_file(string_to_search, file_name, action):
    """
    Search a string in the 'file_name' file.
    """
    search_file = open(file_name, "r")
    for line in search_file:
        if string_to_search in line:
            if action == "print":
                print line
            elif action == "search":
                return True
    search_file.close()


def replace_value_in_file(file_name, search_value, replace_value):
    """
    Replaces the 'search_value' by 'replace_value'.
    """
    for line in fileinput.input(file_name, inplace=1):
        if search_value in line:
            line = line.replace(search_value, replace_value)
        sys.stdout.write(line)


def replace_wnhostname(string_to_search, file_name, site_name):
    """
    Replaces the $WNHOSTNAME adding a new site.
    """
    if search_string_in_file(string_to_search, file_name, "search"):
        replace_value_in_file(file_name, WN_HOSTNAME, "$WNHOSTNAME  =  '" + site_name + "';")
        print "The $WNHOSTNAME was updated to: $WNHOSTNAME  =  '" + site_name + "';"
    else:
        print "The $WNHOSTNAME was not updated."


def replace_wnhostname_row(string_to_search, file_name, site_name):
    """
    Replaces the entire $WNHOSTNAME row (adding an existing site).
    """
    if search_string_in_file(string_to_search, file_name, "search"):
        replace_value_in_file(file_name, WN_HOSTNAME, site_name)
        print "The $WNHOSTNAME was updated to: " + site_name
    else:
        print "The $WNHOSTNAME was not updated."
