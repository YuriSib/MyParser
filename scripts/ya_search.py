from urllib.parse import quote

# from import_from_excel import import_xl


def list_of_requests(list_):
    # products = import_xl()
    products_list = []
    for product in list_:
        products_list.append(quote(product))

    return products_list

