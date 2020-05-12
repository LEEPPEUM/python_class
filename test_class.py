class Athlete:
    def__init__(self, value='Jane'):
        self.thing = value;
    def getAthlete(self):
        return self.thing
a = Athlete()
print(a.getAthlete())
b = Athlete('Holy')
Athlete.__init__(a,'Holy')
print(b.getAthlete())