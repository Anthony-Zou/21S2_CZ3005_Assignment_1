import json
from queue import PriorityQueue
import time
import math

# Zou Ze Ren (U2022422H) Eric Chua Jee Hon (U2020527J)
def openJason(file):
    with open(file) as graph_dict:
        content = json.load(graph_dict)
    graph_dict.close()
    return content

class Graph:

    def __init__(self, total_vertices):
        self.v = total_vertices

    def aStar(self, source_node, target_node, graph_dict, dist_dict, cost_dict, coord_dict, energy_constrain):

        # Initialise counter with time()
        start_time = time.time()
        # Initialise counter for failure
        fail = 0
        # Creating an instance of PriorityQueue FIFO
        priority_queue = PriorityQueue()
        # Creating a set of visited nodes
        visited_nodes = set()
        # Creating a dictionary for cost
        cost = {source_node: 0}
        # Creating a dictionary for distances g(n)
        gn_distance_dict = {source_node: 0}
        # Creating f(n) = 0 + h(n)
        f_n_distance = math.dist(coord_dict[str(source_node)], coord_dict[str(target_node)])
        # Inserting the first element source node ( Distance, Cost, Node)
        priority_queue.put((f_n_distance, 0, source_node))

        while not priority_queue.empty():
            # Getting the current ( Distance, Cost, Node)
            current_distance, current_cost, current_list = priority_queue.get()
            current_node = current_list[-1]
            h_n = math.dist(coord_dict[str(current_node)], coord_dict[str(target_node)])
            current_distance -= h_n

            # Analysing the pre-conditions for PriorityQueue using while loop

            if current_node in visited_nodes:
                continue
            else:
                visited_nodes.add(current_node)

            # Algo starts
            for neighbor in graph_dict.get(str(current_node)):
                # distance between node and neighbor
                old_distance = gn_distance_dict.get(neighbor, float('inf'))
                distance = dist_dict[str(current_node) + "," + str(neighbor)]
                new_distance = distance + current_distance # G(n)
                # Energy cost of neighbor
                old_cost = cost_dict.get(neighbor, float('inf'))
                cost = cost_dict[str(current_node) + "," + str(neighbor)]
                new_cost = cost + current_cost

                if (neighbor not in visited_nodes) or (new_distance < old_distance) or (new_cost < old_cost):
                    gn_distance_dict[neighbor] = new_distance
                    new_list = list(current_list)
                    new_list.append(neighbor)
                    h_n = math.dist(coord_dict[str(neighbor)], coord_dict[str(target_node)])
                    new_distance += h_n
                    # Check if cost is within the energy constraint
                    if new_cost <= energy_constrain:
                        priority_queue.put((new_distance, new_cost, new_list))
                        cost_dict[neighbor] = new_cost
                    # If path fails energy constraint
                    else:
                        fail += 1

                if current_node == target_node:
                    print("Time taken:\t%s seconds" % (time.time() - start_time))
                    path = '->'.join(current_list)
                    print("Shortest path: " + path + '.')
                    # distance = Data.calculate_distance(current_list)
                    print("Shortest distance: " + str(current_distance) + '.')
                    print("Total energy cost: " + str(current_cost) + '.')
                    return "A* COMPLETE"


def main():
    # Opening JSON file
    graph_dict = openJason('G.json')
    dist_dict = openJason('Dist.json')
    cost_dict = openJason('Cost.json')
    coord_dict = openJason('Coord.json')

    # Define SOURCE and TARGET parameter
    source_node = '1'
    target_node = '50'
    energy_constrain = 287932

    # Printline title of algo
    print("STP with  cost using A-star algo with python")

    # Create instance of graph
    graph = Graph(264436)

    graph.aStar(source_node, target_node, graph_dict, dist_dict, cost_dict, coord_dict, energy_constrain)


if __name__ == "__main__":
    main()

# STP with  cost using A-star algo with python
# Shortest path: 1->1363->1358->1357->1356->1276->1273->1277->1269->1267->1268->1284->1283->1282->1255->1253->1260->1259->1249->1246->963->964->962->1002->952->1000->998->994->995->996->987->988->979->980->969->977->989->990->991->2369->2366->2340->2338->2339->2333->2334->2329->2029->2027->2019->2022->2000->1996->1997->1993->1992->1989->1984->2001->1900->1875->1874->1965->1963->1964->1923->1944->1945->1938->1937->1939->1935->1931->1934->1673->1675->1674->1837->1671->1828->1825->1817->1815->1634->1814->1813->1632->1631->1742->1741->1740->1739->1591->1689->1585->1584->1688->1579->1679->1677->104->5680->5418->5431->5425->5429->5426->5428->5434->5435->5433->5436->5398->5404->5402->5396->5395->5292->5282->5283->5284->5280->50.
# Shortest distance: 150784.60722193596.
# Total energy cost: 287931.
# Creating output file...
