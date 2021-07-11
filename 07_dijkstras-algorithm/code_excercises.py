#!/usr/bin/env python

# Import libraries
import json

infinity = float('inf')

# Graph data
graph = {}
graph['start'] = {}
graph['start']['a'] = 5
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['c'] = 4
graph['a']['d'] = 2
graph['b'] = {}
graph['b']['a'] = 8
graph['b']['d'] = 7
graph['c'] = {}
graph['c']['d'] = 6
graph['c']['fin'] = 3
graph['d'] = {}
graph['d']['fin'] = 1
graph['fin'] = {}

# Cost data
costs = {}
costs['a'] = 5
costs['b'] = 2
costs['c'] = infinity
costs['d'] = infinity
costs['fin'] = infinity

# Parents data
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['c'] = None
parents['d'] = None
parents['fin'] = None

# List to keep track of processed nodes
processed = []


# The books real function code
def find_lowest_cost_node(costs:dict):
    lowest_cost = float('inf')
    lowest_cost_node = None
    # Loop over all nodes
    for node in costs:
        cost = costs[node]
        # If it's the lowest cost, unprocessed node...
        if cost < lowest_cost and node not in processed:
            # ... set is as the new lowest-cost node
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def dijkstras_algorithm(graph:dict, costs:dict, parents:dict):
    # Find the lowest cost node that you haven't processed yet
    node = find_lowest_cost_node(costs)
    # If you've processed all the nodes, this while loop is done
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        # Loop over all the neighbors of this node
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            # If it's cheaper to get to this neighbor by going through this node...
            if costs[n] > new_cost:
                # ... update the cost for this node
                costs[n] = new_cost
                # This node becomes the new parent for this neighbor
                parents[n] = node
        # Mark this node as processed
        processed.append(node)
        # Find the next node to process and loop
        node = find_lowest_cost_node(costs)
    return f'costs:\n{json.dumps(costs, indent=4)}\nparents:\n\
{json.dumps(parents, indent=4)}'

print(dijkstras_algorithm(graph, costs, parents))