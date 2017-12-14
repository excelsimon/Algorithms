#coidng:utf-8
"""
图
"""
graph = {
    'A':['B','C'],
    'B':['C','D'],
    'C':['D'],
    'D':['C'],
    'F':['C'],
    'E':['F']
}

def find_path(graph,start,end,path=[]):
    path = path + [start]  #迭代的时候不改变传入的参数
    if start==end:
        return path
    if start not in graph:  #图中节点只入不出，没在graph中列出来，可以列出来，'':[],一般为了方便不列
        return None
    for node in graph[start]:
        if node not in path:  #确保没环
            new_path = find_path(graph,node,end,path)
            if new_path:
                return new_path

    return None

print(find_path(graph,'A','D'))

def find_all_paths(graph,start,end,path=[]):
    path = path + [start]
    if start==end:
        return [path]

    if start not in graph:
        return []

    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_all_paths(graph,node,end,path)
            for new_path in new_paths:
                paths.append(new_path)

    return paths

print(find_all_paths(graph,'A','D'))

def find_shortest_path(graph,start,end,path=[]):
    path = path + [start]
    if start==end:
        return path
    if start not in graph:
        return None

    shortest_path = None
    for node in graph[start]:
        if node not in path:
            new_path = find_shortest_path(graph,node,end,path)
            if new_path:
                if not shortest_path or len(shortest_path)>len(new_path):
                    shortest_path = new_path

    return shortest_path


print(find_shortest_path(graph,'A','D'))



























