import ChiSquared
import RandomSeq
import ParameterFinden
import SequenzGenerator
import RandomGenerator
import subprocess
from time import sleep


def clear():
    subprocess.call("cls", shell=True)


def draw_head():
    print()
    print("--------------------------------------------")
    print(" Userinterface für die benutzen Algorithmen")
    print("--------------------------------------------")
    print()


def draw_choices():
    print("[1] Chi-Quadrat Methode")
    print("[2] Generierung einer zufälligen Sequenz")
    print("[3] Generierung alternierender 0 und 1")
    print("[4] Parameter finden")
    print("[5] Verteilung des Kongruenzgenerators")
    print("[6] Sequenz mit einen Kongruenzgenerator erstellen")
    print()


def handle_chi():
    clear()
    print("---------------------")
    print(" Chi-Quadrat Methode")
    print("---------------------")
    print()
    print("Empfohlen: Wählen Sie 1, um die selben Ergebnisse der Seminararbeit zu erhalten.")
    print("Wählen Sie die 2, wenn Sie eigene Werte eingeben möchten.")
    print()
    user_input = input("Antwort: ")
    clear()

    if user_input == "1":
        print("Sie haben Option 1 gewählt.")
        print()
        ChiSquared.main_chi(n=1000000, r=10)

    if user_input == "2":
        print("Sie haben Option 2 gewählt.")
        print("Trennen Sie die einzelnen Werte mit Kommas und einem Leerzeichen.")
        print()
        try:
            exp, obs = input("die erwarteten Werte: "), input("die beobachteten Werte: ")
            exp = exp.split(", ")
            obs = obs.split(", ")

            exp = [int(i) for i in exp]
            obs = [int(i) for i in obs]

            ChiSquared.interface(obs, exp)

        except Exception:
            print("Es scheint alls hätten Sie etwas falsch eingetippt!")
            sleep(2)
            clear()
            return handle_chi()

    if user_input == "":
        clear()
        return main()

    user_input = input()

    if user_input == "":
        clear()
        return main()


def handle_rand_seq():
    clear()
    print("--------------------------------------")
    print(" Generierung einer zufälligen Sequenz")
    print("--------------------------------------")
    print()
    print("Wählen Sie 1, um die Werte der Seminararbeit zu erhalten.")
    print("Wählen Sie 2, um eine beliebige zu generieren.")
    user_input = input("Antwort: ")
    clear()

    if user_input == "1":
        print("Sie haben Option 1 gewählt.")
        print()
        RandomSeq.main_randSeq(1, 1, 5, 2, 5)

    if user_input == "2":
        print("Sie haben Option 2 gewählt.")
        print()
        a, c, m, x, n = int(input("a = ")), int(input("c = ")), int(input("m = ")), \
                        int(input("x = ")), int(input("n = "))
        try:
            print()
            RandomSeq.main_randSeq(a, c, m, x, n)

        except Exception:
            print("Es scheint als hätten Sie etwas falsch eingetippt!")
            sleep(2)
            clear()
            return handle_rand_seq()

    if user_input == "":
        clear()
        return main()

    user_input = input()

    if user_input == "":
        clear()
        return main()


def handle_alt():
    clear()
    print("------------------------------------")
    print(" Generierung alternierender 0 und 1")
    print("------------------------------------")
    print()
    print("Wählen Sie 1, um das Ergebnis der Seminararbeit zu erhalten.")
    print("Wählen Sie 2, um ein eigenes zu generieren.")
    user_input = input("Antwort: ")
    clear()

    if user_input == "1":
        print("Sie haben Option 1 gewählt.")
        SequenzGenerator.main(7)

    if user_input == "2":
        print("Sie haben Option 2 gewählt.")
        try:
            n = input("Wie lang soll die Sequenz sein? ")
            SequenzGenerator.main(int(n))

        except Exception:
            print("Es scheint als hätten Sie etwas falsch eingetippt!")
            sleep(2)
            clear()
            return handle_alt()

    if user_input == "":
        clear()
        return main()

    user_input = input()

    if user_input == "":
        clear()
        return main()


def handle_param():
    clear()
    print("------------------")
    print(" Parameter finden")
    print("------------------")
    print()
    print("Wählen Sie 1, wenn sie nur die Anzahl sehen wollen.")
    print("Wählen Sie 2, wenn sie auch mögliche Parameter sehen wollen.")
    print("Achtung: Option 2 hat einen großen Output.")

    user_input = input("Antwort: ")
    clear()

    if user_input == "1":
        clear()
        print("Sie haben Option 1 gewählt.")
        try:
            ParameterFinden.main(show=False)
        except Exception as e:
            print(e)

    if user_input == "2":
        clear()
        print("Sie haben Option 2 gewählt.")
        sleep(1)
        ParameterFinden.main(show=True)

    if user_input == "":
        clear()
        return main()

    user_input = input()

    if user_input == "":
        clear()
        return main()


def handle_dis_kon():
    clear()
    print("------------------------------------")
    print(" Verteilung des Kongruenzgenerators")
    print("------------------------------------")
    print()
    print("Wählen Sie 1, um die Ergebnisse der Seminararbeit zu erhalten.")
    print("Wählen sie 2, um eigene Ergebnisse zu erhalten")
    print()
    user_input = input("Antwort: ")

    if user_input == "1":
        clear()
        print("Sie haben Option 1 gewählt.")
        try:
            RandomGenerator.main(10061, 1, 2**16, 54, 1000000, 10)
        except Exception as e:
            print(e)

    if user_input == "2":
        """
        (a, c, m, x, n, length)
        """
        clear()
        print("Sie haben Option 2 gewählt.")
        try:
            a = int(input("a = "))
            c = int(input("c = "))
            m = int(input("m = "))
            x = int(input("x = "))
            n = int(input("n = "))
            length = int(input("Intervall bis (einschließlich) = "))

            RandomGenerator.main(a, c, m, x, n, length)

        except Exception as e:
            clear()
            print(e)
            print("Scheinbar haben Sie einen unzulässigen Wert eingetipp!")
            sleep(2)
            return handle_dis_kon()

    if user_input == "":
        clear()
        return main()

    user_input = input()

    if user_input == "":
        clear()
        return main()


def handle_kon_test():
    clear()
    print("------------------------------------------------")
    print(" Sequenz mit einen Kongruenzgenerator erstellen")
    print("------------------------------------------------")
    print()
    print("Wählen sie die 1, um die Zufallssequenz der Verteilung aus der Seminararbeit zu erhalten.")
    print("Wählen sie die 2, um eigene Reihen zu erstellen.")

    user_input = input("Antwort: ")

    if user_input == "1":
        clear()
        print("Sie haben Option 1 gewählt.")
        print()
        RandomGenerator.main2(10061, 1, 2**16, 54, 1000000, 0, 9)

    if user_input == "2":
        clear()
        print("Sie haben Option 2 gewählt.")
        print()
        try:
            a = int(input("a = "))
            c = int(input("c = "))
            m = int(input("m = "))
            x = int(input("x = "))
            n = int(input("Länge der Sequenz = "))
            start = int(input("Startwert: "))
            end = int(input("Endwert: "))
            RandomGenerator.main2(a, c, m, x, n, start, end)

        except Exception as e:
            print(e)
            print("Ups! Sie haben wohl einen unzulässigen Wert eingegeben!")
            return handle_kon_test()

    if user_input == "":
        clear()
        return main()

    user_input = input()

    if user_input == "":
        clear()
        return main()


def menu():
    user_input = input("Geben Sie ihre Wahl hier ein: ")

    if user_input == "1":
        handle_chi()

    if user_input == "2":
        handle_rand_seq()

    if user_input == "3":
        handle_alt()

    if user_input == "4":
        handle_param()

    if user_input == "5":
        handle_dis_kon()

    if user_input == "6":
        handle_kon_test()
    else:
        print()
        clear()
        print("Es scheint als hätten Sie eine unzulässige Zahl eingegeben!")
        sleep(1)
        clear()
        return main()


def main():
    draw_head()
    draw_choices()
    menu()

main()
