## Graphs

Graphs are defined as a set of vertices connected by edges.

* neighbor of X: any vertex connected to X by an edge.
* path: a route of edges that connects two vertices.
* cycle: a path that begins and end on the same vertex.
* directed acyclic graph (DAG): a directed graph that does not contain any cycles.
* connected graph: a graph in which there is always a path between any two vertices.

>- Graphs can be represented in two ways:
* Adjacency list and adjacency matrices.

In general, the adjacency list representation is more space efficient if there are not that many edges (also known as sparse graph), whereas an adjacency matrix has faster lookup times to check if a given edge exists but uses more space.

>- The two main methods for graph traversals are breadth first search and depth first search.

