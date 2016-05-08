import matplotlib.pyplot as plt
import copy

from node import *
import edge
import path

class Graph(object):

    def __init__(self, nodes=[], edges=[]):
        self.list_of_nodes = nodes
        self.list_of_edges = edges
        self.list_of_paths = []

    def add_nodes(self, node):
        self.list_of_nodes.append(node)

    def add_edges(self, edge):
        self.list_of_edges.append(edge)

    def add_paths(self, path):
        self.list_of_paths.append(path)

    def num_nodes(self):
        return len(self.list_of_nodes)

    def num_edges(self):
        return len(self.list_of_edges)

    def num_paths(self):
        return len(self.list_of_paths)

    def get_node(self, name):
        for n in self.list_of_nodes:
            if (n.is_name(name)): return n
        return None

    def get_edges(self):
        return self.list_of_edges

    def get_paths(self):
        return self.list_of_paths

    def reset_paths(self):
        self.list_of_paths = []

    def display_nodes(self):
        for n in self.list_of_nodes:
            plt.plot(n.pol2cart('x'), n.pol2cart('y'), 'ro', )
            plt.annotate(n.get_name(), xy=n.pol2cart())
        plt.show()

    # Set the neighbors of all nodes in game using known edges
    def set_neighbors(self):
        for e in self.list_of_edges:
            for n in self.list_of_nodes:
                if (e.is_neighbor(n)):
                    n.add_neighbor_edges(e)

    def find_paths(self, start, end, traversed_nodes=[]):
        traversed_nodes.append(start)
        valid_nodes = []

        start_node = self.get_node(start)
        end_node = self.get_node(end)

        #Calculate maxixum allowed distance between current node and final node
        MAX_DIST = start_node.get_distance(end_node)

        if (MAX_DIST == 0):
            # Function ends if distance = 0 implying it is at final destination
            temp_list_nodes = []
            for i in traversed_nodes:
                temp_list_nodes.append(self.get_node(i))
            # temp_list_nodes.append(end_node)
            self.add_paths(path.Path(nodes=temp_list_nodes))
            return 0
        
        else:
            # Only append current node when the current node is not the final destination
            next_nodes = copy.copy(start_node.get_neighbor_nodes())

            # Remove traversed nodes from the total possible set of nodes to visit
            for t in traversed_nodes:
                try:
                    next_nodes.remove(self.get_node(t))
                except ValueError:
                    pass

            for n in next_nodes:
                # Check if distance between the next possible nodes and final node is less than current max distance
                if (n.get_distance(end_node) <= MAX_DIST):
                    # If distance criteria qualifies, then add that node to the list of possible nodes
                    valid_nodes.append(n)

            # Traverse list of nodes that are fit criteria by recursion
            for next_node in valid_nodes:
                self.find_paths(next_node.get_name(), end_node.get_name(), traversed_nodes=traversed_nodes)
                # After completing path, pop off the final node in the path traversed in order to reverse
                traversed_nodes.pop()
            return 1