class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num,0) + 1

        SortedFreq = sorted(frequency, key=frequency.get)
        result = []
        for i in range(k) :
            result.append(SortedFreq.pop())

        return result
        
