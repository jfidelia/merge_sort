numbers = [55, 22, 77, 31, 19, 88, 11, 65]

def mergeSort(aList):

     if len(aList) > 1:
        middle = len(aList) // 2
        left = aList[:middle]
        right = aList[middle:]
        print(left, right)
    

print(mergeSort(numbers))