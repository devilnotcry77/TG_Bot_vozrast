#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import telebot
botTimeWeb = telebot.TeleBot('')
from telebot import types

@botTimeWeb.message_handler(commands=['start'])
def startBot(message):
  first_mess = f"<b>{message.from_user.first_name}</b>, привет!\nЭтот бот для подтверждения заявок на вступление в группу!"
  markup = types.InlineKeyboardMarkup()
  button_yes = types.InlineKeyboardButton(text = 'Мне есть 18', callback_data='yes')
  button_no = types.InlineKeyboardButton(text = 'Мне меньше 18', callback_data='no')
  markup.add(button_no)
  markup.add(button_yes)
  #markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  #btn1 = types.KeyboardButton("Задать вопрос")
  #markup.add(btn1)
  botTimeWeb.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)
  
@botTimeWeb.callback_query_handler(func=lambda call:True)
def response(function_call):
    
  if function_call.message:
     if function_call.data == "no":
        second_mess = "Прости, ты не можешь быть участником сообщества"
        markup = types.InlineKeyboardMarkup()
        botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
        botTimeWeb.answer_callback_query(function_call.id)
    
  if function_call.message:
     
     
     if function_call.data == "yes":
        second_mess = "Отлично, вы можете перейти в сообщество"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Перейти", url="You TG link"))
        botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
        botTimeWeb.answer_callback_query(function_call.id)
        
botTimeWeb.infinity_polling()