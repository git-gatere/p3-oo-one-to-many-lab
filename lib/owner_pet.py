class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    
    def __init__(self, name, pet_type, owner=None):
        self.name = name
        Pet.pet_type_check(pet_type)
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)


    @classmethod
    def pet_type_check (cls , pet_type):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Pet type must be a value in PET_TYPES")
        
        

    

class Owner:
    all_pets = []
    def __init__(self, name):
        self.name = name

    @classmethod
    def pets(self):
        Owner.all_pets.append([pet for pet in Pet.all if pet.owner == self])


    @classmethod
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Input object is not of type Pet")
        pet.owner = self 


    def owner(self, owner):
        if not (isinstance(owner, Owner) or not owner):
            raise Exception("Object is not of type Owner")
        self._owner = owner
