
def majority_element(nums):
    map = {}
    for num in nums:
        map[num] = map.get(num,0) + 1
    
    for n in nums:
        if(map[n] > len(num)//2):
            return n

        
    


def main():
    nums = [2,2,1,1,1,2,2]
    res = majority_element(nums)
    print(res)


if __name__ == "__main__":
    main()

