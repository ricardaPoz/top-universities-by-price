from .Parsing import Parsing
from ..Entity.HigherEducation import HigherEducation
from .CustomLinkPrinter import CustomLinkPrinter
from icrawler.builtin import GoogleImageCrawler
import re


class ParserHigherEducation(Parsing):
    def __init__(self, regex: str, html: str) -> "ParserHigherEducation":
        self.__regex = regex
        self.__html = html

    def parse(self) -> list[HigherEducation]:
        higher_educations: list[HigherEducation] = []
        elements = re.findall(self.__regex, self.__html)

        for element in elements:
            arr: list[str] = []
            for value in element:
                value = value.strip().replace("&quot;", "")
                arr.append(value)
            education: HigherEducation = HigherEducation()

            google_crawler = GoogleImageCrawler(downloader_cls=CustomLinkPrinter)
            google_crawler.downloader.file_urls = []
            google_crawler.crawl(keyword=arr[3], max_num=3)
            image = google_crawler.downloader.file_urls

            arr.append(image)

            education.field_values = arr
            higher_educations.append(education)

        return higher_educations
