__author__ = 'MarceloM Guzman'

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

from resources.methods.UIMethods import accept_alert_before_displayed, is_element_present, \
    click_element, wait_for_load_page, select_checkbox
from resources.uiabstraction.components.widgets.basket.BasketBase import BasketBase


class BasketMarquee(BasketBase):
    """
    Page object modeling the structure and operations of the Basket page for Marquee template.
    """

    # Selectors
    _clear_basket_link = (By.XPATH, "//a[contains(text(),'Clear Collection')]")
    _batch_keyword_apply_link = (By.XPATH, "//a[contains(text(),'Batch Keyword Apply')]")
    _batch_report_link = (By.XPATH, "//a[contains(text(),'Batch Report')]")
    _download_archive_of_fpos_link = (By.XPATH, "//a[contains(text(),'Download Archive of FPOs')]")
    _batch_image_order_link = (By.XPATH, "//a[contains(text(),'Batch Image Order')]")

    _collection_modal = (By.ID, "myModalLabel")
    _close_apply_keywords_button = (By.CSS_SELECTOR, "button.close")
    _close_batch_report_button = (By.ID, "close")
    _generate_batch_report_button = (By.XPATH,"//input[@value='Generate Batch Report']")
    _close_batch_report_dialog_button = (By.XPATH, "//input[@value='Close']")
    _keywords_updated_text = (By.XPATH, "//div[text()='All keywords were successfully updated.']")
    _file_modal = (By.ID, "myModalLabel")
    
    _show_keyword_checked = (By.XPATH, "//input[@id='keywords_checkbox_hidden' and @value='on']")
    _show_keyword_not_checked = (By.XPATH, "//input[@id='keywords_checkbox_hidden' and @value='off']")
    _show_keyword_checkbox = (By.ID, "keywords_checkbox")
    _show_annotations_checked = (By.XPATH, "//input[@id='annotations_checkbox_hidden' and @value='on']")
    _show_annotations_not_checked = (By.XPATH, "//input[@id='annotations_checkbox_hidden' and @value='off']")
    _show_annotations_checkbox = (By.ID, "annotations_checkbox")
    _report_preview_combobox = (By.ID, "preview_menu")

    def __init__(self):
        BasketBase.__init__(self, "Marquee")
        self.basket_elements_template = "//div[@class='thumbnail filebox pull-left']"

    def click_clear_basket_link(self):
        """
        Clicks Clear Basket link.
        """
        accept_alert_before_displayed(self._driver)
        self._wait.until(ec.visibility_of_element_located(self._clear_basket_link))
        click_element(self._driver, self._driver.find_element(*self._clear_basket_link))
        self._wait.until(ec.invisibility_of_element_located((By.XPATH, self.basket_elements_template)))

    def click_batch_keyword_apply_link(self):
        """
        Clicks Batch Keyword Apply link.
        """
        self._wait.until(ec.visibility_of_element_located(self._batch_keyword_apply_link))
        click_element(self._driver, self._driver.find_element(*self._batch_keyword_apply_link))
        self._wait.until(ec.visibility_of_element_located(self._collection_modal))
    
    def click_batch_report_link(self):
        """
        Clicks Batch report link.
        """
        self._wait.until(ec.visibility_of_element_located(self._batch_report_link))
        click_element(self._driver, self._driver.find_element(*self._batch_report_link))
        self._wait.until(ec.visibility_of_element_located(self._collection_modal))
        
    def click_download_archive_of_fpos_link(self):
        """
        Clicks Download Archive of FPOs link.
        """
        self._wait.until(ec.visibility_of_element_located(self._download_archive_of_fpos_link))
        click_element(self._driver, self._driver.find_element(*self._download_archive_of_fpos_link))
        self._wait.until(ec.visibility_of_element_located(self._collection_modal))

    def click_batch_image_order_link(self):
        """
        Clicks Batch Image Order link.
        """
        self._wait.until(ec.visibility_of_element_located(self._batch_image_order_link))
        click_element(self._driver, self._driver.find_element(*self._batch_image_order_link))
        self._wait.until(ec.visibility_of_element_located(self._collection_modal))

    def close_apply_keyword_modal(self):
        """
        Clicks the 'x' button to  close the keyword modal.
        """
        if is_element_present(self._driver, *self._close_apply_keywords_button):
            click_element(self._driver, self._driver.find_element(*self._close_apply_keywords_button))
            self._wait.until(ec.invisibility_of_element_located(self._collection_modal))
    
    def click_generate_batch_report_button(self):
        """
        Clicks Generate Batch Report button.
        """
        self._driver.find_element(*self._generate_batch_report_button).click()
    
    def click_close_batch_report_dialog_button(self):
        """
        Clicks Close button on Batch Report dialog.
        """
        self._wait.until(ec.visibility_of_element_located(self._close_batch_report_dialog_button)).click()
        self._wait.until(ec.invisibility_of_element_located(self._file_modal))
        wait_for_load_page()

    def click_download_button(self):
        """
        Clicks the Download button.
        """
        self._driver.find_element(*self._download_button).click()
        self._wait.until(ec.visibility_of_element_located(self._close_batch_report_button))

    def is_keyword_value_displayed(self, keyword_value):
        """
        Verifies if the keyword value is displayed.
        :param keyword_value: The keyword value.
        :return: True if displayed, otherwise False.
        """
        keyword_value_text = (By.XPATH, "//dl/dd[contains(text(),'" + str(keyword_value) + "')]")
        return is_element_present(self._driver, *keyword_value_text)

    def is_keyword_value_displayed_in_collection(self, keyword_list):
        """
        Verifies if the keyword value is displayed in collection page.
        :param keyword_list: A list of keyword values.
        :return: True if displayed, otherwise False.
        """
        is_displayed = None
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
                folder[1] = str(folder[1]).lower()
            is_displayed = self.is_keyword_value_displayed(folder[1])
            if not is_displayed:
                break
        return is_displayed

    def select_show_annotations_checkbox(self, show_type):
        """
        Checks the show keywords or annotations according to type of show.
        :param show_type: The type of show to check (keywords or annotations) 
        """
        show_type_not_checked = (By.XPATH, "//input[@id='" + show_type + "_checkbox_hidden' and @value='off']/following-sibling::input")
        show_type_checked = (By.XPATH, "//input[@id='" + show_type +"_checkbox_hidden' and @value='on']/following-sibling::input")
        try:
            self._wait.until(ec.visibility_of_element_located(show_type_not_checked))
            select_checkbox(self._driver, *show_type_not_checked)
            self._wait.until(ec.visibility_of_element_located(show_type_checked))
        except TimeoutException:
            print "The " + show_type + " element is already checked."

    def select_report_preview_option(self, report_name):
        """
        Selects the report preview option.
        :param report_name: Type of report to select.
        """
        select = Select(self._driver.find_element(*self._report_preview_combobox))
        select.select_by_visible_text(report_name)
