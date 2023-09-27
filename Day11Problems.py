def rod_cut(values, total_length):
    if total_length == 0:
        return 0
    if total_length < 0:
        return float("-inf")

    maximum = float("-inf")
    for i in range(len(values)):
        maximum = max(maximum, values[i] + rod_cut(values, total_length - i - 1))

    return maximum

values = [1, 5, 8, 9, 10, 17, 17, 20]
total_length = 8
#result = rod_cut(values, total_length)
#print("result = ", result)


def rod_cut_memo(values, total_length, dic):
    if total_length == 0:
        return 0
    if total_length < 0:
        return float("-inf")

    maximum = float("-inf")
    for i in range(len(values)):
        catch = dic.get(str(total_length - i - 1)) #dic[str(total_length - i - 1)]
        if catch is None:
            temp = rod_cut(values, total_length - i - 1)
            dic[str(total_length - i - 1)] = temp
            maximum = max(maximum, values[i] + temp)
        else:
            maximum = max(maximum, values[i] + catch)

    return maximum

values = [1, 5, 8, 9, 10, 17, 17, 20]
total_length = 20
dic = {}
result = rod_cut_memo(values, total_length, dic)
print("result = ", result)