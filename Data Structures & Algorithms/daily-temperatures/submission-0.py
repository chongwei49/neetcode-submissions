class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            actual_day = i
            future_day = i

            if i == len(temperatures)-1:
                result.append(0)

            while future_day < len(temperatures):
                if actual_day == future_day:
                    future_day += 1
                    continue

                if temperatures[future_day] > temperatures[actual_day]:
                    result.append(future_day-actual_day)
                    break
                
                if future_day == len(temperatures)-1:
                    result.append(0)
                    break

                future_day += 1
        
        return result
        