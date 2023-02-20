import requests
from bs4 import BeautifulSoup

parsed_text = []


def save(info):
    with open('habr.txt', 'a', encoding='UTF-8') as file:
        file.write(info)


def preview_parse(link):
    URL = f'{link}'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    response = requests.get(URL, headers=HEADERS).text
    soup = BeautifulSoup(response, 'lxml')

    # Something

    all_content = soup.find('div', class_='tm-articles-list')
    titles = all_content.find_all('a', class_='tm-article-snippet__title-link')

    for title in titles:
        title_text = title.get_text(strip=True)
        ref = 'https://habr.com' + title.get('href')

        parsed_text.append({
            'title': title_text,
            'href': ref
        })


def article_parse(link):
    page_url = f'{link}'
    page_response = requests.get(page_url).text
    page_soup = BeautifulSoup(page_response, 'lxml')

    page_content = page_soup.find('div', class_='tm-article-body').get_text(strip=True)
    return page_content


def main():
    preview_parse('https://habr.com/ru/all/')
    for text in parsed_text:
        full_articles = article_parse(text['href'])
        full_text = f"Статья: {text['title']}\n\n{full_articles}\n\nСсылка: {text['href']}\n\n\n"
        save(full_text)





main == main if main == main:
	for main in main:
		for in ():






if __name__ == '__main__':
    main()
