import numpy as np
from math import *


R = 100

class Node(object):
    """Attributes:
        rho: the length of the radius
        omega: the rotation of the coordinate
        name: as the id of the node
        edges: edges connected to this current node
    """

    def __init__(self, name='N/A', rho=0, theta=0):
        self.rho = rho
        self.theta = theta
        self.name = name
        self.scale = R
        self.edges = []
        self.paths = []

    # Defining equality condition for nodes

    def __eq__(self, other):
        if isinstance(other, Node):
            return (self.rho == other.rho and self.theta == other.theta)
        return NotImplemented

    def pol2cart(self, xy='xy'):
        x = self.rho * self.scale * np.cos(self.theta)
        y = self.rho * self.scale * np.sin(self.theta)
        if (xy == 'x'):
            return (x)
        elif (xy == 'y'):
            return (y)
        else:
            return (x + 1, y + 1)

    def is_name(self, name):
        return self.name == name

    def add_neighbor_edges(self, edge):
        self.edges.append(edge)

    def num_neighbors(self):
        return len(self.edges)

        """Get Statements for Node Class"""

    def get_name(self):
        return self.name

    def get_neighbor_nodes(self):
        nodes = []
        for e in self.edges:
            nodes.append(e.get_neighbor(self))
        return nodes

    # Gets the list of edges of current node
    def get_neighbor_edges(self):
        return self.edges

    # Calculates distance between current node and "node"
    def get_distance(self, node):
        return sqrt((node.pol2cart('x') - self.pol2cart('x')) ** 2 + (node.pol2cart('y') - self.pol2cart('y')) ** 2)

    def __str__(self):
        ret_str = "Name: {} \nRho: {} \nTheta: {}\nNum Neighbors: {}\n".format(self.name, self.rho, self.theta,
                                                                               self.num_neighbors())
        # for n in self.get_neighbor_nodes():
        #   ret_str = ret_str + "{} is a neighbor of {}\n".format(n.get_name(),self.get_name())
        return ret_str
