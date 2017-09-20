
# Replace this comment with your code
import math

L =[1,2,3]

M = []
N = []




def push_middle(L):
    M_f =[]
    Middle_index=math.floor(len(L)/2)
    if len(L)==1:
        return L
    else:
        M_f.append(L[Middle_index])
        if len(L)%2 ==0:
            for index in range(Middle_index):
                M_f.append(L[index])
                M_f.append(L[-(index+1)])
            M_f.pop()
        else:
             for index in range(Middle_index):
                M_f.append(L[index])
                M_f.append(L[-(index+1)])
    return M_f

        
M=push_middle(L)        

print('\nHere is M:')
print('  ', M)
print('\nHere is N:')
print('  ', N)
print('\nHere is L again:')
print('  ', L)