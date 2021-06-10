class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for _from, _to in sorted(tickets, reverse=True):
            graph[_from].append(_to)
        
        route = []
        
        def dfs(s):
            while graph[s]:
                dfs(graph[s].pop())
            route.append(s)
        
        dfs('JFK')
        return route[::-1]
    
            