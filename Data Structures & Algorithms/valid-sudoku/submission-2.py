class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows= defaultdict(set)
        cols= defaultdict(set)
        boxes= defaultdict(set) #key = (r/3 , c/3)

        for r in range(9):
            for c in range(9):
                x=board[r][c]
                if x == ".":
                    continue
                if (x in rows[r]  or 
                    x in cols[c]  or
                    x in boxes[(r//3 ,c//3)]):
                    return False
                else:
                    rows[r].add(x)
                    cols[c].add(x)
                    boxes[(r//3 , c//3)].add(x)
        return True        

                