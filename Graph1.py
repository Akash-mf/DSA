class Graph:
  def __init__(self):
    self.vertices = {}

  def add_vertex(self, vertex):
    self.vertices[vertex] = []

  def add_edge(self, source, target):
    self.vertices[source].append(target)