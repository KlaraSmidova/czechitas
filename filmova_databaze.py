"""V tomto úkolu budeš pracovat s datasetem netflix_titles.tsv. Jedná se o textový soubor ve formátu TSV (Tabulator Separated Values), kde jsou jako oddělovače sloupců použity tabulátory (“\t”). Tvým úkolem bude soubor načíst, vytáhnout z něj některé údaje a uložit je ve formátu JSON.
Z každého řádku nás budou zajímat tyto údaje: 
PRIMARYTITLE (název),
DIRECTOR (režisér/režiséři),
CAST (herci),
GENRES (seznam žánrů),
STARTYEAR (rok vydani).
Údaje o filmech převeď do seznamu, kde bude každý film reprezentován jako slovník obsahující následující položky:
title (název filmu),
directors (seznam všech režisérů nebo prázdný seznam, pokud není režisér uveden),
cast (seznam všech herců nebo prázdný seznam, pokud není žádný herec uveden),
genres (seznam všech žánrů, do kterých byl film zařazen),
decade (dekáda, ve které film vznikl).
Protože formát TSV neumožňuje reprezentovat seznam, jsou herci a režiséři zadání jako jeden řetězec a jednotlivé hodnoty jsou oddělené čárkami. Ve formátu JSON použij pro větší přehlednost seznam, aby bylo například vidět, kolik herců nebo režisérů v seznamu je.
Může se stát, že film neobsahuje údaj o režisérech nebo hercích, ostatní jsou vždy uvedené.
Dekáda je vždy první rok desetiletí, např. rok 1987 patří do dekády 1980 a rok 2017 do dekády 2010.
Vytvořený seznam slovníků ulož do souboru movies.json."""

import json


filmy = []

with open("netflix_titles.tsv", "r", encoding="utf-8") as soubor:
    radek = soubor.readline().split("\t")
    ind_nazev = radek.index("PRIMARYTITLE")
    ind_reziser = radek.index("DIRECTOR")
    ind_herci = radek.index("CAST")
    ind_zanry = radek.index("GENRES")
    ind_rok = radek.index("STARTYEAR")
    
    for radek in soubor:
        rozdeleny_radek = radek.split("\t")
                
        titul = {}
        nazev = rozdeleny_radek[ind_nazev]
        reziser = rozdeleny_radek[ind_reziser]
        reziseri = reziser.split(", ")
        if reziseri == ['']:
           reziseri = []
        herci = rozdeleny_radek[ind_herci]
        herci = herci.split(", ")
        if herci == ['']:
           herci = []
        zanry = rozdeleny_radek[ind_zanry]
        zanry = zanry.split(", ")
        if zanry == ['']:
           zanry = []
        rok = rozdeleny_radek[ind_rok]
        dekada = int(rok)//10*10
        titul["title"] = nazev
        titul["directors"] = reziseri
        titul["cast"] = herci
        titul["genres"] = zanry
        titul["decade"] = dekada
        filmy.append(titul)

with open('movies.json', mode='w', encoding='utf-8') as file:
    json.dump(filmy, file, ensure_ascii=False, indent=4)
