def get_user_inputs():
    #1. Take input for Heuristic value
  heuristic = {}
num_nodes = int(input("Enter total number of nodees: "))
print("\nEnter Heuristic value h(n) for each node:")
for i in range(num_nodes):
    node = input(" Node name:").strip().upper()
    h_value = float(input ( f " Heuristic h({node}): "))
    heuristic[node] = h_value

   #2. Take input Graph edges
graph = {node: [] for node in heuristic}
num_edges = int (input("\n Enter total number of directed))
print ("\nEnter edges in format (from_node to_node weight")
for i in range (num_edges):
   u,v,w =input (f"Edge {i+1}:".strip().split())                      
   u,v = u,uppeer(), v.upper()
   weight = float (w)
   graph[u].append((v,weight))

return graph, heuristic

def astrar(graph, heuristisc, start, goal):
   open_list = [(start, 0)]
   came_from = {}
   g_cost = {start: 0}

   while open_list:
   #select node with minimum f = g+h
   current = min(open_list, key = lambda x: x[1] +heuristic[x[0]])
   open_list.remove(current)

   current_node = current[0]

   # goal  check & path reconstruction
   if current_node in came_from:
   current_node = came_from[current_node]
   path.append(current_node)
   path.reverse()
   return path, g_cost[goal]
            
   #Neighbor exploration
   for neighbor, cost in graph.get(current_node, []):
   new_cost = g_cost[current_node] + cost

   if neighbor not in g_cost or new_cost < g_cost[neighbor]:
      g_cost[neighbor] = new_cost
      came_from[neighbor] = current_node
      open_list.append((neighbor, new_cost))
return None,float ('ingf')
       