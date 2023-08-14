import pandas as pd
import numpy as np
import csv
import os
import matplotlib.pyplot as plt
d={'col1':[1,2,3,4,7],'col2':[4,5,6,9,8],'col3':[7,8,12,1,11]}
df=pd.DataFrame(data=d)
print(df)
count_column=df.shape[1]
print("Number of column: "+str(count_column))
count_row=df.shape[0]
print("Number of rows: "+str(count_row))
Average_pulse_max=max(80,85,90,100,105,110,115,120,125)
print("Maximum number: "+str(Average_pulse_max))
calorie_burnage=[240,245,250,255,260,270,210]
Average_calorie_burnage=np.mean(calorie_burnage)
print("Mean of data:"+str(Average_calorie_burnage))
sports_data={'duration':[30,30,45,45,60,60,60,60,75,75],
      'Average_pulse':[80,85,90,95,100,105,110,115,120,125],
      'Max_Pulse':[120,120,130,130,140,140,145,145,150,150],
      'Calorie_Burnage':[240,250,260,270,280,290,300,310,320,330],
      'Hours_work':[10,10,8,8,0,7,7,9,0,8],
      'Hours_Sleep':[7,7,7,7,7,8,8,8,8,8]}
data_frame=pd.DataFrame(data=sports_data)
print(data_frame)
Average_pulse_min=min(calorie_burnage)
print(Average_pulse_min)

data=pd.read_csv(r"C:\\Users\\ac141\\Downloads\\student.csv")  #read cv file using pandas lib
print(data)
k=pd.DataFrame(data,columns=['name','mark'])  #printing only selective coulms
print(k)

data1={
    "duration":{
        "0":70,
        "1":70,
        "2":80,
        "3":80,
        "4":45,
        "5":70,
        "6":90
    },
    "pulse":{
        "0":110,
        "1":117,
        "2":103,
        "3":109,
        "4":117,
        "5":120,
        "6":102  
    },
    "Maxpulse":{
        "0":130,
        "1":125,
        "2":130,
        "3":145,
        "4":150,
        "5":135,
        "6":127
    },
    "Calories":{
        "0":409.1,
        "1":479.0,
        "2":340.0,
        "3":282.4,
        "4":312.2,
        "5":123.1,
        "6":406.3
    },
}
data1_frame=pd.DataFrame(data1)
print(data1)
print(data1_frame)
print(data.describe())
f=open("C:\\Users\\ac141\\OneDrive\\Desktop\\New Text Document.txt","r")
for x in f:
    print(x)
f=open("C:\\Users\\ac141\\OneDrive\\Desktop\\New Text Document.txt","a")
f.write("I am anurag chaturvedi.\n currently i am pursing btech in electronics and communication  at vit chennai")
f.close()
f=open("C:\\Users\\ac141\\OneDrive\\Desktop\\New Text Document.txt","r")
print(f.read())
if os.path.exists("C:\\Users\\ac141\\OneDrive\\Desktop\\New Text Document.txt"):
    os.remove("C:\\Users\\ac141\\OneDrive\\Desktop\\New Text Document.txt")
#else:
  print("file does'nt exist")
#xpoints=np.array([0,10])
#ypoints=np.array([0,300])
#plt.plot(ypoints,xpoints*5,'*')
#plt.show()
#xpoints=np.array([10,20,30,40,50,60,70,80,90])
#ypoints=np.array([1,2,3,4,5,6,7,8,9])
#plt.plot(ypoints,xpoints)
#plt.show()
#xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])
#plt.plot(xpoints, ypoints,marker='o',ms=20,mec='r')
#plt.show()
y2=np.array([1,2,3,0])
plt.plot(ypoints,color='r',linewidth=3.0)
plt.plot(y2,color='g',linewidth=3.0)
plt.show()    
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("C:\\Users\\ac141\\OneDrive\\Desktop\\CS\\csv data\\data.csv")
print(df.to_string)
print(df)
print(pd.options.display.max_columns)
print(pd.options.display.max_rows)
x=np.random.normal(5.0,1.0,1000)
plt.title("plot random normal data")
plt.xlabel("random data")
plt.ylabel("histogram")
plt.hist(x,100)
plt.show()
x=[5,7,8,7,2,17,2,9,4,11,12,9,6]
y=[99,86,87,88,111,86,103,97,94,78,77,85,86]
plt.title("plot scatter data")
plt.xlabel("scatter")
plt.ylabel("random data")
plt.scatter(x,y)
plt.show()
#x1=np.array([1,2,4,5,3,9,6,7,10,2])
#y1=np.array([20,32,13,24,15,19,8,11,12,14])
#plt.subplot(1,2,1)
#plt.scatter(x1,y1)
#x2=np.array([13,12,11,32,14,15,16,18,19])
#y2=np.array([11,32,13,18,15,19,20,14,2])
#plt.subplot([1,2,2])
#plt.plot(x2,y2)
#plt.show()
x1=np.array(["A","B","C","D"])
y1=np.array([3,1,90,32])
plt.bar(x1,y1,width=0.1)
plt.show()
plt.barh(x1,y1,color="red")
plt.show()
x1=np.array(["A","B","C","D"])
y1=np.array([3,1,90,32])
plt.bar(x1,y1,width=0.1)
plt.show()
plt.barh(x1,y1,color="red")
plt.show()
y=np.array([35,25,25,15])
mylabels=["apples","bananas","cherries","dates"]
plt.pie(y,labels=mylabels,startangle=90)
plt.title("pie data")
plt.show()
x3=np.array([30,21,5,18])
myexplode=[0.2,0.1,0.3,0.6]
plt.pie(x3,labels=x3,explode=myexplode)
plt.title("pie data")
plt.pie(y)
plt.show()
speed=[99,103,95,86,87,83,102,78,77,85,86,88,29,23]
x=np.mean(speed)
print(x)
y=np.median(speed)
print(y)
z=np.std(speed)
print(z)
k=np.var(speed)
print(k) 
ages=[5,31,43,48,50,41,11,15,7,39,80,32,2,8,6,25,36,27,61,31] 
a=np.percentile(ages,75)
print(a)  


    
