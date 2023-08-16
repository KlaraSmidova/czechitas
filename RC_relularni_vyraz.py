# Zadani - over zda se jedna o rodne cislo.

import re

reg_exp = re.compile(r'\d{9,10}')

rodna_cisla = ["1234567898", 
               "759834", 
               "ahoj"
               ]
for rodne_cislo in rodna_cisla:
    print(reg_exp.fullmatch(rodne_cislo))
