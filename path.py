import node
import edge

class Path(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def get_start_node(self):
        return self.nodes[0]

    def get_end_node(self):
        return self.nodes[-1:]

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, edge):
        self.edges.append(edge)

    def nodes_to_edges(self, game):
        game.get_edges()

    def get_length(self):
        length = 0
        for e in self.edges:
            length += e.get_weight()
        return length

    def __str__(self):
        ret_str = "Path list of nodes "
        for i in self.nodes:
            ret_str += "{} ,".format(i.get_name())
        return ret_str