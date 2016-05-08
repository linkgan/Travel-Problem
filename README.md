##Travel Problem Read Me

##Synopsis:
I was searching for math brainteasers and came across this problem on the website, _Braingle_
which was ranked as the hardest problem on Braingle's website.

The problem involves counting the number of paths from A to B where A and B
are the outer nodes of a hexagon. The total number of outer vertices is 6.
Each outer vertex is connected to other outer vertex via a straight path.

Where these paths intersect, they form another node in the graph.

Problem prompt from 
[Braingle](http://www.braingle.com/brainteasers/teaser.php?op=2&id=44101&comm=0). It was listed as the "hardest" problem on this list.

##Code Example
To run the problem solver, run `main()`

I basically implemented from scratch a VERY basic Graph structure, with nodes and edges.

Basic functionality include 

#####Graph class:
* `graph.display_nodes()`: Visually prints all the nodes in the graph using `import matplotlib.pyplot as plt`

#####Node class:
* `node.add_neighbor_edges()`: Add list of edges connected to this node
* `node1.get_distance(node2)`: Returns _physical_ distance between 2 nodes, even if there doesn't exist an edge between these two nodes.

#####Edge class:
* `edge.get_edge_pair()`: Returns the 2 nodes on the end of this edge
* `edge.is_edge(n1,n2)`: Given 2 nodes, determine whether this is the correct edge
* `edge.get_neighbor(node)`: Gets the second node given the first node in the pair


'''python
import graph as gr

def main():
    game_nodes = gr.Graph()
    createNodes(game_nodes)
    createEdges(game_nodes)
    game_nodes.set_neighbors()
    
    while(1):
        game_nodes.display_nodes()
        start_loc = int(raw_input("Start Node: "))
        end_loc = int(raw_input("End Node: "))
        game_nodes.find_paths(start_loc, end_loc)
        print("Num paths = " + str(game_nodes.num_paths()))
        for p in game_nodes.get_paths():
            print(p)
        
        game_nodes.reset_paths()

##To dos

While the list of nodes to traverse for a given solution path has been determined, I have not implemented the drawing of all the possible paths visually. This will help an individual user more easily understand what is happening in real time.

It'll probably look something like `graph.display_solution(path)` where "path" is the solution path, already contained in the Graph object. The `graph.display_solution(path)` would simply output lines onto the screen after calling `graph.display_nodes()`

