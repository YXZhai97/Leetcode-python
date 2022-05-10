graph={
    "A": ["B", "C"],
    "B":["A","C", "D"],
    "C":["A", "B", "D", "E"],
    "D":["B","C", "E", "F"],
    "E":["C", "D"],
    "F":["D"]
}

def DFS(graph, s):
    stack=[]
    stack.append(s)
    seen=set()
    seen.add(s)
    while (len(stack)>0):
        vertex=stack.pop()  # pop the last element
        nodes=graph[vertex]
        for node in nodes:
            if node not in seen:
                stack.append(node)
                seen.add(node)
        print("current node:", vertex)
DFS(graph,"F")
