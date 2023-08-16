""" Napište program, který vylosuje náhodnou hrací kartu z 
klasické whistové sady obsahující 52 karet, 
rozdělených do čtyř barev (kříže, srdce, piky, káry), 
s hodnotami 2, 3, 4, 5, 6, 7, 8, 9, 10, 
J (kluk), Q (dáma), K (král), A (eso) """
import random
cislo = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "kluk", "dáma", "král", "eso"]
barva = ["kříže", "srdce", "piky", "káry"]
print(f"Karta je {random.choice(cislo)} {random.choice(barva)}")
