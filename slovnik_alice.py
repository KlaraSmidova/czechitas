"""Napiš skript v Pythonu, který otevře soubor alice.txt (Alice’s Adventures in Wonderland od Lewise Carrolla) - ke stažení v [1] a spočítá četnost všech znaků:

velká písmena považuj za malá
ignoruj mezery a znaky nového řádku

Jako výstup musí program vytvořit soubor ukol1_output.json, který by měl být shodný se vzorovým výstupem ukol1_output_vzor.json (také v [1]). (VS Code má funkcionalitu na porovnání souborů)

soubor ukol1_output.json je ve formátu JSON
obsahuje slovník, kde klíče jsou znaky a hodnoty jejich četnost
volitelně: slovník je seřazen podle klíčů"""

import json
seznam_znaku = []
with open("alice.txt", encoding='utf-8') as file:
    data = file.read().lower().replace(' ', '').replace('\n','')
    for znak in data:
        if znak not in seznam_znaku:
            seznam_znaku.append(znak)
slovnik = {}
for pismeno in seznam_znaku:
    slovnik[pismeno] = data.count(pismeno)
with open('ukol1_output.json', mode='w', encoding='utf-8') as file:
    json.dump(slovnik, file, sort_keys=True, ensure_ascii=False, indent=2)
