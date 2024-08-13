"""
Provided array sum to index and return result as list index which are matches with target
Example :
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = []
        for key, value in enumerate(nums):
            for key1, value1 in enumerate(nums):
                if key1 != key and key1 > key:
                    if target == value + value1:
                        lst += [key, key1]
        return lst
        