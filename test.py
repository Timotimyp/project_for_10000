# # # import requests
# # # print(requests.get("http://127.0.0.1:5000/api/chat_id_for_registration").json())
# # # # q = {"qwerty": {"name": 1, "ne name": 2}}
# # # # print(q)
# # # # q["ne qwerty"] = {"name": 3, "ne name": 4}
# # # # print(q)
# # # # q.pop("qwerty")
# # # # print(q)
# # print('Вы находитесь в пещере на развилке. Вы можете пойти "налево", "направо" или "прямо".'
# #       'Введите одно из слов в кавычках для выбора.')
# # start = input()
# # # print(start)
# # while start != "налево" and start != "направо" and start != "прямо":
# #     start = input()
# # if start == "налево":
# #     print('Вы направились налево. Через некоторое время вы дошли до двух дверей.'
# #           ' Вы выберете "левую" или "правую"?')
# #     mode1 = input()
# #     if mode1 == "правую":
# #         print('Вы смело открыли правую дверь. Но за ней вас подстерегала гигантская подземная жаба,'
# #               ' которая проглотила вас целиком!')
# #     if mode1 == "левую":
# #         print("Вы открыли не ту дверь и вас съела змея")
# # elif start == "направо":
# #     print('Вы направились направо. Через некоторое время вы дошли до двух дверей.'
# #           ' Вы выберете "левую" или "правую"?')
# #     mode2 = input()
# #     if mode2 == "левую":
# #         print("Вы открыли дверь и за ней увидели лестницу на выход."
# #               " Но когда вы лезли по лесницы одна из ступенек сломалась и вы упали и погобли.")
# #     if mode2 == 'правую':
# #         print("Вы открыли эту дверь слишком сильно и сильно прищимили мизинец,"
# #               " после чего скончались от непереносимоу боли.")
# # elif start == "прямо":
# #     print("Вы направились прямо. Скоро вы дошли до выхода. Поздравляю вы выйграли.")
# def logged(func):
#     count = 0
#
#     def decorated_func(*args, **kwargs):
#         nonlocal count
#         count += 1
#         print(count, '>>', 'Arguments:', args, 'Named arguments:', kwargs)
#         result = func(*args, **kwargs)
#         print('--', 'Result:', result)
#         return result
#
#     return decorated_func
#
#
# @logged
# def make_burger(type_of_meat, with_onion=False, with_tomato=True):
#     print('Булочка')
#     if with_onion:
#         print('Луковые колечки')
#     if with_tomato:
#         print('Ломтик помидора')
#     print('Котлета из', type_of_meat)
#     print('Булочка')
#
#
# @logged
# def drinking_type(type):
#     return 'У нас есть только чай'
#
# make_burger("dadss")
import requests
print(requests.get('http://localhost:5000/api/get_mf/667'))
print(requests.get('http://localhost:5000/api/get_mf/667'))