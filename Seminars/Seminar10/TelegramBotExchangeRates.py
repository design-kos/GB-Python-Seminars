import requests
import telebot
from telebot import types

bot = telebot.TeleBot("5672768794:AAEQNxcMFQxqoeLkG-Kakve1YjBe6TCVLyM")

dictionary = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()
usd_exchange_rate = format(float(dictionary["Valute"]["USD"]["Value"]), ".2f")
eur_exchange_rate = format(float(dictionary["Valute"]["EUR"]["Value"]), ".2f")
cny_exchange_rate = format(float(dictionary["Valute"]["CNY"]["Value"]) / 10, ".2f")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_usd = types.KeyboardButton("Доллар США")
    btn_eur = types.KeyboardButton("Евро")
    btn_cny = types.KeyboardButton("Китайский юань")
    markup.add(btn_usd, btn_eur, btn_cny)
    bot.reply_to(message, "Кликни на валюту, мы покажем тебе актуальный курс к рублю.", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def print_exchange_rates(message):
    if (message.text == "Доллар США"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_eur = types.KeyboardButton("Евро")
        btn_cny = types.KeyboardButton("Китайский юань")
        markup.add(btn_eur, btn_cny)
        bot.send_message(message.chat.id, text=f"Курс доллара к рублю = {usd_exchange_rate}", reply_markup=markup)
    elif (message.text == "Евро"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_usd = types.KeyboardButton("Доллар США")
        btn_cny = types.KeyboardButton("Китайский юань")
        markup.add(btn_usd, btn_cny)
        bot.send_message(message.chat.id, text=f"Курс евро к рублю = {eur_exchange_rate}", reply_markup=markup)
    elif (message.text == "Китайский юань"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_usd = types.KeyboardButton("Доллар США")
        btn_eur = types.KeyboardButton("Евро")
        markup.add(btn_usd, btn_eur)
        bot.send_message(message.chat.id, text=f"Курс юаня к рублю = {cny_exchange_rate}", reply_markup=markup)  
    else:       
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_usd = types.KeyboardButton("Доллар США")
        btn_eur = types.KeyboardButton("Евро")
        btn_cny = types.KeyboardButton("Китайский юань")
        markup.add(btn_usd, btn_eur, btn_cny)
        bot.reply_to(message, "Выберите валюту.", reply_markup=markup)

bot.infinity_polling()    