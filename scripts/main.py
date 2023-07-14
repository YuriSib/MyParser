from html_master import html_obj
from soup import for_ya_search, for_vi, for_ya_m
from ya_search import list_of_requests
from export_in_excel import export_excel, quantity_row


# def pars_in_vi():

def search():
    link_list = []
    first = 'https://yandex.ru/search/?'
    second_list = list_of_requests()
    for second in second_list:
        html = html_obj(first, second)
        links = for_ya_search(html)
        link_list.append(links)

    return link_list


def vi():
    link_list = search()
    specifications = []
    quantity_iter = 5
    # for row in range(2, quantity_row()): - когда работаем со всей таблицей
    for links in link_list:
        for link in links:
            if 'vseinstrumenti.ru' in link:
                html = html_obj(link)
                export_excel(for_vi(html), 2, quantity_iter)
                quantity_iter += 1

    return specifications


search_list = vi()

print(search_list)
