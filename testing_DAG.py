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


unittest.main(exit=False)
