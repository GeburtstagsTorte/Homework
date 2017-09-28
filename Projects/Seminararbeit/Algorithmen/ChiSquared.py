

def chi_squared(observed, expected):
    if len(observed) != len(expected):
        raise Exception('Error: length of observed set unequals length of expected set.')
    else:
        delta_list = []
        for i in range(len(observed)):
            delta_list.append((observed[i] - expected[i]) ** 2)

        for j in range(len(delta_list)):
            delta_list[j] /= expected[j]
        # print(delta_list)
        return sum(delta_list)


def ChiVerteilung(beobachtet, erwartet):
    """
    :param beobachtet: eine Liste von den beobachteten Werten
    :param erwartet:  eine Liste von den erwarteten Werten
    :return: Chi-Wert
    """
    if len(beobachtet) != len(erwartet):
        raise Exception("Error: die Laenge der Listen "
                        "stimmen nicht ueberein!")
        # Ueberpruefung, ob jeder beobachtete Wert auch
    else:
        delta_liste = []
        # Deklarierung einer leeren Liste in dem die einzelnen Werte
        # gespeichert werden
        for i in range(len(beobachtet)):
            # zu jeder Liste wird die quadrierte Differenz zwischen
            # beobachtet und erwartet hinzugefuegt
            delta_liste.append((beobachtet[i] - erwartet[i]) ** 2)

        for j in range(len(delta_liste)):
            # jeder Wert in der Liste wird durch den jeweiligen
            # Erwartungswert geteilt
            delta_liste[j] /= erwartet[j]

        # Gibt die Summe, also den Chi-Quadrat Wert zurueck

        return sum(delta_liste)


def interface(obs, exp):
    for i in range(len(obs)):
        print(str(i) + " occurred " + str(obs[i]) + " times.")
    print()
    print("Chi-Squared method got " + str(chi_squared(obs, exp)) + " for the given numbers.")


def main_chi(n, r):

    obs = [99965, 100008, 100018, 99960, 100020, 99976, 100014, 99976, 100087, 99976]
    exp = [n//r for _ in range(10)]

    interface(obs, exp)

if __name__ == '__main__':
    main_chi(n=1000000, r=10)
