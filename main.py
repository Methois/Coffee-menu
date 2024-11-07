kosten = 0
klaar = False

print("-----| Koffie Menu |-----")
print("-------| Zwart |------------|")
print("1. Espresso..............2,50")
print("2. Americano.............3,25\n")
print("-------| Wit |------------|")
print("3. Cappuccino............3,00")
print("4. Latte.................3,20")
print("5. Flat white............3,50\n")
print("-------| Extra's |------------|")
print("A. Extra suiker.............0,25")
print("B. Extra melk...............0,50\n")

while klaar == False:
    keuze = int(input("Maak uw keuze: "))
    meer = input("Wilt u nog iets bestellen? (y/n): ").lower()
    if meer == "n":
        klaar = True
    