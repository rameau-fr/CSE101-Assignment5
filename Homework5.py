import random

class Weapon:
    def __init__(self, name, damage):
        """
        This method initializes the attributes of the Weapon class.

        Args:
        name (str): Name of the weapon.
        damage (int): Amount of damage the weapon can inflict.
        """
        ...

class Armor:
    def __init__(self, name, defense):
        """
        This method initializes the attributes of the Armor class.

        Args:
        name (str): Name of the armor.
        defense (int): Defense value of the armor.
        """
        ...

class Gladiator:
    def __init__(self, name, weapon, armor, strength, luck):
        """
        This method initializes the attributes of the Gladiator class.

        Args:
        name (str): Name of the gladiator.
        weapon (Weapon): Weapon instance that the gladiator will use.
        armor (Armor): Armor instance that the gladiator will wear.
        strength (float): Strength of the gladiator, affecting the damage they deal in battle.
        luck (float): Luck of the gladiator, randomly affecting their attack and defense power.

        Note: Health, a class attribute, will also need to be initialized to 100.
        """
        ...

    def attack(self):
        """
        This method calculates the damage dealt by the Gladiator when attacking.

        It considers both the Gladiator's strength and luck, the latter being randomly 
        factored in each time the method is called.

        Returns:
        float: The amount of damage dealt by the Gladiator.
        """
        ...
    
    def defend(self, damage):
        """
        This method processes the damage received by the Gladiator when being attacked.

        It considers the Gladiator's Armor defense and luck, the latter being randomly 
        factored in each time the method is called. The damage is subtracted from the Gladiator's health.

        Args:
        damage (float): The amount of damage to be defended against.
        """
        ...

class Arena:
    def __init__(self, gladiator1, gladiator2):
        """
        This method initializes the attributes of the Arena class.

        Args:
        gladiator1 (Gladiator): The first gladiator in the arena.
        gladiator2 (Gladiator): The second gladiator in the arena.
        """
        ...

    def fight(self):
        """
        This method initiates a turn-based fight between the two Gladiators in the Arena.

        The Gladiators take turns attacking each other until one of them has no more health points 
        (i.e., their `health` reaches 0 or below). The method prints out a message for each attack, 
        showing who attacked whom and how much damage was dealt. Once a Gladiator's health points 
        reach 0 or less, the fight ends, and the method prints out the name of the winner.
        """
        ...

        
def main():
    # 1.1 - Prepare your Armory
    pugio = Weapon("pugio", 2)
    spatha = Weapon("spatha", 10)
    fascina = Weapon("fascina", 12)

    # 1.2 - Prepare the armors
    cuirass = Armor("cuirass", 5)
    helmet = Armor("helmet", 2)

    # 2.1 Declare the gladiators
    spartacus = Gladiator("spartacus", spatha, cuirass, 1.5, 0.2)
    flamma = Gladiator("flamma", spatha, helmet, 1.6, 0.1)
    attilius = Gladiator("attilius", pugio, helmet, 1.1, 0.5)

    # 3. Time to fight in the arena
    colliseum = Arena(spartacus, flamma)
    colliseum.fight()


main()