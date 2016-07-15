__author__ = 'MarceloM Guzman'

from resources.commons.GlobalVariables import TEMPLATE
from resources.uiabstraction.PageObjectFactory import PageObjectFactory


class BasketSteps:
    """
    Steps definition for Basket page object.
    """
    _basket = None

    def __init__(self):
        self._basket = PageObjectFactory.create_basket(TEMPLATE)

    def click_clear_basket_link(self):
        """
        Clicks Clear Basket link.
        """
        self._basket.click_clear_basket_link()

    def click_batch_keyword_apply_link(self):
        """
        Clicks Batch Keyword Apply link.
        """
        self._basket.click_batch_keyword_apply_link()

    def click_download_archive_of_fpos_link(self):
        """
        Clicks Download Archive of FPOs link.
        """
        self._basket.click_download_archive_of_fpos_link()

    def click_batch_image_order_link(self):
        """
        Clicks Batch Image Order link.
        """
        self._basket.click_batch_image_order_link()

    def click_apply_keywords_button(self):
        """
        Clicks the Apply Keywords button.
        """
        self._basket.click_apply_keywords_button()

    def close_apply_keyword_modal(self):
        """
        Click the 'x' button to  close the keyword modal.
        """
        self._basket.close_apply_keyword_modal()
    
    def click_batch_report_link(self):
        """
        Clicks Batch report link.
        """
        self._basket.click_batch_report_link()

    def click_download_button(self):
        """
        Clicks the Download button.
        """
        self._basket.click_download_button()

    def click_generate_batch_report_button(self):
        """
        Clicks generate batch report button.
        """
        self._basket.click_generate_batch_report_button()
    
    def click_close_modal_content_button(self):
        """
        Clicks close modal content button
        """
        self._basket.click_close_modal_content_button()

    def set_archive_name(self, archive_name):
        """
        Sets the download archive name.
        :param archive_name: The name of the archive.
        """
        self._basket.set_archive_name(archive_name)
    
    def check_show_annotations_keyword(self, show_type):
        """
        Checks the show keywords or annotations according to type of show.
        :param show_type: The type of show to check (keywords or annotations) 
        """
        self._basket.check_show_annotations_keyword(show_type)
    
    def select_report_preview_option(self, report_name):
        """
        Selects the report preview option.
        :param report_name: Type of report to select.
        """
        self._basket.select_report_preview_option(report_name)

    def set_batch_archive_name(self, archive_name):
        """
        Sets the Batch Image Order archive name.
        :param archive_name: The name of the batch archive.
        """
        self._basket.set_batch_archive_name(archive_name)

    def set_metadata_default_values(self, default_data_field_list_values):
        """
        Sets the metadata values by default.
        :param default_data_field_list_values: A list of MD values to set in the batchapply.
        """
        self._basket.set_metadata_default_values(default_data_field_list_values)

    def download_archive_of_fpos(self, archive_name):
        """
        Actions to perform a Download archive of FPOs.
        :param archive_name: The name of the archive to download.
        """
        self._basket.download_archive_of_fpos(archive_name)

    def download_batch_image_order(self, batch_name, format_name):
        """
        Actions to perform a Batch Image Order download.
        :param batch_name: The batch name.
        :param format_name: The format to select.
        """
        self._basket.download_batch_image_order(batch_name, format_name)

    def verify_if_basket_is_empty(self):
        """
        Verifies if the Basket is empty (Elements displayed equals to 0).
        """
        self._basket.verify_if_basket_is_empty()

    def apply_keyword_to_fields_list(self, metadata_list):
        """
        Applies keyword values to a metadata list.
        :param metadata_list: List of metadata list values, e.g.
                            @{wnv_text} =  wnv_text  five_text  Replace
                            @{wnv_text_popup} =  wnv_text_popup  kiwi
                            @{data_field_list} =  ${wnv_text}  ${wnv_text_popup}
        """
        self._basket.apply_keyword_to_fields_list(metadata_list)

    def wait_until_file_is_created(self, file_name):
        """
        Waits until a file is created in a directory.
        :param file_name: The file name to wait.
        """
        self._basket.wait_until_file_is_created(file_name)
    
    def verify_if_annotation_is_displayed_in_batch_report(self, expected_annotation_batch_report):
        """
        Verifies if annotation is displayed in batch report.
        """
        self._basket.verify_if_annotation_is_displayed_in_batch_report(expected_annotation_batch_report)
    
    def verify_if_metadata_values_are_displayed_in_batch_report(self, expected_metadata_list, file_name):
        """
        Verifies if metadata value is displayed in batch report
        """
        self._basket.verify_if_metadata_values_are_displayed_in_batch_report(expected_metadata_list, file_name)

    def verify_if_keywords_updated_message_is_displayed(self):
        """
        Assertion to verify if the keywords message update is displayed.
        :return: True if displayed, otherwise False.
        """
        self._basket.verify_if_keywords_updated_message_is_displayed()

    def verify_if_keyword_value_is_displayed_in_collection(self, keyword_list):
        """
        Assertion to verify if the keyword value is displayed in collection page.
        :param keyword_list: A list of keyword values.
        :return: True if displayed, otherwise False.
        """
        self._basket.verify_if_keyword_value_is_displayed_in_collection(keyword_list)

    def verify_if_keyword_list_value_is_displayed_in_collection(self, keyword_list):
        """
        Assertion to verify if a list of keyword values is displayed in collection page.
        :param keyword_list: A list of keyword values.
        :return: True if displayed, otherwise False.
        """
        self._basket.verify_if_keyword_list_value_is_displayed_in_collection(keyword_list)

    def verify_if_a_file_is_downloaded(self, file_name):
        """
        Assertion to verify if the file is downloaded from Collection.
        :param file_name: The file name to verify.
        """
        self._basket.verify_if_a_file_is_downloaded(file_name)

    def extract_file(self, file_name):
        """
        Extract all the files from a compressed file.
        :param file_name: The file name to extract.
        """
        self._basket.extract_file(file_name)

    def verify_if_file_list_extracted_is_displayed(self, file_list):
        """
        Assertion to verify if the list of extracted files is displayed.
        :param file_list: A list of files to verify its presence.
        """
        self._basket.verify_if_file_list_extracted_is_displayed(file_list)

    def click_close_in_batch_report(self):
        """
        Clicks close in batch report.
        """
        self._basket.click_close_in_batch_report()
