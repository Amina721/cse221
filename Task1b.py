user1=open("input1b.txt","r")
user1_out=open("output1b.txt","w")
limit= int(user1.readline())
for i in range(limit):
    line = user1.readline().strip().split(" ")
    
    if line[2] == "+":
        print(f"The result of {line[1]} {line[2]} {line[3]} is {str(int(line[1]) + int(line[3]))}", file = user1_out)
    if line[2] == "-":
        print(f"The result of {line[1]} {line[2]} {line[3]} is {str(int(line[1]) - int(line[3]))}", file = user1_out)
    if line[2] == "/":
        print(f"The result of {line[1]} {line[2]} {line[3]} is {str(int(line[1]) / int(line[3]))}", file = user1_out)
    if line[2] == "*":
        print(f"The result of {line[1]} {line[2]} {line[3]} is {str(int(line[1]) * int(line[3]))}", file = user1_out)
        
user1.close()
user1_out.close()
