class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        new_str = ""
        for el in self.matrix:
            for i in el:
                new_str += str(i) + " "
            new_str += "\n"
        return new_str

    def __add__(self, other):
        answer = []
        for el in range(len(self.matrix)):
            answer.append([])
            for i in range(len(self.matrix[0])):
                answer[el].append(self.matrix[el][i] + other.matrix[el][i])
        return Matrix(answer)


t1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m1 = Matrix(t1)
print(m1)
m2 = Matrix(t1)
print(m2)
ans = m1 + m2
print(ans)
