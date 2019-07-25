import requests
import certifi
import json
from bs4 import BeautifulSoup
from urllib import parse
from find_in_html import *

class Order():

    def __init__(self):
        self.url = self.__create_url()

    @staticmethod
    def __create_url():
        items = {}
        breadcrumbs = {}
        item_id = 0
        url = "https://e-dostavka.by/catalog/item_{0}.html".format(item_id)        
        result = requests.get(url).text
        #print(result)
        for i in range(1000):
            if "К сожалению, по данному запросу товар не найден" not in str(result):
                product = find_in_string(str(result), '<title>', '- Каталог товаров</title>')
                brd_crumbs = find_in_string(str(result), '<div class="breadcrumbs">', '</div>')
                crumbs = find_in_string_as_string(brd_crumbs[0], '>', '<')
                items[item_id] = product
                breadcrumbs[item_id] = crumbs
            item_id+=1
            url = "https://e-dostavka.by/catalog/item_{0}.html".format(item_id)
            result = requests.get(url).text
        print(items)
        print(breadcrumbs)
        with open("C:\Python34\_items.txt", "w", encoding="utf-8") as file:
            json.dump(items, file)
        return url

    def get_html(self):
        self.product = input("What are we looking for? ")
        ua = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'
        }
        self.result = requests.get('https://e-dostavka.by/search/?searchtext='+self.product, headers=ua)
        self.html = BeautifulSoup(self.result.text, features="html.parser") #, 'lxml')

    def find_result(self):
        #self.result_vac=self.html.find_all('div', {'data-qa':'vacancy-serp__vacancy'})
        self.result_prod = self.html.find_all('input', {'name':'product_id'})        
      
    def get_vac(self):
        vac_list = []
        for v, c, s, l in zip(self.result_prod, self.result_comp[1:], self.result_sal, self.result_link):
            #vac_list.append("position: {}, company: {}, salary: {}".format(v.text.ljust(50," "), c.text.ljust(50," "), s.text.ljust(50," ")))
            if len(v.text.strip())>30 and " " in v.text.strip()[30:]:
                print("Position:\t"+v.text.strip()[0:(30+v.text.strip()[30:].find(" "))])
                print("\t\t"+(v.text.strip()[(30+v.text.strip()[30:].find(" ")):]).strip())
            else:
                print("Position:\t"+v.text.strip())
            print("Company:\t"+c.text.strip())
            print("Salary:\t\t"+s.text.strip())
            print("\t\t"+l.get('href')+"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")


if __name__ == '__main__':
    a=Order()
    #a.get_html()
    #a.find_result()
    print(a.url)
    #print(a.html)
    #print(a.result_prod)    


    #products = find_in_string(str(a.html), '<input type="hidden" name="product_id" value="', '" />')
    #print(products)
