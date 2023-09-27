# Problem 1
def linear_search(li, toFind):
    for i in li:
        if i == toFind:
            return True

    return False

li = [4, 2, 6, 3, 5, 8, 3, 9, 7, 1]
result = linear_search(li, 10)
print(result)

li = [4, 2, 6, 3, 5, 8, 3, 9, 7, 1]
result = linear_search(li, 9)
print(result)


# Problem 2
def linear_search_pos(li, toFind):
    for i in li:
        if i == toFind:
            return i

    return -1

li = [4, 2, 6, 3, 5, 8, 3, 9, 7, 1]
result = linear_search_pos(li, 10)
print(result)

li = [4, 2, 6, 3, 5, 8, 3, 9, 7, 1]
result = linear_search_pos(li, 9)
print(result)


# Problem 3
def linear_recursive(li, toFind):
    return linear_recursive_helper(li, toFind, 0)

def linear_recursive_helper(li, toFind, index):
    isFound = False
    if index < len(li):
        if li[index] == toFind:
            isFound = True
        else:
            isFound = linear_recursive_helper(li, toFind, index + 1)

    return isFound

li = [4, 2, 6, 3, 5, 8, 3, 9, 7, 1]
result = linear_recursive(li, 10)
print(result)

li = [4, 2, 6, 3, 5, 8, 3, 9, 7, 1]
result = linear_recursive(li, 9)
print(result)


# Problem 4
def binary_search(li, toFind):
    index = int(len(li) / 2)
    left = 0
    right = len(li)
    while left < index and right > index:
        if toFind == li[index]:
            return True
        elif toFind < li[index]:
            right = index
            index = int((left + index) / 2)
        elif toFind > li[index]:
            left = index
            index = int((right + index) / 2)

    return False

li = [1, 3, 4, 5, 7, 8, 10, 22, 40]
result = binary_search(li, 22)
print(result)

li = [1, 3, 4, 5, 7, 8, 10, 22, 40]
result = binary_search(li, 9)
print(result)


# Problem 5
def binary_search_rec(li, toFind):
    return binary_search_rec_helper(li, toFind, int(len(li)/2), 0, len(li))

def binary_search_rec_helper(li, toFind, index, left, right):
    isFound = False
    if left < index and right > index:
        if toFind == li[index]:
            isFound = True
        elif toFind < li[index]:
            right = index
            index = int((left + index) / 2)
            isFound = binary_search_rec_helper(li, toFind, index, left, right)
        elif toFind > li[index]:
            left = index
            index = int((right + index) / 2)
            isFound = binary_search_rec_helper(li, toFind, index, left, right)

    return isFound

li = [1, 3, 4, 5, 7, 8, 10, 22, 40]
result = binary_search_rec(li, 22)
print(result)

li = [1, 3, 4, 5, 7, 8, 10, 22, 40]
result = binary_search_rec(li, 9)
print(result)


# Problem 6
def bubble_sort(li):
    print("before Bubble Sort, li = ", li)

    for i in range(len(li)):
        for j in range(1, len(li) - i):
            if li[j-1] > li[j]:
                temp = li[j-1]
                li[j-1] = li[j]
                li[j] = temp

    print("after Bubble Sort, li = ", li)
    return li

li = [4, 2, 6, 3, 5, 8, 3, 9, 7, 1]
result = bubble_sort(li)
print(result)