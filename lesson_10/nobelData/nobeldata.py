import json

class NobelData:
    def __init__(self):
        self._file = open('nobels.json', 'r')  
        self._data = json.load(self._file)
        
    def get_data(self):
        return self._data
    
    def search_nobel(self, year, category):
        data = self._data['prizes']
        names = []
    
        for object in data:
            if year == object['year'] and category == object['category']:
               for i in range(len(object['laureates'])):
                  names.append(object['laureates'][i]['surname'])
        
        
        return sorted(names)



nd = NobelData()
# print(nd.get_data())
print(nd.search_nobel("1998", "peace"))
            