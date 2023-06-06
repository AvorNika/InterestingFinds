import time

start = time.time()

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if int(nums[i]) + int(nums[j]) == target:
                    a.append(i)
                    a.append(j)
                    break
                else:
                    continue
        return a


end = time.time() - start

print(end)
