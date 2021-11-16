# test your fuzzBuzz skill with for loop

class Solution:
    def twoSum(self, arr : List[int], sum : int ) -> int:
        sum += 12
        arr.append(sum)

        return sum 




sl = Solution()
arr = [1,2]
sum = 7

ans = sl.twoSum(arr, sum)
print(ans)
