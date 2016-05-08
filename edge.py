import node
from math import *

class Edge(object):
    """Attributes:
        n1: first node on edge
        n2: second node on edge
        weight: the weight/length of the edge
        """

    def __init__(self, n1, n2):
        if (n1 is None or n2 is None): raise ValueError
        self.n1 = n1
        self.n2 = n2
        self.weight = sqrt((n2.pol2cart('x') - n1.pol2cart('x')) ** 2 + (n2.pol2cart('y') - n1.pol2cart('y')) ** 2)

    def get_weight(self):
        return self.weight

    def get_edge_pair(self):
        return (self.n1, self.n2)

    def get_neighbor(self, node):
        if (self.n1 == node):
            return self.n2
        else:
            return self.n1

    def is_neighbor(self, node):
        return (self.n1 == node or self.n2 == node)

    def is_edge(self, n1, n2):
        return (self.n1 == n1 and self.n2 == n2)

    def __str__(self):
        return "Edge between node {} and node {}".format(self.n1.get_name(), self.n2.get_name())