'''Section 2: Classes in Python'''
'''
You have a robot with a name, a map, and a set of coordinates to represent where it is in the map.
You need to be able to move your robot around the map to survey the area, as different parts of the map have different values.
Fill in the robot class by filling in the constructor and adding a way to drive the robot.
In the map class, fill in the static method check_neighbors_of_4, which takes in a set of coordinates and returns the values of the cells around it.
In your main script, you should be able to move the robot around the map and see its neighbors.
You should also prevent the robot from driving off the map.
'''

from random import randint # For generating random numbers

class Robot:
    def __init__(self, name):
        ### YOUR CODE HERE ###

        '''Initialize all the variables needed for the robot --> A name, a 6x6 map, and starting coordinates of 0, 0'''

        ### YOUR CODE ENDS ###

    ### YOUR CODE HERE ###

        '''Write function (or functions) to move the robot in the grid and view its neighbors'''

    ### YOUR CODE ENDS ###

class Map:
    def __init__(self, size):
        self.size = size
        self.grid = [[randint(0, 10)] * self.size for i in range(self.size)] # Make size x size array of 0s using list comprehension
    
    @staticmethod # Note that this method should be static
    def check_neighbors_of_4(map_grid, coord_row, coord_col):
        neighbor_values = []

        ### YOUR CODE HERE ###

        '''Add all of the neighboring cells (4) --> Above, Below, Left, and Right'''

        ### YOUR CODE ENDS ###

        return neighbor_values

    def __str__(self): # This method is so we can print our Map directly
        return str(self.grid)

if __name__ == '__main__':
    # Set up our robot and print the map
    robot = Robot("Epsilon")
    print("Current map: " + robot.map)
    
    '''Call your drive function to move your robot around'''