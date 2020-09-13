def common_elements(l1, l2):
    result = []
    for ele in l1:
        if ele in l2:
            result.append(ele)
    return result


a = [1, 2, 3, 4, 5]
b = [2, 6, 7, 8, 9]

print(common_elements(a, b))
