from Model.HTTPClient.HTTPClient import HTTPClient
from Model.Parsing.ParserHigherEducation import ParserHigherEducation

html = HTTPClient("https://tabiturient.ru/vuzcost/").html()

regex = r"(?ms)<a href=\"https://tabiturient\.ru/vuzu/(.*?)\".*?src=\"(.*?)\".*?<b>(.*?)<.*?<br>[^\t](.*?)<.*?<b>(.*?)<"

education = ParserHigherEducation(regex, html).parse()


x = 1
