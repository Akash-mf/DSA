#This exercise has two steps.
# In the first one, you will modify this code so that it can be used to create a weighted graph.
# To do this, you can use a hash table to represent the adjacent vertices with their weights.
# In the second step, you will build the weighted graph.

class WeightedGraph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        # Initialize an empty list to hold the edges of this vertex
        self.vertices[vertex] = []

    def add_edge(self, source, target, weight):
        # Append a tuple (target, weight) to the adjacency list of the source vertex
        if source in self.vertices:
            self.vertices[source].append((target, weight))
        else:
            print(f"Vertex '{source}' does not exist.")

    def __str__(self):
        # Provide a string representation of the graph
        graph_str = ""
        for vertex, edges in self.vertices.items():
            edges_str = ", ".join([f"({target}, {weight})" for target, weight in edges])
            graph_str += f"{vertex} -> {edges_str}\n"
        return graph_str


# Create an instance of WeightedGraph
my_graph = WeightedGraph()

# Create the vertices
my_graph.add_vertex('Paris')
my_graph.add_vertex('Toulouse')
my_graph.add_vertex('Biarritz')

# Create the edges
my_graph.add_edge('Paris', 'Toulouse', 678)
my_graph.add_edge('Toulouse', 'Biarritz', 312)
my_graph.add_edge('Biarritz', 'Paris', 783)

# Print the graph to see its structure
print(my_graph)


