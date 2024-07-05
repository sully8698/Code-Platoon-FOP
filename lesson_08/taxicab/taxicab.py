class Taxicab:
        
        def __init__(self, xcoord, ycoord):
                self._xcoord = xcoord
                self._ycoord = ycoord
                self._odometer = 0
        
        def get_x_coord(self):
                return self._xcoord
        
        def get_y_coord(self):
                return self._ycoord
        
        def get_odometer(self):
                return self._odometer
        
        def move_x(self, moved):
                self._xcoord = self._xcoord + moved
                self._odometer = self._odometer + abs(moved)
        
        def move_y(self, moved):
                self._ycoord = self._ycoord + moved
                self._odometer = self._odometer + abs(moved)
        
        


       
taxi = Taxicab(2, 3)
print(taxi.get_x_coord())
taxi.move_x(3)
taxi.move_y(2)
print(taxi.get_x_coord())
print(taxi.get_y_coord())
print(taxi.get_odometer())
