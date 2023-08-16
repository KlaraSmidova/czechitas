# vypis komponentu z www stranky

session = HTMLSession()
stranka = session.get('https://apps.kodim.cz/python-data/dhmo')
for odstavec in stranka.html.find('p'):
    print(odstavec.text)
    print()

for nadpis2 in stranka.html.find('h2'):
    print(nadpis2.text)
    print()  

for odkaz in stranka.html.find('a'):
    print(odkaz.attrs['href'])
    print()  

for obrazek in stranka.html.find('img'):
    print(obrazek.attrs['src'])
    print()
