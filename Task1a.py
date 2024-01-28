# -*- coding: utf-8 -*-


user1=open("input1a.txt","r")
user1_out=open("output1a.txt","w")
limit=int(user1.readline())
for i in range (limit):
  elem=int(user1.readline())
  if elem%2 ==0:
    print(elem,"is an even number",file=user1_out)
  else:
    print(elem,"is an odd number",file=user1_out)