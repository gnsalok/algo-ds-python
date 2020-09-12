''' string reversal'''


def string_reversal1(mystr):
    revstr = ''
    for i in range(len(mystr)-1, -1, -1):
        revstr = revstr + mystr[i]

    return revstr


def string_reversal_recursive(mystr, num):
    print(num , " :: ", mystr)
    if mystr == "":
        return mystr
    else:
        num += 1
        #return string_reversal_recursive(mystr[1:], num ) + mystr[0]
        return mystr[-1] + string_reversal_recursive(mystr[:-1], num)


def array_revseral_resursive(myarr, start , end):
    if start >= end:
        return myarr
    myarr[start], myarr[end] = myarr[end], myarr[start]
    array_revseral_resursive(myarr, start+1, end-1)

if __name__ == '__main__':
    mystring = 'santosh'
    # rev = string_reversal1(mystring)
    # print(rev)

    rev1 = string_reversal_recursive(mystring, 0)
    print(rev1)

    # myarr = [3, 4, 5, -1]
    # array_revseral_resursive(myarr, 0, len(myarr)-1)
    # print(myarr)