from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, ProgressBarPage, SliderPage


class TestWidgets:
    class TestAccordianPage:
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            third_title, third_content = accordian_page.check_accordian('third')
            assert first_title == "What is Lorem Ipsum?" and first_content > 0, "Incorrect title or missing text"
            assert second_title == "Where does it come from?" and second_content > 0, "Incorrect title or missing text"
            assert third_title == "Why do we use it?" and third_content > 0, "Incorrect title or missing text"

    class TestAutoCompletePage:
        def test_fill_multi_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            colors = autocomplete_page.fill_input_multi()
            colors_result = autocomplete_page.check_color_in_multi()
            assert colors == colors_result, "The added colors are missing in the input"

        def test_remove_value_from_multi(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.fill_input_multi()
            autocomplete_page.remove_value_from_multi_result()
            count_value_before, count_value_after = autocomplete_page.remove_value_from_multi_result()
            assert count_value_before != count_value_after, "The added colors are missing in the input"

        def test_remove_all_value_from_multi(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            colors = autocomplete_page.fill_input_multi_and_clear()
            assert type(colors) is type(None), "Multiple color names form is not empty"

        def test_fill_single_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            color = autocomplete_page.fill_input_single()
            color_result = autocomplete_page.check_color_in_single()
            assert color == color_result, "The added color is missing in the input"

    class TestDatePickerPage:

        def test_change_date(self, driver):
            date_piker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_piker_page.open()
            value_date_before, value_date_after = date_piker_page.select_date()
            assert value_date_before != value_date_after, "The date has not been changed"

        def test_change_date_and_time(self, driver):
            date_piker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_piker_page.open()
            value_date_before, value_date_after = date_piker_page.select_date()
            assert value_date_before != value_date_after, "The date and time has not been changed"

    class TestSliderPage:

        def test_slider(self, driver):
            slider = SliderPage(driver, 'https://demoqa.com/slider')
            slider.open()
            before, after = slider.change_slider_value()
            assert before != after, "The slider value has not been changed"

    class TestProgressBarPage:

        def test_progress_bar(self, driver):
            progress_bar = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar.open()
            before, after = progress_bar.change_progress_bar_value()
            assert before != after, "Progress bar has not changed"

