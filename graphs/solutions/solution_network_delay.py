'''Solution: Network Delay Time (Challenge 4)'''
import heapq

def network_delay_time(times, n, k):
    graph = [[] for _ in range(n + 1)]
    for u, v, w in times:
        graph[u].append((v, w))
    
    dist = [float('inf')] * (n + 1)
    dist[k] = 0
    heap = [(0, k)]
    
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            if dist[node] + weight < dist[neighbor]:
                dist[neighbor] = dist[node] + weight
                heapq.heappush(heap, (dist[neighbor], neighbor))
    
    max_dist = max(dist[1:])
    return max_dist if max_dist < float('inf') else -1
