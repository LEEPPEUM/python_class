
class NamedList(list):
    def __init__(self, a_name):
        list.__init__([])
        self.name = a_name
        self.dob = None
johnny = NamedList('John Paul Jones')
normelvar = 3
johnny.dob = '2017.10.10'
johnny.extend(['Composer', 'Arranger', 'Musician'])

for attr in johnny:
    print(johnny.name + ' is a ' + attr + ', -' + johnny.dob)
