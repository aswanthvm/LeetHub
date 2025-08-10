class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        temp = []
        for i in range(len(matrix)):
            temp.append([])
            accum = 0
            for j in range(len(matrix[i])):
                accum += matrix[i][j]
                temp[i].append(accum)

        self.temp1 = [[0 for j in range(len(matrix[i]))] for i in range(len(matrix))]
        for j in range(len(matrix[0])):
            accum = 0
            for i in range(len(matrix)):
                accum += temp[i][j]
                self.temp1[i][j] = accum
        self.temp1 = [[0 for j in range(len(matrix[i]))] for i in range(len(matrix))]
        for j in range(len(matrix[0])):
            accum = 0
            for i in range(len(matrix)):
                accum += temp[i][j]
                self.temp1[i][j] = accum   

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.temp1[row2][col2]
        elif col1 == 0:
            return self.temp1[row2][col2] - self.temp1[row1 - 1][col2]
        elif row1 == 0:
            return self.temp1[row2][col2] - self.temp1[row2][col1 - 1]
        else:
            return self.temp1[row2][col2] - self.temp1[row1 - 1][col2] - self.temp1[row2][col1 - 1] + self.temp1[row1 - 1][col1 - 1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)