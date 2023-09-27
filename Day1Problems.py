#Question 1
def sum_largest(li):
    firstLargest = float("-inf")
    for temp in li:
        if temp > firstLargest:
            firstLargest = temp

    secondLargest = float("-inf")
    for temp in li:
        if temp > secondLargest and temp != firstLargest:
            secondLargest = temp

    return firstLargest + secondLargest

li = [10, 4, 6, 12, -3, 1, 14, -7, 9]
sum = sum_largest(li)
print(sum)

# Question 2
def sum_largest_1(li):
    li.sort()
    return li[-1] + li[-2]

li = [10, 4, 6, 12, -3, 1, 14, -7, 9]
sum = sum_largest_1(li)
print(sum)

# Question 4
def merge_list(li1, li2):
    mergedList = []

    li1Index = 0
    li1Length = len(li1)
    li2Index = 0
    li2Length = len(li2)

    while li1Index < li1Length and li2Index < li2Length:
        if li1[li1Index] < li2[li2Index]:
            mergedList.append(li1[li1Index])
            li1Index = li1Index + 1
        elif li2[li2Index] < li1[li1Index]:
            mergedList.append(li2[li2Index])
            li2Index = li2Index + 1
        else:
            mergedList.append(li1[li1Index])
            mergedList.append(li2[li2Index])
            li1Index = li1Index + 1
            li2Index = li2Index + 1

        if li1Index == li1Length:
            for temp in li2[li2Index:]:
                mergedList.append(temp)
            print(li2[li2Index:])
            return mergedList
        if li2Index == li2Length:
            for temp in li1[li1Index:]:
                mergedList.append(temp)
            return mergedList
    return mergedList

li1 = [2, 4, 5, 8, 10, 11, 13]
li2 = [3, 6, 7, 8, 10, 12]
mergedList = merge_list(li1, li2)

print(mergedList)

# Question 5
def largest_so_far(li):
    largestList = [li[0]]

    for temp in li:
        if temp > li[len(li) - 1]:
            largestList.append(temp)

    print(largestList)
    return len(largestList)

li = [10, 8, 9, 9, 13, 16, 12]
number = largest_so_far(li)
print(number)

# Question 6
def evens(li):
    index = 0
    numberEven = 0

    while index < len(li):
        if li[index] % 2 == 0:
            numberEven = numberEven + 1
        index = index + 2
    return numberEven

li = [3, -2, 4, 7, -6, 7, 5]
number = evens(li)
print(number)