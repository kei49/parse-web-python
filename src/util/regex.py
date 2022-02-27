import re


def is_valid_domain(domain):
    domain_regex = "^((?!-)[A-Za-z0-9-]" + \
        "{1,63}(?<!-)\\.)" + "+[A-Za-z]{2,6}"
    regex = re.compile(domain_regex)

    if domain is None:
        raise ValueError("ValueError: domain should be not None")

    if not re.search(regex, domain):
        raise ValueError("ValueError: not valid domain")


def is_valid_url(url):
    url_regex = "((http|https)://)(www.)?" + "[a-zA-Z0-9@:%._\\+~#?&//=]" + \
        "{2,256}\\.[a-z]" + "{2,6}\\b([-a-zA-Z0-9@:%" + "._\\+~#?&//=]*)"

    if url is None:
        raise ValueError("ValueError: url should be not None")

    regex = re.compile(url_regex)
    if not re.search(regex, url):
        raise ValueError("ValueError: not valid url")
