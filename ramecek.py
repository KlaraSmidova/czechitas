# vytvor funkci pro vytvoreni ramecku kolem vybraneho slova

def ramecek (text,znak = '*'):
    #funkce ramecek
   
    cara = ( len(text)+4 )*znak
    print(cara)
    
    print(znak,text,znak)
    print (cara)


ramecek("ahoj")
print ()
ramecek("cau",znak= '-')
