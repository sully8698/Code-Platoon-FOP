import json

class DuplicateNameError(Exception):
    pass

class NeighborhoodPets:
    def __init__(self):
        self._pet_data = {}

    def add_pet(self, pet_name, owner, species):

        try:
            if pet_name in self._pet_data:
                raise DuplicateNameError
            
            else:
                pet_name_object = {'owner' : owner, 'species' : species}
                self. _pet_data[pet_name] = pet_name_object
                print(f'{pet_name} : {self._pet_data[pet_name]}')

        except DuplicateNameError:
            print(f'{pet_name} Name already exists')
    
    def delete_pet(self, pet_name):
        try:
            del self._pet_data[pet_name]
        
        except KeyError:
            print(f'{pet_name} not in library')
    
    def get_owner(self, pet_name):
        if pet_name in self._pet_data:
            return self._pet_data[pet_name]['owner']
    
    def save_as_json(self, file_name):
        with open(f'{file_name}', 'w') as outfile:
            json.dump(self._pet_data, outfile)
    
    def read_json(self, file_name):
        with open(f'{file_name}', 'r') as infile:
            pet_data = json.load(infile)
            print(pet_data)
            self._pet_data = pet_data
    
    def get_all_species(self):
        species_list = []
        for key in self._pet_data:
            species_list.append(self._pet_data[key]['species'])
        return set(species_list)


pets = NeighborhoodPets()
pets.add_pet('kujo', 'sandy', 'rotty dog')
pets.add_pet('joey', 'Kenny', 'tabi cat')
pets.add_pet('kujo', 'sandy', 'dogger')


