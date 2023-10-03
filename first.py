#1
X = int(input())
Y = int(input())
Z = int(input())
arr = [X,Y,Z]
print("минимальное значение: ", min(arr))

#2
X = int(input())
Y = int(input())
Z = int(input())
arr1 = [X,Y,Z]
arr2 = []

for i in arr1:
if i>=0:
arr2.append(i*i)
print(arr2)

#3
#R = int(input())
#S = int(input())
Diametr = int(input())
Diag = int(input())
if Diametr >= Diag:
print("Поместится")
else:
print("Не поместится")

#4
F = int(input())
M = int(input())
if F==M/2+7:
print("Возраст подходит")
else:
print("Возраст не подходит")


#5
X = int(input())
Y = int(input())
Z = int(input())
arr = [X,Y,Z]

if Y!=X and Y!=Z:
if X+Y+Z<1:
minn = min(arr)


#6
X = int(input())
Y = int(input())
arr = []



if X>Y:
Y+=X
X-=Y
arr.append(X)
arr.append(Y)
elif X<Y:
X+=Y
Y-=X
arr.append(X)
arr.append(Y)
else:
print("значения равны")
print(arr)








minn = min(arr)
minn = X+Y
arr.append(minn)
maxx = max(arr)
maxx =

