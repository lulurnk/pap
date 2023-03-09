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
        




elif alkohol == n: 
    print("Nach Hause fahren")
