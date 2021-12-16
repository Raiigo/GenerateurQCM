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
        coef = round(number//pow(base, i))
        number = number - coef * pow(base, i)
        coef_list.append(coef)

    print(coef_list)

if __name__ == "__main__":
    decimal_to_base(10, 2)
    print("")