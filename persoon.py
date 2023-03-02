class Persoon:
    aantalpersonen = 0
    aantal_personen_genk = 0
    steden = set()


    def __init__(self,naam,leeftijd,woonplaats):
        self.naam = naam
        self.leeftijd = leeftijd
        self.woonplaats = woonplaats
        Persoon.aantalpersonen += 1
        self.id = "id"+str(Persoon.aantalpersonen)
        if str(self.woonplaats).upper() == "GENK":
            Persoon.aantal_personen_genk += 1
        Persoon.steden.add(str(self.woonplaats).upper())


    def __str__(self):
        return "Persoon met id {} heet {} en is {} jaar oud, woont in {}".format(self.id,self.naam,
                                                                          self.leeftijd,self.woonplaats)
    def toon_info(self):
         print("Persoon met id {} heet {} en is {} jaar oud, woont in {}".format(self.id,self.naam,
                                                                          self.leeftijd,self.woonplaats))
    def toon_alle_steden(self):
        for stad in Persoon.steden:
            print(stad)

    def geef_naam(self):
        return self.naam

    def is_persoon_in_lijst(self):
        naam = input("geef de naam")

        """ #oplossing met behulp van methode geef naam
            if naam in Persoon.geef_naam(self):
                print("gevonden")
            else:
                print("niet gevonden")"""

        #Met Boolean
        gevonden = False
        for persoon in lijst_personen:
            if str(persoon.naam).upper() == naam.upper():
                gevonden = True
                break
        if gevonden == True:
            print("gevonden")
        else:
            print("niet gevonden")

    def verander_naam(self):
        naam = input("geef de naam van de persoon die je van naam wilt veranderen")
        for persoon in lijst_personen:
            if persoon.naam == naam:
                nieuwe_naam = input("geef een nieuwe naam")
                persoon.naam = nieuwe_naam
    def verwijder_persoon(self):
        naam = input("geef de naam van de persoon die je wenst te verwijderen")
        for persoon, o in enumerate(lijst_personen):
            if o.naam == naam:
                del lijst_personen[persoon]
                break
    def sorteer_opnaam(self):
        lijst_personen.sort(key=lambda x: x.naam)
        for x in lijst_personen:
            print(x)





p = Persoon("Peter",30,"Genk")
p2 = Persoon("Jan",24,"Hasselt")
p3 = Persoon("Ann",22,"genk")
p4 = Persoon("Frank",25,"Bilzen")
lijst_personen = [p,p2,p3,p4]
#for persoon in lijst_personen:
#    Persoon.toon_alle_steden(persoon)
#p.is_persoon_in_lijst()
#Persoon.verander_naam(p2)
#p3.verwijder_persoon()
for persoon in lijst_personen:
    print(persoon.naam)
print("einde")
p2.sorteer_opnaam()
