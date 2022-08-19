import requests
from config import config

class CurrencyAPI:
    headers = {
        "apikey": config.API_KEY
    }
    def __init__(self) -> None:
        self.baseUrl = 'https://api.apilayer.com/exchangerates_data'
        
    def getCurrencySymbols(self):
        url = f'{self.baseUrl}/symbols'
        response = requests.get(url, headers=self.headers)
        status_code = response.status_code
        if status_code == 200:
            result = response.json()
            symbols = result['symbols']
            return symbols
        
        return f'Something went wrong {status_code} {response}'
    
    def conversion(self, amount, frm, to):
        url = f'{self.baseUrl}/convert'
        params = {
            'amount': amount,
            'from': frm,
            'to': to
        }
        response = requests.get(url, headers=self.headers, params=params)
        status_code = response.status_code
        if status_code == 200:
            result = response.json()
            print('CONVERTED', result)
            rate = result['info']['rate']
            convVal = result['result']
            return {
                'rate': rate,
                'result': convVal
            }
        return f'Something went wrong {status_code} {response}'
        
c = CurrencyAPI()
c.getCurrencySymbols()
