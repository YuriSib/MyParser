from urllib.parse import urlencode

from import_from_excel import import_xl


def list_of_requests():
    products = import_xl()
    products_list = []
    for product in products:
        encoded_query = urlencode({'text': product})
        products_list.append(encoded_query)

    return products_list