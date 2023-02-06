from telebot import types
import requests
from settings import CURRENCY_API_KEY
import json
from misc import symbols


class Converter:
    def __init__(self):
        self.user_data = {}

    def add_value(self, key, value):
        self.user_data[key] = value

    def values(self):
        return self.user_data

    def reset(self):
        self.user_data = {}

    @staticmethod
    def get_price(user_input):
        api_key = {"apikey": CURRENCY_API_KEY}
        try:
            url = f"https://api.apilayer.com/exchangerates_data/convert?to={user_input['quote']}&from=" \
                  f"{user_input['base']}&amount={user_input['amount']}"
            response = requests.request("GET", url, headers=api_key)
            data = json.loads(response.text)
            if response.status_code != 200:
                raise APIException(f'Ошибка {response.status_code}: {data}\nПопробуйте еще раз')
        except Exception as e:  # inherited from the Exception specifically so that the server does not crash
            return e
        else:
            return f'По текущему курсу {data["query"]["amount"]} {data["query"]["from"]} = ' \
                   f'{data["result"]} {data["query"]["to"]}'


class APIException(Exception):
    pass


def keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=10)
    row = [types.KeyboardButton(symbol) for symbol in symbols.keys()]
    markup.add(*row)
    return markup


converter = Converter()


if __name__ == '__main__':
    print(converter.get_price({'quote': 'RUB', 'base': 'USD', 'amount': '1'}))
