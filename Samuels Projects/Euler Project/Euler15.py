# Lattice path
# How many such routes are there through a 20×20 grid? (only right and down)


def binomial_coefficient(n, k):
    # source: https://en.wikipedia.org/wiki/Binomial_coefficient
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k) # take advantage of symmetry
    c = 1
    for i in range(k):
        c = c * (n - i) / (i + 1)
    return c

grid_size = 20
N = 2*grid_size
# only up and downs 2x2: 1) DDRR 2) DRDR 3) DRRD 4) RDRD 5) RDDR 6) RRDD. -> 2N
K = grid_size

print(binomial_coefficient(N, K))
