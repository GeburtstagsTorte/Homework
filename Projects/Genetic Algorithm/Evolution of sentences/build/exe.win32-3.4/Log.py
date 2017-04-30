
def update_log(info):
    with open('log.txt', 'a') as file:
        for i in info:
            file.write(i + "; ")
        file.write("\n")


def get_log():

    log = []
    file = open('log.txt').read().splitlines()

    for i in file:
        log.append([])
        info = i.split("; ")

        for j in info:
            try:
                if j != '':
                    log[len(log) - 1].append(j)
            except ValueError:
                pass
    return log
