#Implementing DFS for graphs

#In this exercise, you will implement a depth first search algorithm to traverse a graph.

#Recall the steps:

#Start at any vertex

#Add the vertex to the visited vertices list
#For each current node's adjacent vertex
#If it has been visited -> ignore it
#If it hasn't been visited -> recursively perform DFS
#To help you test your code, the following graph has been loaded using a dictionary.

#graph = {
  #'0' : ['1','2'],
  #'1' : ['0', '2', '3'],
  #'2' : ['0', '1', '4'],
  #'3' : ['1', '4'],
  #'4' : ['2', '3']
#}

graph = {
  '0' : ['1','2'],
  '1' : ['0', '2', '3'],
  '2' : ['0', '1', '4'],
  '3' : ['1', '4'],
  '4' : ['2', '3']
}


def dfs(visited_vertices, graph, current_vertex):
    # Check if current_vertex hasn't been visited yet
    if current_vertex not in visited_vertices:
        print(current_vertex)
        # Add current_vertex to visited_vertices
        visited_vertices.add(current_vertex)
        for adjacent_vertex in graph[current_vertex]:
            # Call recursively with the appropriate values
            dfs(visited_vertices, graph, adjacent_vertex)


dfs(set(), graph, '0')