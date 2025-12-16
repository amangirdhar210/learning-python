from scraper import search
from parser.page_parser import get_article_links


search_term = input("Enter search term: ")
html = search(search_term)

if html:
    links = get_article_links(html)
    
    print(f"\nFound {len(links)} articles:\n")
    for  index, link in enumerate(links):
        print(index,":", link,"\n")
else:
    print("Failed to fetch data")
