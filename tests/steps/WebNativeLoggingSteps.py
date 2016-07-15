__author__ = 'Edmundo Cossio'

from resources.uiabstraction.PageObjectFactory import PageObjectFactory


class WebNativeLoggingSteps:
    """
    Steps definition for WebNative Logging page object.
    """
    _webnative_logging = None
    
    def __init__(self):
        self._webnative_logging = PageObjectFactory.create_webnative_logging()
    
    def click_preview_generation_link(self):
        """
        Clicks the 'Preview Generation' link.
        """
        self._webnative_logging.click_preview_generation_link()
    
    def verify_if_the_request_queue_name_is_displayed_in_the_request_queue_list(self, item, processing, waiting, holding):
        """
        Verify in the request queue list if the selected item displays corrected values for processing, waiting, holding.
        :param item: It is the request to verify in the 'Request Queue' list in Preview Generation.
        :param processing: Item value to compare with the actual process.
        :param waiting: Item value to compare with the actual wait.
        :param holding: Item value to compare with the actual hold.
        """
        self._webnative_logging.verify_if_the_request_queue_name_is_displayed_in_the_request_queue_list(item, processing, waiting, holding)
