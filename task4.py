input=open("input4.txt","r")
output=open("output4.txt","w")

total = int(input.readline())
train_names= []
information= {}
for i in range(total):
    str = input.readline().split(" ")
    tm = str[6].split(":")
    time = tm[0] + tm[1][:-1]
    if str[0] not in information:
        information[str[0]] = [str[4]]
    else:
        information[str[0]] += [str[4]]
    information[str[0]] += [time]
    train_names+= [str[0]]
# print(information, file = out)

def insertion_Sort(arr):
    n = len(arr)
    for i in range(1, n):
        val = arr[i]
        hole = i
        while hole > 0 and arr[hole-1] > val:
            arr[hole] = arr[hole-1]
            hole -= 1
        arr[hole] = val
    return arr

train_sorted = insertion_Sort(train_names)

l3 = []

for i in train_sorted:
    time = information[i][1]
    max_time = int(time)
    place = information[i][0]
    for j in range(1, len(information[i]), 2):
        if max_time < int(information[i][j]):
            time = information[i][j]
            max_time = int(information[i][j])
            place = information[i][j-1]   
    print(f"{i} will departure for {place} at {time[:2]}:{time[2:]} ", file = output)
    information[i].remove(time)
    information[i].remove(place)
    
input.close()
output.close()