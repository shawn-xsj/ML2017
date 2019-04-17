import numpy as np

fileA = '/home/xsj/project_our/ML2017/ML2017/hw0/data/matrixA.txt'
fileB = '/home/xsj/project_our/ML2017/ML2017/hw0/data/matrixB.txt'
with open(fileA,"r") as fA:
	matrixA = fA.read().split(',')
	matrixA = list(map(int,matrixA))
	# print(matrixA)

with open(fileB,"r") as fB:
	matrixB = fB.readlines()

	matrixB = [line.strip() for line in matrixB]
	matrixB = [list(map(int,line.split(','))) for line in matrixB]
A = np.array(matrixA)
B = np.array(matrixB)
C = A.dot(B)
C =np.sort(C)
np.savetxt("ans_update.txt",C,fmt="%d")
