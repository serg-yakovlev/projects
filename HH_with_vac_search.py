import requests
from bs4 import BeautifulSoup
from urllib import parse
from iterate_items_bs import *

class HH():

    def __init__(self):
        self.url=self.__create_url()

    @staticmethod
    def __create_url():
        url="https://hh.ru/"
        return url

    def get_html(self):
        vac=input("Vacancy you're searching: ")
        ua={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'
        }
        result=requests.get('https://hh.ru/search/vacancy?text='+vac+'&area=1002', headers=ua)
        #VOZMOZHNA OSHIBKA
        self.html=BeautifulSoup(result.text, features="html.parser") #, 'lxml')

    def find_result(self):

        #self.result_vac=self.html.find_all('div', {'data-qa':'vacancy-serp__vacancy'})
        self.result_vac=self.html.find_all('div', {'class':'vacancy-serp-item'})        
        

        
    def get_vac(self):
        vac_list = []
        for v, c, s, l in zip(self.result_vac, self.result_comp[1:], self.result_sal, self.result_link):
            #vac_list.append("position: {}, company: {}, salary: {}".format(v.text.ljust(50," "), c.text.ljust(50," "), s.text.ljust(50," ")))
            if len(v.text.strip())>30 and " " in v.text.strip()[30:]:
                print("Position:\t"+v.text.strip()[0:(30+v.text.strip()[30:].find(" "))])
                print("\t\t"+(v.text.strip()[(30+v.text.strip()[30:].find(" ")):]).strip())
            else:
                print("Position:\t"+v.text.strip())
            print("Company:\t"+c.text.strip())
            print("Salary:\t\t"+s.text.strip())
            print("\t\t"+l.get('href')+"\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")


if __name__=='__main__':
    a=HH()
    a.get_html()
    a.find_result()
    #print(iterate_items(a.result_vac)[1])
    #print(a.result_vac[1],'\n\n\n\n')
    #print(find_in_string(a.result_vac[1], 'target="_blank">', '</a></div>'))
    pos = find_in_bs_object(a.result_vac, 'target="_blank">', '</a></div>',0,1)
    salary = find_in_bs_object(a.result_vac, 'data-qa="vacancy-serp__vacancy-compensation">', '</div>',0,1)
    schedule = find_in_bs_object(a.result_vac, 'data-qa="vacancy-serp__vacancy-work-schedule">', '</div>',0,1)
    employer = find_in_bs_object(a.result_vac, 'data-qa="vacancy-serp__vacancy-employer" href=', '</a>',0,1)
    link = find_in_bs_object(a.result_vac, '<a class="bloko-link" href=', 'target="_blank">',0,1)
    address = find_in_bs_object(a.result_vac, 'data-qa="vacancy-serp__vacancy-address">', '</span>',0,1)
    metro = find_in_bs_object(a.result_vac, '<span class="metro-station"><span class="metro-point" style="color:', '<div',0,1)
    requir = find_in_bs_object(a.result_vac, '<div data-qa="vacancy-serp__vacancy_snippet_responsibility">', '</div>',0,1)    
    requir_1 = find_in_bs_object(a.result_vac, 'data-qa="vacancy-serp__vacancy_snippet_requirement">', '</div></div><div',0,1)

    #print(pos)
    for p,s,sc,e,l,a,m,r, r_1 in zip(pos, salary, schedule, employer, link, address, metro, requir, requir_1):
        if len(s[0])>50:
            s[0]='не указана'
        if len(sc[0])>50:
            sc[0]='не указано'
        #try:
          #  if len(m[0])>50:
           #     m[0]=''
       # except:
          #  m.append("")
        print(' position:\t',p[0],'\n','salary:\t',s[0],'\n','schedule:\t',sc[0],'\n','employer:\t',e[0],'\n','link:\t',l[0],'\n','address:\t',a[0],'МЕТРО',m[0],'\n','requirements:\t',r[0], r_1[0], '\n\n\n')
