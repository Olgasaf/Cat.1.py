#import telebot

#TOKEN = "5342722255:AAGRbGMvapVvOuMEx6gax80NVQKqmSMJDmk"

#bot = telebot.TeleBot(TOKEN)

#@bot.message_handler(content_types=['photo', ])
#def say_lmao(message: telebot.types.Message):
#    bot.reply_to(message, 'Мир прекрасен')

#@bot.message_handler(commands=['start', 'help'])
#def repeat(message:telebot.types.Message):
#    bot.reply_to(message,f'Привет,/c{message.chat.username}')

# Обрабатываются все документы и аудиозаписи
#@bot.message_handler(content_types=['document', 'audio'])
#def handle_docs_audio(message):
#    pass
#@bot.message_handler(content_types=['voice'])
#def repeat(message:telebot.types.Message):
#    bot.send_message(message.chat.id, "У тебя очень красивый голос")
#bot.polling(none_stop=True)

#import requests  # импортируем наш знакомый модуль
#import lxml.html
#from lxml import etree

#html = requests.get('https://www.python.org/').content  # получим html главной странички официального сайта Python

#tree = lxml.html.document_fromstring(html)
#title = tree.xpath(
#    '/html/head/title/text()')  # забираем текст тега <title> из тега <head> который лежит в свою очередь внутри тега <html> (в этом невидимом теге <head> у нас хранится основная информация о страничке. Её название и инструкции по отображению в браузере.

#print(title)  # выводим полученный заголовок страницы

#import requests  # импортируем наш знакомый модуль
#import lxml.html
#from lxml import etree

# создадим объект ElementTree. Он возвращается функцией parse()
#tree = etree.parse('Welcome to Python.org.html',
#                   lxml.html.HTMLParser())  # попытаемся спарсить наш файл с помощью HTML-парсера. Сам HTML — это то, что мы скачали и поместили в папку из браузера.

#ul = tree.findall('//*[@id="content"]/div/section/div/div[1]/div/ul/li')  # помещаем в аргумент методу findall скопированный xpath. Здесь мы получим все элементы списка новостей. (Все заголовки и их даты)

# создаём цикл? в котором будем выводить название каждого элемента из списка
#for li in ul:
#    a = li.find('a')  # в каждом элементе находим, где хранится заголовок новости. У нас это тег <a>. Т.е. гиперссылка, на которую нужно нажать, чтобы перейти на страницу с новостью. Гиперссылки в HTML — это всегда тэг <a>.
#    print(a.text)  # из этого тега забираем текст — это и будет нашим названием