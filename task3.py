input = open('input3.txt', 'r')
output = open('output3.txt', 'w')
total = int(input.readline())
id = list(map(int, input.readline().split(" ")))
marks = list(map(int, input.readline().split(" ")))

dict_a = {}
for i in range(total):
    if marks[i] not in dict_a:
        dict_a[marks[i]] = [id[i]]
    else:
        dict_a[marks[i]] += [id[i]]

def selection_Sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(i, n-1):
            if arr[i] < arr[j+1]:
                temp = arr[i]
                arr[i] = arr[j+1]
                arr[j+1] = temp
    return arr 

sort_marks= selection_Sort(marks)

for i in dict_a:
    if len(dict_a[i]) > 1:
        dict_a[i] = selection_Sort(dict_a[i])

check = []

for i in sort_marks:
    if i not in check:
        for j in range(len(dict_a[i])-1, -1, -1): 
            print(f"ID: {dict_a[i][j]} Mark: {i}", file = output)
        check += [i]
        
input.close()
output.close()