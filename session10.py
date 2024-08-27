import math

class Polygon():
    def __init__(self, num_edges, circumrad) -> None:
        self.num_edges = num_edges
        self.circumrad = circumrad
        
    def __repr__(self) -> str:
        return "Objective 1 function that implements a Ploygon class"
    
    def __gt__(self, other):
        return self.num_edges > other.num_edges
    
    def __eq__(self, other):
        return self.num_edges == other.num_edges and self.circumrad == other.circumrad

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
