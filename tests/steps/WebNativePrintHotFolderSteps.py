__author__ = 'MarceloM Guzman'

from resources.uiabstraction.PageObjectFactory import PageObjectFactory


class WebNativePrintHotFolderSteps:
    """
    Steps definition for WebNative Print/ Hot Folder page object.
    """
    _webnative_print_hot_folder = None

    def __init__(self):
        self._webnative_print_hot_folder = PageObjectFactory.create_webnative_print_hot_folder()
        
    def click_print_queues_link(self):
        """
        Clicks the Print Queues link.
        """
        self._webnative_print_hot_folder.click_print_queues_link()
        
    def click_hot_folders_link(self):
        """
        Clicks the Hot Folders link
        """
        self._webnative_print_hot_folder.click_hot_folders_link()
        
    def add_new_pdf_ir_queue(self, server_name, queue_name, print_queue_type, printer_sub_type):
        """
        Sets all values to create a new PDF IR queue.
        """
        self._webnative_print_hot_folder.add_new_pdf_ir_queue(server_name, queue_name, print_queue_type, printer_sub_type)
        
    def is_pdf_ir_queue_displayed(self, queue_name):
        """
        Returns true if a PDF IR queue is displayed.
        """
        return self._webnative_print_hot_folder.is_pdf_ir_queue_displayed(queue_name)
    
    def create_new_hot_folder(self, server_name, queue_name):
        """
        Sets all values to create a new Hot Folder.
        """
        self._webnative_print_hot_folder.create_new_hot_folder(server_name, queue_name)
        
    def is_hot_folder_displayed(self, hot_folder_path):
        """
        Returns true if a Hot Folder is displayed.
        """
        return self._webnative_print_hot_folder.is_hot_folder_displayed(hot_folder_path)
        
    def verify_if_pdf_ir_queue_displayed(self, queue_name):
        """
        Verifies if a PDF IR queue is displayed.
        """
        self._webnative_print_hot_folder.verify_if_pdf_ir_queue_displayed(queue_name)

    def verify_if_pdf_ir_queue_is_not_displayed(self, queue_name):
        """
        Verifies if a PDF IR queue is not displayed.
        """
        self._webnative_print_hot_folder.verify_if_pdf_ir_queue_is_not_displayed(queue_name)
        
    def verify_if_hot_folder_displayed(self, server_name):
        """
        Verifies if a Hot Folder is displayed.
        """
        self._webnative_print_hot_folder.verify_if_hot_folder_displayed(server_name)

    def delete_print_queue(self, print_queue_name):
        """
        Deletes a print queue.
        """
        self._webnative_print_hot_folder.delete_print_queue(print_queue_name)
