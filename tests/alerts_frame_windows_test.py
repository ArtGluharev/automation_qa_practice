import allure

from pages.allerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, \
    ModalDialogPage


@allure.suite("Alerts,Frame,Window")
class TestAlertsFrameWindow:
    @allure.feature("Тестирование окон Windows")
    class TestBrowserWindows:
        @allure.title("Тестирование новой вкладки")
        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_tab_page.open()
            text_result = new_tab_page.check_opened_new_tab()
            assert text_result == "This is a sample page", "The new tab has not opened or an incorrect tab has opened"

        @allure.title("Тестирование нового окна")
        def test_new_window(self, driver):
            new_window_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_window_page.open()
            text_result = new_window_page.check_opened_new_window()
            assert text_result == "This is a sample page", "The new window has not opened or an incorrect window has opened"

    @allure.feature("Тестирование страницы Alerts")
    class TestAlertsPage:
        @allure.title("Тестирование прямого Alert")
        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == "You clicked a button", "Alert did not show up"

        @allure.title("Тестирование Alerta через 5 секунд")
        def test_alert_appear_5_sec(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_alert_appear_5_sec()
            assert alert_text == "This alert appeared after 5 seconds", "Alert did not show up"

        @allure.title("Тестирование Alerta с подтверждением ")
        def test_alert_confirm(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_confirm_alert()
            assert alert_text == "You selected Ok", "Alert did not show up"

        @allure.title("Тестирование Alerta с полем для ввода текста")
        def test_prompt_result(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text, alert_text = alert_page.check_prompt_alert()
            assert text in alert_text, "Alert did not show up"

    @allure.feature("Тестирование страницы Frames")
    class TestFramesPage:
        @allure.title("Тестирование двух iFrame'ов")
        def test_frames(self, driver):
            frame_page = FramesPage(driver, 'https://demoqa.com/frames')
            frame_page.open()
            result_frame1 = frame_page.check_frame('frame1')
            result_frame2 = frame_page.check_frame('frame2')
            assert result_frame1 == ['This is a sample page', '500px', '350px'], "The frame does not exist"
            assert result_frame2 == ['This is a sample page', '100px', '100px'], "The frame does not exist"

    @allure.feature("Тестирование Nested фрэймов")
    class TestNestedFramesPage:
        @allure.title("Тестирование Nested")
        def test_nested_frames(self, driver):
            nested_frame_page = NestedFramesPage(driver, 'https://demoqa.com/nestedframes')
            nested_frame_page.open()
            parent_text, child_text = nested_frame_page.check_nested_frame()
            assert parent_text == "Parent frame", 'Nested frame does not exist'
            assert child_text == "Child Iframe", 'Nested frame does not exist'

    @allure.feature("Тестирование Modal Dialog")
    class TestModalDialogPage:
        @allure.title("Тестирование малого модального окна")
        def test_small_modal_dialog(self, driver):
            modal_dialogs_page = ModalDialogPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialogs_page.open()
            title_small, title_text = modal_dialogs_page.check_small_modal_dialog()
            assert title_small == "Small Modal", "Modal dialog has not been opened"
            assert title_text == "This is a small modal. It has very less content", "Modal dialog text does not exist"

        @allure.title("Тестирование большого модального окна")
        def test_large_modal_dialog(self, driver):
            modal_dialogs_page = ModalDialogPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialogs_page.open()
            title_large, body_large_text = modal_dialogs_page.check_large_modal_dialog()
            assert title_large == "Large Modal"
