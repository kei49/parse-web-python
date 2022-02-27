import sys
import numpy as np

from lib.bsc import BeautifulSoupClient
from lib.crawler import Crawler


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


def main(search_type, value):
    url = url_list[value] if search_type == "num" else value

    bsc = BeautifulSoupClient(url)
    bsc.parse()
    bsc.check()


def test():
    # sampling some target urls to avoid multiple meaningless web accesses
    for url in np.random.choice(url_list, size=3, replace=False):
        bsc = BeautifulSoupClient(url)
        bsc.parse()
        bsc.check(True)


def start_cralwer():
    crawler = Crawler()
    crawler.start()


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
elif args[2] == "crawl":
    start_cralwer()
else:
    raise Exception("Please use correct args")
