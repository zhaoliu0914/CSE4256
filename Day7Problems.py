# Question 1
def union(s1, s2):
    result = set()
    for temp in s1:
        result.add(temp)

    for temp in s2:
        if temp not in result:
            result.add(temp)

    return result

s1 = {1, 2, 3, 5}
s2 = {2, 3, 4}

result = union(s1, s2)
print(result)


def difference(s1, s2):
    result = set()
    for temp in s1:
        result.add(temp)

    for temp in s2:
        if temp in result:
            result.remove(temp)

    return result

s1 = {1,2,3,5}
s2 = {2,3,4}
result = difference(s1, s2)
print(result)


def is_subset(s1, s2):
    isSubset = True

    for temp in s2:
        if temp not in s1:
            isSubset = False

    return isSubset

s1 = {1,2,3,4, 5}
s2 = {2,3,4}
result = is_subset(s1, s2)
print(result)


def are_disjoint(s1, s2):
    isDisjoint = True

    for temp in s2:
        if temp in s1:
            isDisjoint = False

    return isDisjoint

s1 = {1,2,3, 5}
s2 = {4}
result = are_disjoint(s1, s2)
print(result)


def symmetric_difference(s1, s2):
    result = set()
    for temp in s1:
        result.add(temp)

    for temp in s2:
        if temp in result:
            result.remove(temp)
        elif temp not in result:
            result.add(temp)

    return result

s1 = {1,2,3,5}
s2 = {2,3,4}
result = symmetric_difference(s1, s2)
print(result)


def cartesian_product(s1, s2):
    result = set()

    for first in s1:
        for second in s2:
            result.add((first, second))

    return result

s1 = {1,2}
s2 = {2,3,4}
result = cartesian_product(s1, s2)
print(result)


def union2(*args):
    result = set()

    for arg in args:
        for temp in arg:
            if temp not in result:
                result.add(temp)

    return result

s1 = {1, 2, 4}
s2 = {2, 5}
s3 = {3, 4, 5, 6, 7}

result = union2(s1, s2, s3)
print(result)


# Question 2a
def encode(s):
    current_char = s[0]
    current_count = 1
    index = 1

    result = ""

    while index < len(s):
        temp = s[index]

        if current_char == temp:
            current_count = current_count + 1
        else:
            result += str(current_count) + current_char

            current_char = temp
            current_count = 1

        index = index + 1

    result += str(current_count) + current_char

    return result

input = "AAAABBBCCDAA"
result = encode(input)
print(result)

# question 2b
def decode(s):
    result = ""
    index = 0

    while index < len(s):
        count = s[index]
        count = int(count)
        index = index + 1
        char = s[index]

        for temp in range(count):
            result += char

        index = index + 1

    return result

input = "4A3B2C1D2A"
result = decode(input)
print(result)


# question 3
def shortest_path(s):
    result = []
    tokens = s.split("/")

    for index in range(1, len(tokens)):
        token = tokens[index]

        if token == ".":
            continue
        elif token == "..":
            result.pop(-1)
        else:
            result.append(token)

    final = "/" + "/".join(result) + "/"

    return final

input = "/usr/bin/../bin/./scripts/../"
result = shortest_path(input)
print(result)