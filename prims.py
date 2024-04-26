import heapq

def prims(graph):
    mst=[]
    adj_list={v:[] for v in graph['v']}
    for edge in graph['e']:
        adj_list[edge[0]].append((edge[1],edge[2]))
        adj_list[edge[1]].append((edge[0],edge[2]))
    start="a"
    visited_set=set()
    visited_set.add(start)
    q=[(weight, start, dest) for dest, weight in adj_list[start]]
    while q:
        w,s,d=heapq.heappop(q)
        if d not in visited_set:
            visited_set.add(d)
            mst.append((s,d,w))
            for n,weight in adj_list[d]:
                if n not in visited_set:
                    heapq.heappush(q,(weight,d,n))  #push the correct weight and destination
                          
    print(mst)
    mini=0
    for ed in mst:
        mini+=ed[2]  #sum the weights of the edges
    print(mini)
    
graph = {
    'v':['a','b','c','d','e'],
    'e':[('a','b',2),('b','d',4),('d','e',5),('c','e',1),('c','d',6),('a','c',3)]
}

prims(graph)
