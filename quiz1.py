from collections import OrderedDict
L =[4,5,8,0,7,3,0,2,1]

def Generate_order(L):
        d = OrderedDict()
        for index in range(len(L)):
            d[index]=L[index]   
        N_f=[]
        Check_exist=set()
        index = 0
        while(len(Check_exist)!=len(L)):
            if index not in Check_exist:     
                N_f.append(d[index])
                Check_exist.add(index)
                index = d[index]
            else:
                for b in range(len(L)):
                    if b not in Check_exist:
                        index = b
                        break
        return N_f
print(Generate_order(L))

