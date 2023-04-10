from collections import deque

mango_sellers = {"Anastasia", "Ivan"}
graph_friends = {"you": {"Eugene", "Anatoliy", "Karim"}, "Eugene": {"Ivan", "Maxim"}, "Anatoliy": {"Ruslan", "Eugene"},
                 "Karim": {"Danil"}, "Ivan": {"Anastasia", "Catherine"}}
graph_friends["Maxim"] = {}
graph_friends["Ruslan"] = {}
graph_friends["Danil"] = {}
graph_friends["Anastasia"] = {}
graph_friends["Catherine"] = {}
for i, j in graph_friends.items():
    if j:
        print(i, ":", *j)


# deque - bilateral queue
def search_mango_seller():
    search_queue = deque()
    search_queue += graph_friends["you"]
    searched = set()
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person in mango_sellers:
                return person
            else:
                search_queue += graph_friends[person]
                searched.add(person)
    print("There is no mango sellers among your friends(")
    return None


if search_mango_seller() != None:
    print(search_mango_seller(), "is a mango seller!")

# Dijkstras algorithm works only with DAG (Directed Acyclic Graph)
# It doesn't work with negative weights
# To do this, you can use the Bellman-Ford algorithm.
graph0 = {}
graph0["start"] = {}
graph0["start"]["a"] = 6
graph0["start"]["b"] = 2
graph0["a"] = {}
graph0["a"]["fin"] = 1
graph0["b"] = {}
graph0["b"]["a"] = 3
graph0["b"]["fin"] = 50
graph0["fin"] = {}

costs0 = {}
infinity = float("inf")
costs0["a"] = 6
costs0["b"] = 2
costs0["fin"] = infinity

parents0 = {}
parents0["a"] = "start"
parents0["b"] = "start"


def find_lowest_cost_node(costs, proceed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in proceed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def Dijkstras_algorithm(graph, costs, parents):
    proceed = []
    node = find_lowest_cost_node(costs, proceed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        proceed.append(node)
        node = find_lowest_cost_node(costs, proceed)
    return costs


print(Dijkstras_algorithm(graph0, costs0, parents0))

# 7.1 A
graph1 = {}
graph1["start"] = {}
graph1["start"]["a"] = 5
graph1["start"]["c"] = 2
graph1["a"] = {}
graph1["a"]["b"] = 4
graph1["a"]["d"] = 2
graph1["b"] = {}
graph1["b"]["fin"] = 3
graph1["b"]["d"] = 6
graph1["c"] = {}
graph1["c"]["a"] = 8
graph1["c"]["d"] = 7
graph1["d"] = {}
graph1["d"]["fin"] = 1
graph1["fin"] = {}

costs1 = {}
costs1["a"] = 5
costs1["c"] = 3
costs1["b"] = infinity
costs1["d"] = infinity
costs1["fin"] = infinity

parents1 = {}
parents1["a"] = "start"
parents1["c"] = "start"

# B
graph2 = {}
graph2["start"] = {}
graph2["start"]["a"] = 10
graph2["a"] = {}
graph2["a"]["b"] = 20
graph2["b"] = {}
graph2["b"]["c"] = 1
graph2["b"]["fin"] = 30
graph2["c"] = {}
graph2["c"]["a"] = 1
graph2["fin"] = {}

costs2 = {}
costs2["a"] = 10
costs2["c"] = infinity
costs2["b"] = infinity
costs2["fin"] = infinity

parents2 = {}
parents2["a"] = "start"

# C
graph3 = {}
graph3["start"] = {}
graph3["start"]["a"] = 2
graph3["start"]["b"] = 2
graph3["a"] = {}
graph3["a"]["fin"] = 2
graph3["a"]["c"] = 2
graph3["b"] = {}
graph3["b"]["a"] = 2
graph3["c"] = {}
graph3["c"]["b"] = -1
graph3["c"]["fin"] = 2
graph3["fin"] = {}

costs3 = {}
costs3["a"] = 2
costs3["b"] = 2
costs3["c"] = infinity
costs3["fin"] = infinity

parents3 = {}
parents3["a"] = "start"
parents3["b"] = "start"

print(Dijkstras_algorithm(graph1, costs1, parents1)["fin"])
print(Dijkstras_algorithm(graph2, costs2, parents2)["fin"])
print(Dijkstras_algorithm(graph3, costs3, parents3))
