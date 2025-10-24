class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.adj_dict = dict()
        self.create_adj()

    def create_adj(self):
        for start, dist in self.edges:
            if start in self.adj_dict:
                self.adj_dict[start].append(dist)
            else:
                self.adj_dict[start] = [dist]


    def get_path(self, start, dist, path=[]):
        path = path + [start]
        if start == dist:
            return  [path]
        if start not in self.adj_dict:
            return []
        paths = []
        for vertex in self.adj_dict[start]:
            if vertex not in path:
                new_paths = self.get_path(vertex, dist, path)
                for p in new_paths:
                    paths.append(p)
        return  paths

routes = [
    ("Kerman", "Yazd"),
    ("Kerman", "Esfahan"),
    ("Esfahan", "Mashhad"),
    ("Yazd", "Mashhad"),
    ("Yazd", "Esfahan"),
    ("Mashhad", "Tehran"),
]
my_graph = Graph(routes)
print(my_graph.get_path("Kerman", "Tehran"))
