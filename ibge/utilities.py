from selenium.webdriver.remote.webelement import WebElement
from datetime import datetime
import time
import pyderman as dr
import os

class Utilities:

    def get_webdriver(self):
        path = dr.install(browser=dr.chrome, file_directory='./driver', overwrite=True, filename='chromedriver.exe', verbose=False)
        path = path.rsplit('\\', 1)[0]
        return path
    
    def extract_and_clean(self, list_elements):
        list_elements = [element.text.strip() for element in list_elements]
        return list_elements

    def separate_words(self, list_texts):
        if type(list_texts) == list:
            splitted_words = [element.text.strip() for element in list_texts]
            if len(splitted_words) == 1:
                splitted_words = splitted_words[0].split(' ', 1)
        elif type(list_texts) == WebElement:
            splitted_words = list_texts.text
            splitted_words = splitted_words.split(' ', 1)
        else:
            splitted_words = list_texts
            splitted_words = splitted_words.split(' ', 1)
        stripped_words = [word.strip() for word in splitted_words]
        return stripped_words

    def code_value(self):
        return self.separate_words()[0]

    def description_value(self):
        return self.separate_words()[-1]

    def set_time(self, wait):
        time.sleep(wait)

    def retry_with_refresh(self, driver, element):
        try:
            driver.find_element_by_xpath(f'//a[text()="{element}"]').click()
        except:
            driver.refresh()
            driver.find_element_by_xpath(f'//a[text()="{element}"]').click()
        finally:
            driver.get(driver.current_url)

    def register_log(self, error):
        dt_today = datetime.now()
        dt_now = dt_today.strftime('%d_%m_%Y')
        hr_now = dt_today.strftime('%H:%M:%S')
        os.makedirs('./logs', exist_ok=True)
        with open(f'./logs/Log_{dt_now}.txt', 'a+') as arqv:
            arqv.write(f'{hr_now} ::: {error}\n')