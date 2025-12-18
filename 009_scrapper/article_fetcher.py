from scraper import search, fetch_article
from parser.page_parser import get_article_links
from parser.article_parser import get_article_body


def fetch_articles(search_term, max_articles=7):
    html = search(search_term)
    
    if not html:
        return None
    
    links = get_article_links(html)
    print(f"\nFound {len(links)} articles")
    print(f"Fetching the first {max_articles} articles...\n")
    
    articles = []
    
    for index, link in enumerate(links[:max_articles], 1):
        print(f"Fetching article {index}/{max_articles}...")
        articles.append(fetch_single_article(index, link))
    
    return articles


def fetch_single_article(index, url):
    article_html = fetch_article(url)
    
    if article_html:
        body = get_article_body(article_html)
        return {
            'number': index,
            'url': url,
            'body': body if body else "No content available"
        }
    else:
        return {
            'number': index,
            'url': url,
            'body': "Failed to fetch article"
        }
