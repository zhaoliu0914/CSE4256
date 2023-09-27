li = [4, 2, 6, 5, 8, 3]
print(li[1: 4])

print(li[:4])

print(li[1:])

print(li[1: 5: 2])

result = []
for num in li:
    result.append(2*num)

print(result)

result1 = [2 * num for num in li]
print(result1)

result2 = [num for num in li if num%2 == 0]
print(result2)

li = [
    [5, 0, -10, 5],
    [-6, 5, -3, 2],
    [5, 6, 7, -4]
    ]

print(li[0])
print(li[1])
print(li[2])
print(li[0][0])
print(li[1][3])