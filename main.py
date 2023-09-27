def add_one(n):
    result = n+1
    return result

a = 5
b = add_one(a)

print("a = ", a)
print("b = ", b)

def if_even(n):
    if n%2 == 0:
        return True
    else:
        return False

def generation(birth_year):
    if birth_year <= 1945:
        return "Silent"
    elif birth_year <= 1964:
        return "Boomer"
    elif birth_year <= 1976:
        return "Gen X"
    elif birth_year <= 1995:
        return "Millenial"
    elif birth_year <= 2015:
        return "Gen Z"
    else:
        return "Gen Alpha"


print(generation(1999))

li = []
li = [3, 6, 2, 8, 4]

print(len(li))

li.append(42)
print(li)
print(li[-1])

for temp in li:
    print(temp)

sum = 0
for temp in li:
    sum = sum + temp

print(sum)

for i in range(5):
    print(i)

x = 1
while x < 10:
    print(x)
    x = x + 2

print("====================")

for temp in range(0, 10, 2):
    print(temp)

for i in range(2):
    for j in range(3):
        print("i = ", i, " j = ", j)

