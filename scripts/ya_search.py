from urllib.parse import quote


def list_of_requests(list_):
    products_list = []
    for product in list_:
        products_list.append(quote(product))

    return products_list

