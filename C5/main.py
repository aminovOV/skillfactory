import telebot
from telebot import types
from weather import Weather, WeatherByGeolocation
from settings import BOT_API_KEY
from converter import converter, keyboard
from misc import joke


bot = telebot.TeleBot(BOT_API_KEY)


@bot.message_handler(commands=['start', 'help'])
def start(message):
    main_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Курсы валют')
    btn2 = types.KeyboardButton('Погода')
    main_keyboard.add(btn1, btn2)
    bot.send_message(message.from_user.id, f"👋 Привет! Я Марвин, робот - помощник.\n\nЧтобы узнать курсы валют, "
                                           f"нажмите /converter\n\nЧтобы узнать погоду, нажмите /weather\n\n"
                                           f"Или выберите из вариантов внизу ⬇️", reply_markup=main_keyboard)


@bot.message_handler(commands=['converter'])
def convert(message):
    bot.send_message(message.from_user.id, "В какую валюту переводим?\nВыберите из вариантов ⬇️\n "
                                           "или напишите обозначение валюты\nПример: RUB", reply_markup=keyboard())
    bot.register_next_step_handler(message, convert_step_1)
    print(message.text)


def convert_step_1(message):
    bot.send_message(message.from_user.id, "Из какой валюты переводим?\nВыберите из вариантов ⬇️\n "
                                           "или напишите обозначение валюты\nПример: USD")
    converter.reset()
    converter.add_value('quote', message.text)
    print(converter.values())
    bot.register_next_step_handler(message, convert_step_2)


def convert_step_2(message):
    bot.send_message(message.from_user.id, "Сколько переводим?")
    converter.add_value('base', message.text)
    print(converter.values())
    bot.register_next_step_handler(message, convert_step_3)


def convert_step_3(message):
    converter.add_value('amount', message.text)
    if message.text == '/start' or message.text == '/help':
        start(message)
    elif message.text == '/weather' or message.text == 'Погода':
        get_location(message)
    elif message.text == '/converter' or message.text == 'Курсы валют':
        convert(message)
    elif message.content_type == 'location':
        geo(message)
    elif message.content_type != 'text':
        get_location(message)
    else:
        bot.send_message(message.from_user.id, converter.get_price(converter.values()))


@bot.message_handler(commands=['weather'])
def get_location(message):
    bot.send_message(message.from_user.id, '❓Для какого города смотрим погоду❓\n\nНажмите значок 📎 и выберите '
                                           '"Геопозиция"\n\nЛибо напиши название города (например: Москва)')
    bot.register_next_step_handler(message, weather)


def weather(message):
    if message.text == '/start' or message.text == '/help':
        start(message)
    elif message.text == '/weather' or message.text == 'Погода':
        get_location(message)
    elif message.text == '/converter' or message.text == 'Курсы валют':
        convert(message)
    elif message.content_type == 'location':
        geo(message)
    elif message.content_type != 'text':
        get_location(message)
    else:
        city = Weather(message.text)
        try:
            bot.send_message(message.from_user.id, joke(), parse_mode='Markdown')
            bot.send_message(message.from_user.id, city.get_weather(), parse_mode='Markdown')
        except Exception:
            bot.send_message(message.from_user.id, 'Что-то пошло не так. Попробуйте еще раз')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Погода':
        bot.send_message(message.from_user.id, '❓Для какого города смотрим погоду❓\n\nНажмите значок 📎 и выберите '
                                               '"Геопозиция"\n\nЛибо напишите название города (например: Москва)')
        bot.register_next_step_handler(message, weather)

    elif message.text == 'Курсы валют':
        bot.send_message(message.from_user.id, joke(), parse_mode='Markdown')
        convert(message)


@bot.message_handler(content_types=['location'])
def geo(message: telebot.types.Message):
    city = WeatherByGeolocation(message.location.latitude, message.location.longitude)
    try:
        bot.send_message(message.from_user.id, f'{city.get_weather()}', parse_mode='Markdown')
    except Exception:
        bot.send_message(message.from_user.id, 'Что-то пошло не так. Попробуйте еще раз')


@bot.message_handler(content_types=['voice'])
def voice(message: telebot.types.Message):
    bot.send_message(message.from_user.id,
                     'Пока я не умею работать с голосом.\nНапишите мне, что полезного я могу делать с голосовыми '
                     'сообщениями.\nМожет быть, превращать голос в текст.\nЯ обязательно передам разработчику.')


@bot.message_handler(content_types=['video'])
def video(message: telebot.types.Message):
    bot.send_message(message.from_user.id,
                     'Пока я не умею работать с видео.\nНапишите мне, что полезного я могу делать с видео.\n '
                     'Например, стримить на ютуб канал или сохранять в облако.\nЯ обязательно передам разработчику.')


@bot.message_handler(content_types=['audio'])
def audio(message: telebot.types.Message):
    bot.send_message(message.from_user.id,
                     'Пока я не умею работать с музыкой.\nНапишите мне, что полезного я могу делать с музыкой.\n'
                     'Может быть, искать название трека или группы, если файл не имеет названия, или искать в сети '
                     'текст песни.\nЯ обязательно передам разработчику.')


@bot.message_handler(content_types=['document'])
def document(message: telebot.types.Message):
    bot.send_message(message.from_user.id,
                     'Пока я не умею работать с документами.\nНапишите мне, что полезного я могу делать с документами.'
                     '\nМожет быть, преобразовывать файлы форматов doc и xlsx в pdf, распознавать сканы документов.\n'
                     'Я обязательно передам разработчику.')


@bot.message_handler(content_types=['sticker'])
def send_sticker(message: telebot.types.Message):
    bot.send_message(message.from_user.id, 'У меня кончились стикеры. Ловите смайлик )')


@bot.message_handler(content_types=['photo'])
def photo(message: telebot.types.Message):
    bot.send_message(message.from_user.id,
                     'Пока я не умею работать с фото.\nНапишите мне, что полезного я могу делать с фото.\n'
                     'Может быть, предлагать список лучших бесплатных приложений для обработки фото прямо '
                     'с телефона или искать по фото в сети.\nЯ обязательно передам разработчику.')


@bot.message_handler(content_types=['video_note'])
def video_note(message: telebot.types.Message):
    bot.send_message(message.from_user.id,
                     'Пока я не умею работать с документами.\nНапишите мне, что полезного я могу делать с этим.\n'
                     'Я обязательно передам разработчику.')


bot.polling(none_stop=True, interval=0)
