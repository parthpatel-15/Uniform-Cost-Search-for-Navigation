# Uniform-Cost-Search-for-Navigation

This Python program showcases the Uniform Cost Search (UCS) algorithm for finding the shortest path between places in a network. It uses a custom-defined graph to represent the connections between different places and their respective locations. The code consists of the following components:

Node class: Represents a node in the search tree, used to construct the UCS tree. The tree helps visualize the exploration process, and the class computes the cost from the root and heuristic values.

State class: Retrieves state information for navigation, such as the current place and its connections in the network.

TreePlot class: Creates a visual representation of the search tree, helping to visualize the exploration process and the path to the goal.

UcsSearch function: Performs the UCS search by exploring the network to find the shortest path to the goal place.

# Sample Usage:
Finding Shortest Path: The main function UcsSearch() demonstrates the UCS algorithm in action. It explores the network to find the shortest path from the initial place to the goal place (AI Lab in this example). The resulting path is printed, and the search tree is displayed.

# Note:
The code visualizes the UCS search tree and path, helping you understand how the algorithm explores different places to find the shortest path.
You can use this code to find the shortest path in your own network by modifying the connections and location dictionaries.
Feel free to use or modify this code to explore navigation in your network and find the shortest paths between different places.
