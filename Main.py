from Model.HTTPClient.HTTPClient import HTTPClient
from Model.Parsing.ParseSpecialitet import ParseSpecialitet

# html = HTTPClient("https://tabiturient.ru/vuzcost/").html()

# regex = r"(?ms)<a href=\"https://tabiturient\.ru/vuzu/(.*?)\".*?src=\"(.*?)\".*?<b>(.*?)<.*?<br>[^\t](.*?)<.*?<b>(.*?)<"

# education = ParserHigherEducation(regex, html).parse()

# education_dict = education[0]


html = HTTPClient("https://tabiturient.ru/vuzu/mgimo/proxodnoi/").html()

specialitets = ParseSpecialitet(html).parse()

x = 1
