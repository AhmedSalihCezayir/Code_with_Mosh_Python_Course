# This is a good multiple inheritance example. Although FlyingFish classs inherits 2 other classes,
# there is no problem because both Flyer and Swimmer classes has nothing in common. But if they had
# sth in common, it might create a problem. For instance, if both classes had a method like walk()
# and FlyingFish class did not implement its walk() method, when we call the walk() method with a
# FlyingFish object, it would run the first inherited class' walk() method. In this case, Flyer's walk()
# method would be executed.
class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimmer):
    pass
