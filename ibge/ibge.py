import ibge.constants as const
from selenium import webdriver
from ibge.utilities import Utilities
import os

class Ibge(webdriver.Chrome):
    def __init__(self, driver_path="C:/SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        self._infos_table = []
        os.environ['PATH'] += ';'+self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-looging'])
        super().__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, *args):
        if self.teardown:
            self.quit()

    def access_main_page(self):
        self.get(const.BASE_URL)

    def get_secao(self):
        list_divisoes = self.find_elements_by_xpath(
            '//a[contains(text(), "..")]'
            )
        list_divisoes = Utilities().extract_and_clean(list_divisoes)
        return list_divisoes

    def click_secao(self, list_secao, iterator):
        link_text = list_secao[iterator]
        self.find_element_by_partial_link_text(link_text).click()
        self.get(self.current_url)

    def get_secao_infos(self):
        infos_secao = self.find_elements_by_css_selector(
            'span[class="destaque"]'
            )
        self._code_secao, self._name_secao = Utilities().separate_words(infos_secao)
        # self._infos_table.append([code_secao, name_secao])

    def get_divisao(self):
        list_divisao = self.find_elements_by_css_selector(
            'td[class="codigo"] a'
            )
        list_divisao = Utilities().extract_and_clean(list_divisao)
        return list_divisao

    def click_divisao(self, divisao):
        Utilities().retry_with_refresh(self, divisao)
        # self.find_element_by_xpath(f'//a[text()="{divisao}"]').click()
        # self.get(self.current_url)

    def get_divisao_infos(self):
        infos_divisao = self.find_elements_by_css_selector(
            'span[class="destaque"]'
            )
        self._code_divisao, self._name_divisao = Utilities().separate_words(infos_divisao)
        # self._infos_table[-1].append(code_divisao)
        # self._infos_table[-1].append(name_divisao)

    def get_grupo(self):
        list_grupo = self.find_elements_by_css_selector(
            'td[class="codigo n1"] a'
            )
        list_grupo = Utilities().extract_and_clean(list_grupo)
        return list_grupo

    def click_grupo(self, grupo):
        Utilities().retry_with_refresh(self, grupo)
        # self.find_element_by_xpath(f'//a[text()="{grupo}"]').click()
        # self.get(self.current_url)

    def get_grupo_infos(self):
        infos_grupo = self.find_elements_by_css_selector(
            'span[class="destaque"]'
            )
        self._code_grupo, self._name_grupo = Utilities().separate_words(infos_grupo)
        # self._infos_table[-1].append(code_grupo)
        # self._infos_table[-1].append(name_grupo)

    def get_classe(self):
        list_classe = self.find_elements_by_css_selector(
            'td[class="codigo n2"] a'
            )
        list_classe = Utilities().extract_and_clean(list_classe)
        return list_classe

    def click_classe(self, classe):
        # self.find_element_by_xpath(f'//a[text()="{classe}"]').click()
        Utilities().retry_with_refresh(self, classe)
        # self.get(self.current_url)

    def get_classe_infos(self):
        infos_classe = self.find_elements_by_css_selector(
            'span[class="destaque"]'
            )
        self._code_classe, self._name_classe = Utilities().separate_words(infos_classe)
        # self._infos_table[-1].append(code_classe)
        # self._infos_table[-1].append(name_classe)

    def get_subclasse(self):
        subclasse_elements = self.find_elements_by_css_selector(
            'td[class="codigo n3"]'
            )
        return subclasse_elements

    def get_subclasse_infos(self, subclasse):
        self._code_subclasse, self._name_subclasse = Utilities().separate_words(subclasse)
        # self._infos_table[-1].append(code_subclasse)
        # self._infos_table[-1].append(name_subclasse)

    def add_infos(self):
        self._infos_table.append([self._code_secao, self._name_secao, self._code_divisao, self._name_divisao, self._code_grupo, self._name_grupo, self._code_classe, self._name_classe, self._code_subclasse, self._name_subclasse])

    def back_to_grupo(self):
        self.find_element_by_css_selector(
            'td[class="codigo n1"] a'
            ).click()
        Utilities().set_time(5)

    def back_to_divisao(self):
        self.find_element_by_css_selector(
            'td[class="codigo"] a'
            ).click()
        Utilities().set_time(5)

    def back_to_secao(self):
        self.find_element_by_css_selector(
            'table[class="tabela-hierarquia"] a'
            ).click()
        Utilities().set_time(5)