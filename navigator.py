graph = {'start': {'a': 6, 'b': 2}, 'a':{'finish': 1}, 'b':{'a': 3, 'finish': 5}, 'finish':{}}

infinity = float('inf')
costs = {'a': 6, 'b': 2, 'finish': None}

parents = {'a': 'start', 'b': 'start', 'finish': None}

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    
    for node in costs:
        cost = cost[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node