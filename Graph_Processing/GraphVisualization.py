import networkx as nx
import matplotlib.pyplot as plt

class GraphVisualization:
    def __init__(self, i):
        self.visual = []
        self.index = i

    def add_edge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    def add_edges_from_matrix(self, mtx):
        for i in range(len(mtx)):
            for j in range(i, len(mtx)):
                if mtx[i][j] == 1:
                    self.add_edge(i, j)

    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.savefig(f"./Graph_Processing/graphs/{self.index}.png")
        plt.close()