import os

from GoogleNews import GoogleNews


#http_proxy = os.environ.get("HTTP_PROXY", None)
#https_proxy = os.environ.get("HTTPS_PROXY", None)
#
#proxies = {
#    "http": http_proxy,
#    "https": https_proxy
#}

#config = Configuration()
#config.proxies = proxies

def search(keyword):
    googlenews = GoogleNews(lang="en", region="US")
    googlenews.get_news(keyword)

    print("Search keyword %s..." % keyword)
    for idx, g in enumerate(googlenews.results(sort=True)):
        print(g["title"])

        if idx > 3:
            break

search("apple")
search("google")
