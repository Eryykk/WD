#lab3


#Zad3

zbA = [1 - x for x in range(1, 11)]
zbB = [4 ** x for x in range(8)]
zbC = [x for x in zbB if x % 2 == 0]
print('Zbior A',zbA)
print('Zbior B', zbB)
print('Zbior C', zbC)

#Zad3
spis = {"baton": "sztuka", "cukier": "kg", "bateria": "sztuka"}
lista = [key for key, value in spis.items() if value.count("sztuka")]
print(lista)