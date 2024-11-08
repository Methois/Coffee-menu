kosten = 0
extraKosten = 0
klaar = False
extraKlaar = False
boodschappenlijst = []

print("-----| Koffie Menu |-----")
print("-------| Zwart |------------|")
print("1. Espresso..............2,50")
print("2. Americano.............3,25\n")
print("-------| Wit |------------|")
print("3. Cappuccino............3,00")
print("4. Latte.................3,20")
print("5. Flat white............3,50\n")

while klaar == False:
    keuze = int(input("Maak uw keuze: "))
    meer = input("Wilt u nog iets bestellen? (y/n): ").lower()
    if meer == "n":
        klaar = True
    elif meer == "y":
        klaar = False
    else:
        print("Ongeldige invoer.")

print("")
print("-------| Extra's |------------|")
print("A. Extra suiker.............0,25")
print("B. Extra melk...............0,50\n")

while extraKlaar == False:
    extra = input("Maak uw keuze voor Extra's? (a/b): ").lower()
    nogmeer = input("Wilt u nog een extra erbij? (y/n): ").lower()
    if nogmeer == "n":
        extraKlaar == True
    elif nogmeer == "y":
        extraKlaar == False
    else: 
        print("Ongeldige invoer")

if keuze == "1": 
    boodschappenlijst.__add__("Espresso..............2,50")

print(boodschappenlijst)
    