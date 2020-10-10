class Animal():

    def __init__(self, id, name, species, status, location_id, customer_id):
        self.id = id
        self.name = name
        self.species = species
        self.status = status
        self.location_id = location_id
        self.customer_id = customer_id

    def __repr__(self):
        return f"{self.name} is a {self.species}"


animal = Animal(1, 'jack', 'dog', 'good boy', 1, 1)

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
#    def __init__(self, animal_id, name, species, status, location_id, customer_id):
#        self.animal_id = animal_id
#        self.name = name
#        self.species = species
#        self.status = status
#        self.location_id = location_id
#        self.customer_id = customer_id
#    def __repr__(self):
#        return f"{self.name} is a {self.species}"
    # def __repr__(self):  
    #    return "id: % s Name:% s Species:% s" % (self.animal_id, self.name, self.species) 
