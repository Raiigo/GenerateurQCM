import random

#DECIMAL vers BINAIRE

titre = "** Conversion decimal vers binaire **"
print ("*" * len(titre))
print (titre)
print ("*" * len(titre))

score = 0
total = 0

nbr = random.randint(0, 1000)
print("Voici le nombre decimal qu'on va convertir en binaire:", nbr)

a = random.randint(0, 1000)
a = bin(a)
a = a[2::]

b = random.randint(0, 1000)
b = bin(b)
b = b[2::]

c = random.randint(0, 1000)
c = bin(c)
c = c[2::]

d = bin(nbr)
d = d[2::]

liste = [a, b, c, d]

random.shuffle(liste)

print("Voici les 4 proposition:")
print(liste[0])
print(liste[1])
print(liste[2])
print(liste[3])


reponse = input("Entrer une des 4 valeur afficher: ")

if reponse == d:
    print("Vrai")
    score = score + 1
    total = total + 1
else:
    print("Faux")
    total = total + 1

#BINAIRE vers DECIMAL

print(int(input('Entrez un nombre binaire:'),2))

#DECIMAL vers OCTAL

titre = "** Conversion decimal vers octal **"
print ("*" * len(titre))
print (titre)
print ("*" * len(titre))

score = 0
total = 0

nbr = random.randint(0, 1000)
print("Voici le nombre decimal qu'on va convertir en octal:", nbr)

a = random.randint(0, 1000)
a = oct(a)
a = a[2::]

b = random.randint(0, 1000)
b = oct(b)
b = b[2::]

c = random.randint(0, 1000)
c = oct(c)
c = c[2::]

d = oct(nbr)
d = d[2::]


liste = [a, b, c, d]


random.shuffle(liste)

print("Voici les 4 proposition:")
print(liste[0])
print(liste[1])
print(liste[2])
print(liste[3])


reponse = input("Entrer une des 4 valeur afficher: ")

if reponse == d:
    print("Vrai")
    score = score + 1
    total = total + 1
else:
    print("Faux")
    total = total + 1

#OCTAL vers DECIMAL

print(int(input('Entrez un nombre octal:'),8))

#DECIMAL vers HEXADECIMAL

titre = "** Conversion decimal vers hexadecimal **"
print ("*" * len(titre))
print (titre)
print ("*" * len(titre))

score = 0
total = 0

nbr = random.randint(0, 1000)
print("Voici le nombre decimal qu'on va convertir en hexadecimal:", nbr)

a = random.randint(0, 1000)
a = hex(a)
a = a[2::]

b = random.randint(0, 1000)
b = hex(b)
b = b[2::]

c = random.randint(0, 1000)
c = hex(c)
c = c[2::]

d = hex(nbr)
d = d[2::]


liste = [a, b, c, d]


random.shuffle(liste)

print("Voici les 4 proposition:")
print(liste[0])
print(liste[1])
print(liste[2])
print(liste[3])


reponse = input("Entrer une des 4 valeur afficher: ")

if reponse == d:
    print("Vrai")
    score = score + 1
    total = total + 1
else:
    print("Faux")
    total = total + 1

#HEXADECIMAL vers DECIMAL

print(int(input('Entrez un nombre hexadécimal:'),16))

#BINAIRE vers C2

a = int(input('Entrez un nombre binaire:'),2)
print("{0:{fill}8b}".format(a%256, fill='0'))

#C2 vers BINAIRE



#FLOTTANTS vers IEEE-754

import struct

getBin = lambda x: x > 0 and str(bin(x))[2:] or "-" + str(bin(x))[3:]

def floatToBinary64(value):
    val = struct.unpack('Q', struct.pack('d', value))[0]
    return getBin(val)

def binaryToFloat(value):
    hx = hex(int(value, 2))
    return struct.unpack("d", struct.pack("q", int(hx, 16)))[0]


a = float(input("Rentrer un flottants: "))
binstr = floatToBinary64(a)
print(binstr)

#IEEE-754 vers FLOTTANTS

