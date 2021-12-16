import math
from os import truncate
from typing import List
from math import *

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
        print("La base se doit d'être un entier positif supérieur à 1")
    higher_power = 0
    for i in range(0, 10): # Determine la plus grande puissance de la base necessaire
        if pow(base, i) > number:
            higher_power = i - 1
            break
    print(higher_power)
    power_list = []
    for i in range(0, higher_power + 1):
        power_list.append(i)
    power_list.reverse()
    print(power_list)
    coef_list = []
    for i in power_list:
        coef = round(number//pow(base, i)) # On récupère trivialement le coefficient de la puissance
        number = number - coef * pow(base, i)
        coef_list.append(coef)

    print(coef_list)
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
    print(opposite)
    retenue = 1
    for i in reversed(range(0, len(opposite))): # Ici on applique une porte XOR sur chaque bit en prenant soin de retenir la retenue potentiel sur laquel on appliquera une porte OR, voir "addition binaire"
        print(str(opposite[i]) + " + " + str(retenue))
        bit_buffer = opposite[i]
        opposite[i] = opposite[i] ^ retenue
        if bit_buffer + retenue == 2:
            retenue = 1
        else:
            retenue = 0
        print(opposite)

    print(opposite)
    return opposite

def signed_bin_to_binary(number: List):
    bin_buffer = []
    for i in range(1, len(number)):
        bin_buffer.append(number[i])
    print(bin_buffer)
    binary = []
    for i in bin_buffer: # On applique une porte NOT sur chaque bit
        if i == 0:
            binary.append(1)
        if i == 1:
            binary.append(0)
    print(binary)
    retenue = 1
    for i in reversed(range(0, len(binary))): # ADD
        print(str(binary[i]) + " + " + str(retenue))
        bit_buffer = binary[i]
        binary[i] = binary[i] ^ retenue
        if bit_buffer + retenue == 2:
            retenue = 1
        else:
            retenue = 0
        print(binary)

def signed_int_to_IEEE_754(number: float):
    sign = 0
    if number < 0:
        sign = 1
    else:
        sign = 0
    decimal_whole_part = int(number)
    exponent = log(decimal_whole_part, 2) + 127 # Formule trivial déduite avec quelques manipulations algébrique aisées
    mantissa_value = number/(pow(2, int(exponent - 127)))
    print(int(exponent))
    print(mantissa_value)
    n = mantissa_value * pow(2, 23)
    q = n
    mantissa = []
    while q != 1:
        print(str(q) + " // 2")
        print(str(math.ceil(q%2)))
        if math.ceil(q%2) == 0:
            mantissa.append(0)
        for i in range(0, math.ceil(q%2)):
            mantissa.append(1)
        q = q // 2
    mantissa.reverse()
    print(mantissa)
    binary_exponent = decimal_to_base(int(exponent), 2)
    result = [sign] + binary_exponent + mantissa
    print(result)
    return result

def IEEE_754_to_signed_int(number: List):
    sign = 1
    if number[0] == 0:
        sign = 1
    else:
        sign = -1

    binary_exponent = number[1:9]
    print(binary_exponent)
    exponent_pow_2 = pow(2, binary_to_decimal(binary_exponent) - 127)
    print(exponent_pow_2)
    binary_mantisse = number[8:32]
    print(binary_mantisse)
    mantisse = binary_mantisse_to_decimal(binary_mantisse)
    print(mantisse)
    result = sign * exponent_pow_2 * mantisse
    print(result)
    return result




if __name__ == "__main__":
    # decimal_to_base(78, 2)
    # signed_bin_to_binary(binary_to_signed_bin(decimal_to_base(78, 2)))
    # binary_to_signed_bin([0, 1, 1, 1, 0, 1])
    # signed_bin_to_binary(binary_to_signed_bin([0, 1, 1, 1, 0, 1]))
    signed_int_to_IEEE_754(89)
    print(binary_to_decimal([1, 0, 1, 0]))
    print(binary_mantisse_to_decimal([1, 0, 1]))
    IEEE_754_to_signed_int([0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    binary_mantisse_to_decimal([0, 1, 1, 0, 0, 1, 0])
    print("")