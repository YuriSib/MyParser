# import g4f
#
#
# def gpt_helper(text_):
#     g4f.debug.logging = True
#     g4f.check_version = False
#
#     for i in range(2):
#         try:
#             response_ = g4f.ChatCompletion.create(
#                 model="gpt-3.5-turbo",
#                 messages=[{"role": "user", "content": f"{text_} Переработай этот текст таким образом, чтобы остались "
#                                                       f"только технические характеристики товара в строгом соответствии"
#                                                       f" с форматом: • Характеристика товара : её значение \n. Сделать"
#                                                       f" нужно кратко, информативно и без брендов."}],
#             )
#         except Exception:
#             response_ = False
#         if 'support' in response_:
#             response_ = False
#         elif '!DOCTYPE html' in response_:
#             response_ = False
#         if response_ is False:
#             continue
#         else:
#             return response_
#
#
# if __name__ == "__main__":
#     text = '''Набор двухсторонних скетчмаркеров Alingar,120 цветов, пулевидный/клиновидный 1-6 мм, спиртовая основа,
#     сумка-чехол с ПВХ каркас-ячейками'''
#     response = gpt_helper(text)
#     print(text)


