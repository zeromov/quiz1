import math

L =[1,2,3,4,5]
# Replace this comment with your code
M = []
N = []




def push_middle(L):
    M_f =[]
    Pop_index=0
    Middle_index=math.floor(len(L)/2)
    if len(L)==1:
        return L
    else:
        M_f.append(L[Middle_index])
        for index in range(Middle_index):
            print(index)
            M_f.append(L[index])
            if len(L)%2 ==0:
                M_f.append(L[-(index)+1])
            else:
                M_f.append(L[-(index+1)])
        
        print('列表的中值：',M_f[0])
        print('列表的中值索引：',Middle_index)
        
        print(M_f)
        
M=push_middle(L)        

print('\nHere is M:')
print('  ', M)
print('\nHere is N:')
print('  ', N)
print('\nHere is L again:')
print('  ', L)