from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList) or (beginWord==endWord):
            return 0
        def neighbours(word):
            res= []
            for i in wordList:
                if i == word:
                    continue
                l = 0
                ch =0
                while l<len(word):
                    if i[l] != word[l]:
                        ch+=1
                    l+=1
                if ch == 1:
                    res.append(i)
            return res    
        graph = defaultdict(list) 
        graph[beginWord] = neighbours(beginWord)
        for word in wordList:
            graph[word] = neighbours(word)
        queue = []
        queue.append((1,beginWord))
        visited = []
        while queue:
            level , w = queue.pop(0)
            visited.append(w)
            if endWord == w:
                return level
            for i in graph[w]:
                if i not in visited:
                    queue.append((level+1,i))
        return 0