# Remove the last element in the array
def popback(self):
    if self.length > 0:
        self.length -= 1

# Get value at i-th index
def get(self, i):
    if i < self.length:
        return self.arr[i]
    # Here we would throw an out of bounds exception

# Insert n at i-th index
def insert(self, i, n):
    if i < self.length:
        self.arr[i] = n
        return
    # Here we would throw an out of bounds exception       

def print(self):
    for i in range(self.length):
        print(self.arr[i])
    print()



    








arr = [4,5,6]



# removeMiddle(arr,1, len(arr))
# removeEnd(arr)

insertEnd(arr, 7, len(arr), 5)


print(arr)
