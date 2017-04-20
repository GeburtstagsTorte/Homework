from time import clock


def count_primes():
    t1 = clock()
    primes = [2]
    cani = 3 # candidate
    count = 2
    while cani < 2000000:
        for i in primes:
            if cani % i == 0:
                cani += 2
                break
        else:
            primes.append(cani)
            count += cani
            cani += 2
    t2 = clock()
    return count, t2-t1
    # (142913828922, 4287.39772664)


def count_primes2(n=2000000):
    from math import sqrt

    t1 = clock()
    primes = [2]
    count = 2
    candidates = [i for i in range(1, n, 2)]
    for i in candidates:
        if sqrt(i) in candidates:
            candidates.remove(i)
    for i in candidates:
        for j in primes:
            if i % j == 0:
                break
        else:
            primes.append(i)
            count += i
    t2 = clock()
    return count, t2-t1


def count_primes3(n=2000000):
    from time import clock
    from math import sqrt

    t1 = clock()
    candidate = 2
    primes = [candidate]
    candidate += 1
    primes.append(candidate)
    count = candidate

    # just something about primes from wikipedia
    # Da mindestens ein Primfaktor einer zusammengesetzten Zahl immer kleiner gleich der Wurzel der Zahl sein muss,
    # ist es ausreichend, nur die Vielfachen von Zahlen zu streichen,
    # die kleiner oder gleich der Wurzel der Schranke S sind.
    # Ebenso genügt es beim Streichen der Vielfachen, mit dem Quadrat der Primzahl zu beginnen,
    # da alle kleineren Vielfachen bereits markiert sind.

    while candidate < n:
        candidate += 2
        for i in primes:
            if i > sqrt(candidate):
                continue
            elif candidate % i == 0:
                break
        else:
            primes.append(candidate)
            count += candidate
    t2 = clock()
    return t2-t1


def pg(inpt):
    from math import sqrt
    from time import time
    # best and most efficient algorithm i know
    # source:
    # https://en.wikibooks.org/wiki/Some_Basic_and_Inefficient_Prime_Number_Generating_Algorithms

    lim = inpt
    sqrtlim = sqrt(float(lim))
    pp = 2
    ep = [pp]
    ss = [pp]
    pp += 1
    i = 0
    rss = [ss[0]]
    tp = [pp]
    xp = []
    pp += ss[0]
    npp = pp
    tp.append(npp)
    rss.append(rss[i] * tp[0])
    bt = time()
    while npp < int(lim):
        i += 1
        while npp < rss[i] + 1:
            for n in ss:
                npp = pp + n
                if npp > int(lim): break
                if npp <= rss[i] + 1: pp = npp
                sqrtnpp = sqrt(npp)
                test = True
                for q in tp:
                    if sqrtnpp < q:
                        break
                    elif npp % q == 0:
                        test = False
                        break
                if test:
                    if npp <= sqrtlim:
                        tp.append(npp)
                    else:
                        xp.append(npp)
            if npp > int(lim): break
        if npp > int(lim): break
        lrpp = pp
        nss = []
        while pp < (rss[i] + 1) * 2 - 1:
            for n in ss:
                npp = pp + n
                if npp > int(lim): break
                sqrtnpp = sqrt(npp)
                test = True
                for q in tp:
                    if sqrtnpp < q:
                        break
                    elif npp % q == 0:
                        test = False
                        break
                if test:
                    if npp <= sqrtlim:
                        tp.append(npp)
                    else:
                        xp.append(npp)
                if npp % tp[0] != 0:
                    nss.append(npp - lrpp)
                    lrpp = npp
                pp = npp
            if npp > int(lim): break
        if npp > int(lim): break
        ss = nss
        ep.append(tp[0])
        del tp[0]
        rss.append(rss[i] * tp[0])
        npp = lrpp
    et = time()
    tt = et - bt
    ep.reverse()
    [tp.insert(0, a) for a in ep]
    tp.reverse()
    [xp.insert(0, a) for a in tp]
    return xp
    # It took 23.740000009536743 seconds to generate the prime set up to:  2000000
    # with 148933 members.
    # 142913828922


def main():
    print(pg(2000000))

if __name__ == '__main__':
    main()

