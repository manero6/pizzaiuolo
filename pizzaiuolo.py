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
    print("\n+---- \033[1;31mPizz\033[1;37mai\033[1;32muolo\033[0;0m ----+")
    print("| Panetto da: \033[4;37m{}\033[0;0mg".format(panetto))
    print("| Totale panetti: \033[4;37m{}\033[0;0m".format(tot_panetti))
    print("| Impasto finale: \033[4;37m{:.1f}\033[0;0mg".format(impasto))
    print("| Farina totale: \033[4;37m{:.1f}\033[0;0mg".format(farina))
    print("| Acqua totale ({}% idrat.): \033[4;37m{:.1f}\033[0;0mml".format(idratazione, acqua))
    print("| {}% di sale: \033[4;37m{:.1f}\033[0;0mg".format(sale_perc, sale))
    print("| {}% di lievito: \033[4;37m{:.1f}\033[0;0mg".format(lievito_perc, lievito))
    print("+---- Biga al 45% ----+")
    print("| Acqua per la biga al 45%: \033[4;37m{:.1f}\033[0;0mml".format(biga45))
    print("| Acqua per completarla: \033[4;37m{:.1f}\033[0;0mml".format(post_biga45))
    print("+---- Biga al 50% ----+")
    print("| Acqua per la biga al 50%: \033[4;37m{:.1f}\033[0;0mml".format(biga50))
    print("| Acqua per completarla: \033[4;37m{:.1f}\033[0;0mml".format(post_biga50))
    print("+---- Biga al 55% ----+")
    print("| Acqua per la biga al 55%: \033[4;37m{:.1f}\033[0;0mml".format(biga55))
    print("| Acqua per completarla: \033[4;37m{:.1f}\033[0;0mml".format(post_biga55))
    print("+---- Poolish al 100% ----+")
    print("| Farina per il poolish: \033[4;37m{:.1f}\033[0;0mg".format(poolish))
    print("| Farina per completarlo: \033[4;37m{:.1f}\033[0;0mg".format(post_poolish))
    print("+---- \033[1;31mPizz\033[1;37mai\033[1;32muolo\033[0;0m ----+\n")

pizzaiuolo(int(input("Per un panetto da quanti grammi? ")),\
           int(input("Quanti panetti in totale? ")),\
           int(input("Quale idratazione in % (default 65%)?") or "65"),\
           int(input("Quanto sale in % (default 3%)? ") or "3"),\
           int(input("Quanto lievito in % (default 3%)? ") or "3"))