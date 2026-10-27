class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        result = 1
        zero_count = 0
        for n in nums:
            if n == 0:
                zero_count += 1
            else:
                result *= n

        for j in nums:
            if zero_count >= 2:
                output.append(0)
            elif zero_count == 1:
                if j == 0:
                    output.append(result)
                else:
                    output.append(0)
            else:
                output.append(result // j)
        return output
