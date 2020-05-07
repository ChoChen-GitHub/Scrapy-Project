import scrapy
from bs4 import BeautifulSoup as soup
import re

class MyProject2Crawler(scrapy.Spider): #注意: spider要大寫
    name = 'MyCrawler'
    start_urls = ['https://tw.carousell.com/categories/sports-10/mens-athletics-and-sports-clothing-1084?search=球衣']
    
    #把抓取到的回應丟到parse函數之中
    def parse(self,response):
        res = soup(response.body)#原始碼放在body中
        #for item in res.select('.rtddt'): #新聞分頁都在class rtddt底下
         #   print(item.select('h1')[0].text)
        
        for index,item in enumerate(res.find_all('div',{'class':'An6bc8d5sQ _9IlksbU0Mo _2t71A7rHgH'})):
            print('------------------------------------------------------------')
            print('item'+str(index))
            print('title: '+str(item.find('p',{'class':'_1gJzwc_bJS _2rwkILN6KA mT74Grr7MA nCFolhPlNA lqg5eVwdBz uxIDPd3H13 _30RANjWDIv'}).get_text()))
            print('price: '+str(item.find('p',{'class':'_1gJzwc_bJS _2rwkILN6KA mT74Grr7MA nCFolhPlNA lqg5eVwdBz _19l6iUes6V _3k5LISAlf6'}).get_text()))
            
        
        