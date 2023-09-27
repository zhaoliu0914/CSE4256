di = {}

di = {
    "Joe": 46,
    "Brian": 20,
    "Sam": 21,
    "Marcy": 18,
    "Mary": 38
}

print(di)
print(di["Sam"])

di["Sam"] = 28

# print(di["Max"])

for k, v in di.items():
    print(k, ",", v)


def oldest(di):
    oldest_person = ""
    oldest_age = 0
    for name, age in di.items():
        if age > oldest_age:
            oldest_person = name
            oldest_age = age
    return oldest_person


oldest_person = oldest(di)

print(oldest_person)

grades = {
    "Mike": [70, 89, 55, 98],
    "Jane": [89, 75, 87, 90],
    "Mary": [55, 72, 80, 59]
}

def average_grade(grades):
    average = {}
    for name, grade in grades.items():
        aver = sum(grade) / len(grade)
        average[name] = aver
        #print("name = ", name)
        #print("grade = ", grade)
    return average

average = average_grade(grades)
print(average)