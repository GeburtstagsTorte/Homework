# definition of randomness


def generate_sequence(n):
    """
    :param n: length of sequence; integer type
    :return: sequence of alternating 0 and 1
            example:
                    n = 7
                    output -> 0101010
    """
    seq = ""
    switch = False

    for i in range(n):
        seq += str(int(switch)) + ", "
        switch = not switch

    return seq


def SequenzGenerator(n):
    """
    :param n: Laenge der Sequenz; Ganzzahliger Typ
    :return: Eine Sequenz von alternierenden 0 und 1
             Beispiel:
                      n = 7
                      Ergebnis -> 0101010
    """
    seq, schalter = "", False
    # Deklarierung von einem leeren String und einer Boolean
    for i in range(n):
        seq += str(int(schalter))
        schalter = not schalter # Nachdem der Schalter eine boolsche
        #  Variable ist, wird diese bei jedem Durchgang geaendert.
        # True entspricht einer 1, False einer 0.
    return seq


def main(n):
    print("generated sequence: " + generate_sequence(n))

if __name__ == '__main__':
    main(7)
