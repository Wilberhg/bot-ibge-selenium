import ibge.constants as const
from selenium import webdriver
from ibge.utilities import Utilities
import os

class Ibge(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        self._infos_table = []
        self.util = Utilities()
        os.environ['PATH'] += ';'+self.util.get_webdriver()
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-looging'])
        super().__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, *args):
        if self.teardown:
            self.quit()

    def get_infos_table(self):
        return self._infos_table

    def access_main_page(self):
        self.get(const.BASE_URL)

    def get_secao(self):
        list_divisoes = self.find_elements_by_xpath(
            '//a[contains(text(), "..")]'
            )
        list_divisoes = self.util.extract_and_clean(list_divisoes)
        return list_divisoes

    def click_secao(self, list_secao, iterator):
        link_text = list_secao[iterator]
        self.find_element_by_partial_link_text(link_text).click()
        self.get(self.current_url)

    def get_secao_infos(self):
        infos_secao = self.find_elements_by_css_selector(
            'span[class="destaque"]'
            )
        self._code_secao, self._name_secao = self.util.separate_words(infos_secao)

    def get_divisao(self):
        list_divisao = self.find_elements_by_css_selector(
            'td[class="codigo"] a'
            )
        list_divisao = self.util.extract_and_clean(list_divisao)
        return list_divisao

    def click_divisao(self, divisao):
        self.util.retry_with_refresh(self, divisao)

    def get_divisao_infos(self):
        infos_divisao = self.find_elements_by_css_selector(
            'span[class="destaque"]'
            )
        self._code_divisao, self._name_divisao = self.util.separate_words(infos_divisao)

    def get_grupo(self):
        list_grupo = self.find_elements_by_css_selector(
            'td[class="codigo n1"] a'
            )
        list_grupo = self.util.extract_and_clean(list_grupo)
        return list_grupo

    def click_grupo(self, grupo):
        self.util.retry_with_refresh(self, grupo)

    def get_grupo_infos(self):
        infos_grupo = self.find_elements_by_css_selector(
            'span[class="destaque"]'
            )
        self._code_grupo, self._name_grupo = self.util.separate_words(infos_grupo)

    def get_classe(self):
        list_classe = self.find_elements_by_css_selector(
            'td[class="codigo n2"] a'
            )
        list_classe = self.util.extract_and_clean(list_classe)
        return list_classe

    def click_classe(self, classe):
        self.util.retry_with_refresh(self, classe)

    def get_classe_infos(self):
        infos_classe = self.find_elements_by_css_selector(
            'span[class="destaque"]'
            )
        self._code_classe, self._name_classe = self.util.separate_words(infos_classe)

    def get_subclasse(self):
        subclasse_elements = self.find_elements_by_css_selector(
            'td[class="codigo n3"]'
            )
        return subclasse_elements

    def get_subclasse_infos(self, subclasse):
        self._code_subclasse, self._name_subclasse = self.util.separate_words(subclasse)

    def add_infos(self):
        self._infos_table.append([self._code_secao, self._name_secao, self._code_divisao, self._name_divisao, self._code_grupo, self._name_grupo, self._code_classe, self._name_classe, self._code_subclasse, self._name_subclasse])

    def back_to_grupo(self):
        self.find_element_by_css_selector(
            'td[class="codigo n1"] a'
            ).click()
        self.util.set_time(5)

    def back_to_divisao(self):
        self.find_element_by_css_selector(
            'td[class="codigo"] a'
            ).click()
        self.util.set_time(5)

    def back_to_secao(self):
        self.find_element_by_css_selector(
            'table[class="tabela-hierarquia"] a'
            ).click()
        self.util.set_time(5)