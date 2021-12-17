import math
from os import truncate
from typing import List
from math import *
import random

def binary_to_decimal(number: List):
    number.reverse()
    result = 0
    for i in range(0, len(number)):
        result = result + number[i] * pow(2, i)
    return result

def binary_mantisse_to_decimal(number: List):
    result = 0.0
    for i in range(0, len(number)):
        result = result + float(number[i]) * float(pow(2, -i))
    return result

# Fonction donner la représentation d'un nombre decimal en une base quelconque
# Le résultat est représenté comme une liste des coefficients devant les puisssances successives de la base
def decimal_to_base(number: int, base: int):
    if base < 1: # Python ne permet pas de réstreindre le type des paramètres, les annotations servant uniquement à l'interpréteur et au linter, une vérification est donc necessaire
        return
    higher_power = 0
    for i in range(0, 10): # Determine la plus grande puissance de la base necessaire
        if pow(base, i) > number:
            higher_power = i - 1
            break
    power_list = []
    for i in range(0, higher_power + 1):
        power_list.append(i)
    power_list.reverse()
    coef_list = []
    for i in power_list:
        coef = round(number//pow(base, i)) # On récupère trivialement le coefficient de la puissance
        number = number - coef * pow(base, i)
        coef_list.append(coef)

    return coef_list


def binary_to_signed_bin(number: List): # Ici on représente le nombre binaire sous la forme d'une liste des coefficients des puissances successives de la base
    opposite_buffer = number
    opposite = [0]
    for i in opposite_buffer:
        opposite.append(i)
    opposite_buffer = opposite
    opposite = []
    for i in opposite_buffer: # On applique une porte NOT sur chaque bit
        if i == 0:
            opposite.append(1)
        if i == 1:
            opposite.append(0)
    retenue = 1
    for i in reversed(range(0, len(opposite))): # Ici on applique une porte XOR sur chaque bit en prenant soin de retenir la retenue potentiel sur laquel on appliquera une porte OR, voir "addition binaire"
        bit_buffer = opposite[i]
        opposite[i] = opposite[i] ^ retenue
        if bit_buffer + retenue == 2:
            retenue = 1
        else:
            retenue = 0

    opposite = opposite[1:len(opposite)]
    return opposite

def signed_bin_to_binary(number: List):
    bin_buffer = []
    for i in range(1, len(number)):
        bin_buffer.append(number[i])
    binary = []
    for i in bin_buffer: # On applique une porte NOT sur chaque bit
        if i == 0:
            binary.append(1)
        if i == 1:
            binary.append(0)
    retenue = 1
    for i in reversed(range(0, len(binary))): # ADD
        bit_buffer = binary[i]
        binary[i] = binary[i] ^ retenue
        if bit_buffer + retenue == 2:
            retenue = 1
        else:
            retenue = 0

    return binary

def signed_int_to_IEEE_754(number: float):
    sign = 0
    if number < 0:
        sign = 1
    else:
        sign = 0
    decimal_whole_part = int(number)
    exponent = log(decimal_whole_part, 2) + 127 # Formule trivial déduite avec quelques manipulations algébrique aisées
    mantissa_value = number/(pow(2, int(exponent - 127)))
    n = mantissa_value * pow(2, 23)
    q = n
    mantissa = []
    while q != 1:
        if math.ceil(q%2) == 0:
            mantissa.append(0)
        for i in range(0, math.ceil(q%2)):
            mantissa.append(1)
        q = q // 2
    mantissa.reverse()
    binary_exponent = decimal_to_base(int(exponent), 2)
    result = [sign] + binary_exponent + mantissa
    return result

def IEEE_754_to_signed_int(number: List):
    sign = 1
    if number[0] == 0:
        sign = 1
    else:
        sign = -1

    binary_exponent = number[1:9]
    exponent_pow_2 = pow(2, binary_to_decimal(binary_exponent) - 127)
    binary_mantisse = number[8:32]
    mantisse = binary_mantisse_to_decimal(binary_mantisse)
    result = sign * exponent_pow_2 * mantisse
    return result




if __name__ == "__main__":
    # decimal_to_base(78, 2)
    # signed_bin_to_binary(binary_to_signed_bin(decimal_to_base(78, 2)))
    # binary_to_signed_bin([0, 1, 1, 1, 0, 1])
    # signed_bin_to_binary(binary_to_signed_bin([0, 1, 1, 1, 0, 1]))
    # signed_int_to_IEEE_754(12.89)
    # print(binary_to_decimal([1, 0, 1, 0]))
    # print(binary_mantisse_to_decimal([1, 0, 1]))
    # IEEE_754_to_signed_int([0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    # binary_mantisse_to_decimal([0, 1, 1, 0, 0, 1, 0])
    print("1 pour des questions aléatoires")
    response = str(input())
    if response == "1":
        question = random.randint(1, 5)
        if question == 1: # Decimal -> base quelconque
            decimal = random.randint(1, 1000)
            base = random.randint(2, 20)
            solution = decimal_to_base(decimal, base)
            print("Donnez les coefficients des puissances successives de " + str(base) + " (séparée par des ',') afin de représenter le nombre " + str(decimal) + " en base " + str(base))
            response = str(input())
            response = response.replace(" ", "")
            response = response.split(",")
            response_buffer = response
            response = []
            for i in response_buffer:
                i.replace(",", "")
                print(i)
                response.append(int(i))
            if response == solution:
                print("Bravo !")
            else:
                print("Raté")

        if question == 2: # Binaire -> C2
            binary = []
            for _ in range(0, 8):
                binary.append(random.randint(0, 1))
            solution = binary_to_signed_bin(binary)
            print("Représentez le nombre binaire " + str(binary) + " en compléments à 2 (séparer chaque coefficient par une ',')")
            response = str(input())
            response = response.replace(" ", "")
            response = response.split(",")
            response_buffer = response
            response = []
            for i in response_buffer:
                i.replace(",", "")
                print(i)
                response.append(int(i))
            if response == solution:
                print("Bravo !")
            else:
                print("Raté")

        if question == 3: # C2 -> Binaire
            binary = []
            for _ in range(0, 8):
                binary.append(random.randint(0, 1))
            solution = signed_bin_to_binary(binary)
            print("Représentez le nombre binaire ayant pour complément à deux " + str(binary) + " (séparer chaque coefficient par une ',')")
            response = str(input())
            response = response.replace(" ", "")
            response = response.split(",")
            response_buffer = response
            response = []
            for i in response_buffer:
                i.replace(",", "")
                print(i)
                response.append(int(i))
            if response == solution:
                print("Bravo !")
            else:
                print("Raté")

        if question == 4: # float -> IEEE-754
            entiere = random.randint(-125, 125)
            virgule = random.randint(10000, 10000)
            number = float(str(entiere) + "." + str(virgule))
            solution = signed_int_to_IEEE_754(number)
            print("Indiquez le nombre au format IEEE-754 représentant " + str(number) + " (séparer chaque coefficient par une ',')")
            response = str(input())
            response = response.replace(" ", "")
            response = response.split(",")
            response_buffer = response
            response = []
            for i in response_buffer:
                i.replace(",", "")
                print(i)
                response.append(int(i))
            if response == solution:
                print("Bravo !")
            else:
                print("Raté")

        if question == 5: # IEEE-754 -> float
            binary = []
            for _ in range(0, 32):
                binary.append(random.randint(0, 1))
            solution = str(IEEE_754_to_signed_int(binary))[0:6]
            print(solution)
            print("Indiquez la valeur decimal du nombre " + str(binary) + " représentez avec le format IEEE-754 (6 caractères au total)")
            result = str(input())
            if result == solution:
                print("Bravo !")
            else:
                print("Raté")
    else:
        print("Entrez un nombre valide")
    