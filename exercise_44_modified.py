class Pet(object):

    def MySound(self):
        print("My sound is... ", end="")


class Dog(Pet):
    #pass
    def MySound(self):
        super().MySound()
        print("barking! ", end="")

class DoubleDog(Dog):

    def MySound(self):
        super().MySound()
        print("barking! ", end="")

class Kitty(Pet):

    def MySound(self):
        super().MySound()
        print("Meow! ", end="")


class HybridOne(Dog, Kitty):

    def MySound(self):
        super().MySound()
        print("Kill me... ", end="")

class HybridTwo(DoubleDog, HybridOne):

    def MySound(self):
        super().MySound()
        print("please!")

pet = HybridTwo()
pet.MySound()

print(HybridTwo.__mro__)
