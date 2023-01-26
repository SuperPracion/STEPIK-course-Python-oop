class Zebra:
    def __init__(self, start_color=False):
        self.color = start_color

    def which_stripe(self):
        if self.color:
            print('Полоска черная')
        else:
            print('Полоска белая')

        self.color = not self.color


z1 = Zebra()
z1.which_stripe() # печатает "Полоска белая"
z1.which_stripe() # печатает "Полоска черная"
z1.which_stripe() # печатает "Полоска белая"

z2 = Zebra()
z2.which_stripe() # печатает "Полоска белая"