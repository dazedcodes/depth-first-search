"""
Depth-First Search Program

Author: Maya Murphy
Carleton College, 2022

"""
def initialize_adj_list(vertices, edges):
    """
    Takes in a set of verticies and edges and returns an adjaceny list.
    Input: verticies (Array) - an array of all the vertices for graph
        edges (2D Array) - a 2D array of all the edges in the graph
    Output: adjacency list (Dictionary) - a dictionary representing the
        graph of all of the vertices and edge connections.
    """
    adj_list = {}

    for vertex in vertices:
        adj_list.setdefault(vertex, [])
        adj_list = add_edges(vertex, edges, adj_list)
    return adj_list

def add_edges(vertex, edges, list):
    """
    Takes a vertex, set of edges, and an adjaceny list as input and returns
        an adjaceny list where the vertex's edges are added.
    Input: vertex (String), edges (2D Array), and adjaceny list (Dictionary)
    Output: adjaceny list (Dictionary)
    """
    i = 0
    for edge in edges:
        if edge[i] == vertex:
            list[vertex].append(edge[i+1])
    return list

def main():
    import sys

    print "We're going to implement depth-first search using an adjaceny list. "
    print ""


    V = ("a","b","c", "d", "e", "m", "n")
    E = (("a","b"), ("a","c"), ("b","d"), ("b","e"), ("c","m"), ("c","n"))

    graph = initialize_adj_list(V,E)
    print graph

if __name__ == '__main__':
    main()
