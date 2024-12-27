"""
[27-12-24] 169. Majority Element.py
https://leetcode.com/problems/majority-element/

https://leetcode.com/problems/majority-element/solutions/3676530/3-method-s-beats-100-c-java-python-beginner-friendly
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        def majorityElementSort() -> int:
            nums.sort()
            return nums[len(nums)//2]

        def majorityElementMooreVotin() -> int:
            can = 0
            count = 0
            for i in nums:
                if count == 0 : can = i
                if can == i :
                    count = count + 1
                else:
                    count = count - 1

            return can



        # return majorityElementSort()
        return majorityElementMooreVotin()
