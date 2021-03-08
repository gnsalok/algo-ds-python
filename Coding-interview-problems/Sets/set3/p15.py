def remove_dup(a):
    """ remove duplicates using extra array """
    res = []
    count = 0
    for i in range(0, len(a)-1):
        if a[i] != a[i+1]:
            res.append(a[i])
            count = count + 1

    res.append(a[len(a)-1])
    print('Total count of unique elements: {}'.format(count + 1))

    return res


if __name__ == '__main__':
    sorted_a = [1, 2, 2, 3, 3, 4, 5, 10, 11, 11]
    res = remove_dup(sorted_a)
    print(res)
