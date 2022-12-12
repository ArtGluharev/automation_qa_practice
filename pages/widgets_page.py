from selenium.common import TimeoutException

from locators.widgets_page_locators import AccordianPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {'first': {'title': self.locators.SECTION_ONE,
                               'content': self.locators.SECTION_ONE_CONTENT},
                     'second': {'title': self.locators.SECTION_TWO,
                                'content': self.locators.SECTION_TWO_CONTENT},
                     'third': {'title': self.locators.SECTION_THREE,
                               'content': self.locators.SECTION_THREE_CONTENT},
                     }
        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        try:
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        return [section_title.text, len(section_content)]
