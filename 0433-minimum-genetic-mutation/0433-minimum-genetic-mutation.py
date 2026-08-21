class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if not bank:
            return -1

        wordGraph = {}
        bank.append(startGene)
        def makeGraph(wordGraph):
            for i in range(len(bank)):
                source = bank[i]
                for j in range(i,len(bank)):
                    count = 0
                    target = bank[j]
                    for k in range(8):
                        if source[k] != target[k]:
                            count+=1
                        if count>1:
                            break
                    if count == 1:
                        if source not in wordGraph:
                            wordGraph[source] = []
                        if target not in wordGraph:
                            wordGraph[target] = []

                        wordGraph[source].append(target)
                        wordGraph[target].append(source)
        
        makeGraph(wordGraph)

        q = deque()
        q.append([startGene,0])
        dist = 0
        visited = set()
        visited.add(startGene)
        while q:
            currentGene,dist = q.popleft()
            
            for nei in wordGraph[currentGene]:
                if nei == endGene:
                    return dist+1
                if nei in visited:
                    continue
                visited.add(nei)
                q.append([nei,dist+1])
        return -1