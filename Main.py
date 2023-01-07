from Controller.Controller import Controller
from sqlalchemy.engine import URL
from sqlalchemy import create_engine





# from Model.HTTPClient.HTTPClient import HTTPClient
# from Model.Parsing.ParseSpecialitet import ParseSpecialitet
# from Model.Parsing.ParserHigherEducation import ParserHigherEducation
# import threading as th
# from time import perf_counter
# from Model.Entity.HigherEducation import HigherEducation
# from multiprocessing import Pool, cpu_count, Manager, Process
# from multiprocessing.sharedctypes import Array



# html = HTTPClient("https://tabiturient.ru/vuzcost/").html()
# regex = r"(?ms)<a href=\"https://tabiturient\.ru/vuzu/(.*?)\".*?src=\"(.*?)\".*?<b>(.*?)<.*?<br>[^\t](.*?)<.*?<b>(.*?)<"

# educations = ParserHigherEducation(regex, html).parse()

# [print(v.field_values) for v in educations]


# html = HTTPClient("https://tabiturient.ru/vuzu/tubryansk/proxodnoi/").html()
# spec = ParseSpecialitet(html).parse()

# [print(v.field_values) for v in spec]


# def add_speciality(education, i, lock):
#     lock.acquire()
#     s = education.field_values[0]
#     html = HTTPClient(s).html()
#     specialitets = ParseSpecialitet(html).parse()
#     education.specialitets = specialitets
#     print(f'Для {i} - "{education.field_values[3]}" добавлены специальности')
#     lock.release()


# if __name__ == "__main__":
#     start_time = perf_counter()

#     html = HTTPClient("https://tabiturient.ru/vuzcost/").html()
#     regex = r"(?ms)<a href=\"https://tabiturient\.ru/vuzu/(.*?)\".*?src=\"(.*?)\".*?<b>(.*?)<.*?<br>[^\t](.*?)<.*?<b>(.*?)<"

#     educations = ParserHigherEducation(regex, html).parse()

#     threads = []

#     manager = Manager()

#     lock = manager.Lock()

#     for i, education in enumerate(educations):
#         thread = Process(target=add_speciality, args=(education, i, lock))
#         threads.append(thread)
#         thread.start()

#     [thread.join() for thread in threads]

#     f = list(filter(lambda e: len(e.specialitets) > 0, educations))
#     print(f"Длинна сорт {len(f)}")

#     end_time = perf_counter()
#     print(f"Выполнение заняло {start_time - end_time: 0.2f} секунд.")
