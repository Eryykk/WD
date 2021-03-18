#zadanie1
datainput = input(u"Wpisz dowolny tekst zawierający litere 'a' : ")
datacount = datainput.count("a") + datainput.count("A")
print(u"Litery 'a' uzyles:", datacount, "razy.")

#zadanie2
import sys as system
system.stdout.write(u"Wpisz liczbę całkowitą 'a': ")
rla = system.stdin.readline()

system.stdout.write(u"Wpisz liczbę całkowitą 'b': ")
rlb = system.stdin.readline()

system.stdout.write(u"Wpisz liczbę całkowitą 'c': ")
rlc = system.stdin.readline()

result = (int(rla) ** int(rlb) + int(rlc))
print(u"Wynik: ", result)