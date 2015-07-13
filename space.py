import sample
import math
pi = math.pi

# Create space where dht will be embedded  
class Space():
    
    def __init__(self):
        self.constraints=[]
        self.members = {} 
    
    # Raise an error if the location is not in space
    def in_space(self,location):
        const = self.constraints
        num_constraints = len(const)
        num_coordinates = len(location)
        
        assert num_coordinates == num_constraints

        for i in range(num_constraints):
            coord = location[i]
            lower = const[i][0]
            upper = const[i][1]
            
            in_boundary = (lower <= coord) and (coord <= upper)
            assert in_boundary 

class S1(Space):

    def __init__(self):
        self.constraints = [(0, 2* pi)]
        self.members = {}

    def insert_member(self, member, location):
        self.in_space(location) # check if the location is valid 
        self.members[member] = location 

    def members_in_range(self, start, end):
        members = self.members
        def in_range(x, start, end):
            loc = members[x][0]
            return (start <= loc and loc <= end)
        return [x for x in members if in_range(x,start,end)]

    def count_members_in_range(self, start, end):
        return len(self.members_in_range(start, end))
