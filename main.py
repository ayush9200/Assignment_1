# Assignment 1 Trains (Ayush Kumar Singh C0799530)
# Problem - To find the distance along a certain route,
# the number of different routes between two towns,
# the shortest route between two towns.

# Solutions -
# Distance Class will find out distance along a certain route (Working for questions A1, A2, A3, A4)
# ShortestPath Class will find the shortest route between two towns (Working for questions B3, B4)

import ShortestPath
import Distance

# Main class will call both module for solution
if __name__ == "__main__":
    Distance.calculate_distance()   # Calling method from Distance module
    ShortestPath.find_shortest_path()   # Calling method from ShortestPath module

