from article_fetcher import fetch_articles
from file_writer import save_articles_to_file


def main():
    search_term = input("Enter search term: ")
    
    articles = fetch_articles(search_term)
    
    if not articles:
        print("Failed to fetch search results")
        return
    
    filename = save_articles_to_file(search_term, articles)
    print(f"\n✓ Successfully saved {len(articles)} articles to: {filename}")


if __name__ == "__main__":
    main()
