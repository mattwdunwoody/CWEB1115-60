"""data = [1,3,4,6,7,8,10,13,14,18,19,21,24,37,40,45,71]
elem = 7

# linear search
for i in range(len(data)):
    if data[i] != elem:
        print("linear search:",i)
    elif data[i] == elem:
        print("linear search matching index:",i)
        break
# binary search
def binary_search(data, elem):
    low = 0
    high = len(data)-1
    while low <= high:
        print(f"binary search-high {high} ", end='')
        print(f"binary search-low {low}")
        middle = (low + high)//2
        if data[middle] == elem:
            return middle
        elif data[middle] > elem:
            high = middle - 1
        else:
            low = middle + 1
    return -1

print(binary_search(data, elem))

from bisect import bisect_left

def BinarySearch(data, elem):
    i = bisect_left(data,elem)
    if i != len(data) and data[i] == elem:
        return i
    else:
        return -1
    
result = BinarySearch(data, elem)
if result == 1:
    print(elem, "is absent.")
else:
    print(f'bisect function matches index: {result}')"""

def demo_big_o_squared(num):
    i = 0
    while i < num:
        i = i + 1
        j = 0
        while j < num:
            j = j + 1
            print("i is now: " + str(i) + " and j is now: " + str(j))

demo_big_o_squared(2)

def demo_big_o_cubed(num):
    i = 0
    while i < num:
        i = i + 1
        j = 0
        while j < num:
            j = j + 1
            k = 0
            while k < num:
                k = k + 1
                print("i is now: " + str(i) + ", j is now: " + str(j) + ", and k is now: " + str(k))

demo_big_o_cubed(2)