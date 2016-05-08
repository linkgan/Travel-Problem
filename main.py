

"""
    Included packages

"""

import copy
from math import *


"""
    Include classes
"""

import graph as gr
import node as no
import edge as ed

###Global Variables
K_LEVEL = 6
NUM_BASE = 3


base_v1 = (pi / 3, 1)
base_v2 = (pi / 3, 0.5)
base_v3 = (pi / 6, sqrt(3) / 3)

axis = (pi / 3)

###


def createNodes(game):
    game.add_nodes(no.Node(name=game.num_nodes()))
    for i in range(K_LEVEL):
        game.add_nodes(no.Node(game.num_nodes(), 1, pi / 3 + pi / 3 * i))
        game.add_nodes(no.Node(game.num_nodes(), 0.5, pi / 3 + pi / 3 * i))
        game.add_nodes(no.Node(game.num_nodes(), sqrt(3) / 3, pi / 6 + pi / 3 * i))


def createEdges(game):
    f = open('edges.txt', 'r')
    for line in f:
        e = line.split(',')
        n1 = int(e[0])
        n2 = int(e[1])
        new_edge = ed.Edge(game.get_node(n1), game.get_node(n2))
        game.add_edges(new_edge)

def print_node_list(nodes):
    ret_str = "Node sequence: ("
    for i in nodes:
        ret_str += "{} ,".format(i.get_name())
    ret_str += ")"
    print ret_str
    return None


def main():
    game_nodes = gr.Graph()
    createNodes(game_nodes)
    createEdges(game_nodes)
    game_nodes.set_neighbors()
    END = False
    while(not END):
        game_nodes.display_nodes()
        start_loc = int(raw_input("Start Node: "))
        end_loc = int(raw_input("End Node: "))
        game_nodes.find_paths(start_loc, end_loc)
        print("Num paths = " + str(game_nodes.num_paths()))
        for p in game_nodes.get_paths():
            print(p)
        ask_end = raw_input("Do you want to continue? (Y/N): ")
        if(ask_end == 'N'): END = True
        game_nodes.reset_paths()

if __name__ == "__main__":
    main()



