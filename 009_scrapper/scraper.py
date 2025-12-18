import requests


def search(query):
    url = f"https://techcrunch.com/?s={query.strip().replace(' ', '+')}"
    try:
        response = requests.get(url)
        return response.text
    except:
        return None


def fetch_article(url):
    try:
        response = requests.get(url)
        return response.text if response.status_code == 200 else None
    except:
        return None
