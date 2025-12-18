from bs4 import BeautifulSoup
from locators.article_locator import ArticleLocator


def get_article_body(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    locator = ArticleLocator()
    article_content = soup.select_one(locator.ARTICLE_CONTENT)
    
    if not article_content:
        return ""
    
    paragraphs = article_content.select(locator.ARTICLE_PARAGRAPHS)
    paragraph_texts = [p.get_text(strip=True) for p in paragraphs]
    non_empty_paragraphs = [text for text in paragraph_texts if text]
    return "\n\n".join(non_empty_paragraphs)
