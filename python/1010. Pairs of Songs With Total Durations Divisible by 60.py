"""
1010. Pairs of Songs With Total Durations Divisible by 60
https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60
"""
import collections
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        reminders = collections.defaultdict(int)
        pairs = 0
        # a%c + b%c should be 60, 
        for i in range(len(time)):
            time_i = time[i]
            if time_i % 60 == 0:
                pairs += reminders[0]
            else:
                pairs += reminders[60 - time_i%60]
            reminders[time_i%60] +=1
        return pairs
        
