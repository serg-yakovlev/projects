import requests
import certifi
import json
import cities_id
from bs4 import BeautifulSoup
from urllib import parse

class City():

    def get_city_url(self):
        url='http://dateandtime.info/ru/city.php?id='
        city=input("Город (часть названия): ")
        cities = cities_id.cities()
        for c in cities:
            if city.lower() in c.lower():
                self.city = c
                city_url = url + cities[c]
                self.city_id=cities[c]
                print(c, city_url)
                return(city_url)
            
    @staticmethod
    def sql_request(city, lat, long):
        sql_r = 'INSERT INTO location ("city", "latitude", "longitude") VALUES ({0}, {1}, {2});'.format('"'+city+'"', lat, long)
        return(sql_r)
            
    def get_wiki_coordinates(self, city):
        ua={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'
        }
        url='https://ru.wikipedia.org/wiki/'+city+'#/maplink/0'
        print(url)
        result=requests.get(url, headers=ua)
        self.html=BeautifulSoup(result.text, features="html.parser") #, 'lxml'
        #print(self.html)
        coord_start=str(self.html).find('"wgCoordinates":{')+len('"wgCoordinates":{')
        rest = str(self.html)[coord_start:]
        coord_end=rest.find('}')
        coordinates=rest[:coord_end]
        #print(coordinates)
        lat = coordinates[6:coordinates.find(',')]
        long = (coordinates[coordinates.find(',')+7:coordinates.find(',')+7+15]).replace('},"','')
        #print('!!!!', lat, 'and!!!!!!!!!!', long)
        return(lat, long)

    @staticmethod
    def grades_to_real(g_m_s):
        try:#         если число градусов  - двузначное
                grades = int(g_m_s[0:2])
                minutes = int(g_m_s[3:5])
                seconds = int(g_m_s[6:8])
        except:
                try:#                        трёхзначное
                    grades = int(g_m_s[0:3])
                    minutes = int(g_m_s[4:6])
                    seconds = int(g_m_s[7:9])
                except:#                     однозначное
                    grades = int(g_m_s[0:1])
                    minutes = int(g_m_s[2:4])
                    seconds = int(g_m_s[5:7])
        return((grades*60*60+minutes*60+seconds)/60/60)
        
    def get_coordinates(self):
        
        ua={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'
        }
        try:
            url=self.get_city_url()
            city = self.city
            print(url)
            result=requests.get(url, headers=ua)            
            self.html=BeautifulSoup(result.text, features="html.parser") #, 'lxml')
            coordinates=self.html.find_all('div', {'class':'level1'})
            coordinates = str(coordinates[4]).replace('-','')
            self.coordinates=coordinates[coordinates.find("</a>:")+6:coordinates.find("</a>:")+6+30]# строка с координатами
            #разбиваем на 2 строки (широта и долгота) 
            lat = self.coordinates[:8]
            long = self.coordinates[self.coordinates.find(',')+2:self.coordinates.find(',')+2+15]
            #переводим градусы и минуты в десятичную дробь
            self.long = str(self.grades_to_real(long))
            self.lat = str(self.grades_to_real(lat))
        except: # если города нет в списке - идем за координатами в википедию
            city = input("Ничего не нашлось... Попробуйте указать полное название города: ")
            coord=self.get_wiki_coordinates(city)            
            self.lat, self.long = coord
        print(self.lat, self.long)
        sql_r = self.sql_request(city, self.lat, self.long)
        print(sql_r)

class Weather():

    def __init__(self, lat, long):
        self.url='https://api.weather.yandex.ru/v1/forecast?lat='+lat+'&lon='+long+'&extra=true'

    def send_request(self):
        ua_key={
            'X-Yandex-API-Key': '2414fc48-5065-42db-a861-f8f62c38bb16' #'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36',
            }
        self.result=requests.get(self.url, headers=ua_key).text

    def get_json(self):
        self.json_str=self.result
        
    @staticmethod
    def get_prec(self):
        pass

    @staticmethod
    def get_cloudness(self):
        pass

    @staticmethod
    def get_prec_strength(self):
        pass
    
    @staticmethod
    def get_condition(cond_code):
        conditions = {
        'clear':'Ясно',
        'partly-cloudy':'Малооблачно',
        'cloudy':'Облачно с прояснениями',
        'overcast':'Пасмурно',
        'partly-cloudy-and-light-rain':'Небольшой дождь',
        'partly-cloudy-and-rain':'Дождь',
        'overcast-and-rain':'Сильный дождь',
        'overcast-thunderstorms-with-rain': 'Сильный дождь, гроза',
        'cloudy-and-light-rain': 'Небольшой дождь',
        'overcast-and-light-rain':'Небольшой дождь',
        'cloudy-and-rain':'Дождь',
        'overcast-and-wet-snow':'Дождь со снегом',
        'partly-cloudy-and-light-snow':'Небольшой снег',
        'partly-cloudy-and-snow':'Снег',
        'overcast-and-snow':'Снегопад',
        'cloudy-and-light-snow':'Небольшой снег',
        'overcast-and-light-snow':'Небольшой снег',
        'cloudy-and-snow':'Снег',
        }
        return(conditions[cond_code])

    @staticmethod
    def get_wind_direct(wind_direct_code):
         directions = {
        'nw':'северо-западный',
        'n':'северный',
        'ne':'северо-восточный',
        'e':'восточный',
        'se':'юго-восточный',
        's':'южный',
        'sw':'юго-западный',
        'w': 'западный',
        'с': 'штиль'
        }
         return(directions[wind_direct_code])
                
    def json_parce_now(self):
        self.parsed_string = json.loads(self.json_str)
        print('\t\tСейчас: \n')
        print(self.get_condition(self.parsed_string['fact']['condition']))       
        print('Температура воздуха', self.parsed_string['fact']['temp'], '*C')
        print('Ощущается как', self.parsed_string['fact']['feels_like'], '*C')
        try:
            print('Температура воды',    self.parsed_string['fact']['temp_water'])
        except:
            pass
        print('Ветер', str(self.get_wind_direct(self.parsed_string['fact']['wind_dir']))+', скорость', self.parsed_string['fact']['wind_speed'],'м/с, порывы до', self.parsed_string['fact']['wind_gust'],'м/с')
        print('Атмосферное давление', self.parsed_string['fact']['pressure_mm'], 'мм. рт. ст.')
        print('Относительная влажность', str(self.parsed_string['fact']['humidity'])+'%')


    def json_parce_fore(self):
        self.parsed_string = json.loads(self.json_str)
        part=['morning','day','evening','night']
        head=['утро','день','вечер','ночь']
        print('\t\tПрогноз:')
        for p, h in zip(part, head):
            print('\n\t\t',h)
            print(self.get_condition(self.parsed_string['forecasts'][0]['parts'][p]['condition']))
            #print(self.parsed_string['forecasts'][0]['parts'])
            print('Температура воздуха', self.parsed_string['forecasts'][0]['parts'][p]['temp_avg'], '*C')
            print('Ощущается как', self.parsed_string['forecasts'][0]['parts'][p]['feels_like'], '*C')
            try:
                print('Температура воды',    self.parsed_string['forecasts'][0]['parts'][p]['temp_water'])
            except:
                pass
            print('Ветер', str(self.get_wind_direct(self.parsed_string['forecasts'][0]['parts'][p]['wind_dir']))+', скорость', self.parsed_string['forecasts'][0]['parts'][p]['wind_speed'],'м/с, порывы до', self.parsed_string['forecasts'][0]['parts'][p]['wind_gust'],'м/с')
            print('Атмосферное давление', self.parsed_string['forecasts'][0]['parts'][p]['pressure_mm'], 'мм. рт. ст.')
            print('Относительная влажность', str(self.parsed_string['forecasts'][0]['parts'][p]['humidity'])+'%')
       


if __name__ == '__main__':

    c=City()
    c.get_coordinates()
    long=c.long
    lat=c.lat

    w=Weather(lat,long)
    w.send_request()
    w.get_json()
    w.json_parce_now()
    print('\n\n')
    w.json_parce_fore()
