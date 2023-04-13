from locators.quote_locators import QuotesLocators
from selenium.webdriver.common.by import By


class QuoteParser:
    """
    Given one of the specific quote divs,find out the data about
    the quote( quote content, author, tags)
    """

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f' {self.content}'

    @property
    def content(self):
        locator = QuotesLocators.CONTENT_LOCATOR
        return self.parent.find_element(By.CSS_SELECTOR, locator).text

    @property
    def author(self):
        locator = QuotesLocators.AUTHOR_LOCATOR
        return self.parent.find_element(By.CSS_SELECTOR, locator).text

    @property
    def tags(self):
        locator = QuotesLocators.TAGS_LOCATOR
        return [e.string for e in self.parent.find_elements(By.CSS_SELECTOR, locator)]
