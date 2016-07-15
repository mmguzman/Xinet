__author__ = 'MarceloM Guzman'

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

from resources.methods.UIMethods import is_element_present, click_element, \
    select_checkbox
from resources.uiabstraction.components.widgets.basket.BasketBase import BasketBase


class BasketExhibit(BasketBase):
    """
    Page object modeling the structure and operations of the Basket page for Exhibit template.
    """

    # Selectors
    _clear_basket_link = (By.ID, "clearbasket")
    _batch_keyword_apply_link = (By.XPATH, "//div[contains( @onclick,'batchapply')]")
    _batch_report_link = (By.XPATH, "//div[contains( @onclick,'batchreport')]")
    _generate_batch_report_button = (By.NAME, "process")
    
    _download_archive_of_fpos_link = (By.ID, "downloadbasketfpoplugin")
    _batch_image_order_link = (By.ID, "batchorderplugin")

    _batch_apply_content = (By.ID, "batchapply")
    _download_archive_of_fpos_content = (By.ID, "downloadbasketfpocntl")
    _batch_image_order_content = (By.ID, "batchordercntl")
    _tech_info = (By.XPATH, "//div[@class='techinfo']")
    _progress_frame = (By.ID, "progress")
    _download_progress_text = (By.XPATH, "//a[contains(text(),'Your download should start in five seconds.')]")
    _report_preview_combobox = (By.ID, "preview_menu")

    def __init__(self):
        BasketBase.__init__(self, "Exhibit")
        self.basket_elements_template = "//div[@class='preview_outerbox']"

    def click_clear_basket_link(self):
        """
        Clicks Clear Basket link.
        """
        self._driver.find_element(*self._clear_basket_link).click()
        self._wait.until(ec.invisibility_of_element_located((By.XPATH, self.basket_elements_template)))

    def click_batch_keyword_apply_link(self):
        """
        Clicks Batch Keyword Apply link.
        """
        self._wait.until(ec.visibility_of_element_located(self._batch_keyword_apply_link)).click()
        self._wait.until(ec.visibility_of_element_located(self._batch_apply_content))

    def click_download_archive_of_fpos_link(self):
        """
        Clicks Download Archive of FPOs link.
        """
        self._wait.until(ec.visibility_of_element_located(self._download_archive_of_fpos_link)).click()
        self._wait.until(ec.visibility_of_element_located(self._download_archive_of_fpos_content))

    def click_batch_image_order_link(self):
        """
        Clicks Batch Image Order link.
        """
        self._wait.until(ec.visibility_of_element_located(self._batch_image_order_link)).click()
        self._wait.until(ec.visibility_of_element_located(self._batch_image_order_content))

    def click_download_button(self):
        """
        Clicks the Download button.
        """
        parent_page = self._driver.current_window_handle
        self._driver.find_element(*self._download_button).click()
        try:
            self._wait.until(ec.frame_to_be_available_and_switch_to_it(self._progress_frame))
            self._wait.until(ec.visibility_of_element_located(self._download_progress_text))
        finally:
            self._driver.switch_to_window(parent_page)

    def set_batch_archive_name(self, archive_name):
        """
        Sets the Batch Image Order archive name.
        :param archive_name: The name of the batch archive.
        """
        self._driver.find_element(*self._batch_archive_name_textbox).clear()
        self._driver.find_element(*self._batch_archive_name_textbox).send_keys(archive_name)

    def is_keyword_value_displayed(self, keyword_value):
        """
        Verifies if the keyword value is displayed.
        :param keyword_value: The keyword value.
        :return: True if displayed, otherwise False.
        """
        keyword_value_text = (By.XPATH, "//tr/td[contains(text(),'" + str(keyword_value) + "')]")
        return is_element_present(self._driver, *keyword_value_text)

    def is_keyword_value_displayed_in_collection(self, keyword_list):
        """
        Verifies if the keyword value is displayed in collection page.
        :param keyword_list: A list of keyword values.
        :return: True if displayed, otherwise False.
        """
        is_displayed = None
        self._wait.until(ec.visibility_of_element_located(self._tech_info))
        for keyword in keyword_list:
            is_displayed = self.is_keyword_value_displayed(keyword)
            if not is_displayed:
                break
        return is_displayed

    def is_keyword_value_list_displayed_in_collection(self, keyword_list):
        """
        Verifies if a list of keyword values is displayed in collection page.
        :param keyword_list: A list of keyword values.
        :return: True if displayed, otherwise False.
        """
        is_displayed = None
        for folder in keyword_list:
            if folder[1] == True:
                folder[1] = folder[0]
            is_displayed = self.is_keyword_value_displayed(folder[1])
            if not is_displayed:
                break
        return is_displayed
    
    def click_batch_report_link(self):
        """
        Clicks Batch report link.
        """
        self._wait.until(ec.visibility_of_element_located(self._batch_report_link))
        click_element(self._driver, self._driver.find_element(*self._batch_report_link))
        self._wait.until(ec.visibility_of_element_located(self._generate_batch_report_button))
    
    def select_show_annotations_checkbox(self, show_type):
        """
        Checks the show keywords or annotations according to type of show.
        :param show_type: The type of show to check (keywords or annotations) 
        """
        show_type_not_checked = (By.XPATH, "//input[@id='"+show_type + "_checkbox_hidden' and @value='off']")
        show_checked = (By.XPATH, "//input[@id='"+show_type + "_checkbox_hidden' and @value='on']")
        show_type_checked = (By.ID, show_type + '_checkbox')
        try:
            self._wait.until(ec.presence_of_element_located(show_type_not_checked))
            select_checkbox(self._driver, *show_type_checked)
            self._wait.until(ec.visibility_of_element_located(show_checked))
        except TimeoutException:
            print "The " + show_type + " element is already checked."
    
    def select_report_preview_option(self, report_name):
        """
        Selects the report preview option.
        :param report_name: Type of report to select.
        """
        select = Select(self._driver.find_element(*self._report_preview_combobox))
        select.select_by_visible_text(report_name)
    
    def click_generate_batch_report_button(self):
        """
        Clicks Generate Batch Report button.
        """
        self._driver.find_element(*self._generate_batch_report_button).click()
