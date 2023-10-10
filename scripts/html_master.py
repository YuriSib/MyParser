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


def click_to_photo(driver, choose_photo):
        wait = WebDriverWait(driver, 20)

        choose_photo[0].click()
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        html = driver.page_source
        soup_ = BeautifulSoup(html, 'lxml')

        return soup_


def sima_master(url):
        driver = settings()
        driver.get(url=url)
        wait = WebDriverWait(driver, 20)

        image_list = []
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        try:
                image_list.append(soup.find('div', {'class': '_ujOS'}).find('img')['src'])
        except AttributeError:
                image_list.append(soup.find('div', {'data-testid': 'product-photo:root'}).find('img')['src'])

        xpath_list = [
                '''//*[@id="product__root"]/div/div[3]/div[1]/div/div[1]/div/div[1]/div/div/div/div/div[2]''',
                '''//*[@id="product__root"]/div/div[3]/div[1]/div/div[1]/div/div[1]/div/div/div/div/div[3]''',
                '''//*[@id="product__root"]/div/div[3]/div[1]/div/div[1]/div/div[1]/div/div/div/div/div[4]'''
        ]
        for xpath in xpath_list:
                choose_photo = driver.find_elements("xpath", xpath)
                if choose_photo:
                        soup = click_to_photo(driver, choose_photo)
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
        specifications = soup.find_all('div', {'class': 'vunEu'})
        property_list = str
        general_list = specifications[0].find_all('div', {'class': 'S3jLY'})

        for general in general_list:
                property_name = general.find('div', {'class': 'property-name'}).get_text(strip=True)
                if 'Артикул' not in property_name and 'Сертификат' not in property_name and \
                        'Торговая марка' not in property_name and 'Европодвес' not in property_name and\
                        'Штрихкод' not in property_name:
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


def relefopt_master(url):
        driver = settings()
        driver.get(url=url)
        wait = WebDriverWait(driver, 20)

        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/main/div/div[1]/div/span/div[1]/'
                            'div/div/div[3]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/div[1]/div/div/div/img')))
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')

        html_list_specification = soup.find_all('a', {'class': 'src-components-Product-PropertyTable--trProperty '
                                                                'src-components-Product-PropertyTable--trProductTabs'})

        dirty_list_specification = []
        property_list = str

        for dirty_specification in html_list_specification:
                property_name = dirty_specification.find('div', {'class': 'src-components-Product-PropertyTable--'
                                'propertyItem src-components-Product-PropertyTable--overflow'}).get_text(strip=True)
                try:
                        property_value = dirty_specification.find('span', {'class': 'src-components-Product-'
                                                'PropertyTable--filterLink src-components-'
                                                'Product-Property''Table--filterLinkTitle'}).get_text(strip=True)
                except AttributeError:
                        property_value = dirty_specification.find('span', {'class': 'src-components-Product-'
                                                                'PropertyTable--filterLink'}).get_text(strip=True)
                finally:
                        property_ = f"• {property_name} : {property_value} \n"
                        property_list = f'{property_list} {property_}'

        image_list = []
        dirty_photo_list = soup.find('div', {'class': 'src-components-ColumnMain--columnMain src-components-ColumnMain--'
                                    'columnMainFullWidth'})
        html_photo_list = dirty_photo_list.find('div', {'class': 'slick-track'})
        photo = html_photo_list.find('div', {'style': 'outline: none; width: 47px;'}).find('div', {'role':
                                            'presentation'}).img['src']
        image_list.append(photo)

        xpath_list = [
                '''//*[@id="content"]/div/main/div/div[1]/div/span/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div[2]
                /div[1]/div/div/div/div[1]/div/div/div''',
                '''//*[@id="content"]/div/main/div/div[1]/div/span/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div[2]
                /div[1]/div/div/div/div[3]/div/div/div''',
                '''//*[@id="content"]/div/main/div/div[1]/div/span/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div[2]
                /div[1]/div/div/div/div[2]/div/div/div'''
        ]
        for xpath in xpath_list:
                choose_photo = driver.find_elements("xpath", xpath)
                if choose_photo:
                        soup2 = click_to_photo(driver, choose_photo)
                        image_list.append(soup2.find('div', {'style': 'outline: none; width: 47px;'}).find('div', {'role'
                                                                                        : 'presentation'}).img['src'])

        return property_list, image_list


if __name__ == "__main__":
        url = 'https://relefopt.ru/catalog/product/2876347'
        relefopt_master(url)
