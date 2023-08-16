""" Napište program, který vylosuje seznam 4 náhodných hracích karet 
podobně jako v předchozím úkolu. Můžeme si představovat, 
že rozdáváme karty například v pokeru. Zatím pro jednoduchost 
nebudeme řešit, že se nám může nějaká karta v seznamu opakovat.

Vymyslete, jak budete vylosovanou kartu v seznamu reprezentovat. 
Vypište pak tento seznam na výstup.
Dále k tomuto seznamu vypište součet hodnot všech vylosovaných 
karet. Položme hodnotu karet J, Q a K rovnu deseti a eso rovnu 
jedné. """
import random

hodnoty = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'kluk', 'dama', 'kral', 'eso']
barvy = ['kříže', 'srdce', 'piky', 'káry']

soucet_hodnot = 0
for _ in range(4):
    hodnota = random.choice(hodnoty)
    barva = random.choice(barvy)
    print(f'{hodnota} - {barva}')
    if hodnota == 'kluk' or hodnota == 'dama' or hodnota == 'kral':
        soucet_hodnot += 10
    elif hodnota == 'eso':
        soucet_hodnot += 1
    else:
        soucet_hodnot += int(hodnota)
print(soucet_hodnot)