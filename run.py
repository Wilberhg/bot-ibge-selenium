from ibge.ibge import Ibge
from excel.create_excel import CreateExcel
from excel.treat_excel import TreatExcel
from ibge.utilities import Utilities

try:
    with Ibge(True) as bot:
        bot.access_main_page()
        secoes = bot.get_secao()
        for secao in range(0, 3):
            bot.click_secao(list_secao=secoes, iterator=secao)
            bot.get_secao_infos()
            divisoes = bot.get_divisao()
            for divisao in divisoes:
                bot.click_divisao(divisao=divisao)
                bot.get_divisao_infos()
                grupos = bot.get_grupo()
                for grupo in grupos:
                    bot.click_grupo(grupo=grupo)
                    bot.get_grupo_infos()
                    classes = bot.get_classe()
                    for classe in classes:
                        bot.click_classe(classe=classe)
                        bot.get_classe_infos()
                        subclasses = bot.get_subclasse()
                        for subclasse in subclasses:
                            bot.get_subclasse_infos(subclasse=subclasse)
                            bot.add_infos()
                        bot.back_to_grupo()
                    bot.back_to_divisao()
                bot.back_to_secao()
            bot.access_main_page()

    ibge_results = bot.get_infos_table()

    c_excel = CreateExcel()
    c_excel.set_sheet_name()
    c_excel.set_headers()
    c_excel.write_lines(ibge_results)
    c_excel.save_excel()

    t_excel = TreatExcel()
    t_excel.lower_strings()
    t_excel.remove_accents()
    t_excel.remove_non_digits()
    t_excel.save_excel()
except BaseException as e:
    Utilities().register_log(e)