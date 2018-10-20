import sys
# Lowest Common Ancestor Problem with DAG implementation


class DAG(object):

    def __init__(self):
        self.graph = {}

    # Add node if it doesn't exist already
    def add_node(self, node):
        graph = self.graph

        if node in graph:
            return False

        graph[node] = []

    def add_edge(self, node_one, node_two):
        graph = self.graph

        if node_one in graph and node_two in graph:
            graph[node_one].append(node_two)
        else:
            raise ValueError("Both keys must exist")

    # Finds and returns the node that is the LCA
    def dfs_wrapper(self, graph, node_one, node_two):
        global nodeOne_list
        global nodeTwo_list
        nodeOne_list = []
        nodeTwo_list = []

        # If the same node is passed in twice, then the LCA is that node
        if(node_one == node_two):
            return node_one

        for node in graph:
            self.lca_dfs([node], graph, node, 1, node_one)
            self.lca_dfs([node], graph, node, 2, node_two)

        lowest_count = sys.maxsize

        for a in nodeOne_list:
            for b in nodeTwo_list:
                count = 0
                for index, node1 in enumerate(reversed(a)):
                    count = index
                    for node2 in reversed(b):
                        if node1 == node2 and count < lowest_count:
                            LCANode = node2
                            return LCANode

                        count += 1

    def lca_dfs(self, node_list, graph, node, index, end_node):
        if(node == end_node):
            # Index distinguishes between the two routes
            if index == 1:
                nodeOne_list.append(node_list[:])
            elif index == 2:
                nodeTwo_list.append(node_list[:])
            return True

        if not graph[node]:
            return True

        else:
            for child in graph[node]:
                if child not in node_list:
                    node_list.append(child)
                    if not self.lca_dfs(node_list, graph, child, index, end_node):
                        return False
                    node_list.remove(child)
                else:
                    return False
            return True