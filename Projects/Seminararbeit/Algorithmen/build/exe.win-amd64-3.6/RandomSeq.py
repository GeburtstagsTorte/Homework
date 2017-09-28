

def RandomSeq(a, c, m, x, n):

    print(x)
    y = (a*x + c) % m
    if n > 0:
        # Solange n > 0 rufe die Funktion
        # noch einmal auf mit n-1
        RandomSeq(a, c, m, y, n-1)

def main_randSeq(a, c, m, x, n):
    print("Random sequence with a={}, c={}, m={}, x={} with length {}".format(a, c, m, x, n))
    RandomSeq(a, c, m, x, n)

if __name__ == '__main__':
    RandomSeq(1, 1, 5, 2, 5)
# Rufe Funktion mit den Werten a=3, c=9, m=10, x=2 und n=7 auf

