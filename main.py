import telebot
from telebot import types
import pymorphy2
import wikipedia
from flask import Flask
from flask_login import LoginManager
from flask_restful import Api, Resource, reqparse
import base64
import requests


app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


morph = pymorphy2.MorphAnalyzer()
wikipedia.set_lang("ru")

bot = telebot.TeleBot('5255950308:AAEY37BTzLlJLAWfgQj3X-w3fDlBjA_1zuY')


markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1_1 = types.KeyboardButton("Добавить Позицию")
btn2_1 = types.KeyboardButton("Изменить Позицию")
btn3_1 = types.KeyboardButton("Добавить Категорию")
btn4_1 = types.KeyboardButton("Изменить Категорию")
btn5_1 = types.KeyboardButton("Удалить Категорию")
btn6_1 = types.KeyboardButton("Удалить Позицию")
btn7_1 = types.KeyboardButton("Изменить самовывоз")
btn8_1 = types.KeyboardButton("Изменить доставку")
btn9_1 = types.KeyboardButton("Пороговая сумма доставки")
markup.add(btn1_1, btn3_1)
markup.add(btn2_1, btn4_1)
markup.add(btn6_1, btn5_1)
markup.add(btn7_1, btn8_1)
markup.add(btn9_1)


markup_del = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1_1 = types.KeyboardButton("Изменить")
btn2_1 = types.KeyboardButton("Удалить")
markup_del.add(btn1_1, btn2_1)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Это бот для редактирования. Здесь вы можете создавать, менять,'
                                      ' удалять категории и позиции.'
                                      'Хочу напомнить, что изначально цена доставки и самовывоза 0 рублей.'
                                      'Также прошу, когда вы пишите стоимость, пожалуйста, не пишите'
                                      'валюту', reply_markup=markup)


@bot.message_handler(content_types=["text"])
def func(message):
    if message.text == "Изменить Категорию":
        markup_2 = types.InlineKeyboardMarkup()
        q = requests.get('https://serverfor10000.herokuapp.com/api/sorted_keys').json()['q']
        if q:
            for i in q:
                btn1 = types.InlineKeyboardButton(i, callback_data=i)
                markup_2.add(btn1)
            bot.send_message(message.chat.id, 'Прекрасно', reply_markup=types.ReplyKeyboardRemove())
            bot.send_message(message.chat.id, 'Для начала выберете категорию', reply_markup=markup_2)
        else:
            bot.send_message(message.chat.id, 'Для начала добавьте хоть одну категорию', reply_markup=markup)
    if message.text == "Добавить Категорию":
        r = bot.send_message(message.chat.id, "Напишите Новую Категорию", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(r, rr)
    if message.text == "Добавить Позицию":
        markup_2 = types.InlineKeyboardMarkup()
        q = requests.get('https://serverfor10000.herokuapp.com/api/sorted_keys').json()['q']
        if q:
            for i in q:
                btn1 = types.InlineKeyboardButton(i, callback_data=f"pos_{i}")
                markup_2.add(btn1)
            bot.send_message(message.chat.id, 'Прекрасно', reply_markup=types.ReplyKeyboardRemove())
            bot.send_message(message.chat.id, 'Для начала выберете категорию', reply_markup=markup_2)
        else:
            bot.send_message(message.chat.id, 'Для начала добавьте хоть одну категорию', reply_markup=markup)
    if message.text == "Изменить Позицию":
        markup_2 = types.InlineKeyboardMarkup()
        q = requests.get('https://serverfor10000.herokuapp.com/api/sorted_keys').json()['q']
        if q:
            for i in q:
                btn1 = types.InlineKeyboardButton(i, callback_data=f"pos_cor_{i}")
                markup_2.add(btn1)
            bot.send_message(message.chat.id, 'Прекрасно', reply_markup=types.ReplyKeyboardRemove())
            bot.send_message(message.chat.id, 'Для начала выберете категорию', reply_markup=markup_2)
        else:
            bot.send_message(message.chat.id, 'Для начала добавьте хоть одну позицию', reply_markup=markup)
    if message.text == "Удалить Категорию":
        markup_2 = types.InlineKeyboardMarkup()
        q = requests.get('https://serverfor10000.herokuapp.com/api/sorted_keys').json()['q']
        if q:
            for i in q:
                btn1 = types.InlineKeyboardButton(i, callback_data=f"del_{i}")
                markup_2.add(btn1)
            bot.send_message(message.chat.id, 'Прекрасно', reply_markup=types.ReplyKeyboardRemove())
            bot.send_message(message.chat.id, 'Для начала выберете категорию', reply_markup=markup_2)
        else:
            bot.send_message(message.chat.id, 'Для начала добавьте хоть одну категорию', reply_markup=markup)
    if message.text == "Удалить Позицию":
        markup_2 = types.InlineKeyboardMarkup()
        q = requests.get('https://serverfor10000.herokuapp.com/api/sorted_keys').json()['q']
        if q:
            for i in q:
                btn1 = types.InlineKeyboardButton(i, callback_data=f"pos_del_{i}")
                markup_2.add(btn1)
            bot.send_message(message.chat.id, 'Прекрасно', reply_markup=types.ReplyKeyboardRemove())
            bot.send_message(message.chat.id, 'Для начала выберете категорию', reply_markup=markup_2)
        else:
            bot.send_message(message.chat.id, 'Для начала добавьте хоть одну категорию', reply_markup=markup)
    if message.text == "Изменить самовывоз":
        r = bot.send_message(message.chat.id, "Напишите новую стоимость самовывоза", reply_markup=types.ReplyKeyboardMarkup())
        bot.register_next_step_handler(r, self_delivery)
    if message.text == "Изменить доставку":
        r = bot.send_message(message.chat.id, "Напишите новую стоимость Доставки", reply_markup=types.ReplyKeyboardMarkup())
        bot.register_next_step_handler(r, delivery_delivery)
    if message.text == "Пороговая сумма доставки":
        r = bot.send_message(message.chat.id, "Напишите новую стоимость пороговую стоимость", reply_markup=types.ReplyKeyboardMarkup())
        bot.register_next_step_handler(r, porog_delivery)


def self_delivery(message):
    try:
        if message.text != None:
            try:
                w = int(message.text)
                r = requests.post('https://serverfor10000.herokuapp.com/api/self_delivery_post', json={'cost': w}).json()
                if "success" in dict(r).keys():
                    bot.send_message(message.chat.id, "Всё успешно выполнено", reply_markup=markup)
            except ValueError:
                r = bot.send_message(message.chat.id, "Напишите новую стоимость самовывоза",
                                     reply_markup=types.ReplyKeyboardMarkup())
                bot.register_next_step_handler(r, self_delivery)
        else:
            raise Exception
    except Exception:
        r = bot.send_message(message.chat.id, "Напишите новую стоимость самовывоза",
                             reply_markup=types.ReplyKeyboardMarkup())
        bot.register_next_step_handler(r, self_delivery)


def delivery_delivery(message):
    try:
        if message.text != None:
            try:
                int(message.text)
                r = requests.post('https://serverfor10000.herokuapp.com/api/delivery_delivery_post', json={'cost': int(message.text)}).json()
                if "success" in dict(r).keys():
                    bot.send_message(message.chat.id, "Всё успешно выполнено", reply_markup=markup)
            except ValueError:
                r = bot.send_message(message.chat.id, "Напишите новую стоимость Доставки",
                                     reply_markup=types.ReplyKeyboardMarkup())
                bot.register_next_step_handler(r, delivery_delivery)
        else:
            raise Exception
    except Exception:
        r = bot.send_message(message.chat.id, "Напишите новую стоимость Доставки",
                             reply_markup=types.ReplyKeyboardMarkup())
        bot.register_next_step_handler(r, delivery_delivery)


def porog_delivery(message):
    try:
        if message.text != None:
            try:
                int(message.text)
                r = requests.post('https://serverfor10000.herokuapp.com/api/porog_delivery_post', json={'cost': int(message.text)}).json()
                if "success" in dict(r).keys():
                    bot.send_message(message.chat.id, "Всё успешно выполнено", reply_markup=markup)
            except ValueError:
                r = bot.send_message(message.chat.id, "Напишите новую стоимость пороговую стоимость",
                                     reply_markup=types.ReplyKeyboardMarkup())
                bot.register_next_step_handler(r, porog_delivery)
        else:
            raise Exception
    except Exception:
        r = bot.send_message(message.chat.id, "Напишите новую стоимость пороговую стоимость",
                             reply_markup=types.ReplyKeyboardMarkup())
        bot.register_next_step_handler(r, porog_delivery)


def rr(message):
    try:
        if message.text != None:
            r = requests.post('https://serverfor10000.herokuapp.com/api/category_new_post', json={'cat': message.text,
                                                                                   'cat_new': message.text}).json()
            if "success" in dict(r).keys():
                bot.send_message(message.chat.id, "Всё успешно выполнено", reply_markup=markup)
        else:
            raise Exception
    except Exception:
        r = bot.send_message(message.chat.id, "Напишите Новую Категорию", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(r, rr)


def rr2(message, e):
    try:
        if message.text != None:
            r = requests.post('https://serverfor10000.herokuapp.com/api/category_correct_post', json={'cat': e, 'cat_new': message.text}).json()
            if "success" in dict(r).keys():
                bot.send_message(message.chat.id, "Всё успешно выполнено", reply_markup=markup)
        else:
            raise Exception
    except Exception:
        r = bot.send_message(message.chat.id, "Напишите Новую Категорию", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(r, rr2, e)


def rr3(message, e, name,  photo, description):
    try:
        int(message.text)
        r = requests.post('https://serverfor10000.herokuapp.com/api/position_new_post', json={'category': e, 'name': name, 'photo': photo, 'description': description, 'cost': int(message.text)}).json()
        if "success" in dict(r).keys():
            bot.send_message(message.chat.id, "Всё успешно выполнено", reply_markup=markup)
    except ValueError:
        r = bot.send_message(message.chat.id, "Напишите Стоимость")
        bot.register_next_step_handler(r, rr3, e, name, photo, message.text)


@bot.message_handler(content_types=['document'])
def posit_first(message, category):
    fi2 = requests.get(f'https://serverfor10000.herokuapp.com/api/get_first_fi2/{category}').json()
    try:
        if message.text != None and message.text not in fi2:
            r = bot.send_message(message.chat.id, "Отправьте Фотографию")
            bot.register_next_step_handler(r, posit_second, category, message.text)
        else:
            raise Exception
    except Exception:
        r = bot.send_message(message.chat.id, "Напишите Новую Позицию", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(r, posit_first, category)
        # bot.send_message(message.chat.id, "Ошибка попробуйте сначала", reply_markup=markup)


@bot.message_handler(content_types=['document'])
def posit_second(message, category,  name):
    if message.photo:
        fileID = message.photo[-1].file_id
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)

        with open("image.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)
        encoded = base64.b64encode(open("image.jpg", "rb").read())
        r = bot.send_message(message.chat.id, "Напишите описание")
        bot.register_next_step_handler(r, posit_third, category,  name, str(encoded))
    else:
        r = bot.send_message(message.chat.id, "Отправьте Фотографию")
        bot.register_next_step_handler(r, posit_second, category, message.text)


def posit_third(message, category, name,  photo):
    try:
        if message.text != None:
            r = bot.send_message(message.chat.id, "Напишите Стоимость")
            bot.register_next_step_handler(r, rr3, category, name, photo, message.text)
        else:
            raise Exception
    except Exception:
        r = bot.send_message(message.chat.id, "Напишите описание")
        bot.register_next_step_handler(r, posit_third, category, name, photo)


def correct_pos(message, posit, cat_old):
    try:
        if message.text != None:
            r = requests.post('https://serverfor10000.herokuapp.com/api/position_correct_posit_name_post', json={'cat_old': cat_old, 'posit': posit, 'new_pos': message.text}).json()
            if "success" in dict(r).keys():
                bot.send_message(message.chat.id, "Всё успешно выполнено", reply_markup=markup)
        else:
            raise Exception
    except Exception:
        r = bot.send_message(message.chat.id, "Напишите Новую Позицию",
                             reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(r, correct_pos, posit, cat_old)


@bot.message_handler(content_types=['document'])
def correct_photo(message, posit, cat_old):
    if message.photo:
        fileID = message.photo[-1].file_id
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)

        with open("image.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)
        encoded = base64.b64encode(open("image.jpg", "rb").read())
        r = requests.post('https://serverfor10000.herokuapp.com/api/position_correct_posit_photo_post', json={'cat_old': cat_old, 'posit': posit, 'encoded': str(encoded)}).json()
        if "success" in dict(r).keys():
            bot.send_message(message.chat.id, "Всё успешно выполнено", reply_markup=markup)
    else:
        r = bot.send_message(message.chat.id, "Отправьте Фотографию")
        bot.register_next_step_handler(r, correct_photo, posit, cat_old)


def correct_description(message, posit, cat_old):
    try:
        if message.text != None:
            r = requests.post('https://serverfor10000.herokuapp.com/api/position_correct_posit_description_post',
                              json={'cat_old': cat_old, 'posit': posit, 'description': message.text}).json()
            print(r)
            print('ok')
            if "success" in dict(r).keys():
                bot.send_message(message.chat.id, "Всё успешно выполнено", reply_markup=markup)
        else:
            raise Exception
    except Exception:
        r = bot.send_message(message.chat.id, "Напишите новое описание")
        bot.register_next_step_handler(r, correct_description, posit, cat_old)


def correct_cost(message, posit, cat_old):
    try:
        int(message.text)
        try:
            r = requests.post('https://serverfor10000.herokuapp.com/api/position_correct_posit_cost_post', json={'cat_old': cat_old, 'posit': posit, 'cost': int(message.text)}).json()
            if "success" in dict(r).keys():
                bot.send_message(message.chat.id, "Всё успешно выполнено", reply_markup=markup)
        except Exception:
            bot.send_message(message.chat.id, "Ошибка попробуйте сначала", reply_markup=markup)
    except ValueError:
        r = bot.send_message(message.chat.id, "Напишите Стоимость")
        bot.register_next_step_handler(r, correct_cost, posit, cat_old)


@bot.callback_query_handler(func=lambda c:True)
def inline(c):
    q = requests.get('https://serverfor10000.herokuapp.com/api/sorted_keys').json()['q']
    if c.data in q:
        r = bot.send_message(c.message.chat.id, "Напишите Новую Категорию", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(r, rr2, c.data)
    elif "del_" in c.data and c.data[4:] in q:
        try:
            r = requests.post('https://serverfor10000.herokuapp.com/api/delete_category_post', json={'cat_old': c.data[4:]}).json()
            if "success" in dict(r).keys():
                bot.send_message(c.message.chat.id, "Всё успешно выполнено", reply_markup=markup)
        except Exception:
            bot.send_message(c.message.chat.id, "Ошибка", reply_markup=markup)
    elif c.data[4:] in q and "pos_" in c.data:
        r = bot.send_message(c.message.chat.id, "Напишите Новую Позицию", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(r, posit_first, c.data[4:])
    elif c.data[8:] in q and "pos_cor_" in c.data:
        try:
            fi2 = requests.get(f'https://serverfor10000.herokuapp.com/api/get_first_fi2/{c.data[8:]}').json()['fi2']
            markup_4 = types.InlineKeyboardMarkup()
            if fi2:
                for i in fi2:
                    btn1 = types.InlineKeyboardButton(i, callback_data=f"pos_cor_new_{c.data[8:]}/{i}")
                    markup_4.add(btn1)
                bot.send_message(c.message.chat.id, "Выберите Позицию", reply_markup=markup_4)
            else:
                bot.send_message(c.message.chat.id, "У вас нет ни одной позиции, добавьте хоть одну позицию",
                                 reply_markup=markup)

        except Exception:
            bot.send_message(c.message.chat.id, "У вас нет ни одной позиции, добавьте хоть одну позицию", reply_markup=markup)
    elif c.data.split('/')[0] in q:
        try:
            cat_old = c.data.split('/')[1]
            podition_ppp = c.data.split('/')[2]
            podition_old = c.data.split('/')[-1]
            if podition_ppp == "Позиция":
                r = bot.send_message(c.message.chat.id, "Напишите Новую Позицию",
                                     reply_markup=types.ReplyKeyboardRemove())
                bot.register_next_step_handler(r, correct_pos, podition_old, cat_old)
            if podition_ppp == "Фото":
                r = bot.send_message(c.message.chat.id, "Отправьте Новую Фотографию")
                bot.register_next_step_handler(r, correct_photo, podition_old, cat_old)
            if podition_ppp == "Описание":
                r = bot.send_message(c.message.chat.id, "Напишите новое описание")
                bot.register_next_step_handler(r, correct_description, podition_old, cat_old)
            if podition_ppp == "Стоимость":
                r = bot.send_message(c.message.chat.id, "Напишите Новую стоимость")
                bot.register_next_step_handler(r, correct_cost, podition_old, cat_old)
        except Exception:
            bot.send_message(c.message.chat.id, "Ошибка", reply_markup=markup)
    elif c.data[8:] in q and "pos_del_" in c.data:
        try:
            fi = requests.get(f'https://serverfor10000.herokuapp.com/api/get_fi/{c.data[8:]}').json()['fi']
            fi2 = requests.get(f'https://serverfor10000.herokuapp.com/api/get_first_fi2/{c.data[8:]}').json()['fi2']
            markup_4 = types.InlineKeyboardMarkup()
            if fi2:
                for i in fi2:
                    btn1 = types.InlineKeyboardButton(i, callback_data=f"del_pos_{c.data[8:]}/{fi}/{i}")
                    markup_4.add(btn1)
                bot.send_message(c.message.chat.id, "Выберите Позицию", reply_markup=markup_4)
            else:
                bot.send_message(c.message.chat.id, "Сначала добавьте хоть одну позицию", reply_markup=markup)

        except Exception:
            bot.send_message(c.message.chat.id, "У вас нет ни одной позиции, добавьте хоть одну позицию", reply_markup=markup)
    elif c.data.split('/')[0][4:] in q:
        try:
            r = requests.post('https://serverfor10000.herokuapp.com/api/0_4', json={'1': c.data.split('/')[0][4:], '2': c.data.split('/')[-1]}).json()
            if "success" in dict(r).keys():
                bot.send_message(c.message.chat.id, "Всё успешно выполнено", reply_markup=markup)
        except Exception:
            pass
    elif c.data[12:].split("/")[0] in q and "pos_cor_new_" in c.data:
        try:
            fi2 = requests.get(f"https://serverfor10000.herokuapp.com/api/get_first_fi2/{c.data[12:].split('/')[0]}").json()['fi2']
            fi = requests.get(f"https://serverfor10000.herokuapp.com/api/get_fi/{c.data[12:].split('/')[0]}").json()['fi']
            if c.data[12:].split('/')[-1] in fi2:
                markup_4 = types.InlineKeyboardMarkup()
                w = ["Позиция", "Фото", "Описание", "Стоимость"]
                for i in w:
                    btn1 = types.InlineKeyboardButton(i, callback_data=f"{c.data[12:].split('/')[0]}/{fi}/{i}/{c.data[12:].split('/')[-1]}")
                    markup_4.add(btn1)
                bot.send_message(c.message.chat.id, "Выберите что хотите Изменить", reply_markup=markup_4)

        except Exception:
            bot.send_message(c.message.chat.id, "Ошибка", reply_markup=markup)
    elif c.data[8:].split("/")[0] in q and "del_pos_" in c.data:
        try:
            r = requests.post('https://serverfor10000.herokuapp.com/api/delete_position_post', json={'position1': c.data[8:].split("/")[1], 'position2': c.data[8:].split("/")[-1]}).json()
            if "success" in dict(r).keys():
                bot.send_message(c.message.chat.id, "Всё успешно выполнено", reply_markup=markup)
        except Exception:
            bot.send_message(c.message.chat.id, "Ошибка", reply_markup=markup)


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
    # bot.infinity_polling()


