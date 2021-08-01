import telebot # importamos la libreria de telebot
bot = telebot.TeleBot('1910960403:AAHzikBdQ7hRoPqXPfhMoAzIrDwp1jA-KNY') #anadimos el token
updates = bot.get_updates()
message = updates[0].message
from_user = message.from_user
id = from_user.id
get_me = bot.get_me()
@bot.message_handler(commands=['hola', 'hi']) #definimos el comando
def hola(mensaje):
    bot.reply_to(mensaje, "Hola como estás?")
    print("Mandaron hola o hi")
@bot.message_handler(commands=['celsius', 'celsius']) #definimos el comando
def hola(mensaje):
    bot.reply_to(mensaje, "  ºF = (ºC · 1,8) + 32")
    print("Mandaron Celsius o Celsius")
@bot.message_handler(commands=['Farenheit', 'Farenheit']) #definimos el comando
def hola(mensaje):
    bot.reply_to(mensaje, "  ºC = (ºF -32) / 1,8")
    print("Mandaron Farenheit o Farenheit")
bot.polling()