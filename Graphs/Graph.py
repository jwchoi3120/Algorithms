########################################
# Graphs
# Author : Tom Choi
########################################

import random

def Generate_edges(size, connectedness):
    """
    Generates directed edges between vertices to form a DAG
    :return: A generator object that returns a tuple of the form (source ID, destination ID)
    used to construct an edge
    """

    assert connectedness <= 1
    random.seed(10)
    for i in range(size):
        for j in range(i + 1, size):
            if random.randrange(0, 100) <= connectedness * 100:
                yield f'{i} {j}'


# Custom Graph error
class GraphError(Exception): pass


class Vertex:
    """
    Class representing a Vertex in the Graph
    """
    __slots__ = ['ID', 'index', 'visited']

    def __init__(self, ID, index):
        """
        Class representing a vertex in the graph
        :param ID : Unique ID of this vertex
        :param index : Index of vertex edges in adjacency matrix
        """
        self.ID = ID
        self.index = index  # The index that this vertex is in the matrix
        self.visited = False

    def __repr__(self):
        return f"Vertex: {self.ID}"

    __str__ = __repr__

    def __eq__(self, other):
        """
        :param other: Vertex to compare
        :return: Bool, True if same, otherwise False
        """
        return self.ID == other.ID and self.index == other.index

    def out_degree(self, adj_matrix):
        """
        given an adj_matrix, return the number of outgoing edges to its vertex
        :param adj_matrix: matrix
        :return: number of outgoing edges
        """
        count = 0
        for lst in adj_matrix[self.index]:
            if lst is not None:
                count += 1
        return count

    def in_degree(self, adj_matrix):
        """
        same as out_degree, but incoming edges
        :param adj_matrix: matrix
        :return: number of incoming edges
        """
        count = 0
        for lst in adj_matrix:
            if lst[self.index] is not None:
                count += 1
        return count

    def visit(self):
        """
        set the visit flag to seen
        :return: none
        """
        self.visited = True


class Graph:
    """
    Graph Class ADT
    """

    def __init__(self, iterable=None):
        """
        Construct a random Directed Graph
        :param size: Number of vertices
        :param: iterable: iterable containing edges to use to construct the graph.
        """
        self.id_map = {}
        self.size = 0
        self.matrix = []
        self.iterable = iterable
        self.construct_graph()
        if hasattr(iterable, 'close'):
            iterable.close()

    def __eq__(self, other):
        """
        Determines if 2 graphs are Identical
        :param other: Graph Object
        :return: Bool, True if Graph objects are equal
        """
        return self.id_map == other.id_map and self.matrix == other.matrix and self.size == other.size

    def get_vertex(self, ID):
        """
        given an ID that is the same type as vertex.ID, get the corresponding vertex object
        :param ID: id
        :return: vertex or none
        """
        if ID in self.id_map:
            return self.id_map[ID]
        return None

    def get_edges(self, ID):
        """
        given an ID with type vertex.ID, return the set of outgoing vertex ID's from the input vertex
        :param ID: id
        :return: vertex or none
        """
        returnSet = set()
        if ID in self.id_map:
            for lst in self.matrix[self.id_map[ID].index]:
                if lst is not None:
                    returnSet.add(lst)
        return returnSet

    def construct_graph(self):
        """
        iterates through iterable and calls insert_edge to create the graph representation stored in self.matrix
        :return: none
        """
        try:
            for e in self.iterable:
                s, d = e.split()
                self.insert_edge(int(s), int(d))
        except TypeError:
            raise GraphError()


    def insert_edge(self, source, destination):
        """
        creates vertex objects, if needed, then adds edge representation into the matrix between the
        given source and destination, and updates self.id_map
        :param source: vertex.ID
        :param destination: vertex.ID
        :return: none
        """
        if self.size == 0:
            self.matrix.append([None])
            self.id_map[source] = Vertex(source, len(self.matrix) - 1)
            self.size = 1

        if source not in self.id_map:
            for lst in self.matrix:
                lst.append(None)
            self.matrix.append([None for i in range(len(self.matrix[0]))])
            self.id_map[source] = Vertex(source, len(self.matrix) - 1)
            self.size += 1

        if destination not in self.id_map:
            for lst in self.matrix:
                lst.append(None)
            self.matrix.append([None for i in range(len(self.matrix[0]))])
            self.id_map[destination] = Vertex(destination, len(self.matrix) - 1)
            self.size += 1

        self.matrix[self.id_map[source].index][self.id_map[destination].index] = destination


    def bfs(self, start, target, path=None):
        """
        does a breadth first search to generate a path from start to target visiting a node only once
        :param start: start position
        :param target: to find it
        :param path: the visited nodes
        :return: list
        """
        templist = [(start, [start])]
        while templist is not None:
            (vertex, path) = templist.pop(0)
            edges = self.get_edges(vertex)
            for val in edges:
                if self.id_map[val].visited is False:
                    if val == target:
                        return path + [val]
                    else:
                        templist.append((val, path + [val]))
                        self.id_map[val].visit()

    def dfs(self, start, target, path=None):
        """
        same as bfs, but doing a depth first search instead
        :param start: start
        :param target: find it
        :param path: the visited nodes
        :return: list
        """
        templist = [(start, [start])]
        while templist is not None:
            (vertex, path) = templist.pop()
            if self.id_map[vertex].visited is False:
                edges = self.get_edges(vertex)
                self.id_map[vertex].visit()
                for val in edges:
                    if val == target:
                        return path + [val]
                    else:
                        templist.append((val, path + [val]))

def find_k_away(K, iterable, start):
    """
    given a starting ID and value K, return all vertex ID's that are K vertices away
    :param K: far away
    :param iterable: edges
    :param start: starting point
    :return: set of K away values
    """
    all_paths = []
    returnList = set()
    g = Graph(iterable=iterable)

    if K == 0:
        return {start}
    templist = [(start, [start])]
    while templist:
        (vertex, path) = templist.pop(0)
        edges = g.get_edges(vertex)
        idmap = g.get_vertex(vertex)
        if idmap:
            idmap.visit()
        for val in edges:
            values = g.get_vertex(val)
            if values.visited is False:
                templist.append((val, path + [val]))
        if len(templist) > 0:
            all_paths.append(templist[0][1])
    for item in all_paths:
        if len(item) > K:
            returnList.add(item[K])
    return returnList

