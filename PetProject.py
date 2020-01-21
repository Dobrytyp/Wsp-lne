class Konto:
    def __init__(self, imie_nazwisko, stan, status):
        self.imie_nazwisko = imie_nazwisko
        self.stan = stan
        self.status = status

    def description(self):
        return f"Witaj {imie_nazwisko}. Twoje konto jest {self.status} znajduje się na nim {self.stan} złotych"

    def stan_konta(self):
        return self.stan

    def wplyw(self, wplyw):
        self.stan += wplyw

    def stats(self):
        return self.imie_nazwisko, self.stan, self.status


imie_nazwisko = input("Podaj imię i nazwisko\n")

lower = "aąbcćdeęfghijklłmnńopqrstóuwxyzźż"
upper = lower.upper()
digits = "01234567890"
specials = "!@$%^&*"
totatlcounter = ""

def petla(password):
    totatlcounter = ""
    for i in password:
        if i in lower:
            totatlcounter += "l"
        elif i in upper:
            totatlcounter += "u"
        elif i in digits:
            totatlcounter += "d"
        elif i in specials:
            totatlcounter += "s"
    return totatlcounter

password = input("Witamy w systemie bankowości elektronicznej.\n \nWpisz nowe hasło. Hasło musi mieć od 6 do 12 "
                 "znaków. \nHasło musi zawierać przynajmniej jedną wielką, jedną mała litere, cyfrę i znak "
                 "specjalny\n")
petla(password)
totatlcounter = petla(password)

quit1 = True

while quit1:
    while "l" not in totatlcounter or "u" not in totatlcounter or "d" not in totatlcounter or "s" not in totatlcounter or len(password) > 12 or len(password) < 6:
        totatlcounter = ""
        print("Twoje hasło nie spełnia wymagań\n")
        password = input("Wpisz jeszcze raz hasło\n")
        petla(password)
        totatlcounter = petla(password)


    print("Hasło zostało zmienione\n")

    #

    import sys
    ask1 = ''
    quitprogram = False

    while ask1 != "t" or ask1 != "n":
        ask1 = input("czy chcesz się teraz zalogowaćC? \n tak(t), nie 👎?\n")
        if ask1 == "t" or ask1 == "n":
            break
    if ask1 == "n":
        print("Dziękujemy za skorzystanie z naszego systemu logowania\n")
        sys.exit(0)
    elif ask1 == "t":
        while True:
            ownerpassword = input("podaj swoje hasło\nWyjdź (e)\n")
            if ownerpassword == "e":
                sys.exit()
            elif ownerpassword != password:
                print("Podałeś błedne hasło")
            else:
                print("Witamy w systemie bankowosci elektronicznej\n")
                break

    if quitprogram:
        sys.exit()

    #

    program = ''
    while program != "k" or program != "e" or program != "b" or program != "r":
        program = input("Z jakiej funkcji chcesz skorzystać?\nKalkulator oprocentowania: (k)\nKalkulator Brutto - Netto ("
                        "b)\nOferta kont (r)\nWyjście z systemu bankowości: (e)\n")

        if program == "k":                                              # Kalkulator oprocentowania
            stan_p = float(input("podaj stan poczatkwy konta\n"))
            procent = float(input("podaj oprocentowanie\n"))
            okres = float(input("ile lat będziez trzymał środki\n"))
            pytanie = input("Co jaki okres występuje kapitalizacja?\n Dziennie (d), miesiąc (m), rok (r)\n")
            pytanie = pytanie.lower()
            while not pytanie in ["m", "d", "r"]:
                print("Wybierz zdefiniowaną odpowedź: d - dzień, m - miesiąc, r - rok")
                pytanie = input("Co jaki okres występuje kapitalizacja?\n Dziennie (d), miesiąc (m), rok (r)\n")

            miesiąc = okres * 12
            procent_m = procent / 12

            dzień = okres * 365
            procent_d = procent / 365

            if pytanie == "m":
                wynik = stan_p * ((1 + (procent_m / 100)) ** miesiąc)
                print("Twój kapitał po wskaznym okresie, wyniesie:", round(wynik, 2), "\n")

            elif pytanie == "r":
                wynik = stan_p * ((1 + (procent / 100)) ** okres)
                print("Twój kapitał po wskaznym okresie, wyniesie:", round(wynik, 2), "\n")

            elif pytanie == "d":
                wynik = stan_p * ((1 + (procent_d / 100)) ** dzień)
                print("Twój kapitał po wskaznym okresie, wyniesie:", round(wynik, 2), "\n")
        elif program == "b":                            # Kalkulator Brutto/Netto
            podaj = ''
            while podaj != "b" or podaj != "n" or podaj != "e" or podaj != "r":
                podaj = input("Co chcesz obliczyć? Brutto (b) czy netto (n)?\nPowrót do menu (r)\nZakończ program (e)\n ")
                if podaj == "b":
                    kwota = float(input("Podaj wysokść wynagrrodzenia netto\n"))
                    wynagrodzenie = kwota * 140.26 / 100
                    print("twoja kwota brutto to:", round(wynagrodzenie, 2))
                elif podaj == "n":
                    kwota = float(input("Podaj wysokść wynagrrodzenia brutto\n"))
                    wynagrodzenie = kwota * 71.3 / 100
                    print("twoja kwota netto to:", round(wynagrodzenie, 2))
                elif podaj == "e":
                    print("Dziękujemy za skorzystanie z naszego systemu bankowości\n")
                    sys.exit(0)
                elif podaj == "r":
                    break
        elif program == "r":
            typ_konta = ''
            print("Zapraszamy do skoszystania z baszej bogatej oferty.\nDzięki dostoswanej do każdego oferty, "
                  "napewno znajdziesz coś dla siebie.\n")
            while typ_konta != 'k' or typ_konta != 'e' or typ_konta != 'w' or typ_konta != 'r':
                podaj = input("Jaki typ konta chcesz otworzyć?\n Rachunek Bierzący (k)\n Konto oszczędnościowe "
                              "(e)\n Konto Walutowe (w)\n Powrót do menu (r)\n\n")
                if podaj == "k":
                    user = Konto(imie_nazwisko, 0, "otwarte")
                    print(user.description())
                    break
                elif podaj == "r":
                    break


        elif program == "e":
            print("Dziękujemy za skorzystanie z naszego systemu bankowości\n")
            sys.exit(0)

user3 = Konto.