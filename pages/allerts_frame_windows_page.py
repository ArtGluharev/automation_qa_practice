import random
import time

import allure
from selenium.common.exceptions import UnexpectedAlertPresentException

from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators, \
    NestedFramesPageLocators, FramesPageLocators, TestModalDialogPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    @allure.step("Открытие новой вкладки")
    def check_opened_new_tab(self):
        self.go_to_new_tab(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.NEW_TITLE_TEXT).text
        return text_title

    @allure.step("Открытие нового окна")
    def check_opened_new_window(self):
        self.go_to_new_tab(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.NEW_TITLE_TEXT).text
        return text_title


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    @allure.step("Нажатие кнопки и открытие первого Alerta")
    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        try:
            alert_window = self.driver.switch_to.alert
            return alert_window.text
        except UnexpectedAlertPresentException:
            alert_window = self.driver.switch_to.alert
            return alert_window

    @allure.step("Нажатие кнопки и открытие Alerta с задержкой 5 секунд")
    def check_alert_appear_5_sec(self):
        self.element_is_visible(self.locators.APPEAR_ALERT_AFTER_5_SEC_BUTTON).click()
        time.sleep(6)
        try:
            alert_window = self.driver.switch_to.alert
            return alert_window.text
        except UnexpectedAlertPresentException:
            alert_window = self.driver.switch_to.alert
            return alert_window

    @allure.step("Нажатие кнопки и открытие Alerta с выбором кнопок")
    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        text_result = self.element_is_present(self.locators.CONFIRM_RESULT).text
        return text_result

    @allure.step("Нажатие кнопки и открытие Alerta с полем для ввода данных")
    def check_prompt_alert(self):
        with allure.step("Выбор случайного числа от 0 до 999"):
            text = f"autotest{random.randint(0, 999)}"
        self.element_is_visible(self.locators.PROMPT_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_present(self.locators.PROMPT_RESULT).text
        return text, text_result


class FramesPage(BasePage):
    locators = FramesPageLocators()

    @allure.step("Два метода для проверки окон")
    def check_frame(self, frame_num):
        with allure.step("Метод для первого окна"):
            if frame_num == 'frame1':
                frame = self.element_is_present(self.locators.FIRST_FRAME)
                width = frame.get_attribute('width')
                height = frame.get_attribute('height')
                self.driver.switch_to.frame(frame)
                text = self.element_is_present(self.locators.TITLE_FRAME).text
                self.driver.switch_to.default_content()
                return [text, width, height]
        with allure.step("Метод для второго окна"):
            if frame_num == 'frame2':
                frame = self.element_is_present(self.locators.SECOND_FRAME)
                width = frame.get_attribute('width')
                height = frame.get_attribute('height')
                self.driver.switch_to.frame(frame)
                text = self.element_is_present(self.locators.TITLE_FRAME).text
                self.driver.switch_to.default_content()
                return [text, width, height]


class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    @allure.step("Проверка предка и дочернего окна")
    def check_nested_frame(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_TEXT).text
        return parent_text, child_text


class ModalDialogPage(BasePage):
    locators = TestModalDialogPageLocators()

    @allure.step("Метод для маленького модального окна")
    def check_small_modal_dialog(self):
        self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
        title_small = self.element_is_visible(self.locators.TITLE_SMALl_MODAL).text
        body_small_text = self.element_is_visible(self.locators.BODY_SMALl_MODAL).text
        self.element_is_visible(self.locators.SMALL_MODAL_CLOSE_BUTTON).click()
        return title_small, body_small_text

    @allure.step("Метод для большого модального окна")
    def check_large_modal_dialog(self):
        self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
        title_large = self.element_is_visible(self.locators.TITLE_LARGE_MODAL_MODAL).text
        body_large_text = self.element_is_visible(self.locators.BODY_LARGE_MODAL_MODAL).text
        self.element_is_visible(self.locators.LARGE_MODAL_CLOSE_BUTTON).click()
        return title_large, body_large_text
