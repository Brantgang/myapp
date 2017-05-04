class Animal(object):
    def running(self):
        print("animal is running")


class Dog(Animal):
    def running(self):
        print('dog is running')
    def flying(self):
        print('flying')
class  Bird(Animal):
    def check(self):
        print('checking')


class Pterosaur(Dog,Bird):
    pass
p=Pterosaur()
p.check()
p.flying()
