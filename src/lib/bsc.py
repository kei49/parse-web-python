import requests
import numpy as np
from bs4 import BeautifulSoup


class BeautifulSoupClient:
    def __init__(self, url) -> None:
        self.url = url
        self.__get_soup()
        self.__get_base_el()

    def parse(self) -> None:
        self.__parse_all_texts()

    def check(self, is_test=False) -> None:
        self.__parsed_result_check(is_test)

    def __get_soup(self):
        ua = self.ua_list[np.random.randint(0, len(self.ua_list))]
        response = requests.get(self.url, headers={"User-Agent": ua})
        self.soup = BeautifulSoup(response.content, "html.parser")

    def __get_base_el(self, use_body=True):
        if use_body:
            body = self.soup.find("body")
            if body is not None:
                self.base = body

        target_base_elements = [
            self.soup.find("main"),
            self.soup.find(id="article-body"),
            self.soup.find(id="cmsBody"),
            self.soup.find("div", class_="mg-main"),
            self.soup.find(id="content")
        ]

        for target in target_base_elements:
            if target is not None:
                self.base = target

    def __parse_all_texts(self):
        if self.base is not None:
            texts_list = []
            for target in self.target_text_element_list:
                li = self.base.find_all(target)
                if (li is not None) and (len(li) > 0):
                    texts = [el.text for el in li]
                    texts_list = texts_list + texts

            self.texts_list = texts_list

    def __parsed_result_check(self, is_test=False):
        if len(self.texts_list) < 5:
            print("ALERT: This url may not be parsed successfully: ", self.url)
        else:
            if not is_test:
                print(self.texts_list)
            print("INFO: This url seemed to be parsed successfully: ", self.url)

    ua_list = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    ]

    target_text_element_list = ["title", "h1", "h2", "h3", "h4", "p", "span"]
