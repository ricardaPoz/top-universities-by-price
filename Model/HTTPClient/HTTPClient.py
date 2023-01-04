import urllib.request as r
from urllib.error import HTTPError, URLError


class HTTPClient:
    def __init__(self, url, encoding="utf-8", timeouth=10) -> "HTTPClient":
        self.__url = url
        self.__encoding = encoding
        self.__timeouth = timeouth

    def html(self) -> str | None:
        try:
            response = r.urlopen(self.__url, timeout=self.__timeouth).read()
            html = response.decode(self.__encoding)
            return html
        except URLError as error:
            print(error)
        except HTTPError as error:
            print(error)
