from telebot import types
import telebot

bot = telebot.TeleBot('5668693444:AAHYdEwXG3rb9cD5QEyH5Fmh0S8EaudTGAQ')

@bot.message_handler(commands=['start'])
def start(message):
    mass = f'Привет!  <b>{message.from_user.first_name}</b> давай скачаем с Youtube видосик '
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Посетить сайт YouTube', url='https://www.youtube.com/'))
    markup.add(types.InlineKeyboardButton('Скачать с сайта YouTube', url='https://y2mate.mx/ru45'))
    bot.send_message(message.chat.id, mass, parse_mode='html', reply_markup=markup)
    # bot.send_message('U+1F600')

# @bot.message_handler()
# def user_text(message):
#     if message.text == 'Привет':
#         bot.send_message(message.chat.id, 'И тебе приветик', parse_mode='html')
#     else:
#         bot.send_message(message.chat.id, 'Я тебя непонимать', parse_mode='html')

# @bot.message_handler(commands=['website'])
# def website(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('Посетить сайт', url='https://www.youtube.com/'))
#     bot.send_message(message.chat.id,'Перейти на сайт', reply_markup=markup)
    

bot.polling(non_stop=True)