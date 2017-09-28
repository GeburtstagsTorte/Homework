class Zufall:

    """
    Wahl der Namen der Funktionen nach Informatikstandards
    random: (eng. Zufall) Zahl zwischen 0 und 1
    randint: kurz fuer random integer: ganzzahlige Zahlen
    """

    def __init__(self, seed):
        """
        :param seed: der Startwert, wird beim Initialisieren
                     der Klasse festgelegt.

        Deise Funktion wird jedesmal, beim Erstellen eines
        neuen Objektes aus der Klasse Random aufgerufen
        """
        self.x = seed

    def random(self, a, c, m):
        """
        :param a: der Faktor
        :param c: das Inkrement
        :param m: das Modul
        :return: den neuen Wert der Sequenz

        In dieser Funktion werden Zahlen groesser gleich 0
        und kleiner 1 generiert.
        """
        self.x = (a * self.x + c) % m
        # Benutzen der Formel der Arbeit in einer Zeile

        return float(self.x / m)
        # Teilen des Wertes durch m, um Werte < 1 zu erhalten
        # float() ist in Python nicht zwingend noetig, zur
        # Sicherheit wird der Wert dennoch konvertiert

    def randint(self, start, ende, a, c, m):
        """
        :param start: Startwert
        :param ende: Endwert
        :return: Zufaellige ganzzahlige Zahl im Intervall
                [Startwert; Endwert]
        """
        ende += 1
        # ende + 1, um Endwert erreichen zu koennen
        # denn python rundet ab.
        x = int(self.random(a, c, m) * (ende-start)) + start
        # Konvertieren des Zufallswerts und die Differenz, um
        # spaeter auch ein ganzzahliges Ergebnis zu erhalten.
        #
        # Addieren des Staatwertes um ein Minimum zu erhalten
        # Differenz, um zwischen beiden Werten eine Zahl zu
        # erhalten. Durch int() wird die Zahl gerundet.
        if x > ende:
            # Sicherheitsmassnahme
            return ende
        return x
        # Zurueckgeben der neuen Zahl


def main(a, c, m, x, n, length):
    """a = 10061
    c = 1
    m = 2**16
    x = 54
    n = 1000000"""
    Rand = Zufall(x)
    # Erstellen eines Zufallsobjekts
    total = [0 for _ in range(length)]
    # Erstellen eines Arrays, in dem die Summen
    # der einzelnen Zahlen gespeichert werden
    str_text = "Random number generator seeded with "

    print(str_text + str(x))
    print("a={}, c={}, m ={}".format(a, c, m))

    for _ in range(n):
        total[Rand.randint(0, length-1, a, c, m)] += 1
        # Das jeweilige Element des Arrays, welches
        # als Summe dient um 1 erhoehen

    # Erstellen eines Outputs
    print("-" * (len(str_text) + len(str(x))), end="\n")
    print()
    for i in range(len(total)):
        print("{}: {}".format(i, total[i]))
    print()
    print("-" * (len(str_text) + len(str(x))), end="\n")


def main2(a, c, m, x, n, start, end):
    Rand = Zufall(x)
    lst = [Rand.randint(start, end, a, c, m) for i in range(n)]

    for i in range(len(lst)):
        if i % 20 == 0:
            print()
        print(str(lst[i]), end=", ")

if __name__ == '__main__':
    main(10061, 1, 2**16, 54, 1000000, 10)
