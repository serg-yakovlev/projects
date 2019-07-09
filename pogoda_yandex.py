import requests
import certifi
import json
from bs4 import BeautifulSoup
from urllib import parse


class Weather():

    def __init__(self):
        self.url='https://api.weather.yandex.ru/v1/forecast?lat=53.9045&lon=27.5615&extra=true'

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
    w=Weather()
    w.send_request()
    w.get_json()
    w.json_parce_now()
    print('\n')
    w.json_parce_fore()


    
                  
