# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    def __init__(self, n="", a=0):
        self.name =n
        self.age=a
    def __str__(self):
        s=f"{self.name} is {self.age} years old"
l=Dog("k",2)
a=Dog("e", 8)
s=Dog("u",9)
print(l)