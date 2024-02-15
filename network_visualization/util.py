import networkx as nx
import uuid
import numpy as np
import random


def get_test_graph(n_node: int, seed: int = 1234) -> nx.DiGraph:
    test_graph = nx.scale_free_graph(n=n_node, seed=seed)
    nx.set_node_attributes(test_graph, nx.betweenness_centrality(test_graph), name='betweenness_centrality')
    nx.set_node_attributes(test_graph, dict(nx.degree(test_graph)), name='node-degree')

    for node, data in test_graph.nodes(data=True):
        # Assign a node_type attribute to make our graph heterogeneous
        data['node_type'] = random.randint(1, 100) % 3

        data['node_identifier'] = str(uuid.uuid4())
        data['label'] = np.random.randint(1,4)
        data['f1'] = np.random.random()
        data['f2'] = np.random.randint(0, high=100)
        data['f3'] = 1 if np.random.random() > 0.5 else 0

    for u, v, data in test_graph.edges(data=True):
        data['label'] = 1 if np.random.randint(0, 100) % 10 > 0 else 1
        data['f1'] = np.random.random()
        data['f2'] = np.random.randint(0, high=100)

    return test_graph
