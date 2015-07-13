from random import random as rand
from space import *

# Utils to sample 

class Sample():
   
    def range_samp(self,a,b):
        random_value =  a + (b - a) * rand() 
        return random_value

    # Zone is a constraint on the coordinates of the space
    def zone_sample(self,zone):
        random_position = [self.range_samp(x[0],x[1]) for x in zone]
        return random_position           

    # Sample uniformly from a given space
    def u_samp(self,space):
        const = space.constraints
        return self.zone_sample(const)
