"""
- Das Inkrement c ist vom Modul m teilerfremd
- Jeder Primfaktor von m teilt a-1
- Wenn m ein vielfaches von 4 ist, dann auch  a-1
"""


def gcd(a, b):
    """
    :param a: Zahl 
    :param b: Zahl
    :return: groesster gemeinsamer Teiler
             eng: greatest common divisor
    """
    while b:
        a, b = b, a % b
    return a


def lesePrimzahlen(file_name):
    """
    :param file_name: der Name der Textdatei
    :return: alle Primzahlen bis 2**16
    diese Funktion importiert die zuvor generierten 
    Primzahlen aus einer Textdatei in das Programm
    
    """
    with open(file_name, 'r') as f:
        Primzahlen = f.read().split(", ")
        # Nachdem die Primzahlen in der Textdatei
        # von einem Komma getrennt sind, werden 
        # alle Kommas von den Zahlen entfernt
        # und in eine Liste gespeichert

    if Primzahlen[len(Primzahlen) - 1] == "":
        del Primzahlen[len(Primzahlen) - 1]
        # Durch die Generierung endet die letzte
        # Zahl auch mit einem Komma, wodurch 
        # in der Liste ein leerer Platz am Ende 
        # gespeichert wird, dieser wird hier entfernt.

    return Primzahlen
    # Zurueck geben der Liste, damit andere Funktionen 
    # diese Verwenden koennen
    # Dabei zu beachten ist, dass jede Zahl in der Liste 
    # durch das Lesen ein string-Typ ist, mit dem der Computer
    # nicht rechnen kann.

def PrimfaktorZerlegung(n):
    """
    :param n: Die Zahl, von der man die Primfaktoren braucht
    :return:  Liste mit jedem einzigartigen Primfaktor
    """
    faktoren = []
    # Definierung einer leeren Liste
    Primzahlen = lesePrimzahlen("Primzahlen.txt")
    # Aufrufen der Funktion lesePrimzahlen(), um alle 
    # notwendigen Primzahlen zu erhalten.
    
    for i in range(len(Primzahlen)):
        if n % int(Primzahlen[i]) == 0:
            # Falls n modulo jeder Primzahl = 0, also 
            # wenn die Primzahl in die Zahl passt
            faktoren.append(int(Primzahlen[i]))
            # speichere diese in die Liste der Faktoren
            n //= int(Primzahlen[i])
            # teile die Zahl durch die Primzahl
    
    # Zu beachten ist, dass bei einer Primfaktor Zerlegung
    # Zahlen haeufiger auftreten koennen. Dies ist hier fuer
    # diese Anwendung allerdings nicht notwendig, weshalb 
    # sie nur einzelnd in die Liste gespeichert werden.
    return faktoren


def FindeParameter(m):
    """
    :param m: Das Modul
    :return: alle moeglichen Belegungen fuer die
            Parameter a, b unter Beruecksichtigung des Moduls
    """
    c_list = []
    a_list = []
    # Deklarierung leerer Listen
    faktoren = PrimfaktorZerlegung(m)
    # Aufrufen der Funktion PrimfaktorZerlegung(), um
    # die noetigen Primfaktoren zu erhalten
    # Anmerkung: Weil 2 hoch 16 eine gerade Zahl ist,
    # wird der einzige Primfaktor hier 2 sein
    for c in range(1, m):
        if gcd(c, m) == 1:
            # wenn der groesste gemeinsame Teiler 1 ist,
            # c und m also teilerfremd sind
            c_list.append(c)
            # fuege c zur Liste der moeglichen c's hinzu

    for a in range(1, m):
        if m % 4 == 0 and (a - 1) % 4 == 0:
            # Falls m ein vielfaches von 4 und
            # a - 1 ein vielfaches von 4
            for j in range(len(faktoren)):
                # teste, ob jeder Primfaktor von m
                # a-1 teilt
                if not (a-1) % faktoren[j] == 0:
                    break
                    # wenn nicht ueberspringe die Zahl
                if j == len(faktoren)-1:
                    a_list.append(a)
            # Hinzufuegen der bestandenen a's"

    return a_list, c_list


def main(show=False):
    # for m in range(n, e+1):
    m = 2**16
    parameters = FindeParameter(m)

    print("m as modulo: m={}".format(m), end='\n')
    print("possible parameters for a: (total number of a parameter: {})".format(len(parameters[0])), end="\n")
    if show:
        for i in range(len(parameters[0])):
            if i % 10 == 0:
                print()
            print("{}".format(parameters[0][i]), end=", ")
        print()
    print("possible parameters for c: (total number of c parameter: {})".format(len(parameters[1])), end="\n")
    if show:
        for i in range(len(parameters[0])):
            if i % 10 == 0:
                print()
            print("{}".format(parameters[1][i]), end=", ")
        print()
    print("----------------------")

if __name__ == '__main__':
    n = 100
    e = 2**16 - 1
    main()
