class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}
        for i in nums:
            if i in numbers:
                numbers[i] += 1
            else:
                numbers[i] = 1
        sorted_data = dict(sorted(numbers.items(), key=lambda item: item[1], reverse=True))
        result = []
        for i in range(0,k):
            result.append(list(sorted_data)[i])
        return result
            

        