x = ("salut la winfous !")
print (x)
y = (type(x))
print (y)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

def menu():
    print("1. Creer une personne ")
    print("2. afficher les infos de la personne ")
    print("3. Exit")
    choice = int(input("Entrer votre choix: "))
    return choice

while True:
    choice = menu()
    if choice == 1:
        name = input("Entrer le nom: ")
        age = int(input("Entrer l'age: "))
        person = Person(name, age)
    elif choice == 2:
        if 'person' in locals():
            person.print_info()
        else:
            print("Aucune personne n’a encore été créée.")
    elif choice == 3:
        break
    else:
        print("Choix non valide. Veuillez réessayer.")