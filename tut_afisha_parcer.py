import requests
from bs4 import BeautifulSoup
from urllib import parse


class TutBy():

    def __init__(self):
        self.url=self.__create_url()

    @staticmethod
    def __create_url():
        url="https://afisha.tut.by/film/"
        return url

    def get_html(self):
        ua={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'
        }
        result=requests.get(self.url, headers=ua)
        #VOZMOZHNA OSHIBKA
        self.html=BeautifulSoup(result.text, features="html.parser") #, 'lxml')

    def get_items(self):
        self.extract=self.html.find_all('div', {'class':'film-name'})

    def double_iterate_items(self):
        print(type(self.extract))
        i=0
        for item in self.extract:
            while i<10:            
                print('\n###'+str(i), type(item),'###\t')
                i+=1
                j=0
                for tag in item:
                    #if tag!=None:
                    print("\t###"+str(j), type(tag),'###\t', tag, '\n')
                    j+=1

    def iterate_items(self):
        i=0
        for item in self.extract:
            print("\t###"+str(i)+'###\t', tag_1, '\n')
            i+=1
            
    def parce_result(self):
        prev_place="" #предыдущий кинотеатр

        #---------------обработка ввода-----------------
        
        requested_hour = input("Time (from, hh - till, hh) ") #временной интервал (example: "11-14)"
        go_further = False #для обработки ошибок
        meaningful = False #для обработки незначащих интервалов
        while not go_further: #ошибка при обработке временного интервала
            try:
                req_from = int(requested_hour[0:2].replace("-","")) #11
                req_till = int(requested_hour[len(requested_hour)-2:len(requested_hour)].replace("-","")) #14
                while not meaningful: # формально корректный но бессмысленный интервал
                    if req_from not in range(0,25) or req_till not in range(0,25) or req_from==req_till:
                        #нулевой интервал или одно/оба значения - не час суток
                        requested_hour = input("Incorrect interval, let's try again ")
                        req_from = int(requested_hour[0:2]) #11
                        req_till = int(requested_hour[len(requested_hour)-2:len(requested_hour)]) #14
                    else:
                        meaningful = True
                req_hours=set(range(req_from,req_till)) #{11,12,13}
                go_further = True
            except:
                if requested_hour == "":
                    req_hours=set(range(0,25)) #покажем все сеансы
                    go_further = True
                else:
                    requested_hour = input("Incorrect interval, let's try again ")
            
        requested_film = input("Part of film title ")
        requested_place = input("Part of theater title ")
        
        #------------------------парсинг self.extract------------------------
        
        for item in self.extract:
            time=[]
            hours=[]
            minutes=[]
            link=""
            place=""
            film=""            
            for tag in item:
                if tag!=None:
                    if "href=" in str(tag):#вытягиваем ссылку на фильм
                        link = str(tag)[len('<a href="'):str(tag).find('" itemprop="url">')]
                    if "time datetime=" in str(tag):#вытягиваем дату и время
                        t=str(tag)[len('<time datetime="'):str(tag).find('" itemprop="startDate"')]
                        time.append(t[11:16])#время как строка (hh:mm)
                        hours.append(int(t[11:13]))#часы как int
                        minutes.append(int(t[14:16]))#минуты как int
                    if "meta content=" in str(tag):#название кинотеатра
                        place = str(tag)[str(tag).find('<meta content="')+len('<meta content="'):str(tag).find('</span>')]
                        place = place.replace('&lt;br&gt;', " ")#вычищаем разный трэш
                        place = place.replace('" itemprop="name"', "")#
                        place = place.replace('""=""/>', "")#
                        place = place.replace('=""', "")#
                        place = place.replace('/>', "") #
                    if '<span itemprop="summary">' in str(tag): #название фильма
                        film = str(tag)[str(tag).find('<span itemprop="summary">')+len('<span itemprop="summary">'):str(tag).find('</span>')]

        #-----------------------вывод результата----------------------------------------------
                        
            if len(list(req_hours&set(hours)))>=1 and requested_film.lower() in film.lower() and requested_place.lower() in place.lower(): #непустое пересечение
                                                    #запрошенного интервала и имеющихся сеансов, фильм соответствует запросу,
                                                    #кинотеатр соответствует запросу
                if prev_place != place: #следующий кинотеатр
                    print("\n\n\n\t----------------------------")
                    print("\t",place,"\t----------------------------")#place оканчивается на \n(видимо)
                #print(requested_film.lower())
                #print(film.lower())
                if requested_film.lower() in film.lower(): # фильм соответствует запросу
                    print("\n", film, "\t", link, '\n')
                    for h, m, t in zip(hours, minutes, time):
                        if h in req_hours: #время соответствует запрошенному интервалу
                            print(t)
                print("-------------------------------------------------------------------------------")
                prev_place = place #запоминаем название кинотеатра



if __name__=='__main__':
    a=TutBy()
    a.get_html()
    a.get_items()
    #a.parce_result()
    #print(a.items)
    #a.iterate_items()
    a.double_iterate_items()
    #print(a.extract)
