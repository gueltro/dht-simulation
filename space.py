import sample
import math
pi = math.pi

# Create space where dht will be embedded  
class Space():
    
    def __init__(self):
        self.constraints=[]
        self.members = []
    
    # Raise an error if the location is not in space
    def in_space(self,location):
        const = self.constraints
        num_constraints = len(const)
        num_coordinates = len(location)
        
        assert num_coordinates == num_constraints

        for i in range(num_constraints):
            coord = location[i]
            lower = const[i][1]
            upper = const[i][1]
            
            in_boundary = (lower <= coord) and (coord <= upper)
            
            assert in_boundary 

class S1(Space):

    def __init__(self):
        self.constraints = [(0, 2* pi)]
    
