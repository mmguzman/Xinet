import os
from platform import system

from robot.libraries.BuiltIn import BuiltIn


try:
    from robot.libraries.BuiltIn import RobotNotRunningError
except ImportError:
    RobotNotRunningError = AttributeError

# ************************** Browser ******************************
try:
    BROWSER = BuiltIn().get_variable_value("${BROWSER}")
except RobotNotRunningError:
    BROWSER = None

try:
    IMPLICIT_WAIT = BuiltIn().get_variable_value("${IMPLICIT_WAIT}")
except RobotNotRunningError:
    IMPLICIT_WAIT = 20

try:
    EXPLICIT_WAIT = BuiltIn().get_variable_value("${EXPLICIT_WAIT}")
except RobotNotRunningError:
    EXPLICIT_WAIT = 20

# ************************** Servers ******************************
try:
    PORTAL_IP = BuiltIn().get_variable_value("${PORTAL_IP}")
except RobotNotRunningError:
    PORTAL_IP = None

try:
    SERVER_IP = BuiltIn().get_variable_value("${SERVER_IP}")
except RobotNotRunningError:
    SERVER_IP = None

try:
    SERVER_NAME = BuiltIn().get_variable_value("${SERVER_NAME}")
except RobotNotRunningError:
    SERVER_NAME = None

try:
    TEMPLATE = BuiltIn().get_variable_value("${TEMPLATE}")
except RobotNotRunningError:
    TEMPLATE = None
        
# ************************** Data Base ******************************
DB_API_MODULE_NAME = "pymysql"
DB_HOST = SERVER_IP
DB_PORT = "3306"
DB_NAME = "webnative"
DB_USER = "root"
DB_PASS = "xinetrlz"

# ************************** Settings ******************************
if system() == "Windows":
    CHROME_DRIVER_PATH = os.path.join(os.getcwd(), 'drivers', 'chromedriver.exe')
    IE_DRIVER_PATH = os.path.join(os.getcwd(), 'drivers', 'IEDriverServer.exe')
elif system() == "Darwin" or system() == "Linux":
    CHROME_DRIVER_PATH = os.path.join(os.getcwd(), 'drivers', 'chromedriver')

SELENIUM_SERVER_JAR = os.path.join(os.getcwd(), 'drivers', 'selenium-server-standalone.jar')
DOWNLOAD_PATH = os.path.join(os.getcwd(), 'downloads')

# ************************** Volumes ******************************
VOLUME_PATH_KARINA = ['xinetVols']
VOLUME_PATH_RH7WNV = ['home', 'xinetVols']
VOLUME_PATH_BUDDY64 = ['home', 'volumes']
VOLUME_PATH_ZBODIKOVA_MINI = ['xinetVols']
VOLUME_PATH_ALL = ['space', 'xinetVols']

# ************************** Output Folder (Queues) **************************
OUTPUT_FOLDER_PATH_KARINA = ['xinetVols', SERVER_NAME +  '_wnv', 'pdfir_out']
OUTPUT_FOLDER_PATH_RH7WNV = ['home', 'xinetVols', SERVER_NAME + '_wnv', 'pdfir_out']
OUTPUT_FOLDER_PATH_BUDDY64 = ['home', 'volumes', SERVER_NAME + '_wnv', 'pdfir_out']
OUTPUT_FOLDER_PATH_ZBODIKOVA_MINI = ['xinetVols', SERVER_NAME + '_wnv', 'pdfir_out']
OUTPUT_FOLDER_PATH_ALL = ['space', 'xinetVols', SERVER_NAME + '_wnv', 'pdfir_out']

# ************************** Path To Hot Folder ******************************
PATH_TO_HOT_FOLDER_VOLUME_PATH_KARINA = ['xinetVols', SERVER_NAME + '_wnv', 'pdfir_hot_folder']
PATH_TO_HOT_FOLDER_VOLUME_PATH_RH7WNV = ['home', 'xinetVols', SERVER_NAME + '_wnv', 'pdfir_hot_folder']
PATH_TO_HOT_FOLDER_VOLUME_PATH_BUDDY64 = ['home', 'volumes', SERVER_NAME + '_wnv', 'pdfir_hot_folder']
PATH_TO_HOT_FOLDER_ZBODIKOVA_MINI = ['xinetVols', SERVER_NAME + '_wnv', 'pdfir_hot_folder']
PATH_TO_HOT_FOLDER_VOLUME_PATH_ALL = ['space', 'xinetVols', SERVER_NAME + '_wnv', 'pdfir_hot_folder']

# ************************** Backup Directory *******************************
BACKUP_DIRECTORY_PATH_KARINA = ['xinetVols', 'venture_backups']
BACKUP_DIRECTORY_PATH_RH7WNV = ['home', 'xinetVols', 'venture_backups']
BACKUP_DIRECTORY_PATH_BUDDY64 = ['home', 'volumes', 'venture_backups']
BACKUP_DIRECTORY_PATH_ZBODIKOVA_MINI = ['xinetVols', 'venture_backups']
BACKUP_DIRECTORY_PATH_ALL = ['space', 'xinetVols', 'venture_backups']

# ************************** Exception type *********************************
STALE_ELEMENT_REFERENCE_EXCEPTION = 'StaleElementReferenceException'
NO_SUCH_ELEMENT_EXCEPTION = 'NoSuchElementException'
TIMEOUT_EXCEPTION = 'TimeoutException'
EXCEPTION = 'Exception'

# ************************** Clear browsing data *********************************
CHROME_PATH = '/private/var/root/Library/Application Support/Google/Chrome'

# ************************** Built-in Facets ******************************
DEFAULT_BUILT_IN_FACETS = ['Type', 'Archived', 'Creator']
