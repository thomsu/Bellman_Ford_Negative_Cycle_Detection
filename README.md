# Bellman_Ford_Negative_Cycle_Detection

The Bellman-Ford algorithm finds the shortest path to each vertex in the directed graph from the source node. Unlike Dijkstra’s algorithm, Bellman-Ford will work when there is negative edges in the graph. That said, the algorithm can be modified to detect negative cycles in the graph due to negative edges.

### Procedure

Step 1: Create a list to keep track of the minimum distance from the source node. Set the distance of the source to 0 and all other distance to infinity.

Step 2: Loop through all the edges (V - 1) times, V being the total number of nodes in the graph. Each time checking to update the minimum distance from the source node. By relaxing the edges this way will lead us to the shortest path from the source.

Step 3: Loop through all the edges another (V - 1) times, this time update any change in distance to negative infinity. This way, we can document the nodes that are in the negative cycle.

 
