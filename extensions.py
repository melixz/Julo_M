import requests
import json
from config import keys, url



r = requests.get(url)
payload = {}
headers= {
  "apikey": "IntLEHAdDHFOOABkuaJKaLNbaqu2kWKK"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
total_base = json.loads(r.content)

class ConversionException(Exception):
    pass

class CurrencyExchange:
 @staticmethod
 def convert(quote: str, base: str, amount: str):
   if quote == base:
    raise ConversionException(f'Невозможно перевести одинаковые валюты {base}.')

try:
 quote_ticker = keys[quote]
except KeyError:
 raise ConversionException(f'Не удалось обработать валюту {quote}')

try:
 base_ticker = keys[base]
except KeyError:
 raise ConversionException(f'Не удалось обработать валюту {base}')

try:
 amount = float(amount)
except ValueError:
 raise ConversionException(f'Не удалось обработать количество {amount}')




