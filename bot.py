# -*- coding: utf-8 -*-
import config
import telebot
import requests
from bs4 import BeautifulSoup as BS
from DateTime import DateTime


dt = DateTime('EEST')

bot = telebot.TeleBot(config.token)
r = requests.get('https://sinoptik.ua//погода-чернигов/')
html = BS(r.content, 'html.parser')


for el in html.select('#content'):
	t_min = el.select('.temperature .min')[0].text
	t_max = el.select('.temperature .max')[0].text
	text = el.select('.wDescription .description')[0].text
	forecast = t_min + ", " + t_max + '\n' + text








# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
#     bot.send_message(message.chat.id, message.text)


@bot.message_handler(commands=["start", "help"])
def main(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, 'Погода на сегодня: ' + '\n' + forecast)
    if dt.h_24() == 1:
    	bot.send_message(message.chat.id, 'Поздно уже')


print(dt.h_24())

if __name__ == '__main__':
    bot.polling(none_stop=True)