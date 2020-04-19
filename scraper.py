import requests
from bs4 import BeautifulSoup

class GetStockPrice(object):

    def __init__(self, symbol):
        self.url = 'https://finance.yahoo.com/quote/'
        self.symbol = symbol

    def current_price(self):
        r = requests.get(self.url+self.symbol+'.NS?p='+self.symbol+'.NS&.tsrc=fin-srch')
        soup = BeautifulSoup(r.content, 'html.parser')
        cur_price = soup.find(class_= 'Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)')
        return cur_price.text
