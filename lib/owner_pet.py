class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Can only add Pet objects")
        self._pets.append(pet)
        pet.owner = self   # make sure pet knows its owner

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner   # ✅ link pet to owner if given

        Pet.all.append(self)

        # if owner provided, auto-add pet to owner
        if owner is not None:
            owner.add_pet(self)
