import pickle
from collections import Counter
import os

from search import search_xml
from ya_search import list_of_requests
from import_from_excel import import_xl


def save_in_pickle():
    qwery_list = list_of_requests(import_xl("Атласы; Грамоты; Календари.xlsx"))

    count = 0
    for qwery in qwery_list:
        count += 1
        list_link = search_xml(qwery)
        clean_list = []
        for link in list_link:
            parts = link.split('/')
            new_link = '/'.join(parts[:3])
            clean_list.append(new_link)
        with open(f'List link/link_list{count}.pkl', 'wb') as file:
            pickle.dump(clean_list, file)

    with open('List link/link_list1.pkl', 'rb') as file:
        loaded_list = pickle.load(file)


full_list_link = []
file_list = os.listdir('List link')

for file_name in file_list:
    with open(f'List link/{file_name}', 'rb') as file:
        loaded_list = pickle.load(file)
    full_list_link.extend(loaded_list)

counted_elements = Counter(full_list_link)
for element, count in counted_elements.items():
    if count > 1:  # Фильтруем элементы, которые повторяются хотя бы один раз
        print(f"Сайт {element} встречается в поиске {count} раз(а)")