class Person:
    """Create a new person"""
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def new(self):
        print("Hi, my name is " + self.fname)

newPerson = Person("Dony","Beclman")

print(newPerson)
print(newPerson.fname, newPerson.lname)

newPerson.fname = "Cris"
print(newPerson.fname, newPerson.lname)

newPerson.new()

class Player:
    def __init__(self, fname,lname):
        self.fname = fname
        self.lname = lname
class NewPlayer(Player):
    def __init__(self, fname, lname,total):
        Player.__init__(self,fname,lname)
        self.total = total

    def getDetails(self):
            return "%s %s has spent %s in total" % (self.fname, self.lname, self.total)

newP = NewPlayer("Dony","Beclman",1000)
print(newP.getDetails())
