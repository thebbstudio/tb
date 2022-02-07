import telebot
import database as db
import msglist
import mail
import time
import conf
import os

bot = telebot.TeleBot(conf.token)


def select_data_user(msg_chat_id):
    return db.select_user_data(msg_chat_id)





@bot.message_handler(commands=['start'])
def send_welcome(message):
    # First msg
    bot.send_message(message.chat.id, msglist.start_msg)
    # What`s u name
    msg = bot.send_message(message.chat.id, msglist.name_city)
    bot.register_next_step_handler(msg, desc)


def desc(message):
    # set name_city
    db.insert_name_city(message.chat.id, message.text)
    # what`s u desc
    msg = bot.send_message(message.chat.id, msglist.desc)
    bot.register_next_step_handler(msg, contact_data)


def contact_data(message):
    # set desc
    db.insert_client_desc(message.chat.id, message.text)
    # get u contact_data
    msg = bot.send_message(message.chat.id, msglist.contact_data)
    bot.register_next_step_handler(msg, market_place)


def market_place(message):
    # set contact_data
    db.insert_contact_data(message.chat.id, message.text)
    # u going to mp
    msg = bot.send_message(message.chat.id, msglist.market_place)
    bot.register_next_step_handler(msg, finish_msg)


# Записали почту и должны будем отправлять итоговое сообщение
def finish_msg(message):
    db.insert_market_place(message.chat.id, message.text)
    bot.send_message(message.chat.id, msglist.finish_msg)
    mail.send_email(select_data_user(message.chat.id))


if __name__ == '__main__':
    db.create_tables()
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(3)
            print(e)


