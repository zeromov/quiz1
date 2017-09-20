from collections import OrderedDict
L =[3,4,1,6,7,2,1,1]

d = OrderedDict()
for index in range(len(L)):
    d[index]=L[index]
    
N_f=[]
Check_exist=set()
N_f.append(d[0])
# if not 0
#Check_exist.add(0)

#for index in range(len(L)):
    #print(index)
index = 0
#while(len(Check_exist)!=(len(L))):
if d[index] not in Check_exist:
    #N_f.append(d[index])
    Check_exist.add(index)
    index = d[index]
if d[index] not in Check_exist:
    N_f.append(d[index])
    Check_exist.add(index)
    index = d[index]
if d[index] not in Check_exist:
    N_f.append(d[index])
    Check_exist.add(index)
    index = d[index]
if d[index] not in Check_exist:
    N_f.append(d[index])
    Check_exist.add(index)
    index = d[index]
if d[index] not in Check_exist:
    N_f.append(d[index])
    Check_exist.add(index)
    index = d[index]
    print(index)
    if d[index] not in Check_exist:
        N_f.append(d[index])
        Check_exist.add(index)
        index = d[index]
        print(index)
    else:
        for i in range(len(L)):
            if(i) not in Check_exist:
                N_f.append(d[i])
                Check_exist.add(i)
                index = d[i]
                print(index)
                break
        if d[index] not in Check_exist:
            N_f.append(d[index])
            Check_exist.add(index)
            index = d[index]
            print(index)
        else:
            for i in range(len(L)):
                if(i) not in Check_exist:
                    N_f.append(d[i])
                    Check_exist.add(i)
                    index = d[i]
                    print(index)
                    break    
        
  
     
  

print(N_f)
print(Check_exist)
