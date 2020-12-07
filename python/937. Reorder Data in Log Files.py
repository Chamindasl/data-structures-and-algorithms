"""
937. Reorder Data in Log Files
https://leetcode.com/problems/reorder-data-in-log-files/
"""
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def log_sorting(log):
            id, rest = log.split(" ", maxsplit=1)
            return (0, rest, id) if rest[0].isalpha() else (1, )
        return sorted(logs, key=log_sorting)
        
