# Fonction donner la représentation d'un nombre decimal en une base quelconque
# Le résultat est représenté comme une liste des coefficients devant les puisssances successives de la base
from typing import List


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
        


if __name__ == "__main__":
    decimal_to_base(78, 2)
    signed_bin_to_binary(binary_to_signed_bin(decimal_to_base(78, 2)))
    print(0|1)