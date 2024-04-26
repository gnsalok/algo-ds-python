# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:

    '''
    TC : O N
    SP : O N
    '''
    # Solution using hashmap
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for n in nums:
            seen[n] = seen.get(n,0) + 1
        val = list(seen.values())
        return val[-k:]
    




