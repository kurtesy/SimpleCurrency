from locale import currency
from conversion_api import CurrencyAPI


class CurrencyConverter:
    def __init__(self):
        self.currencyList = {}
        self.value = 0
        self.base = 'INR'
        self.currAPI = CurrencyAPI()
        
    def setBaseCurr(self, base):
        self.base = base
    
    def convert(self, value, to):
        self.value = value
        symbols = self.fetchAllSymbols()
        data = []
        print('TO', to, to in symbols)
        if to and to in symbols:
            return [self.currAPI.conversion(value, self.base, to)]
        for symbol, currency in symbols.items()[:3]:
            result = self.currAPI.conversion(value, self.base, symbol)
            data.append(result)
        return data
            
    def fetchAllSymbols(self):
        if len(self.currencyList) == 0:
            self.currencyList = self.currAPI.getCurrencySymbols()
        return self.currencyList
