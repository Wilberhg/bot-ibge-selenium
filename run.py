from ibge.ibge import Ibge

with Ibge() as bot:
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
    ...