from playwright.sync_api import sync_playwright


def html_obj(url):
    with sync_playwright() as p:
        # для отображения браузера-эмулятора в аргументе функции прописать - (headless=False, slow_mo=50)
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(url)

        html = page.content()
        browser.close()
    return html


