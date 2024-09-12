
class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = [] 

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type.")
        self.pet_type = pet_type
        self.owner = owner

        
        if owner:
            owner.add_pet(self)

        
        Pet.all.append(self)

    def __repr__(self):
        return f"<Pet name: {self.name}, type: {self.pet_type}>"

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("The object passed is not of type Pet.")
        pet.owner = self 
        self._pets.append(pet)

    def get_sorted_pets(self):
        """Returns a list of pets sorted by their names."""
        return sorted(self._pets, key=lambda pet: pet.name)


