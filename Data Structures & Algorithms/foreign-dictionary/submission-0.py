from collections import deque

class Solution:
    def foreignDictionary(self, words):
        adj = {c: set() for w in words for c in w}
        indeg = {c: 0 for c in adj}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return ""                              # "abc" before "ab"
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])          # note: w1[j] before w2[j]
                        indeg[w2[j]] += 1
                    break                              # first difference only

        q = deque([c for c in indeg if indeg[c] == 0])
        res = []
        while q:
            c = q.popleft()
            res.append(c)
            for nei in adj[c]:
                indeg[nei] -= 1                        # tear up the note
                if indeg[nei] == 0:
                    q.append(nei)

        return "".join(res) if len(res) == len(indeg) else ""