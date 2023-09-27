# Question 1
def matrix_to_dict(mat):
    matrix_di = {}
    for row in range(len(mat)):
        temp_array = []
        for column in range(len(mat[row])):
            if column != row and mat[row][column] == 1:
                temp_array.append(column)
        matrix_di[row] = temp_array
    return matrix_di

matrix = [[0, 1, 0, 0, 1],
 [1, 0, 0, 1, 1],
 [0, 0, 0, 1, 0],
 [0, 1, 1, 0, 0],
 [1, 1, 0, 0, 0]]

matrix_di = matrix_to_dict(matrix)
print(matrix_di)

# Question 2
def complete_graph_matrix(n):
    result = []
    for i in range(n):
        result.append([1] * n)

    for index in range(n):
        result[index][index] = 0
    return result

matrix = complete_graph_matrix(4)
print(matrix)

# Question 3
def path_d(n):
    matrix_di = {}

    for index in range(n):
        temp_array = []

        last_index = index - 1
        next_index = index + 1
        if last_index >= 0:
            temp_array.append(last_index)
        if next_index < n:
            temp_array.append(next_index)

        matrix_di[index] = temp_array
    return matrix_di

def path_m(n):
    matrix_array = []
    for i in range(n):
        matrix_array.append([0] * n)

    for index in range(n):
        last_index = index - 1
        next_index = index + 1
        if last_index >= 0:
            matrix_array[index][last_index] = 1
        if next_index < n:
            matrix_array[index][next_index] = 1
    return matrix_array

temp_matrix = path_d(4)
print(temp_matrix)

temp_matrix = path_m(4)
print(temp_matrix)

# Question 4
def cycle_d(n):
    matrix_di = path_d(n)
    first_array = matrix_di[0]
    first_array.append(n-1)

    last_array = matrix_di[n-1]
    last_array.append(0)

    return matrix_di
def cycle_m(n):
    matrix_array = path_m(n)
    matrix_array[0][n-1] = 1
    matrix_array[n-1][0] = 1

    return matrix_array

temp_matrix = cycle_d(4)
print(temp_matrix)

temp_matrix = cycle_m(4)
print(temp_matrix)

# Question 5
def star_d(n):
    matrix_di = {}

    first_array = []
    for index in range(1, n):
        first_array.append(index)
    matrix_di[0] = first_array

    for index in range(1, n):
        temp_array = [0]
        matrix_di[index] = temp_array

    return matrix_di
def star_m(n):
    matrix_array = []
    for i in range(n):
        matrix_array.append([0] * n)

    for i in range(1, n):
        matrix_array[0][i] = 1

    for index in range(1, n):
        matrix_array[index][0] = 1

    return matrix_array

temp_matrix = star_d(4)
print(temp_matrix)

temp_matrix = star_m(4)
print(temp_matrix)

# Question 6a
def complement_d(di):
    matrix_di = {}

    for k, v in di.items():
        temp_array = []
        for index in range(len(di)):
            temp_array.append(index)
        temp_array.remove(k)
        for index in range(len(v)):
            temp_array.remove(v[index])

        matrix_di[k] = temp_array

    return matrix_di

test_di = {0 : [3, 4],
           1 : [2, 4],
           2 : [1],
           3 : [0],
           4 : [0, 1]}

temp_matrix = complement_d(test_di)
print(temp_matrix)

# Question 6b
def complement_m(mat):
    matrix_array = []
    for i in range(len(mat)):
        matrix_array.append([0] * len(mat[0]))

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if i != j and mat[i][j] == 0:
                matrix_array[i][j] = 1

    return matrix_array

test_array = [[0, 0, 0, 1, 1],
              [0, 0, 1, 0, 1],
              [0, 1, 0, 0, 0],
              [1, 0, 0, 0, 0],
              [1, 1, 0, 0, 0]]
temp_matrix = complement_m(test_array)
print(temp_matrix)