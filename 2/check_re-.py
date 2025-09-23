ans2=open("challenge/challenge2.out",'r').read().rstrip()
'''
A=['Ba','Be','Bk','Bj','Bo','Bn']
for i in range(len(A)):
    ans2=ans2.replace(A[i],str(i))
'''
print(len(ans2))
ans2=ans2.replace('B','')
print(len(ans2))

with open('2/prt.txt','w')as f:
    f.write(ans2)
