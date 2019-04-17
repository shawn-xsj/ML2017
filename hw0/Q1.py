
fileA = open('/home/xsj/project_our/ML2017/ML2017/hw0/data/matrixA.txt')

import numpy as np
fileB = open('/home/xsj/project_our/ML2017/ML2017/hw0/data/matrixB.txt')
dataA=[]
dataB=[]

for line in fileA.readlines():
	per_Line = line.strip('').split(",")
	for a in per_Line:
		dataA.append(int(a))

dataA_arr = np.array(dataA)
print(dataA_arr.shape)


for lineB in fileB.readlines():


	per_LineB = lineB.split(",", 9)
	print(per_LineB[-1])
	for b in per_LineB:
		dataB.append(int(b))



dataB_arr = np.array(dataB)
# print(dataB_arr)
dataB_arr.resize(50,10)

result = np.dot(dataA_arr,dataB_arr)
result.sort(axis=0,kind='quicksort',order=None)

# print(result[1])

with open('Q1_ans.txt','w') as fR:
	for i in range(len(result)):
		r = result[i]
		r2 = str(r)
		fR.write(r2)
		fR.write('\n')








# strA = fileA.read()
# print(strA)

# with open(fileA, 'r') as fA:
	
	
# 	strA = fA.read()


# strB = []
# with open(fileB, 'r') as fB:
	
# 	for line in fB:
# 		strB_Tmp = fB.readline()
# 		strB.append(line)




# strA_List = list(strA)
# print(strA_List)
# print(strB)

