from pojisteny import Pojisteny

class Evidence():
    """
    Třída reprezentující evidenci pojištěných.
    """

    def __init__(self):
        """
        Konstruktor třídy
        """
        self.seznam_pojistenych = []
        self.akce = ""

    def vrat_evidenci(self):
        """
        Vrátí evidenci umožňující přidat pojištěného, vypsat všechny pojištěné
        a vyhledat pojištěného.
        """

        # dokud není požadována akce 4
        while self.akce != "4":
            # výpis menu možných akcí
            print("\nMůžete provést tyto akce:\n"
                  "1 - Přidat nového pojištěného\n"
                  "2 - Vypsat všechny pojištěné\n"
                  "3 - Vyhledat pojištěného\n"
                  "4 - Konec\n")

            # výběr akce uživatelem
            self.akce = input("Vyberte požadovanou akci:\n")

            # když je požadována akce 1
            if self.akce == "1":
                # vytvoření pojištěného se zadanými údaji
                pojisteny = Pojisteny()
                pojisteny.pridej_pojisteneho()
                # přidání pojištěného do seznamu pojištěných
                self.seznam_pojistenych.append(pojisteny)

                input("\nData byla uložena. Pokračujte libovolnou klávesou...")
            # když je požadována akce 2
            elif self.akce == "2":
                if self.seznam_pojistenych != []:  # když není seznam pojištěných prázdný

                    # výpis seznamu pojištěných ve sloupcích podle jména, příjmení, věku a tel. čísla
                    nazvy_sloupcu = ["Jméno", "Příjmení", "Věk", "Telefon"]
                    print(f"\n{nazvy_sloupcu[0]: <11}{nazvy_sloupcu[1]: <14}{nazvy_sloupcu[2]: <7}{nazvy_sloupcu[3]: <10}\n"
                          f"-----------------------------------------")
                    for zaznam in self.seznam_pojistenych:
                        print(f"{zaznam.jmeno: <11}{zaznam.prijmeni: <14}{zaznam.vek: <7}{zaznam.telefonni_cislo: <10}")

                else:  # když nebyl přidán žádný pojištěný
                    print("\nV evidenci zatím není žádný pojištěný")

                input("\nPokračujte libovolnou klávesou... ")
            # když je požadována akce 3
            elif self.akce == "3":
                if self.seznam_pojistenych != []:  # když není seznam pojištěných prázdný
                    print("\nZadejte jméno a příjmení pojištěného, kterého chcete vyhledat")
                    pojisteny_jmeno = input("Jméno:\n").capitalize()
                    pojisteny_prijmeni = input("Příjmení:\n").capitalize()
                    nalezeny_pojisteny = []

                    for zaznam in self.seznam_pojistenych:
                        if pojisteny_jmeno == zaznam.jmeno and pojisteny_prijmeni == zaznam.prijmeni:
                            nalezeny_pojisteny.append(zaznam)

                            # výpis vyhledaného pojištěného podle jména, příjmení, věku a tel. čísla
                            nazvy_sloupcu = ["Jméno", "Příjmení", "Věk", "Telefon"]
                            print(f"\n{nazvy_sloupcu[0]: <11}{nazvy_sloupcu[1]: <14}{nazvy_sloupcu[2]: <7}{nazvy_sloupcu[3]: <10}\n"
                                  f"-----------------------------------------")
                            print(f"{zaznam.jmeno: <11}{zaznam.prijmeni: <14}{zaznam.vek: <7}{zaznam.telefonni_cislo: <10}")

                    if nalezeny_pojisteny == []:  # pokud nebyl nalezen pojištěný se zadaným jménem a příjmením
                        print("\nNebyl nalezen pojištěný s tímto jménem a příjmením")

                else:  # když nebyl přidán žádny pojištěný
                    print("\nV evidenci zatím není žádný pojištěný")

                input("\nPokračujte libovolnou klávesou... ")
            # když je požadována akce 4, aplikace se ukončí
            elif self.akce == "4":
                print("\nDěkujeme za využití této evidence, nashledanou.")
            # pokud byla zadána jiná hodnota než číslo od 1 do 4
            else:
                print("\nNeplatná volba. Zadejte prosím číslo od 1 do 4.\n")