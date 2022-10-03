class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    def get_paths(self, start, end, path=None, deep=0, max_deep=None):
        path = [] if path is None else path
        path = path + [start]
        deep += 1
        if start == end:
            return [path]
        elif start not in self.graph_dict or deep == max_deep:
            return []
        else:
            paths = []
            for node in self.graph_dict[start]:
                if node not in path:
                    new_paths = self.get_paths(node, end, path, deep=deep, max_deep=max_deep)
                    for p in new_paths:
                        paths.append(p)
            return paths

    def get_shortest_paths(self, start, end):
        paths = self.get_paths(start, end)
        min_length = min([len(path) for path in paths])
        shortest_paths = [path for path in paths if len(path) == min_length]
        return shortest_paths


if __name__ == '__main__':
    route_graph = Graph([
        ('Kaliningrad', 'Moscow'),
        ('Moscow', 'Saint-Petersburg'),
        ('Moscow', 'Dubai'),
        ('Moscow', 'Tbilisi'),
        ('Kaliningrad', 'Istanbul'),
        ('Istanbul', 'Tbilisi'),
        ('Saint-Petersburg', 'Tbilisi'),
        ('Dubai', 'Hong Kong'),
        ('Moscow', 'Kaliningrad'),
        ('Tbilisi', 'Hong Kong'),
        ('Tbilisi', 'Moscow')
    ])

    kgd_hkg_paths = route_graph.get_paths('Kaliningrad', 'Hong Kong', max_deep=3)
    shortest_kgd_tbs_paths = route_graph.get_shortest_paths('Kaliningrad', 'Tbilisi')
    print(kgd_hkg_paths)
    print(shortest_kgd_tbs_paths)