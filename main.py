from division import division
from addition import addition
from soustraction import soustraction
from multiplication import multiplication

nombre1, operateur, nombre2 = float(input("Entre un premier nombre : ")), input("choisis ton opérateur de calcul : "), float(input("Entre un deuxième nombre : "))

if operateur == "/":
    print(division(nombre1,nombre2))
elif operateur == "+":
    print(addition(nombre1,nombre2))
elif operateur == "-":
    print(soustraction(nombre1,nombre2))
elif operateur == "*":
    print(multiplication(nombre1,nombre2))
else:
    print("Erreur d'opérateur")