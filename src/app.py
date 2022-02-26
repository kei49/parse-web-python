import sys
import requests
import numpy as np
from bs4 import BeautifulSoup


ua_list = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
           'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
           ]


def get_soup(url):
    ua = ua_list[np.random.randint(0, len(ua_list))]
    response = requests.get(url, headers={"User-Agent": ua})
    soup = BeautifulSoup(response.content, "html.parser")
    return soup


def get_base_el(soup, use_body=True):
    if use_body:
        body = soup.find("body")
        if body is not None:
            return body

    target_base_elements = [
        soup.find("main"),
        soup.find(id="article-body"),
        soup.find(id="cmsBody"),
        soup.find("div", class_="mg-main"),
        soup.find(id="content")
    ]

    for target in target_base_elements:
        if target is not None:
            return target


def parse_all_texts(base_el):
    target_element_list = ["title", "h1", "h2", "h3", "h4", "p", "span"]

    texts_list = []
    for target in target_element_list:
        li = base_el.find_all(target)
        if (li is not None) and (len(li) > 0):
            texts = [el.text for el in li]
            texts_list = texts_list + texts

    return texts_list


url_list = [
    "https://voice-ping.com/",  # VoicePing
    "https://news.yahoo.co.jp/articles/e77efd79d476b266f592cc22035950a30143902f",  # ヤフーNews
    "https://coinpost.jp/?p=324207",  # CoinPost
    "https://toyokeizai.net/articles/-/518845",  # 東洋経済
    "https://www.itmedia.co.jp/news/articles/2202/26/news044.html",  # ITmedia
    "https://gendai.ismedia.jp/articles/-/92036",  # マネー現代
    "https://www.moguravr.com/meta-next-generation-vr-ar-headset/",  # Mogra VR
    "https://vrinside.jp/news/post-204731/",  # VRInside
]


def parse_result_check(url, li, is_test=False):
    if len(li) < 5:
        print("ALERT: This url may not be parsed successfully: ", url)
    else:
        if not is_test:
            print(li)
        print("INFO: This url seemed to be parsed successfully: ", url)


def main(search_type, value):
    url = url_list[value] if search_type == "num" else value
    soup = get_soup(url)

    base_el = get_base_el(soup, use_body=True)

    if base_el is not None:
        texts_list = parse_all_texts(base_el)
        parse_result_check(url, texts_list, is_test=False)


def test():
    # sampling some target urls to avoid multiple meaningless web accesses
    for url in np.random.choice(url_list, size=3, replace=False):
        soup = get_soup(url)
        base_el = get_base_el(soup)

        if base_el is not None:
            texts_list = parse_all_texts(base_el)
            parse_result_check(url, texts_list, is_test=True)


args = sys.argv

if args[1] == "main":
    if len(args) <= 2:
        raise Exception("Please enter one value as int or url")

    value = args[2]
    if value is not None:
        if "http" in value:
            main("url", value)
        else:
            try:
                num = int(value)
                if len(url_list) <= num:
                    raise Exception(
                        "Please enater an integer less than {}".format(len(url_list)))
            except ValueError:
                raise Exception("Please enter an int or a url")

            main("num", num)

elif args[1] == "test":
    test()
else:
    raise Exception("Please use correct args")
