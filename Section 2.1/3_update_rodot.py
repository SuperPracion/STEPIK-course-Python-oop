class Robot:
    def set_name(self, name):
        self.name = name

    def say_hello(self):
        if hasattr(self, 'name'):
            print(f'Hello, human! My name is {self.name}')
        else:
            print('У робота нет имени')

    def say_bye(self):
        print('See u later alligator')



c3po = Robot()
c3po.say_hello() # печатает У робота нет имени
c3po.set_name('R2D2')
c3po.say_hello() # печатает Hello, human! My name is R2D2
c3po.say_bye() # печатает See u later alligator

r = Robot()
r.set_name('Chappy')
r.say_hello()# печатает Hello, human! My name is Chappy