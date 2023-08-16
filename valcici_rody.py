"""Zadání příkladu
V rámci této lekce si vyzkoušíme vyřešit příklad, ve kterém využijeme koncepty, které jsme si ukazovali v předchozích lekcích.

Zadání příkazu je následující:

Ze souboru battles.tsv si načti informace o bitvách, které se odehrály ve knižní sérii Písně ohně a ledu, 
jejímž autorem je spisovatel George R. R. Martin a podle níž byl natočen slavný seriál Hra o trůny. 
Naším úkolem je ze zadaných dat zjistit následující:

Statistiku, kolikrát byl který rod v pozici útočníků. Výsledná data ulož do CSV souboru attackers.csv.
Pokud je zadaná síla obou armád (sloupce attacker_size a defender_size, indexy sloupců jsou 17 a 18), 
vytvoř seznam velitelů, kteří v boji porazili silnější armádu (vítěze poznáš podle sloupce attacker_outcome, 
který obsahuje hodnoty win a loss, platí vždy z pohledu útočníka). Kolik takových bitev je?"""

with open("battles.tsv", encoding="utf-8") as soubor:
    soubor = soubor.readlines()

ATTACKRS_COL_START = 5
ATTACKRS_COL_END = 8 
attackers = {}   

for radek in soubor[1:]:
        #print(radek)
    radek = radek.split("\t")
    attackers_line = radek[ATTACKRS_COL_START:ATTACKRS_COL_END + 1]
        
    for attacker in attackers_line:
        if attacker != '': #lze nahradit nize uvedenym
        #if attacker:
            #print(attacker)
            if attacker in attackers:
                attackers[attacker] = attackers[attacker] + 1
            else:
                attackers[attacker] = 1
with open('attackers.csv', mode='w', encoding='utf-8') as file_write:                    
    for attacker, count in attackers.items():
        print(f'{attacker},{count}', file=file_write)
