class Point:
    def __init__(self, x_coord, y_coord):
        self._x_coord = x_coord
        self._y_coord = y_coord

    def get_x_coord(self):
        return self._x_coord
    
    def get_y_coord(self):
        return self._y_coord
    
    def distance_to(self, point_object):
        distance_one = (self._x_coord - point_object.get_y_coord()) ** 2
        distance_two = (point_object.get_x_coord() - self._y_coord) ** 2
        
        return (distance_one + distance_two) ** 0.5



class LineSegment:
    def __init__(self, endpoint_1, end_point_2):
        self._endpoint_1 = endpoint_1
        self._endpoint_2 = end_point_2
    
    def get_endpoint_1(self):
        x_coord = self._endpoint_1.get_x_coord()
        y_coord = self._endpoint_1.get_y_coord()
        return f'{x_coord}, {y_coord}'
    
    def get_endpoint_2(self):
        x_coord = self._endpoint_2.get_x_coord()
        y_coord = self._endpoint_2.get_y_coord() 
        return f'{x_coord}, {y_coord}'
    
    def length(self):
        return self._endpoint_1.distance_to(self._endpoint_2)
    
    def slope(self):
        return (self._endpoint_1.get_y_coord() - self._endpoint_2.get_y_coord()) / (self._endpoint_1.get_x_coord() - self._endpoint_2.get_x_coord())
    
    def is_parallel_to(self, lineSegment):
        print(f'{self.slope()} self.slope')
        print(f'{lineSegment.slope()} lineSegment.slope')
        if self.slope() == lineSegment.slope():
            return True
        else:
            return False

# Not sure if code works, Check the is_parallel_to function is working
#   and that the slopes compare bs(num_1 - num_2) < 0.000001**

# video time 1:13:36

point_1 = Point(7,4)
point_2 = Point(-6,18)
print(point_1.distance_to(point_2))
line_seg_1 = LineSegment(point_1,point_2)
print(line_seg_1.length())
print(line_seg_1.slope())

point_3 = Point(-2,2)
point_4 = Point(24, 12)
line_seg_2 = LineSegment(point_3,point_4)
print(line_seg_1.is_parallel_to(line_seg_2))