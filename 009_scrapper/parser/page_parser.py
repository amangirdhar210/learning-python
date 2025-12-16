from bs4 import BeautifulSoup
from locators.page_locator import PageLocator


locator = PageLocator()


def get_article_links(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    links = []
    articles = soup.select(locator.ARTICLE_LIST)
    
    for article in articles:
        link_element = article.select_one(locator.TITLE_LINK)
        if link_element and link_element.get('href'):
            links.append(link_element.get('href'))
    
    return links