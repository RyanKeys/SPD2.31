# By Kamran Bigdely
# Extract superclass


class Character:

    def __init__(self, health=100):
        self.health = health

    def take_damage(self, damage):
        self.health -= damage

class AngryMushroom(Character):
    
    def __init__(self):
        super().__init__()
        
    def spread_poison(self):
        print('spreading poison!')


class AngryBot(Character):
    
    def __init__(self):
        super().__init__()
        self.n_bullets = 40
        
    def punch_iron_fist(self):
        print("punching with iron fist!")
        
    def shoot(self):
        print("shot a bullet!")
        self.n_bullets -= 1



class AgressiveAlligator(Character):
    
    def __init__(self):
        super().__init__()
        
    def bite(self):
        print('bitting!')


angryMushroom = AngryMushroom()
print("initial health level:", angryMushroom.health)
angryMushroom.take_damage(25)
print("took damage!")
print("current health level:",angryMushroom.health)
