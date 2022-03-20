def pizzaiuolo(panetto, tot_panetti, idratazione, sale_perc, lievito_perc):
    unpercento = panetto * tot_panetti / (idratazione + 100 + sale_perc + lievito_perc)
    farina = unpercento * 100
    acqua = unpercento * idratazione
    sale = unpercento * sale_perc
    lievito = unpercento * lievito_perc
    impasto = farina + acqua + sale + lievito
    biga45 = unpercento * 45
    post_biga45 = unpercento * (idratazione - 45)
    biga50 = unpercento * 50
    post_biga50 = unpercento * (idratazione - 50)
    biga55 = unpercento * 55
    post_biga55 = unpercento * (idratazione - 55)
    poolish = acqua
    post_poolish = farina - acqua
    txt_result = "\033[4;37m" 
    txt_reset = "\033[0;0m"
    txt_pizzaiuolo = "\033[1;31mPizz\033[1;37mai\033[1;32muolo\033[0;0m"
    print("\n+---- {} ----+".format(txt_pizzaiuolo))
    print("| Panetto da: {}{}{}".format(txt_result, panetto, txt_reset))
    print("| Totale panetti: {}{}{}".format(txt_result, tot_panetti, txt_reset))
    print("| Impasto finale: {}{:.1f}{}g".format(txt_result, impasto, txt_reset))
    print("| Farina totale: {}{:.1f}{}g".format(txt_result, farina, txt_reset))
    print("| Acqua totale ({}% idrat.): {}{:.1f}{}ml".format(idratazione, txt_result, acqua, txt_reset))
    print("| {}% di sale: {}{:.1f}{}g".format(sale_perc, txt_result, sale, txt_reset))
    print("| {}% di lievito: {}{:.1f}{}g".format(lievito_perc, txt_result, lievito, txt_reset))
    print("+---- Biga al 45% ----+")
    print("| Acqua per la biga al 45%: {}{:.1f}{}ml".format(txt_result, biga45, txt_reset))
    print("| Acqua per completarla: {}{:.1f}{}ml".format(txt_result, post_biga45, txt_reset))
    print("+---- Biga al 50% ----+")
    print("| Acqua per la biga al 50%: {}{:.1f}{}ml".format(txt_result, biga50, txt_reset))
    print("| Acqua per completarla: {}{:.1f}{}ml".format(txt_result, post_biga50, txt_reset))
    print("+---- Biga al 55% ----+")
    print("| Acqua per la biga al 55%: {}{:.1f}{}ml".format(txt_result, biga55, txt_reset))
    print("| Acqua per completarla: {}{:.1f}{}ml".format(txt_result, post_biga55, txt_reset))
    print("+---- Poolish al 100% ----+")
    print("| Farina per il poolish: {}{:.1f}{}g".format(txt_result, poolish, txt_reset))
    print("| Farina per completarlo: {}{:.1f}{}g".format(txt_result, post_poolish, txt_reset))
    print("+---- {} ----+\n".format(txt_pizzaiuolo))

pizzaiuolo(int(input("Per un panetto da quanti grammi (default: 250)? ") or "250"),\
           int(input("Quanti panetti in totale (default: 4)? ") or "4"),\
           int(input("Quale idratazione in % (default: 65)? ") or "65"),\
           int(input("Quanto sale in % (default: 3)? ") or "3"),\
           int(input("Quanto lievito in % (default: 3)? ") or "3"))
