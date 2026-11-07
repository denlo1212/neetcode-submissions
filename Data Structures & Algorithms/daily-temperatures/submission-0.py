class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        for index, temperature in enumerate(temperatures):
            colderDays = 0
            for future_day in range(index + 1, len(temperatures)):
                if temperatures[future_day] > temperature:
                    colderDays = future_day - index
                    break
            stack.append(colderDays)
        return stack