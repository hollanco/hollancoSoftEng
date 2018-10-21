from DirectedAcyclicGraph import DAG
import unittest


class TestDAG(unittest.TestCase):

    def test_add_nodes(self):
        graph = DAG()
        graph.add_node('A')
        self.assertEqual(graph.graph, {'A':[]})

        graph.add_node('B')
        graph.add_node('C')
        self.assertEqual(graph.graph, {'A': [], 'B': [], 'C': []})

    def test_recognise_nodes(self):
        graph = DAG()
        graph.add_node('A')
        self.assertFalse(graph.add_node('A'))

    def test_add_edges(self):
        graph = DAG()
        graph.add_node('B')
        graph.add_node('C')
        graph.add_edge('B', 'C')

        self.assertEqual(graph.graph, {'B': ['C'], 'C': []})

    def test_recognise_edges(self):
        graph = DAG()
        graph.add_node('B')
        graph.add_node('C')
        graph.add_edge('B', 'C')

        self.assertRaises(ValueError, graph.add_edge('B', 'C'))

    def test_complex(self):
        graph = DAG()
        graph.add_node('A')
        graph.add_node('B')
        graph.add_node('C')
        graph.add_node('D')
        graph.add_node('E')
        graph.add_node('F')
        graph.add_node('G')
        graph.add_node('H')
        graph.add_node('I')
        graph.add_edge('A', 'B')
        graph.add_edge('B', 'C')
        graph.add_edge('B', 'D')
        graph.add_edge('C', 'F')
        graph.add_edge('C', 'E')
        graph.add_edge('D', 'F')
        graph.add_edge('D', 'H')
        graph.add_edge('B', 'G')
        graph.add_edge('H', 'I')
        graph.add_edge('C', 'I')
        self.assertEqual(graph.graph, {'A': ['B'], 'B': ['C', 'D', 'G'], 'C': ['F', 'E', 'I'], 'D': ['F', 'H'],
                                       'E': [], 'F': [], 'G': [], 'H': ['I'], 'I': []})

    def test_basic_lca(self):
        graph = DAG()
        graph.add_node('A')
        print(graph.dfs_wrapper(graph.graph, 'A', 'A'))

    def test_complex_lca(self):
        graph = DAG()
        graph.add_node('A')
        graph.add_node('B')
        graph.add_node('C')
        graph.add_node('D')
        graph.add_node('E')
        graph.add_node('F')
        graph.add_node('G')
        graph.add_node('H')
        graph.add_node('I')
        graph.add_edge('A', 'B')
        graph.add_edge('B', 'C')
        graph.add_edge('B', 'D')
        graph.add_edge('C', 'F')
        graph.add_edge('C', 'E')
        graph.add_edge('D', 'F')
        graph.add_edge('D', 'H')
        graph.add_edge('B', 'G')
        graph.add_edge('H', 'I')
        graph.add_edge('C', 'I')
        self.assertEqual(graph.dfs_wrapper(graph.graph, 'A', 'A'), 'A')
        self.assertEqual(graph.dfs_wrapper(graph.graph, 'F', 'E'), 'C')
        self.assertEqual(graph.dfs_wrapper(graph.graph, 'I', 'G'), 'B')
        self.assertEqual(graph.dfs_wrapper(graph.graph, 'F', 'I'), 'C')


unittest.main(exit=False)
