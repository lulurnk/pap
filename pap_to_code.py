age = int(input("Wie alt bist du?: "))

if not age >= 18:
    not_allowed = True
else:
    license_request = int(input("Do you have a license?:\n(1) Yes\(2) No"))
    if license_request == 2:
        not_allowed = True
    elif license_request == 1:    
        alcohol = input("Hast du Alkohol GEtrunken? (y/n)")


if alkohol == y:




elif alkohol == n: 
    print("Nach Hause fahren")

def alcohol_test():
    print("Das ist der Alkoholtest")
    
    test1 = int(input("Was ist 2 + 2?"))
    if test1 == 4: 
        print("Test 1/3 bestanden")
    test2 = int(input("Was ist 4 + 4?"))
    if test2 == 8: 
        print("Test 2/3 bestanden")
    test3 = int(input("Was ist 10 - 5?"))
    if test3 == 5: 
        print("Test 3/3 bestanden")
