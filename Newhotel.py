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
#       print self.d.price

    def show(self):
            print "in show"
            print self.name,self.price

m = Menu('dosa','25')
m.additem()
m.getitem('dosa')

#m.show()


#Menu.additem('idly','25')
#m.additem()


