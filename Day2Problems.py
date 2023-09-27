# Problem 1
li = [4, 2, 6, 3, 5, 8, 3, 9, 7, 1]

new_li = li[2: len(li): 3]
print(new_li)

# Problem 2
li = [3, 2, 1, 6, 4]
cubes_odd = [pow(num, 3) for num in li if num % 2 != 0]
#for num in li:
#    if num % 2 != 0:
#        cubes_odd.append(pow(num, 3))

print(cubes_odd)


# Problem 3
def matrix(m, n):
    temp = []
    for i in range(m):
        temp.append([0] * n)
#    temp = [[0] * n for i in range(m)]

    index = 1;
    for i in range(len(temp)):
        for j in range(len(temp[0])):
            temp[i][j] = index
            index = index + 1
    return temp


result_temp = matrix(4, 3)
print(result_temp)


# Problem 4
def dot_product(l1, l2):
    sum = 0
    for i in range(len(l1)):
        sum = sum + l1[i] * l2[i]
    return sum

l1 = [4, -2, 3]
l2 = [-1, -3, 7]

result = dot_product(l1, l2)
print(result)


# Problem 5
def identity(n):
    id_matrix = []
    for i in range(n):
        id_matrix.append([0] * n)

    for i in range(len(id_matrix)):
        for j in range(len(id_matrix[0])):
            if i == j:
                id_matrix[i][j] = 1
            else:
                id_matrix[i][j] = 0
    return id_matrix


result = identity(5)
print(result)


# Problem 6
def anti_diag(n):
    anti_id_matrix = []
    for i in range(n):
        anti_id_matrix.append([0] * n)

    for i in range(len(anti_id_matrix)):
        for j in range(len(anti_id_matrix[0])):
            if (i + j == n - 1):
                anti_id_matrix[i][j] = 1
            else:
                anti_id_matrix[i][j] = 0
    return anti_id_matrix


result = anti_diag(5)
print(result)


# Problem 7
def transpose(m):
    transpose_matrix = []
    for i in range(len(m[0])):
        transpose_matrix.append([0] * len(m))

    for i in range(len(m)):
        for j in range(len(m[0])):
            transpose_matrix[j][i] = m[i][j]
    return transpose_matrix


result = transpose(result_temp)
print(result)

# practice
print("practice..........")
result = []
for i in range(5):
    result.append([1, 1, 1])
print(result)

li = [4, 2, 6, 3, 5, 8, 3, 9, 7, 1]
result = [2 * num for num in li if num % 2 == 0]
print(result)
