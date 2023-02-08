def menu():
    print ("1: Ecrivez une phrase")
    print ("2: Afficher la phrase")
    print ("3: Taille en caractere de la phrase")
    print ("4: Exit")

    choice = int(input("Entrez votre choix: "))
    return choice

while True:
    choice = menu()
    if choice == 1:
        x = (input("Entrez une phrase: "))
    elif choice == 2:
        print(x)
    elif choice == 3:
        y = len(x)     #La fonction len va permettre d'afficher la longueur de la chaine de caractère
        print (y)
    elif choice == 4:
        break
    else:
        print ("Erreur")

        