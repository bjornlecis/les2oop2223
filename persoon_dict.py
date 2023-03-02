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
    def voeg_persoon_toe(self):
        keyname = input("geef de key naam van de persoon")
        naam = input("geef de naam van de persoon")
        leeftijd = int(input("geef de leeftijd van de persoon"))
        woonplaats = input("geef de woonplaats van de persoon")
        p = Persoon(naam,leeftijd,woonplaats)
        dict_personen[keyname] = p

p = Persoon("Peter",30,"Genk")
p2 = Persoon("Jan",24,"Hasselt")
p3 = Persoon("Ann",22,"genk")
p4 = Persoon("Frank",25,"Bilzen")

dict_personen = {"persoon1":p,"persoon2":p2,"persoon3":p3,"persoon4":p4}
for persoon in dict_personen:
    print(persoon)
p.voeg_persoon_toe()
for persoon in dict_personen.values():
    print(persoon)
print("einde")
