from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create a dictionary to store the numbers and their indices
        num_to_index = {}

        #iterate through the list of numbers

        for index, num in enumerate(nums):
            complement = target - num

            if complement in num_to_index:
                return [num_to_index[complement], index] 

            num_to_index[num]= index   
            
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result)  # Output should be [0, 1]
