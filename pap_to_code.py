not_allowed = False

def alcohol_test():
    print("Das ist der Alkoholtest")
    
    test1 = int(input("Was ist 2 + 2?"))
    if test1 == 4: 
        print("Test 1/3 bestanden")
        test2 = int(input("Was ist 4 + 4?"))
        test = False
        if test2 == 8: 
            print("Test 2/3 bestanden")
            test3 = int(input("Was ist 10 - 5?"))
            test = False
            if test3 == 5: 
                print("Test 3/3 bestanden")
                test = False
            else:
                test = True
        else:
            Test = True
    else:
        test = True
    return test

age = int(input("Wie alt bist du?: "))

if not age >= 18:
    not_allowed = True
else:
    license_request = int(input("Hast du einen Führerschein?:\n(1) Ja\(2) Nein"))
    if license_request == 2:
        not_allowed = True
    elif license_request == 1:    
        alcohol = input("Hast du Alkohol GEtrunken? (y/n)")
        if alcohol == 'y':
            test = alcohol_test()
            if test == True:
                not_allowed = True

if not_allowed == True:
    print("Ruf deine Eltern an!")
else:
    print("Fahr nach Hause!")
        
