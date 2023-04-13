from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.quotes_page import QuotesPage, InvalidTagForAuthorError
from csv import writer

with open('quote.csv', 'a', newline='') as f:
    Writer = writer(f)
    Writer.writerow(['Author', 'Quote'])

    try:
        author = input('Enter the author:').title()
        tag = input('Enter your desired tag:').lower()
        service = Service("C:/Users/chromedriver.exe")
        chrome = webdriver.Chrome(service=service)
        chrome.get("https://quotes.toscrape.com/search.aspx")
        page = QuotesPage(chrome)
        q = page.search_for_quotes(author, tag)
        lis = [([author], q)]
        Writer.writerows(lis)

    except InvalidTagForAuthorError as e:
        print(e)
    except Exception:
        print('An unknown error occurred. Pleas try again!')



