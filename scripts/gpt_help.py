import g4f


def gpt_helper(text_):
    response_ = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"{text_} Переработай этот текст таким образом, чтобы остались только "
                                              f"  eго технические характеристики в формате: • Характеристика: "
                                              f"её значение. Сделать нужно кратко, информативно и без брендов"}],
    )

    return response_


if __name__ == "__main__":
    text = '''Набор двухсторонних скетчмаркеров Alingar,120 цветов, пулевидный/клиновидный 1-6 мм, спиртовая основа, 
    сумка-чехол с ПВХ каркас-ячейками'''
    response = gpt_helper
