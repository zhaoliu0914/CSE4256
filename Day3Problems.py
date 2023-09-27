from math import sqrt

# Question 1
def evens(di):
    sumInt = 0
    for k, v in di.items():
        if (v % 2 == 0):
            sumInt += v
    return sumInt


di = {3: 1,
      4: 5,
      1: 6,
      2: 4,
      8: 1,
      3: 2
      }
sum = evens(di)
print(sum)


# Question 2
def odds(di):
    result = {}
    for k, v in di.items():
        oddList = [oddValue for oddValue in v if (oddValue % 2 != 0)]
        result[k] = oddList
    return result


di = {"ab": [3, 10, -2, 1, 5],
      "bca": [4, 2, -1],
      "aca": [-6, -2, 4]
      }
oddNum = odds(di)
print(oddNum)


# Question 3
def chess_board(n):
    result = []
    evenValue = []
    oddValue = []
    for i in range(n):
        if i % 2 == 0:
            evenValue.append(1)
            oddValue.append(0)
        else:
            evenValue.append(0)
            oddValue.append(1)
    di = {
        "oddValue": oddValue,
        "evenValue": evenValue
    }
    for i in range(n):
        if (i % 2 == 0):
            result.append(di["evenValue"])
        else:
            result.append(di["oddValue"])
    return result


result = chess_board(5)
print(result)


# Question 4
def multiply(m1, m2):
    result = []

    m2t = transpose(m2)
    for i in range(len(m1)):
        entry = []
        for j in range(len(m2t)):
            product = 0
            for tempIndex in range(len(m1[i])):
                product += m1[i][tempIndex] * m2t[j][tempIndex]
            entry.append(product)
        result.append(entry)
    return result


def transpose(m):
    transpose_matrix = []
    for i in range(len(m[0])):
        transpose_matrix.append([0] * len(m))

    for i in range(len(m)):
        for j in range(len(m[0])):
            transpose_matrix[j][i] = m[i][j]
    return transpose_matrix


m1 = [[2, -3, 4],
      [5, 6, 0]]

m2 = [[1, -2],
      [5, 3],
      [4, 3]]

result = multiply(m1, m2)
print(result)


# Question 5a
def is_prime(n):
    sqrtValue = sqrt(n)
    print("n = ", n)
    print("sqrtValue = ", sqrtValue)
    print("int(sqrtValue) = ", int(sqrtValue))
    for i in range(2, int(sqrtValue) + 1):
        if n % i == 0:
            return False
    return True


result = is_prime(7)
print("7 is prime: ", result)
result = is_prime(10)
print("10 is prime: ", result)


# Question 5b
def primes(n):
    result = []
    number = 2
    while len(result) < n:
        isPri = is_prime(number)
        if isPri:
            result.append(number)
        number += 1
    return result


result = primes(7)
print(result)


# Question 6
def sort(li):
    temp = []
    for i in range(10):
        temp.append(0)
    for i in range(len(li)):
        currentValue = li[i]
        currentValue = currentValue - 1
        number = temp[currentValue]
        temp[currentValue] = number + 1
    result = []
    for i in range(10):
        count = temp[i]
        for j in range(count):
            result.append(i + 1)

    return result


li = [1, 5, 6, 6, 7, 7, 2, 6, 8, 1, 3, 9, 10, 5, 4, 2, 3, 3, 4, 5, 6, 8, 9, 10]
result = sort(li)
print(result)
