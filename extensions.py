import requests
import json
from config import keys, API_KEY, API_URL


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

        url = API_URL.format(quote_ticker=quote_ticker, base_ticker=base_ticker, amount=amount)
        payload = {}
        headers = {
         "apikey": API_KEY
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        returns_data = json.loads(response.content)
        print('возвращаемое значение - ', returns_data)
        return returns_data['result']
