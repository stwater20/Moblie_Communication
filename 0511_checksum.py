#!/usr/bin/env python
# coding: utf-8

# In[49]:


import sys

def checksum(ex1):
#    ex1=["8400","0047","32EC","4022","7645","XXXX","CE54","035B","5123","5421"]
    tempData = int(ex1[0],16)
    tempSum = 0
    for i in range(1,len(ex1)):
        if len(str(hex(tempData)))>6:
            tempData = tempData+int(str(hex(tempData))[2],16)
            tempData = int(str(hex(tempData))[3:],16)
        if ex1[i]=="XXXX":
            ex1[i]="0000"
        temp1 = int(ex1[i],16)
        tempSum = int(tempData)+int(temp1)
        tempData = tempSum
        print(hex(tempData))
    print("----------")
    print(hex(int("0xffff",16)-tempData+1))
    answer = hex(int("0xffff",16)-tempData+1)
    return answer

def checksum_split(s):
    ex1 = []
    ex1 = s.split(" ")
    print(ex1)
    return ex1[2:]
    
if __name__=="__main__":
    ex = []
    a = sys.argv
    for i in range(1,len(a)):
        ex.append(a[i])
    print(checksum(ex))


# In[25]:





# In[ ]:




