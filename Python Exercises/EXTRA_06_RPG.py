# A Class where
# - we set health and damage attribute
# - inherits from an entity that has an attack function which
# - - prints attack with damage (from the mentioned)
# - creating an instance returns a monster with health hp when the class is printed

# Class point
class Enemy:
    def __init__(self, damage):
        self.damage = damage
    
    def attack(self):
        print(f'Attack deals {self.damage} damage')


class Monster(Enemy):
    def __init__(self, health, damage):
        super().__init__(damage)
        self.health = health
    
    def __str__(self):
        return f'A monster with {self.health} HP'    
        
        
# Execution point

monster = Monster(420, 69)
monster.attack()
print(monster)

# # Alt Approaches:
# # # Apparently you don't need lines 9 -> 11
# # # Line 18 can be replaced with self.damage = damage
# # # Replace __str__ with __repr__

# class Entity:
#     def attack(self):
#         print(f'Attack deals {self.damage} damage')


# class Monster(Entity):
#     def __init__(self, health, damage):
#         self.damage = damage
#         self.health = health
    
#     def __repr__(self):
#         return f'A monster with {self.health} HP'    

# monster = Monster(420, 69)
# monster.attack()
# print(monster)
