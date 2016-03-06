class Menu:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.d ={}

    def additem(self):
        d = {self.name:self.price}
#        d.update({self.name:self.price})
        print d
        return d

    def getitem(self, name):
        print self.price
#The below statement doesnt work
#       print self.d.items()

    def show(self):
            print "in show"

m = Menu('dosa','25')
m.additem()
m.getitem('dosa')
m.show()

#m.show()


#Menu.additem('idly','25')
#m.additem()


