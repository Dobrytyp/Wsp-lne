def netto_brutto(kwota):
    wynagrodzenie = kwota * 140.26 / 100
    return print("Twoja kwota brutto to:", round(wynagrodzenie, 2), "\n")


def brutto_netto(kwota):
    wynagrodzenie = kwota * 71.3 / 100
    return print("Twoja kwota netto to:", round(wynagrodzenie, 2), "\n")

def kalkulator_oprocentowania(stan_p, procent, okres, pytanie):
    miesiąc = okres * 12
    procent_m = procent / 12

    dzień = okres * 365
    procent_d = procent / 365
    if pytanie == "m":
        wynik = stan_p * ((1 + (procent_m / 100)) ** miesiąc)
        return print("Twój kapitał po wskaznym okresie, wyniesie:", round(wynik, 2), "\n")

    elif pytanie == "r":
        wynik = stan_p * ((1 + (procent / 100)) ** okres)
        return print("Twój kapitał po wskaznym okresie, wyniesie:", round(wynik, 2), "\n")

    elif pytanie == "d":
        wynik = stan_p * ((1 + (procent_d / 100)) ** dzień)
        return print("Twój kapitał po wskaznym okresie, wyniesie:", round(wynik, 2), "\n")


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


def petla(password):
    totatlcounter = ""
    lower = "aąbcćdeęfghijklłmnńopqrstóuwxyzźż"
    upper = lower.upper()
    digits = "01234567890"
    specials = "!@$%^&*"
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
