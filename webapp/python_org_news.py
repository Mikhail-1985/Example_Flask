import requests
from bs4 import BeautifulSoup
from datetime import datetime
from webapp.model import db, News

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False

def get_python_news(): # парсим новости
    html = get_html('https://www.python.org/blogs/')
    if html:
        soup = BeautifulSoup(html, 'html.parser') #закидываем в "суп" хтмл страницу
        all_news = soup.find('ul', class_='list-recent-posts').findAll('li') #ищем нужное
        result_news = [] # создаем будущий список словарей с заголовками новостей, юрл, датой
        for news in all_news:
            title = news.find('a').text # заголовки
            url = news.find('a')['href'] # юрл
            published = news.find('time').text # дата
            try:
                published = datetime.strptime(published, '%Y-%m-%d')
            except(ValueError):
                published = datetime.now()
            save_news(title, url, published)

def save_news(title, url, published):
    news_exists = News.query.filter(News.url == url).count()
    if not news_exists:
        new_news = News(title=title, url=url, published=published)
        db.session.add(new_news)
        db.session.commit()