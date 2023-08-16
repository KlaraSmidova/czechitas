#cena listku a vyse slevy
number_of_tickets = int(input("Kolik si přejete lístků? "))
price_per_ticket = 190
total_price = number_of_tickets * price_per_ticket
if total_price >= 500:
    discount = 0.1
    total_price = total_price * (1 - discount)
    print(f"Získáváte slevu {discount * 100} %")
    print(type(total_price))
    total_price = int(total_price)
    print(type(total_price))

print(f"Celková cena nákupu je {total_price} Kč.")


#ziskani roku narozeni, oprava chyby
id_number = input("Zadejte rodné číslo: ")
year_of_birth = id_number[0] + id_number[1]
year_of_birth = int(year_of_birth)
if year_of_birth > 23: #povodne spatne zadene cislo 20, coz odpovidalo roku napsani 2020.
    year_of_birth = 1900 + year_of_birth
else:
    year_of_birth = 2000 + year_of_birth
print(f"Uživatel(ka) se narodil(a) v roce {year_of_birth}.")

#pridani hosta na seznam, kontrola prichozich
guest_list = ["Jirka", "Klára", "Natálie"]
new_guest = input("Zadej jmeno noveho hosta:")
guest_list.append(new_guest)
print(guest_list)
print(len(guest_list))
name_incoming_guest = input("Jmeno prichoziho:")
if name_incoming_guest in guest_list:
    print("Vitej!")
else:
    print("Bohuzel, nejsi zvan")

#seznam v seznamu
school_marks = [
    ["Jiří", 1, 4, 3, 2],
    ["Natálie", 2, 3, 4],
    ["Klára", 3, 2, 4, 1, 3]
]

print(f"První student(ka) v seznamu je {school_marks[0][0]}.")
print(f"Její/jeho poslední známka je {school_marks[0][-1]}.")

print(f"První student(ka) v seznamu je {school_marks[2][0]}.")
print(f"Její/jeho poslední známka je {school_marks[0][3]}.")

school_report = [
    ["Český jazyk", 1],
    ["Anglický jazyk", 1],
    ["Matematika", 1],
    ["Přírodopis", 2],
    ["Dějepis", 1],
    ["Fyzika", 2],
    ["Hudební výchova", 4],
    ["Výtvarná výchova", 2],
    ["Tělesná výchova", 3],
    ["Chemie", 4],
]

sum_of_marks = 0
for mark in school_report:
    sum_of_marks += mark[1]
print(sum_of_marks)
#average = sum_of_marks/len(school_report) #moje reseni, funguje
average = round(sum_of_marks / len(school_report), 2) #reseni s urcenim zaokrouchleni (round) na desetinne misto, to je ta dvojka na konci
print(f"prumer zaka je {average}")
    

pohyby = [1200, -250, -800, 540, 721, -613, -222]

""" Vypište v pořadí třetí pohyb z uvedeného seznamu.
Vypište všechny pohyby kromě prvních dvou.
Vypište kolik je všech pohybů dohromady.
Pomocí volání vhodných funkcí vypište nejvyšší a nejnižší pohyb.
Spočítejte celkový přírůstek na účtu za dané období. Pozor, že přírůstek může vyjít i záporný. """
print(pohyby[2])
print(pohyby[2:])
print(len(pohyby))
print(max(pohyby))
print(min(pohyby))
print(sum(pohyby))

""" Mějme proměnnou s, ve které předpokládáme uložený nějaký seznam. Sestavte v výraz (vzoreček), 
který spočítá průměrnou hodnotu v takovém seznamu. Otestujte jej na seznamech různých délek. """

s = [1200, -250, -800, 540, 721, -613, -222, 46, 234, 56]
print(f"prumerna hodnota seznamu je: {sum(s)/len(s)}")
print(f"rozpeti seznamu je: {max(s)-min(s)}")

""" Sestavte výraz, který vrátí číslo nacházející se přesně uprostřed v zadaném seznamu s. 
U seznamů liché délky je střed jasně definovaný, ovšem u seznamů sudé délky nám padne mezi dvě čísla. 
V takovém případě vyberte jako střed číslo blíže ke konci seznamu. """
stred = s[len(s) // 2]

print(f'stred {s} je {stred}')

""" Sestavte vzoreček, který vrátí číslo nacházející se přesně uprostřed v zadaném seznamu s. 
Tentokrát však u seznamů sudé délky vyberte jako střed číslo blíž k začátku seznamu. """
if len(s) % 2 == 0:  # je sudy
    index = len(s) // 2 - 1
else:
    index = len(s) // 2

stred = s[index]

print(f'stred {s} je {stred}')

print('martin'.upper())
print('  martin   '.strip())
print('po ut st čt pá'.split(' '))

print('+'.join(['1', '2', '3', '4']))
print('/'.join(['dokumenty', 'dapraha', 'python', 'priklady']))