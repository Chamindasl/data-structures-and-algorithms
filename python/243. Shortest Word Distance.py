# 243. Shortest Word Distance
# https://leetcode.com/problems/shortest-word-distance/
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        shortest_dis = float(inf)
        w1_idx, w2_idx = -1, -1
        for idx, word in enumerate(words):
            if word == word1:
                w1_idx = idx
                if w2_idx !=-1:
                    shortest_dis = min(shortest_dis, abs(w1_idx - w2_idx))
                    w2_idx = -1
            elif word == word2:
                w2_idx = idx
                if w1_idx !=-1:
                    shortest_dis = min(shortest_dis, abs(w1_idx - w2_idx))
                    w1_idx = -1
        return shortest_dis
            
            
