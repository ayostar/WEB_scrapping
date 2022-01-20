import requests
import bs4


class WEBScrapper:
    def __init__(self):
        self.scrap_url = 'https://habr.com/ru/all/'
        self.headers = {
            'Cookie': '_ym_uid=1639148487334283574; _ym_d=1639149414; _ga=GA1.2.528119004.1639149415;'
                      '_gid=GA1.2.512914915.1639149415; habr_web_home=ARTICLES_LIST_ALL; hl=ru; fl=ru;'
                      '_ym_isad=2;'
                      ' __gads=ID=87f529752d2e0de1-221b467103cd00b7:T=1639149409:S=ALNI_MYKvHcaV4SWfZmCb3_wXDx2olu6kw',
            'Accept-Language': 'ru-RU,ru;q=0.9',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0',
            'If-None-Match': 'W/"37433-+qZyNZhUgblOQJvD5vdmtE4BN6w"',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
            'sec-ch-ua-mobile': '?0'
        }

    def web_scraping_keywords(self, KEYWORDS):
        response = requests.get(self.scrap_url, headers = self.headers)
        response.raise_for_status()
        text = response.text

        soup = bs4.BeautifulSoup(text, features = 'html.parser')
        articles = soup.find_all('article')
        for article in articles:
            article_title = article.find('h2')
            p_article = article.find_all('div', class_ = "article-formatted-body article-formatted-body_version-2")
            for p in p_article:
                p_string = p.text.lower()
                for word in KEYWORDS:
                    if word in p_string:
                        time_tag = article.find('time')
                        article_date = time_tag.attrs['title']
                        a_tag = article_title.find('a')
                        href = a_tag.attrs['href']
                        article_url = 'https://habr.com' + href
                        print(article_date, article_title.text, article_url)
                        print('----')


if __name__ == '__main__':

    def keywords_request():
        # KEYWORDS = []
        # for word in input('Введите через запятую слова для web scrapping: ').split(', '):
        #     KEYWORDS.append(word)
        KEYWORDS = ['дизайн', 'фото', 'web', 'python']
        return KEYWORDS

    KEYWORDS = keywords_request()
    HABR_WEBScrapper = WEBScrapper()
    HABR_WEBScrapper.web_scraping_keywords(KEYWORDS)


# url = 'https://habr.com/ru/all/'
# HABR_HEADERS = {
#     'Cookie': '_ym_uid=1639148487334283574; _ym_d=1639149414; _ga=GA1.2.528119004.1639149415;'
#               '_gid=GA1.2.512914915.1639149415; habr_web_home=ARTICLES_LIST_ALL; hl=ru; fl=ru;'
#               '_ym_isad=2;'
#               ' __gads=ID=87f529752d2e0de1-221b467103cd00b7:T=1639149409:S=ALNI_MYKvHcaV4SWfZmCb3_wXDx2olu6kw',
#     'Accept-Language': 'ru-RU,ru;q=0.9',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'same-origin',
#     'Sec-Fetch-User': '?1',
#     'Cache-Control': 'max-age=0',
#     'If-None-Match': 'W/"37433-+qZyNZhUgblOQJvD5vdmtE4BN6w"',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
#     'sec-ch-ua-mobile': '?0'
# }
#
# response = requests.get(url, headers = HABR_HEADERS)
# response.raise_for_status()
# text = response.text
# KEYWORDS = ['дизайн', 'фото', 'web', 'python']
# MY_HUBS = {'Смартфоны', 'Удалённая работа', 'IT-компании'}
#
# soup = bs4.BeautifulSoup(text, features = 'html.parser')
# articles = soup.find_all('article')
# for article in articles:
#     article_title = article.find('h2')
#     p_article = article.find_all('div', class_ = "article-formatted-body article-formatted-body_version-2")
#     hubs = article.find_all('a', class_ = "tm-article-snippet__hubs-item-link")
#     hubs_list = [hub.find('span').text for hub in hubs]
#     article_hubs_set = set(hubs_list)
#     for p in p_article:
#         p_string = p.text.lower()
#         for word in KEYWORDS:
#             if word in p_string:
#                 time_tag = article.find('time')
#                 article_date = time_tag.attrs['title']
#                 a_tag = article_title.find('a')
#                 href = a_tag.attrs['href']
#                 article_url = 'https://habr.com' + href
#                 print(article_date, article_title.text, article_url)
#                 print('----')