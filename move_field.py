# By Kamran Bigdely Nov. 2020
# Move Field (attribute)
class Gun:
    def __init__(self, name, bullet_count=10):
        self.name = name
        self.bullet_count = bullet_count
        # initialize with 10 bullets in each gun's cathridge.
        self.num_cathridge_bullets = [bullet_count]

    def shoot(self):
        print('shoot')

    def reload(self):
        print('reload')
        for _ in range(len(guns)):
                self.num_cathridge_bullets[0] = self.bullet_count 


class Player:
    def __init__(self, guns):        
        self.guns = guns
        
        
    def fire_once(self):
        for i, gun in enumerate(self.guns):
            if gun.num_cathridge_bullets[i] > 0:
                gun.shoot()
                gun.num_cathridge_bullets[i] -= 1
                break
        

def game_loop():
    while (True):
        
        player.fire_once()
        for gun in player.guns:
            gun.reload()
            print(gun.num_cathridge_bullets)
        # other logic here.
        break

guns = [Gun('pistol'), Gun('rifle')]
player = Player(guns)
game_loop()


