def pizzaiuolo(panetto, tot_panetti, idratazione, sale_perc, lievito_perc):
    unpercento = panetto * tot_panetti / (idratazione + 100 + sale_perc + lievito_perc)
    farina = unpercento * 100
    acqua = unpercento * idratazione
    sale = unpercento * sale_perc
    lievito = unpercento * lievito_perc
    lievito_secco = lievito / 3
    impasto = farina + acqua + sale + lievito
    impasto_secco = farina + acqua + sale + (lievito / 3)
    panetto_secco = impasto_secco / tot_panetti
    #biga45 = unpercento * 45
    #post_biga45 = unpercento * (idratazione - 45)
    biga50 = unpercento * 50
    post_biga50 = unpercento * (idratazione - 50)
    #biga55 = unpercento * 55
    #post_biga55 = unpercento * (idratazione - 55)
    poolish = acqua
    post_poolish = farina - acqua
    # started from here: (100/5)+(60/3)+(100*4/5)+(60*2/3)
    biga_poolish_poolish = unpercento * (idratazione - 50) * 2
    biga_poolish_biga = unpercento * (100 - idratazione) * 2
    biga_poolish_biga_acqua = unpercento * (100 - idratazione)
    #farina_perc = 100, 95, 90, 85, 80, 75, 70, 66, 60, 50, 40, 33, 30, 25, 20, 15, 10, 5, 1
    farina_perc = 99, 98, 95, 90, 85, 80, 75, 70, 66, 60, 50
    txt_result = "\033[4;37m"
    txt_reset = "\033[0;0m"
    txt_pizzaiuolo = "\033[1;31mPizz\033[1;37mai\033[1;32muolo\033[0;0m"
    print()
    print("+----> {} <----+".format(txt_pizzaiuolo))
    print("| Panetto da: {}{}{}g".format(txt_result, panetto, txt_reset))
    print("| Totale panetti: {}{}{}".format(txt_result, tot_panetti, txt_reset))
    print("| Farina totale: {}{:.1f}{}g".format(txt_result, farina, txt_reset))
    print("| Acqua totale ({}{}{}% idrat.): {}{:.1f}{}ml".format(txt_result, idratazione, txt_reset, txt_result, acqua, txt_reset))
    print("| {}% di sale: {}{:.1f}{}g".format(sale_perc, txt_result, sale, txt_reset))
    print("| {}% di lievito fresco: {}{:.1f}{}g".format(lievito_perc, txt_result, lievito, txt_reset))
    print("| Impasto finale con lievito fresco: {}{:.1f}{}g".format(txt_result, impasto, txt_reset))
    print("|")
    print("| 1/3 del lievito: {}{:.1f}{}g".format(txt_result, lievito_secco, txt_reset))
    print("| Impasto finale con lievito secco: {}{:.1f}{}g".format(txt_result, impasto_secco, txt_reset))
    print("| Panetto con lievito secco: {}{:.1f}{}g".format(txt_result, panetto_secco, txt_reset))
    print("|")
    #print("+----> Biga al 45% <----+")
    #print("| Acqua per la biga al 45%: {}{:.1f}{}ml".format(txt_result, biga45, txt_reset))
    #print("| Acqua da aggiungere: {}{:.1f}{}ml".format(txt_result, post_biga45, txt_reset))
    #print("|")
    print("+----> Biga al 50% <----+")
    print("| Acqua per la biga: {}{:.1f}{}ml".format(txt_result, biga50, txt_reset))
    print("| Acqua da aggiungere: {}{:.1f}{}ml".format(txt_result, post_biga50, txt_reset))
    print("|")
    #print("+----> Biga al 55% <----+")
    #print("| Acqua per la biga al 55%: {}{:.1f}{}ml".format(txt_result, biga55, txt_reset))
    #print("| Acqua da aggiungere: {}{:.1f}{}ml".format(txt_result, post_biga55, txt_reset))
    #print("|")
    print("+----> Poolish al 100% <----+")
    print("| Farina per il poolish: {}{:.1f}{}g".format(txt_result, poolish, txt_reset))
    print("| Farina da aggiungere: {}{:.1f}{}g".format(txt_result, post_poolish, txt_reset))
    print("|")
    print("+----> Poolish al 100% + Biga al 50% <----+")
    print("| Farina per il Poolish: {}{:.1f}{}g".format(txt_result, biga_poolish_poolish, txt_reset))
    print("| Acqua per il Poolish: {}{:.1f}{}ml".format(txt_result, biga_poolish_poolish, txt_reset))
    print("| Farina per la biga: {}{:.1f}{}g".format(txt_result, biga_poolish_biga, txt_reset))
    print("| Acqua per la biga: {}{:.1f}{}g".format(txt_result, biga_poolish_biga_acqua, txt_reset))
    print("|")
    print("+----> Farina in % <----+")
    for perc in farina_perc:
        calcolo_perc = farina * perc / 100
        print("| {:>3}%: {}{:.1f}{}".format(perc, txt_result, calcolo_perc, txt_reset), end=" ")
        perc = 100 - perc
        calcolo_perc = farina * perc / 100
        print("    {:>3}%: {}{:.1f}{}".format(perc, txt_result, calcolo_perc, txt_reset))
    print("|")
    print("+----> {} <----+".format(txt_pizzaiuolo))
    print()

#thanks figlet ;)
print("\033[0;31m                   \033[0;37m         \033[0;32m             _       \033[0;0m")
print("\033[0;31m      o            \033[0;37m      o  \033[0;32m            | |      \033[0;0m")
print("\033[0;31m   _      __   __  \033[0;37m __,     \033[0;32m        __  | |  __  \033[0;0m")
print("\033[0;31m |/ \_|  / / _/ / _\033[0;37m/  |  |  \033[0;32m|   |  /  \_|/  /  \_\033[0;0m")
print("\033[0;31m |__/ |_/ /_/  /_/ \033[0;37m\_/|_/|_/\033[0;32m \_/|_/\__/ |__/\__/ \033[0;0m")
print("\033[0;31m/|         /|   /| \033[0;37m         \033[0;32m                     \033[0;0m")
print("\033[0;31m\|         \|   \| \033[0;37m         \033[0;32m                     \033[0;0m")
print()
 
pizzaiuolo(int(input("Per un panetto da quanti grammi (default: 250)? ") or "250"),
           int(input("Quanti panetti in totale (default: 4)? ") or "4"),
           int(input("Quale % di idratazione (default: 65)? ") or "65"),
           int(input("Quale % di sale sulla farina (default: 3)? ") or "3"),
           float(input("Quale % di lievito sulla farina (default: 0.5)? ") or "0.5"))
