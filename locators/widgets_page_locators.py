from selenium.webdriver.common.by import By


class AccordianPageLocators:
    SECTION_ONE = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    SECTION_ONE_CONTENT = (By.CSS_SELECTOR, 'div[id="section1Content"] p')
    SECTION_TWO = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    SECTION_TWO_CONTENT = (By.CSS_SELECTOR, 'div[id="section2Content"] p')
    SECTION_THREE = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    SECTION_THREE_CONTENT = (By.CSS_SELECTOR, 'div[id="section3Content"] p')


class AutoCompletePageLocators:
    MULTI_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    MULTI_VALUE = (By.CSS_SELECTOR, 'div[class="css-12jo7m5 auto-complete__multi-value__label"]')
    MULTI_VALUE_REMOVE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"] svg path')
    MULTI_ALL_REMOVE = (By.CSS_SELECTOR, 'svg[height="20"][width="20"] path')
    SINGLE_CONTAINER = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')
    SINGLE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')
