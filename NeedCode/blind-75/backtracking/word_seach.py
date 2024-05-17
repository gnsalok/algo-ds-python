''''
Word Search
https://leetcode.com/problems/word-search/

'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
                     # 3 * 3
        rows, cols = len(board), len(board[0])
        # do not visit the same char in the path
        path = set()
        def dfs(r,c,i):
            if i == len(word):
                return True
            # base cases important to analyse
            if (r < 0 or c < 0 or
                r >= rows or c >=cols or 
                (r,c) in path or
                word[i] != board[r][c]):
                return False

            path.add((r,c))

            res = (
            dfs(r+1, c, i+1) or
            dfs(r-1, c, i+1) or
            dfs(r, c+1, i+1) or
            dfs(r, c-1, i+1))
            
            path.remove((r,c))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0): return True
        return False




        