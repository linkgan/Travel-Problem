#Travel Problem/"Six Villages Problem" Read Me

##Synopsis:
I was searching for math brainteasers and came across this problem on the website, _Braingle_
which was ranked as the hardest problem on Braingle's website.

The problem involves counting the number of paths from A to B where A and B
are the outer nodes of a hexagon. The total number of outer vertices is 6.
Each outer vertex is connected to other outer vertex via a straight path.

Where these paths intersect, they form another node in the graph.

Problem prompt from 
[Braingle](http://www.braingle.com/brainteasers/teaser.php?op=2&id=44101&comm=0). It was listed as the "hardest" problem on this list.

##Code Explanation
To run the problem solver, run `main()`

I basically implemented from scratch a VERY basic Graph structure, with nodes and edges.

Basic functionality include 

#####Graph class:
Here are some functions that are beyond the basic population of the graph. Those functions are `add_nodes()`, `add_edges()`
* `graph.display_nodes()`: Visually prints all the nodes in the graph using `import matplotlib.pyplot as plt`
* `graph.set_neighbors()`: Goes through every node in the graph, and using the list of edges, sets the known neighbor of each node based on the edge that's connected to the node
* `graph.find_paths(n1, n2)`: This is the key to solving the problem. Given the beginning node, and end node, the funcion will add a solved path to the `graph`'s list of solved paths. This is a recursive function, so it continues to apply this function, resetting the starting node to the next node in the path. 

#####Node class:
* `node.add_neighbor_edges()`: Add list of edges connected to this node
* `node1.get_distance(node2)`: Returns _physical_ distance between 2 nodes, even if there doesn't exist an edge between these two nodes.

#####Edge class:
* `edge.get_edge_pair()`: Returns the 2 nodes on the end of this edge
* `edge.is_edge(n1,n2)`: Given 2 nodes, determine whether this is the correct edge
* `edge.get_neighbor(node)`: Gets the second node given the first node in the pair

#####Path class:
is a collection of nodes and edges that form a solution path.


#####`main()` function explained:

```python
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
```

* `edges.txt` is a global variable that contains the hard coded edge relationships. This should be dynamically generated in theory based on the specifications of the graph.
* `game_nodes = gr.Graph()`: initializes the game/graph.
* `start_loc`, `end_loc`: User inputs the beginning and end node IDs to solve for.
* `find_paths()`: Adds the list of solved paths based on the start and end nodes to the graph object.
* Few lines simply prints the solution to console, so the user can see in list form, the path of the traversed solution. The solution list is the node ids. The node ids can be seen by printing the nodes from graph using `graph.display_nodes()`

##To dos

While the list of nodes to traverse for a given solution path has been determined, I have not implemented the drawing of all the possible paths visually. This will help an individual user more easily understand what is happening in real time.

It'll probably look something like `graph.display_solution(path)` where "path" is the solution path, already contained in the Graph object. The `graph.display_solution(path)` would simply output lines onto the screen after calling `graph.display_nodes()`

A dynamically generated list of edges will need to be generated to replace `edges.txt`.

