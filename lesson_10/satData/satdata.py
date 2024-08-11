import json

class SatData:
    def __init__(self):
        self._read_sat = open('sat.json', 'r')
        self._sat_data = json.load(self._read_sat)
    
    def get_sat(self): # returns keys from sat.json file
        print(self._sat_data.keys())
        print("\n")
        print(self._sat_data['meta']['view'].keys())
        print("\n")
        print(self._sat_data['data'])
    
    def save_as_csv(self, dbn_list):
        csv_file = 'DBN, School Name, Number of Test Takers, Critical Reading Mean, Mathematics Mean, Writing Mean, \n'
        
        for i in range(len(self._sat_data['data'])):
            print()
            if self._sat_data['data'][i][8] in dbn_list:
                dbn = self._sat_data['data'][i][8]
                school = self._sat_data['data'][i][9]
                tests = self._sat_data['data'][i][10]
                reading = self._sat_data['data'][i][11]
                math = self._sat_data['data'][i][12]
                schoolwriting = self._sat_data['data'][i][13]

                if ',' in school:
                    school = f'"{school}"'

                dbn_line = f'{dbn}, {school}, {tests}, {reading}, {math}, {schoolwriting} \n'
                csv_file = csv_file + dbn_line
        
        with open('output.csv', 'w') as outfile:
            outfile.write(csv_file)


sd = SatData()
dbns = ["02M303", "02M294", "01M450", "02M418"]
sd.save_as_csv(dbns)