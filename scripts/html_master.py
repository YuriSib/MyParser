from selenium import webdriver
from selenium_stealth import stealth
import time
import pyautogui
from bs4 import BeautifulSoup
from seleniumbase import SB
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium_stealth import stealth
import time


def settings():
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")

        # options.add_argument("--headless")

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


def html_obj(url):
    with SB(headed=True) as driver:
        driver.open(url)
        page_html1 = driver.get_page_source()

        return page_html1


def sima_master(url):
        driver = settings()
        driver.get(url=url)
        wait = WebDriverWait(driver, 10)

        image_list = []
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        try:
                image_list.append(soup.find('div', {'class': '_ujOS'}).find('img')['src'])
        except AttributeError:
                image_list.append(soup.find('div', {'data-testid': 'product-photo:root'}).find('img')['src'])

        choose_photo = driver.find_elements("xpath", '''//*[@id="product__root"]/div/div[3]/div[1]/div/div[1]/div/div[1]/div
                                                                                        /div/div/div/div[2]''')
        if choose_photo:
                choose_photo[0].click()
                wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                html = driver.page_source
                soup = BeautifulSoup(html, 'lxml')
                image_list.append(soup.find('span', {'class': 'iEmif LHQ7Y'}).find('img')['src'])
                ActionChains(driver).send_keys(Keys.ESCAPE).perform()

                choose_photo = driver.find_elements("xpath", '''//*[@id="product__root"]/div/div[3]/div[1]/div/div[1]/div/div[1]/div
                                                                /div/div/div/div[3]''')
                if choose_photo:
                        choose_photo[0].click()
                        html = driver.page_source
                        soup = BeautifulSoup(html, 'lxml')
                        image_list.append(soup.find('span', {'class': 'iEmif LHQ7Y'}).find('img')['src'])
                        ActionChains(driver).send_keys(Keys.ESCAPE).perform()

        button_specifications = driver.find_elements("xpath", '''//*[@id="product__root"]/div/div[3]/div[2]/div[1]/ul/li[2]''')
        if button_specifications:
                button_specifications[0].click()

        button_deploy = driver.find_elements("xpath", '''//a[@data-testid='rolled-up-button']''')
        if button_deploy:
                button_deploy[0].click()

        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        specifications = soup.find_all('div', {'class': 'NmqWz'})
        property_list = str
        general_list = specifications[0].find_all('div', {'class': 'BheKE'})

        for general in general_list:
                property_name = general.find('div', {'class': 'property-name'}).get_text(strip=True)
                if 'Артикул' not in property_name and 'Сертификат' not in property_name:
                        property_value = general.find('div', {'class': 'MZwdI'}).get_text(strip=True)
                        property_ = f"• {property_name} : {property_value} \n"
                        property_list = f'{property_list} {property_}'

        try:
                general_list = specifications[3].find_all('div', {'class': 'BheKE'})
                for general in general_list:
                        property_name = general.find('div', {'class': 'property-name'}).get_text(strip=True)
                        property_value = general.find('div', {'class': 'MZwdI'}).get_text(strip=True)
                        property_ = f"• {property_name} : {property_value}\n"
                        property_list = f'{property_list} {property_}'
        except IndexError as e:
                print(e)


        driver.close()
        driver.quit()

        return property_list, image_list


# def ozon_master(url):
#         driver = settings()
#         driver.get(url=url)
#         wait = WebDriverWait(driver, 10)
#
#         image_list = []
#         html = driver.page_source
#         soup = BeautifulSoup(html, 'lxml')
#         image_list.append(soup.find('div', {'class': 'mj9'}).find('img')['src'])
#
#         try:
#                 driver.find_element("xpath", '''//*[@id="layoutPage"]/div[1]/div[4]/div[3]/div[1]/div[1]/div[1]/div/div[2]
#                                                                 /div/div[2]/div[1]/div/div[2]/div[3]/div/img''').click()
#                 html = driver.page_source
#                 soup = BeautifulSoup(html, 'lxml')
#                 image_list.append(soup.find('div', {'class': 'mj9'}).find('img')['src'])
#
#                 driver.find_element("xpath", '''//*[@id="layoutPage"]/div[1]/div[4]/div[3]/div[1]/div[1]/div[1]/div/div[2]
#                                                                 /div/div[2]/div[1]/div/div[2]/div[4]/div/img''').click()
#                 html = driver.page_source
#                 soup = BeautifulSoup(html, 'lxml')
#                 image_list.append(soup.find('div', {'class': 'mj9'}).find('img')['src'])
#         except AttributeError:
#                 pass
#
#         specifications = soup.find_all('div', {'style': 'width: calc(50%);'})
#         specification = specifications[0].find_all('dl', {'class': 't7j'})
#
#         property_list = str
#         for property_ in specification:
#                 property_name = property_.find('dt', {'class': 't6j'}).get_text(strip=True)
#                 property_value = property_.find('dd', {'class': 'jt7'}).get_text(strip=True)
#                 property_ = f"• {property_name} : {property_value}\n"
#                 property_list = f'{property_list} {property_}'
#
#         return property_list, image_list



