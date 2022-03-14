import json
from queue import PriorityQueue
import time

# Zou Ze Ren (U2022422H) Eric Chua Jee Hon (U2020527J)
def openJason(file):
    with open(file) as graph_dict:
        content = json.load(graph_dict)
    graph_dict.close()
    return content


class Graph:

    def __init__(self, total_vertices):
        self.v = total_vertices

    def min_distance(self, parent_node, target_node):
        node = target_node
        shortest_path = []
        while node is not None:
            shortest_path.append(node)
            node = parent_node[node]
        print("Shortest Path: " + " -> ".join(shortest_path) + "\n")

    def dijkstra(self, source_node, target_node, graph_dict, dist_dict, cost_dict):
        # Initialise counter with time()
        start_time = time.time()

        # Creating a set of visited nodes
        visited_nodes = set()

        # Creating a dictionary for distances
        distance = {source_node: 0}

        # Creating a dictionary for cost
        cost = {source_node: 0}

        # Creating a dictionary for shortest path
        parent_node = {source_node: None}

        # Creating an instance of PriorityQueue FIFO
        priority_queue = PriorityQueue()

        # Inserting the first element source node
        priority_queue.put((0, source_node))

        while not priority_queue.empty():
            # Always getting the second element only from the PriorityQueue
            (_, current_node) = priority_queue.get()

            # Analysing the pre-conditions for PriorityQueue using while loop
            if current_node == target_node:
                break
            elif current_node in visited_nodes:
                continue
            else:
                visited_nodes.add(current_node)

            # Start algorithm once pre-conditions met
            for neighbor in graph_dict.get(str(current_node)):
                old_distance = distance.get(neighbor, float('inf'))
                new_distance = distance[current_node] + dist_dict[str(current_node) + "," + str(neighbor)]
                old_cost = cost.get(neighbor, float('inf'))
                new_cost = cost[current_node] + cost_dict[str(current_node) + "," + str(neighbor)]

                if new_distance < old_distance:
                    priority_queue.put((new_distance, neighbor))
                    distance[neighbor] = new_distance
                    cost[neighbor] = new_cost
                    parent_node[neighbor] = current_node
            # End of for loop
        # End of while loop

        # Check if connection between source node and target node exist
        if target_node in parent_node.keys():
            print("Time taken:\t%s seconds" % (time.time() - start_time))
            print("Shortest distance: " + str(distance[target_node]))
            print("Total energy cost:" + str(cost[target_node]))
            self.min_distance(parent_node, target_node)
        else:
            return None
        # End of Dijkstra


def main():
    # Opening JSON file
    graph_dict = openJason('G.json')
    dist_dict = openJason('Dist.json')
    cost_dict = openJason('Cost.json')

    # Define SOURCE and TARGET parameter
    source_node = '1'
    target_node = '50'

    # Printline title of algo
    print("STP with no energy constrain using dijkstra algo with python")

    # Create instance of graph
    graph = Graph(264436)

    # Activate algorithm
    graph.dijkstra(source_node, target_node, graph_dict, dist_dict, cost_dict)


if __name__ == "__main__":
    main()
