import telebot
import random
import datetime
import time

bot = telebot.TeleBot('')
hall = 'Sportski Centar Master'
_chat_id = ''


def define_intro():
    text = ['folks', 'guys', 'colleagues']
    return f'Hi {random.choice(text)}!'


def send_text_message():
    text = define_intro() + f'I have just created new poll about new training at {hall}'
    bot.send_message(chat_id=_chat_id, text=text)


def create_new_poll(date):
    send_text_message()
    bot.send_poll(chat_id=_chat_id, question=f'Game in {hall}({date})',
                  options=['I will', 'Without me', 'I want to see results'], is_anonymous=False)


first_time = datetime.datetime.now()
future_day = datetime.datetime.today().date() + datetime.timedelta(days=1)
send_time = first_time

while True:
    future_day = datetime.datetime.today().date() + datetime.timedelta(days=1)
    create_new_poll(future_day)
    time.sleep(604800)
