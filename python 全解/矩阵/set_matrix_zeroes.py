# 矩阵行列置零

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = 0 in matrix[0]
        
        # 不能动第一行
        # 其他全部在表头记录 0
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, m):
            # 倒着遍历，避免提前把 matrix[i][0] 改成 0，
            # 误认为这一行要全部变成 0
            for j in range(n - 1, -1, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
                
if __name__ == "__main__":
    m = int(input())

    matrix = []
    for _ in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)

    sol = Solution()
    sol.setZeroes(matrix)
    
    for row in matrix:
        print(" ".join(map(str, row)))