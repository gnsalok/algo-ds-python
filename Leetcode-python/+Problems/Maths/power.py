def calculatePower(num, pow):
    result = num
    while(pow != 1):
        result = result * num
        pow -= 1
    return result


print(calculatePower(3,2))   #   3 * 3 = 9