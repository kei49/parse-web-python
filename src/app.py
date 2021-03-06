import sys

from lib import bsc
from lib import crawler
from common.const import url_list
from common.init import init
from common.services import domain as domain_service
from common.services import url as url_service


def dev():
    init()

    domain = "fast.com"
    url = "https://fast.com/"

    domain = domain_service.create_domain(domain)

    domains = domain_service.read_all_domains()
    print(domains)

    url = url_service.create_url(url, domain.id)
    print(url)

    urls = url_service.read_all_domains()
    print(urls)


args = sys.argv

if args[1] == "dev":
    dev()
elif args[1] == "main":
    if len(args) <= 2:
        raise Exception("Please enter one value as int or url")

    value = args[2]
    if value is not None:
        if "http" in value:
            bsc.main("url", value)
        else:
            try:
                num = int(value)
                if len(url_list) <= num:
                    raise Exception(
                        "Please enater an integer less than {}".format(len(url_list)))
            except ValueError:
                raise Exception("Please enter an int or a url")

            bsc.main("num", num)

elif args[1] == "test":
    bsc.test()
elif args[2] == "crawl":
    crawler.init()
else:
    raise Exception("Please use correct args")
