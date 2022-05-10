
graph={
    "A": ["B", "C"],
    "B":["A","C", "D"],
    "C":["A", "B", "D", "E"],
    "D":["B","C", "E", "F"],
    "E":["C", "D"],
    "F":["D"]
}

def BFS(graph, s):
    queue=[]
    queue.append(s)

    seen=set()
    seen.add(s)

    parent_node={s:None}

    while (len(queue)>0):
        vertex=queue.pop(0) # pop the first element
        nodes=graph[vertex]
        for node in nodes:
            if node not in seen:
                queue.append(node)
                seen.add(node)
                parent_node[node]=vertex
        print("current node:", vertex)
    return parent_node
parent=BFS(graph,"E")
for key, value in parent.items():
    print(value,"->",key)



