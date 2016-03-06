def f():
    class Basic(object):
        print "it is processed"
        def __init__(self,name):
            print "in __init__"
            self.name = name
            print self
        def show(self):
            print "in show"
            print self
            print 'Basic -- name: %s' % self.name

#print Basic
f()
x=Basic(2)
#print x
#x.show()

#unless you call the class to create an
#object the code will processed.
# It creates class and keeps it in memory.

