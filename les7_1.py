class Matrix:
    def __init__(self, list_1, list_2):
        self.my_str = list_1, list_2
        self.list_1 = list_1
        self.list_2 = list_2

    def __str__(self):

        my_str = '\n'
        for row in self.my_str:
            for el in row:
                my_str += f'{el:>10}'
            my_str += '\n'
        return my_str


    def __add__(self):
        matrix1 = [[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matrix1[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix1]))


my_matrix = Matrix([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]],
                   [[11, 12, 13],
                    [14, 15, 16],
                    [17, 18, 19]])


print(my_matrix.my_str)
print(my_matrix.__add__())
