input=open("input2.txt","r")
output=open("output2.txt","w")

limit=int(input.readline())
#arr=input.readline().split()
flag=False
def bubbleSort(arr):
    for i in range(len(arr)-1):
        flag = True
        for j in range(len(arr)-i-1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                is_sorted = False
        if is_sorted:
           break
    return arr

numbers = bubbleSort(list(map(int, input.readline().split(" "))))

sorted_array= ""
for k in range(limit):
    sorted_array += str(numbers[k]) + " "
print(sorted_array, file = output)

"""The best-case scenario occurs when the array is already sorted. In this case, there is no need for any swapping operations. During the first iteration of the outer loop, if the inner loop does not perform any swapping operations, it indicates that the array is sorted. In my code, when the argument "is_sorted" is True in the first iteration, the loop will automatically break. Therefore, the loop will run only once in the best-case scenario."""