import numpy as np

print("随机零")
print(np.zeros([6,5]))

print("随机数")
print(np.random.rand())
print(np.random.rand(3,2))

print("整数随机数")
print(np.random.randint(1,100,3))

print("正态分布")
print(np.random.randn(3,3))

print("Choice")
print(np.random.choice([2,4,6]))

print("distribute")
print(np.random.beta(1,10,10))

# lst = print(np.arange(1,13).reshape([3,-1]))
#
# print('exp')
# print(np.exp(lst),dtype=np.float32)
# print('exp2')
# print(np.exp2(lst))
# print('sqrt')
# print(np.sqrt(lst))
# print('sin')
# print(np.sin(lst))
# print('log')
# print(np.log(lst))

lst = np.array([
        [[1,2,3,4],[4,5,6,7]],
        [[7,8,9,10],[11,12,13,14]],
        [[14,15,16,17],[18,19,20,21]]
    ])

print('sum')
print(lst.sum(axis=2))
print('max')
print(lst.max(axis=1))
print('mini')
print(lst.min(axis=0))

lst1 = np.array([10,20,30,40,50,60])
lst2 = np.array([6,5,4,3,2,1])
print('add')
print(lst1+lst2)
print('sub')
print((lst1-lst2))
print('mul')
print(lst1*lst2)
print('div')
print(lst1/lst2)
print('square')
print(lst1**lst2)
print('dot：点乘')
print(np.dot(lst1.reshape([2,3]),lst2.reshape([3,2])))

print('Cancatenate')
print(np.concatenate((lst1,lst2),axis=0))
print('合并矩阵')
print(np.vstack((lst1,lst2)))
print('同级合并')
print(np.hstack((lst1,lst2)))
print('分割')
print(np.split(lst1,2))
print('拷贝')
print(np.copy(lst1))

from numpy.linalg import *
print(np.eye(3))
lst3 = np.array([[1,2],[3,4]])

print('Inv:逆矩阵')
print(inv(lst3))

print("T：转置矩阵")
print(lst3.transpose())

print('Det:矩阵的行列式')
print(det(lst3))

print('eig')
print(eig(lst3))

y = np.array([[5],[7]])
print('Solve')
print(solve(lst3,y))

print('FFT：傅里叶变换')
print(np.fft.fft(np.array([1,1,1,1,1,1,1,1])))

print('Coef：相关系数运算')
print(np.corrcoef([1,0,1],[0,2,1]))

print('Poly:一元多次函数')
print(np.poly1d([2,1,3]))
