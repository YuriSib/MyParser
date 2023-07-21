from html_master import html_obj
from soup import for_goo_search, for_ya_search, for_vi, vi_photo, for_ya_m
from ya_search import list_of_requests
from export_in_excel import export_excel, quantity_row


# def pars_in_vi():

def search():
    link_list = []
    first = 'https://www.google.com/search?q='
    # first = 'https://yandex.ru/search/?'
    second_list = list_of_requests()
    for second in second_list:
        html = html_obj(first, second)
        links = for_goo_search(html)
        link_list.append(links)

    return link_list


def vi():
    links_list = search()
    specifications = []
    quantity_iter = 2
    for row in range(2, quantity_row()):
        for links in links_list:
            for link in links:
                if 'vseinstrumenti.ru' in link:
                    html = html_obj(link)
                    export_excel(for_vi(html), 2, quantity_iter)
                    export_excel(vi_photo(html), 3, quantity_iter)
                    quantity_iter += 1

    return specifications


search_list = vi()

print(search_list)
