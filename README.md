# 21S2_CZ3005_Assignment_1
21S2 CZ3005 - Assignment 1
Finding A Shortest Path With An Energy Budget

Zou Ze Ren (U2022422H)
Eric Chua Jee Hon (U2020527J)

1 Introduction
1.1 Problem Statement
A constrained shortest path problem could be used to describe the problem. We need to identify the fastest route that is also within the energy budget. Dijkstra’s Algorithm finds the path that minimizes the overall distance/weight between the source node and all other nodes by using the weight of the edges. Uniform Cost Search’s Algorithm uses the path’s cost from the initial node to the current node as the extension criterion. A* Algorithm is implemented using weighted graphs which employ numbers to indicate the cost of choosing each path. As a result, the algorithm may select the path with the lowest cost and determine the optimal route in terms of distance and time.
1.2 Programming Language
The algorithms in this project are implemented in Python. 
1.3 Libraries
Sqrt
PriorityQueue
Time
Json
1.4 Data Preparation
Converted four json files into a network graph object. 
Graph contains 264346 nodes and 730100 edges.  
Energy Budget of 287932


2 Task One
2.1 Algorithm Design
We used the dijkstra algorithm to discover the shortest path problem between node 1 and node 50 because there are no budget constraints in Task 1. Once it reaches the destination node, the dijkstra will come to a halt. In order to construct the path after executing the algorithm, the algorithm will maintain a priority queue to obtain the distance, current node tuple and the parent node of each traversed node is saved and updated.


2.2 Output

2.3 Discussion
The Dijkstra algorithm’s time complexity is (E+V log(v)), and it runs extremely quickly. However, we noticed that the overall energy cost of the shortest trip exceeds the acceptance cost budget, indicating that the shortest path we determined will not satisfy the criterion.
3 Task Two
3.1 Algorithm Design
We used the Uniform Cost Search (UCS) to solve the NYC instance. UCS is an uninformed search algorithm that finds the shortest path that finds the shortest path from the root node to the target node with the lowest cumulative cost in a weight search space where nodes are expanded according to their cost of traversal from the root node.

3.2 Output

3.2 Discussion
The UCS Algorithm’s time complexity is O(b(1+C/ε)) where b is the branching factor, c is the optimal cost and ε is the cost of each step. UCS is optimal because in every state, the path with the least cost is chosen.
4 Task Three
4.1 Algorithm Design



4.2 Output

4.3 Discussion
A* Search considers greedy information, it could help the algorithm to choose the child more wisely. However, greedy information is not guaranteed to provide an optimal path, it will only improve the algorithm’s speed incrementally.
5 Conclusion
We have worked through these three tasks using dijkstra algorithm, uniform cost search algorithm and A* search. We can see why A* is similar to Dijkstra since the main difference is that A* uses a heuristic function to try to find a better path by prioritizing nodes that are intended to be better than others, whereas Dijkstra simply examines all possible paths. We can also see why A* and UCS have a lists of expanded nodes but A* will try to minimize the amount of expanded nodes due to the main difference of these two algorithms which is the heuristic function.

Difference Between The Three Algorithms


Distance
Time
Energy
Dijkstra
148648.637
0.86275s
294853
Uniform Cost Search
150784.607
0.05876s
287931
A* Search
150784.607
0.02658s
287931


