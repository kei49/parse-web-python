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


def get_main_el(soup):
    main = soup.find("main")
    if main is not None:
        # print(main.prettify())
        return main


def parse_all_texts(main_el):
    parse_element_list = ["title", "h1", "h2", "h3", "h4", "p", "span"]

    texts_list = []
    for base_el in parse_element_list:
        li = main_el.find_all(base_el)
        if (li is not None) and (len(li) > 0):
            texts = [el.text for el in li]
            texts_list = texts_list + texts

    print(texts_list)


def main():
    url = "https://coinpost.jp/?p=324207"
    soup = get_soup(url)
    # print(soup.prettify())

    main_el = get_main_el(soup)

    if main_el is not None:
        parse_all_texts(main_el)


if __name__ == "__main__":
    main()
