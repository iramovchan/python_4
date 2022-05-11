import os
import random

DELETE = 'd'
EXTENSIE = '.wrd'
KIES_LIJST = 'k'
MAX_WOORDLENGTE = 20
NIEUWE_LIJST = 'n'
OPSLAAN = 'w'
OVERHOREN = 'o'
SCHEIDER = '='
SCHERMBREEDTE = 80
SCHERMHOOGTE = 40
STANDAARD_LIJST = 'EN-NED'
STOPPEN = 'q'
TOEVOEGEN = 't'


def print_alle_woordenlijsten():
    print_regel("Alle woordenlijsten: ")
    print_regel()
    files = []

    for file in os.listdir("."):
        if file.endswith(".txt"):
            files.append(file)

    for i in files:
        print_regel(i)

    print_regel()


def kies_lijst(lijst_naam):
    leeg_scherm()
    print_header()
    print_regel(f"Huidige lijst: {lijst_naam}")
    print_alle_woordenlijsten()
    print_regel("Druk op q om terug te gaan")
    print_footer()

    while (STANDAARD_LIJST := input("Kies een lijst: ")) != STOPPEN:
        lijst_naam = STANDAARD_LIJST

        leeg_scherm()
        print_header()
        print_regel(f"Huidige lijst: {lijst_naam}")
        print_alle_woordenlijsten()
        print_regel("Druk op q om terug te gaan")
        print_footer()

    else:
        STANDAARD_LIJST = lijst_naam

    return STANDAARD_LIJST


def leeg_scherm():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def lees_woordenlijst(bestandsnaam):
    woordenlijst = {}
    woordenlijst_bestand = open(bestandsnaam + ".txt", 'r')

    for line in woordenlijst_bestand:
        woord1, woord2 = line.split(SCHEIDER)
        woordenlijst[woord1] = woord2

    return woordenlijst


def voeg_woorden_toe(woordenlijst, lijst_naam):
    leeg_scherm()
    print_header()
    print_regel(f"Huidige lijst: {lijst_naam}")
    print_regel()
    print_regel("Om woorden toe te voegen, schrijf het woord, = en vertaling. Zonder spaties")
    print_regel()
    print_regel("Druk op q om terug te gaan")
    print_footer()

    while (nieuwe_woord := input("Uw keuze: ")) != STOPPEN:
        woord, vertaling = nieuwe_woord.split(SCHEIDER)
        woordenlijst[woord] = vertaling + "\n"

        leeg_scherm()
        print_header()
        print_regel("{} toegevoegd".format(nieuwe_woord))
        print_regel()
        print_regel("Druk ENTER om door te gaan.")
        print_regel("Druk op q om terug te gaan")
        print_footer()
        if (keuze := input("Uw keuze: ")) != STOPPEN:
            leeg_scherm()
            print_header()
            print_regel(f"Huidige lijst: {lijst_naam}")
            print_regel()
            print_regel("Om woorden toe te voegen, schrijf het woord, = en vertaling. Zonder spaties")
            print_regel()
            print_regel("Druk op q om terug te gaan")
            print_footer()
        else:
            break

    schrijf_woordenlijst(lijst_naam, woordenlijst)

    return woordenlijst


def schrijf_woordenlijst(bestandsnaam, woordenlijst):
    woordenlijst_bestand = open(bestandsnaam + ".txt", 'w')

    for woord, vertaling in woordenlijst.items():
        woordenlijst_bestand.write(woord + "=" + vertaling)

    woordenlijst_bestand.close()


def nieuwe_lijst_maken():
    leeg_scherm()
    print_header()
    print_alle_woordenlijsten()
    print_regel("Druk op q om terug te gaan")
    print_footer()
    keuze = ''
    while (lijst_naam := input("Voer in de naam van de nieuwe lijst: ")) != STOPPEN and (keuze != "q"):

        leeg_scherm()
        print_header()

        if lijst_naam.endswith(".txt"):
            nieuwe_lijst = open(lijst_naam, 'w')
            print_regel("{} toegevoegd".format(lijst_naam))

        else:
            nieuwe_lijst = open(lijst_naam + ".txt", 'w')
            print_regel("{} toegevoegd".format(lijst_naam + ".txt"))

        print_regel()
        print_regel("Druk ENTER om door te gaan.")
        print_regel("Druk op q om terug te gaan")
        print_footer()

        keuze = input("Uw keuze: ")

        leeg_scherm()
        print_header()
        print_alle_woordenlijsten()
        print_regel("Druk op q om terug te gaan")
        print_footer()


def overhoren(woordenlijst, lijst_naam):
    woordenlijst_0 = woordenlijst.copy()
    antwoord = ''
    keuze = ''
    while antwoord != STOPPEN and keuze != STOPPEN:
        leeg_scherm()
        print_header()
        if len(woordenlijst_0) == 0:
            print_regel("Er zijn geen woorden in deze woordenlijst.")
            print_regel("Druk ENTER om terug te gaan")
            print_footer()
            weg = input("Uw keuze: ")
            antwoord = 'q'

        else:
            woord, vertaling = random.choice(list(woordenlijst_0.items()))
            vertaling = vertaling.replace("\n", "")
            print_regel(f"Huidige lijst: {lijst_naam}")
            print_regel()
            print_regel("Woord: {} Vertaling: ".format(woord))
            print_footer()

            antwoord = input("Vertaling: ")

            leeg_scherm()
            print_header()

            if antwoord != 'q':
                if antwoord.lower() == vertaling:
                    print_regel("Het is het goede antwoord :]")
                    del woordenlijst_0[woord]
                else:
                    print_regel("Helaas is uw antwooord fout.")
                    print_regel("Het goede antwoord: {}".format(vertaling))
                    print_regel("Uw antwoord: {}".format(antwoord))

                print_regel("Druk ENTER om door te gaan.")
                print_regel("Druk op q om terug te gaan")
                print_footer()
                keuze = input("Uw keuze: ")


def verwijder_woord(woordenlijst, lijst_naam):
    leeg_scherm()
    print_header()
    print_regel(f"Huidige lijst: {lijst_naam}")
    print_regel()
    print_regel("Alle woorden in dit woordenlijst: ")
    for key, value in woordenlijst.items():
        value = value.replace("\n", "")
        print_regel(key + " = " + value)

    print_regel()
    print_regel("Druk op q om terug te gaan")
    print_footer()

    while (woord := input("Welke woord wilt u verwijderen? ")) != STOPPEN:
        if woord in woordenlijst:

            leeg_scherm()
            print_header()
            print_regel("Weet u zeker dat u dit woord wilt verwijderen? (ja/nee)")
            print_footer()
            keuze = input("Uw keuze: ")

            if keuze.lower() == "ja":
                del woordenlijst[woord]

        else:
            print("Deze woord staat niet in dit woordenlijst")
            keuze = input("Druk ENTER om door te gaan ")

        leeg_scherm()
        print_header()
        print_regel(f"Huidige lijst: {lijst_naam}")
        print_regel()
        print_regel("Alle woorden in dit woordenlijst: ")
        for key, value in woordenlijst.items():
            value = value.replace("\n", "")
            print_regel(key + " = " + value)

        print_regel()
        print_regel("Druk op q om terug te gaan")
        print_footer()

    schrijf_woordenlijst(lijst_naam, woordenlijst)

    return woordenlijst


def toon_alle_woorden(woordenlijst, lijst_naam):

    print_header()
    print_regel(f"Huidige lijst: {lijst_naam}")
    print_regel()
    print_regel("Alle woorden in dit woordenlijst: ")
    for key, value in woordenlijst.items():
        value = value.replace("\n", "")
        print_regel(key + " = " + value)
    print_footer()
    keuze = input("Druk ENTER om terug te gaan")


def main():

    STANDAARD_LIJST = 'EN-NED'

    leeg_scherm()
    print_header()
    print_menu(STANDAARD_LIJST)
    print_footer()

    while (keuze := input('Uw keuze: ')) != STOPPEN:
        leeg_scherm()

        woordenlijst = lees_woordenlijst(STANDAARD_LIJST)

        if keuze == "n":
            nieuwe_lijst_maken()
        elif keuze == KIES_LIJST:
            STANDAARD_LIJST = kies_lijst(STANDAARD_LIJST)
        elif keuze == TOEVOEGEN:
            voeg_woorden_toe(woordenlijst, STANDAARD_LIJST)
        elif keuze == OVERHOREN:
            overhoren(woordenlijst, STANDAARD_LIJST)
        elif keuze == 'a':
            toon_alle_woorden(woordenlijst, STANDAARD_LIJST)
        elif keuze == 'v':
            verwijder_woord(woordenlijst, STANDAARD_LIJST)

        leeg_scherm()
        print_header()
        print_menu(STANDAARD_LIJST)
        print_footer()

    leeg_scherm()
    print_afscheid()


def print_regel(inhoud=''):
    print(("| {:" + str(SCHERMBREEDTE - 1) + "}|").format(inhoud))


def print_menu(lijst_naam):
    print_regel("Welkom bij het overhoorprogramma")
    print_regel(f"Huidige lijst: {lijst_naam}")
    print_regel("n - nieuwe woordenlijst maken")
    print_regel("k - kies een andere woordenlijst")
    print_regel("a - alle woorden van dit woordenlijst tonen")
    print_regel("t - woorden toevoegen aan een woordenlijst")
    print_regel("v - woorden uit de lijst verwijderen")
    print_regel("o - woordenlijsten overhoren")
    print_regel("q - stoppen met het programma")


def print_footer():
    print(("| {:>" + str(SCHERMBREEDTE) + "}").format("|"))
    print("=" * (SCHERMBREEDTE + 2))


def print_header():
    print("=" * (SCHERMBREEDTE + 2))
    print(("| {:>" + str(SCHERMBREEDTE) + "}").format("|"))


def print_afscheid():
    print_header()
    print_regel("Bedankt voor het gebruiken van dit overhoorprogramma. :]")
    print_footer()


main()
