from datetime import datetime


def save_articles_to_file(search_term, articles):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"search_results_{search_term.replace(' ', '_')}_{timestamp}.txt"
    
    with open(filename, 'w', encoding='utf-8') as f:
        write_header(f, search_term, len(articles))
        write_articles(f, articles)
    
    return filename


def write_header(file, search_term, article_count):
    file.write("=" * 80 + "\n")
    file.write(f"SEARCH RESULTS FOR: {search_term.upper()}\n")
    file.write(f"Date: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}\n")
    file.write(f"Total Articles: {article_count}\n")
    file.write("=" * 80 + "\n\n")


def write_articles(file, articles):
    for article in articles:
        file.write(f"ARTICLE {article['number']}\n")
        file.write("-" * 80 + "\n")
        file.write(f"URL: {article['url']}\n")
        file.write("-" * 80 + "\n")
        file.write(f"{article['body']}\n")
        file.write("\n" + "=" * 80 + "\n\n")
