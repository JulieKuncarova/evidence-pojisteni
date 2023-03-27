class Pojisteny():
    """
    Třída reprezentující pojištěného.
    """

    def __init__(self):
        """
        Konstruktor třídy
        """
        self.jmeno = ""
        self.prijmeni = ""
        self.vek = ""
        self.telefonni_cislo = ""

    def pridej_pojisteneho(self):
        """
        Vytvoří pojištěného se zadanými údaji.
        """
        print("\nZadejte požadované údaje")
        self.jmeno = input("Jméno pojištěného:\n").capitalize()
        self.prijmeni = input("Příjmení pojištěného:\n").capitalize()
        self.vek = input("Věk:\n")
        self.telefonni_cislo = input("Telefonní čílo:\n")

    def __str__(self):
        """
        Vrací textovou reprezentaci pojištěného.
        """
        return self.jmeno, self.prijmeni, self.vek, self.telefonni_cislo