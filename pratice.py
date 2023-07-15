import matplotlib.pyplot as plt
import numpy as np
#numpy basic
arr=np.array([1,2,3,4,5,6,7,8])
print(arr[-3:-1])
print(arr[1:3])
print(arr[::2])
print(arr)
print(arr[0])
print(arr[1]+arr[4])
print(np.__version__)
print(type(arr))
ar=np.array([[1,2,4,6,7],[2,8,3,5,7]])
print(ar[0,2])
print(ar)
print(arr.ndim)
arr=np.array([1,2,3,4,5,6,7,8])
x=arr.copy()
y=arr.view()
arr[0]=42
print(arr)
print(x)
print(y)
print(arr.dtype)
print(arr.ndim)
arr=np.array([1,2,3,4,5,6,7,8,9,10])
ar=np.array([1,2,3,4,5,6,7,8,9])
x=arr.view()
arr[0]=42
print(arr)
print(x.base)
print(arr.shape)
new_arr=arr.reshape(5,2)
new_3=ar.reshape(3,3)
print(new_3)
print(new_arr)


#plotting 
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("SALES")
plt.xlabel('x-axis')
plt.ylabel('y-axis')

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 2, 2)
plt.plot(x,y,linestyle="--",linewidth=0.5,color='r')
plt.title("INCOME")
plt.xlabel('x-axis',color='red')
plt.ylabel('y-axis',color='blue')
plt.grid(color='black',linestyle=":")
plt.show()

#plot 3:
plt.subplot(2,2,3)
x=np.array([10,20,30,40,50,60,70,80,90])
y=np.array([100,200,300,400,500,600,700,800,900])
plt.title("random data",color="red")
plt.xlabel("x axis",color="blue")
plt.ylabel("y axis",color="green")
plt.bar(x,y,linestyle=":",linewidth=0.6)
plt.show()


#pie chart and histogram
x=np.random.normal(170,10,250)
print(x)
plt.hist(x)
plt.show()
plt.pie(x)
plt.show()x=np.array([1,2,3,4,5,6,7,8,9,10])
y=np.array([10,20,30,40,50,60,70,80,90,100])
plt.plot(x,y)
plt.title("random data")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(color='red',linestyle=':',linewidth=0.8)
plt.show()
ypoints=np.array([3,6,7,8,9,1,10])
xpoints=([1,2,3,4,5,6,7])
plt.plot(xpoints,ypoints,marker='*',ms=10,mec='g',mfc='y')
zpoints = np.array([3, 8, 1, 10])
plt.plot(zpoints, 'o--r',ms=10,mec='m',mfc='y')
plt.show()
y=np.array([35,25,25,15])
mylabels=["apple","bananas","cherries","dates"]
plt.pie(y,labels=mylabels)
plt.show()
