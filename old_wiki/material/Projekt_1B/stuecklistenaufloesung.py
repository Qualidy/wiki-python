def stuecklistenaufloesung(bestellungen):

    bedarf_A = 0
    bedarf_B = 0
    bedarf_C = 0
    bedarf_D = 0
    bedarf_E = 0
    bedarf_F = 0

    for bestellung in bestellungen:

        if bestellung.split()[2] == "Modul_A":
            bedarf_A += 5*bestellung.split()[0]
            bedarf_C += 7*bestellung.split()[0]
            bedarf_D += 200*bestellung.split()[0]
            bedarf_E += 10.7*bestellung.split()[0]


        if bestellung.split()[2] == "Modul_B":
            bedarf_A += 7*bestellung.split()[0]
            bedarf_B += 10*bestellung.split()[0]
            bedarf_E += 30.5*bestellung.split()[0]
            bedarf_F += 23.5*bestellung.split()[0]

        if bestellung.split()[2] == "Modul_C":

            bedarf_C += 34*bestellung.split()[0]
            bedarf_D += 600*bestellung.split()[0]
            bedarf_E += 90.7*bestellung.split()[0]
            bedarf_F += 3*bestellung.split()[0]


    return bedarf_A, bedarf_B, bedarf_C, bedarf_C, bedarf_E, bedarf_F 


bestellungen = [ "345 mal Modul_A", "123 mal Modul_B" , "456 mal Modul_C"]

bedarfe = stuecklistenaufloesung(bestellungen)

print(bedarfe)



def lagerbestand():
    # read txt
    with open("../wiki/material/bestand.txt") as f:
        lines = f.readlines()
    
    # extract values
    bestand_A = lines[0].split(" ")[2]
    bestand_B = lines[1].split(" ")[2]
    bestand_C = lines[2].split(" ")[2]
    bestand_D = lines[3].split(" ")[2]
    bestand_E = lines[4].split(" ")[2]
    bestand_F = lines[5].split(" ")[2]

    return bestand_A, bestand_B, bestand_C, bestand_C, bestand_E, bestand_F





if __name__ == "__main__":
    print(lagerbestand())

    import os  
    print ("Updated directory:" , os.getcwd())