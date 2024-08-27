import math

class Polygon:
    def __init__(self, num_edges, circumrad) -> None:
        self._num_edges = num_edges
        self._circumrad = circumrad

    def __len__(self):
        return len(self._num_edges -2)

    def __iter__(self):
        print ("Calling Polygon __iter__")   
        return self.PolygonIterator(self)
    
        class PolygonIterator:
            def __init__(self, polyobj):            
                print ("Calling PolygonIterator __init__")
                self._polyobj = polyobj
                self._index = 0

            def __iter__(self):
                return self
            
            def __next__(self):
                item = self._polyobj._numedges[self._index]
                self._index += 1
                return item

            def __repr__(self) -> str:
                return "Objective 1 function that implements a Ploygon class"
            
            def __gt__(self, other):
                return self._num_edges > other._num_edges
            
            def __eq__(self, other):
                return self._num_edges == other._num_edges and self._circumrad == other._circumrad

            def edges(self):
                return self.num_edges

            def vertices (self):
                return self.num_edges 
            
            def interior_angle (self):
                inter_angl = (self.num_edges - 2) * (180/self.num_edges)
                return inter_angl
            
            def edge_length(self):
                edge_l = 2 * self.circumrad * math.sin(math.pi / self.num_edges)
                return edge_l
            
            def apotheum (self):
                a = self.circumrad * math.cos(math.pi/self.num_edges)
                return a
            
            def area (self):
                area = 0.5 * self.num_edges * self.edge_length() * self.apotheum() 
                return area 
            
            def perimeter (self):
                perimeter = self.num_edges * self.edge_length()
