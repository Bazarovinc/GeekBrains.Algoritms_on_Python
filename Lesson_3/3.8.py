"""8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму
    введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести
    полученную матрицу."""


def print_matrix(matrix):
    for line in matrix:
        for i in line:
            print(f"{i:>10}", end='')
        print()


matrix = []
last_line = []
for i in range(4):
    matrix.append([])
    last_line.append(0)
    for j in range(4):
        matrix[i].append(int(input("Введите элемент матрицы: ")))
        last_line[i] += matrix[i][j]
matrix.append(last_line)
print_matrix(matrix)
