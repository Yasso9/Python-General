class Human:
    """Class of human being""" # Commentaire de la classe

    human_created = 0
    homeland = "Earth"

    # Constructeur
    def __init__(self, newName, newAge=0):
        print("Human created ", self)
        self.name = newName
        self._age = newAge
        Human.human_created += 1

    # Getter
    def _getage(self):
        try:
            return self._age
        except AttributeError:
            print("Age doesn't exist")
    
    # Setter
    def _setage(self, newAge):
        if(newAge < 0):
            self._age = 0
        elif(newAge > 150):
            self._age = 150
        else:
            self._age = newAge

    # Deleter
    def _delage(self):
        del self._age

    # On appilique les propriétés de l'age
    age = property(_getage, _setage, _delage, "I m the age of the human")

    # Méthode ou methode d'instance (self)
    def speak(self, message):
        print("{} says : {}".format(self.name, message))

    # Methode de classe (cls)
    def change_planet(cls, newPlanet):
        Human.homeland = newPlanet
    change_planet = classmethod(change_planet)

    # Methode statique
    def definition():
        print("Humain is the most intelligent espece form on  earth")
    definition = staticmethod(definition)




# print("Existing human : ", Human.human_created)

# h1 = Human("Ilyas")

# print("Existing human : ", Human.human_created)

# print("h1's name :", h1.name)
# print("h1's _age :", h1._age)

# h1.name = "Yasso"
# print("h1's name :", h1.name)

# h1.speak("What's up guys")




# h2 = Human("Julien", 15)
# print("Existing human : ", Human.human_created)




h3 = Human("Baba", 800)
print(h3.age)
h3.age = -8
print(h3.age)
h3.age = 200
print(h3.age)
del h3.age
print(h3.age)




# print("Homeland : {}".format(Human.homeland))
# Human.change_planet("Mars")
# print("Homeland : {}".format(Human.homeland))




# Human.definition()