class Attacker:
    def stats(self):
        print("Attack: 100")
        

class Defender:
    def stats(self):
        print("Defense: 100")


class Player(Defender, Attacker):
    pass


p = Player()

p.stats()

print(Player.__mro__)