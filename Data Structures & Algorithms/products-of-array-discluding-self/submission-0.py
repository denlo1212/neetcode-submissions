class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multiplacationList = []

        for i in range(len(nums)):  # Use index i
            multiplacationNumber = 1
            for j, number in enumerate(nums):
                if i == j:  # Skip the current index
                    continue
                multiplacationNumber *= number
            multiplacationList.append(multiplacationNumber)
        return multiplacationList