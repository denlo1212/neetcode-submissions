class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbersSet = set(nums)
        highestStreak = 0

        for number in nums:
            if (number - 1) not in numbersSet:
                streak = 1
                while (number + streak) in numbersSet:
                    streak += 1
                highestStreak = max(streak, highestStreak)
        return highestStreak