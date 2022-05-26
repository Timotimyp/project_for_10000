import telebot
from telebot import types
from data import db_session
from data.all import all
from data.cat import cat
import pymorphy2
import wikipedia, re


morph = pymorphy2.MorphAnalyzer()
wikipedia.set_lang("ru")

bot = telebot.TeleBot('5317333483:AAE-7tTnPlld9XydPWDIVipq0CDH-DVABgU')

q = {"0": "Напитки", "1": "Товары", "2": "Разное"}
q2 = {}


markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1_1 = types.KeyboardButton("Добавить Позицию")
btn2_1 = types.KeyboardButton("Изменить Позицию")
btn3_1 = types.KeyboardButton("Добавить Категорию")
btn4_1 = types.KeyboardButton("Изменить Категорию")
btn5_1 = types.KeyboardButton("Удалить Категорию")
btn6_1 = types.KeyboardButton("Удалить Позицию")
markup.add(btn1_1, btn3_1)
markup.add(btn2_1, btn4_1)
markup.add(btn6_1, btn5_1)


markup_del = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1_1 = types.KeyboardButton("Изменить")
btn2_1 = types.KeyboardButton("Удалить")
markup_del.add(btn1_1, btn2_1)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Приветствую, для начала выберете категорию', reply_markup=markup)


@bot.message_handler(content_types=["text"])
def func(message):
    if message.text == "Изменить Категорию":
        markup_2 = types.InlineKeyboardMarkup()
        db_sess = db_session.create_session()
        q = [prof.category_new for prof in db_sess.query(cat).all()]
        q = sorted(q)
        if q:
            for i in q:
                btn1 = types.InlineKeyboardButton(i, callback_data=i)
                markup_2.add(btn1)
            bot.send_message(message.chat.id, 'Прекрасно', reply_markup=types.ReplyKeyboardRemove())
            bot.send_message(message.chat.id, 'Для начала выберете категорию', reply_markup=markup_2)
        else:
            bot.send_message(message.chat.id, 'Для начала добавьте хоть одну категорию', reply_markup=markup)
    if message.text == "Добавить Категорию":
        db_sess = db_session.create_session()
        q = [prof.category for prof in db_sess.query(cat).all()]
        r = bot.send_message(message.chat.id, "Напишите Новую Категорию", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(r, rr)
    if message.text == "Добавить Позицию":
        markup_2 = types.InlineKeyboardMarkup()
        db_sess = db_session.create_session()
        q = [prof.category_new for prof in db_sess.query(cat).all()]
        q = sorted(q)
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
        db_sess = db_session.create_session()
        q = [prof.category_new for prof in db_sess.query(cat).all()]
        q = sorted(q)
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
        db_sess = db_session.create_session()
        q = [prof.category_new for prof in db_sess.query(cat).all()]
        q = sorted(q)
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
        db_sess = db_session.create_session()
        q = [prof.category_new for prof in db_sess.query(cat).all()]
        q = sorted(q)
        if q:
            for i in q:
                btn1 = types.InlineKeyboardButton(i, callback_data=f"pos_del_{i}")
                markup_2.add(btn1)
            bot.send_message(message.chat.id, 'Прекрасно', reply_markup=types.ReplyKeyboardRemove())
            bot.send_message(message.chat.id, 'Для начала выберете категорию', reply_markup=markup_2)
        else:
            bot.send_message(message.chat.id, 'Для начала добавьте хоть одну категорию', reply_markup=markup)


def rr(message):
    user = cat()
    user.category = message.text
    user.category_new = message.text
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    bot.send_message(message.chat.id, "Всё успешно выполнено", reply_markup=markup)


def rr2(message, e):
    db_sess = db_session.create_session()
    news = db_sess.query(cat).get(e)
    db_sess.delete(news)
    db_sess.commit()
    user = cat()
    user.category = e
    user.category_new = message.text
    db_sess.add(user)
    db_sess.commit()
    bot.send_message(message.chat.id, "Всё успешно выполнено", reply_markup=markup)


def rr3(message, e):
    db_sess = db_session.create_session()
    try:
        fi = db_sess.query(cat).filter(cat.category_new == e).first()
        fi2 = db_sess.query(all).filter(all.category == fi.category).first()
        news = db_sess.query(all).get(fi.category)
        db_sess.delete(news)
        db_sess.commit()
        user = all()
        user.category = fi.category
        if message.text not in fi2.position:
            user.position = message.text + "//" + fi2.position
        else:
            user.position = fi2.position

    except Exception:
        fi = db_sess.query(cat).filter(cat.category_new == e).first()
        db_sess.commit()
        user = all()
        user.category = fi.category
        user.position = message.text
    db_sess.add(user)
    db_sess.commit()
    bot.send_message(message.chat.id, "Всё успешно выполнено", reply_markup=markup)


def rr4(message, e, e1):
    db_sess = db_session.create_session()
    try:
        fi = db_sess.query(cat).filter(cat.category_new == e).first()
        fi2 = db_sess.query(all).filter(all.category == fi.category).first()
        fi2 = fi2.position.replace(e1, "")
        news = db_sess.query(all).get(fi.category)
        db_sess.delete(news)
        db_sess.commit()
        user = all()
        user.category = fi.category
        user.position = fi2 + "//" + message.text
        db_sess.add(user)
        db_sess.commit()
        bot.send_message(message.chat.id, "Всё успешно выполнено", reply_markup=markup)
    except Exception:
        pass


@bot.callback_query_handler(func=lambda c:True)
def inline(c):
    db_sess = db_session.create_session()
    q = [prof.category_new for prof in db_sess.query(cat).all()]
    q = sorted(q)
    if c.data in q:
        r = bot.send_message(c.message.chat.id, "Напишите Новую Категорию", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(r, rr2, c.data)
    elif "del_" in c.data and c.data[4:] in q:
        print(c.data[4:])
        try:
            db_sess = db_session.create_session()
            fi = db_sess.query(cat).filter(cat.category_new == c.data[4:]).first()
            news = db_sess.query(cat).get(fi.category)
            db_sess.delete(news)
            db_sess.commit()
            bot.send_message(c.message.chat.id, "Всё успешно выполнено", reply_markup=markup)
        except Exception:
            pass
    elif c.data[4:] in q and "pos_" in c.data:
        r = bot.send_message(c.message.chat.id, "Напишите Новую Позицию", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(r, rr3, c.data[4:])
    elif c.data[8:] in q and "pos_cor_" in c.data:
        db_sess = db_session.create_session()
        try:
            fi = db_sess.query(cat).filter(cat.category_new == c.data[8:]).first()
            fi2 = db_sess.query(all).filter(all.category == fi.category).first()
            fi2 = sorted(i for i in fi2.position.split("//"))
            print(fi2)
            markup_4 = types.InlineKeyboardMarkup()
            for i in fi2:
                btn1 = types.InlineKeyboardButton(i, callback_data=f"{c.data[8:]}/{i}")
                markup_4.add(btn1)
            bot.send_message(c.message.chat.id, "Выберите Позицию", reply_markup=markup_4)

        except Exception:
            bot.send_message(c.message.chat.id, "У вас нет ни одной позиции, добавьте хоть одну позицию", reply_markup=markup)
    elif c.data.split('/')[0] in q:
        try:
            fi = db_sess.query(cat).filter(cat.category_new == c.data.split('/')[0]).first()
            fi2 = db_sess.query(all).filter(all.category == fi.category).first()
            fi2 = sorted(i for i in fi2.position.split("//"))
            if c.data.split('/')[-1] in fi2:
                r = bot.send_message(c.message.chat.id, "Напишите Новую Позицию", reply_markup=types.ReplyKeyboardRemove())
                bot.register_next_step_handler(r, rr4, c.data.split('/')[0], c.data.split('/')[-1])
        except Exception:
            pass
    elif c.data[8:] in q and "pos_del_" in c.data:
        db_sess = db_session.create_session()
        try:
            fi = db_sess.query(cat).filter(cat.category_new == c.data[8:]).first()
            fi2 = db_sess.query(all).filter(all.category == fi.category).first()
            fi2 = sorted(i for i in fi2.position.split("//"))
            markup_4 = types.InlineKeyboardMarkup()
            for i in fi2:
                btn1 = types.InlineKeyboardButton(i, callback_data=f"del_{c.data[8:]}/{i}")
                markup_4.add(btn1)
            bot.send_message(c.message.chat.id, "Выберите Позицию", reply_markup=markup_4)

        except Exception:
            bot.send_message(c.message.chat.id, "У вас нет ни одной позиции, добавьте хоть одну позицию", reply_markup=markup)
    elif c.data.split('/')[0][4:] in q:
        db_sess = db_session.create_session()
        try:
            fi = db_sess.query(cat).filter(cat.category_new == c.data.split('/')[0][4:]).first()
            fi2 = db_sess.query(all).filter(all.category == fi.category).first()
            fi2 = fi2.position.replace(c.data.split('/')[-1], "")
            print(c.data.split('/')[-1])
            print(fi2)
            news = db_sess.query(all).get(fi.category)
            db_sess.delete(news)
            db_sess.commit()
            user = all()
            user.category = fi.category
            user.position = fi2
            db_sess.add(user)
            db_sess.commit()
            bot.send_message(c.message.chat.id, "Всё успешно выполнено", reply_markup=markup)
        except Exception:
            pass


# bot.infinity_polling()
# bot.polling(none_stop=True, interval=0)

if __name__ == '__main__':
    db_session.global_init("db/users.db")
    db_sess = db_session.create_session()
    # fi2 = db_sess.query(all).filter(all.category == "eat").first()
    # print(fi2)
    # user = all()
    # user.category = "eat"
    # user.position = ["banana"]
    # db_sess.add(user)
    # db_sess.commit()
    # fi = db_sess.query(cat).filter(cat.category_new == "eat").first()
    bot.polling(none_stop=True, interval=0)
    # bot.infinity_polling()


