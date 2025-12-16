import requests


def search(query):
    url = f"https://techcrunch.com/?s={query.replace(' ', '+')}"
    try:
        response = requests.get(url)
        return response.text
    except:
        return None
