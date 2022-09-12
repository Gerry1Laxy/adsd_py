import re

import requests
from bs4 import BeautifulSoup


KEYWORDS = ['api', 'мозг']
HEADERS = {
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  'Chrome/67.0.3396.62 Safari/537.36 OPR/54.0.2952.64'
}


def is_keywords(keywords, text):
    pattern = '|'.join(keywords)
    return True if re.search(pattern, text, re.IGNORECASE) else False


def main():
    base = 'https://habr.com'
    url = base + '/ru/all'
    response = requests.get(url, headers=HEADERS)

    soup = BeautifulSoup(response.text, features='html.parser')

    for article in soup.find_all('article'):
        if is_keywords(KEYWORDS, article.text):
            data = article.find('time')['title']
            title = article.find('h2').text
            ref = base + article.find('h2').a['href']
            print(f'{data} - {title} - {ref}')


if __name__ == '__main__':
    main()
