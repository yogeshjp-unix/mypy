class Menu:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def additem(self):
        d = {}
        d = {self.name:self.price}
#        d.update({self.name:self.price})
        print d
        return d

    def getitem(self, name):
        print self.price


    def show(self):
            print "in show"
            print self.name,self.price

m = Menu('dosa','25')
m.additem()
m.getitem('dosa')

#m.show()


#Menu.additem('idly','25')
#m.additem()


