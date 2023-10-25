from bs4 import BeautifulSoup
from gpt_help import gpt_helper

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium_stealth import stealth
from selenium.common.exceptions import NoSuchElementException


def settings():
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")

        options.add_argument("--no-sandbox")
        options.add_argument("--headless")

        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(options=options)

        stealth(driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )

        return driver


def click_to_photo(driver, choose_photo):
        wait = WebDriverWait(driver, 20)

        choose_photo[0].click()
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        html = driver.page_source
        soup_ = BeautifulSoup(html, 'lxml')

        return soup_


def yandex_market_master(url):
        driver = settings()
        driver.get(url=url)
        wait = WebDriverWait(driver, 20)

        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')

        property_list = None
        html_list_specification = soup.find_all('div', {'class': '_198Aj cXkP_ _3wss4 _1XOOj'})
        for specification in html_list_specification:
                property_name = specification.find('div', {'class': '_1oG4-'}).get_text(strip=True)
                if 'Вес' not in property_name and 'ранспорт' not in property_name and \
                        'Торговая марка' not in property_name and 'ополнительн' not in property_name:
                        property_value = specification.find('div', {'class': '_3K3f3'}).get_text(strip=True)
                        property_ = f"• {property_name} : {property_value} \n"
                        property_list = f'{property_list} {property_}'

        image_list = []
        html_list_photo = soup.find('div', {'id': 'ProductImageGallery'})
        list_photo = html_list_photo.find('div', {'class': '_1HSAJ'}) if html_list_photo else False
        photo = 'https:' + list_photo.img['src'] if list_photo else 0
        image_list.append(photo)

        xpath_list = [
                '''//*[@id="ProductImageGallery"]/div[19]/div[1]/ul/li[2]/div''',
                '''//*[@id="ProductImageGallery"]/div[19]/div[1]/ul/li[3]/div''',
                '''//*[@id="ProductImageGallery"]/div[19]/div[1]/ul/li[4]/div'''
        ]
        for xpath in xpath_list:
                choose_photo = driver.find_elements("xpath", xpath)
                if choose_photo:
                        click_to_photo(driver, choose_photo)
                        html2 = driver.page_source
                        soup2 = BeautifulSoup(html2, 'lxml')
                        image_list.append('https://market.yandex.ru/' + soup2.find('div', {'id': 'ProductImageGallery'})
                                          .find('div', {'class': '_1HSAJ'}).img['src'])

        return image_list, property_list


# if __name__ == "__main__":
#         url = 'https://www.wildberries.ru/catalog/153534702/detail.aspx'
#         wb_master(url)
