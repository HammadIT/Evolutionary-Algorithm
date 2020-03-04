from matplotlib.image import imread
import numpy as np
np.seterr(all='warn')
np.seterr(over='ignore')
import math
from random import randint
def crossover_mutate(arra):
    i=0
    while i<(np.shape(arra)[0]):    # will loop for each population
        p11=(arra[i,0])            # and make each consective parent
        p11=int(p11)
        binary_p11=np.binary_repr(p11) # for parent from X cordinates

        p21=(arra[i+1,0])
        p21=int(p21)
        binary_p21=np.binary_repr(p21)

        if(p11>p21):                # from parent pick the smaller one
            vallen=(len(binary_p21)) #beacue for corssover larger index will not present 
            cross_len1=(len(binary_p21))/2
            cross_len1=int(cross_len1)
            value1=randint(cross_len1,len(binary_p21)-1)
        else:
            vallen=(len(binary_p11))
            cross_len1=(len(binary_p11))/2
            cross_len1=int(cross_len1)
            value1=randint(cross_len1,len(binary_p11)-1) # crossover point mid to end

        
        while(value1<vallen):    # crossover each bit from random number to end
            temp1=binary_p11[value1]
            temp2=binary_p21[value1]
            binary_p21=  binary_p21[:value1] + temp1+  binary_p21[value1+1:]
        #binary_p21[value1]=temp1
        #binary_p11[value1]=temp2
            binary_p11=  binary_p11[:value1] + temp2+  binary_p11[value1+1:]
            value1+=1

        p12=(arra[i,1])            # for parent from Y cordinates
        p12=int(p12)
        binary_p12=np.binary_repr(p12)
        
       
        
        p22=(arra[i+1,1])
        p22=int(p22)
        binary_p22=np.binary_repr(p22)

        if(p12>p22):
            vallen=(len(binary_p22))
            cross_len2=(len(binary_p22))/2
            cross_len2=int(cross_len2)
            value2=randint(cross_len2,len(binary_p22)-1)
        else:
            vallen=(len(binary_p12))
            cross_len2=(len(binary_p12))/2
            cross_len2=int(cross_len2)
            value2=randint(cross_len2,len(binary_p12)-1)
        while(value2<vallen):
            temp1=binary_p12[value2]
            temp2=binary_p22[value2]
            binary_p22=  binary_p22[:value2] + temp1+  binary_p22[value2+1:]
            binary_p12=  binary_p12[:value2] + temp2+  binary_p12[value2+1:]
            value2+=1

        # mutation
        j=0
        for j in range(cross_len1,len(binary_p11)):  # from half length of bianry number till end
            if(np.random.uniform(0,1)<=0.02):
                if(binary_p11[j]=="0"):
                   binary_p11 = binary_p11[:j] + '1'+ binary_p11[j+ 1:]
                if(binary_p11[j]=="1"):
                   binary_p11 = binary_p11[:j] + '0'+ binary_p11[j+ 1:]
        j=0          
        for j in range(cross_len1,len(binary_p12)):
            if(np.random.uniform(0,1)<=0.02):
                if(binary_p12[j]=="0"):
                   binary_p12 = binary_p12[:j] + '1'+ binary_p12[j+ 1:]
                if(binary_p12[j]=="1"):
                   binary_p12 = binary_p12[:j] + '0'+ binary_p12[j+ 1:]
        j=0           
        for j in range(cross_len1,len(binary_p21)):
            if(np.random.uniform(0,1)<=0.02):
                if(binary_p21[j]=="0"):
                   binary_p21 = binary_p21[:j] + '1'+ binary_p21[j+ 1:]
                if(binary_p21[j]=="1"):
                   binary_p21 = binary_p21[:j] + '0'+ binary_p21[j+ 1:]
        j=0           
        for j in range(cross_len1,len(binary_p22)):
            if(np.random.uniform(0,1)<=0.02):
                if(binary_p22[j]=="0"):
                   binary_p22 = binary_p22[:j] + '1'+ binary_p22[j+ 1:]
                if(binary_p22[j]=="1"):
                   binary_p22 = binary_p22[:j] + '0'+ binary_p22[j+ 1:]
        # converison to decimal
        arra[i,0]=int(binary_p11,2)
        arra[i+1,0]=int(binary_p21,2)
        arra[i,1]=int(binary_p12,2)
        arra[i+1,1]=int(binary_p22,2)
        i=i+2
    


    




barriImage = imread('groupgray.jpg')
chotiImage = imread('boothigray.jpg')

print(np.shape(chotiImage))
z=barriImage[0:10][0:10]

print("yes")

population = np.zeros((30,3),dtype=np.float64)  # third cordinate will contain how much similarity

print(np.shape(barriImage)[0])
print(np.shape(barriImage)[1])
print(np.shape(chotiImage)[0])
print(np.shape(chotiImage)[1])

print(np.random.random())
print("yes")

def somcorr(a):         # this procedure is for watching similarity
    col=np.shape(a)[0]   #check for each corresponding indec of both images if similar then count increase
    row=np.shape(a)[1]
    picture=a.flatten('F')
    #print(np.shape(a))
    a=picture
    template=chotiImage.flatten('F')
    b=template
    z=0
    for k in range(0,len(a)):
        if(a[k]==b[k]):
            z+=1
    #print(z)
   
    divider=col*row      #total number of elements in flatten array
    #print(divider)
    return z/divider    # normalized
        
    
def normcorr(a):
    picture=a.flatten('F')
    #print(np.shape(a))
    a=picture
    template=chotiImage.flatten('F')
    b=template
    z=np.correlate(a,b)
    #print("lena")
    #print(len(a))
    #print("lenb")
    #print(len(a))
    
    #z=0
    #for k in range(0,len(a)):
     #   z=z+(a[k]*b[k])


        
    k=0
    h=0
    #print(z)
    for x in range(0,len(a)):
      k=int(k+(a[x]*a[x]))
    #print (k)
    kk=k
    for y in range(0,len(b)):
        h=int(h+(b[y]*b[y]))
    #print (h)
    hh=h
    f=int(kk*hh)
    #print(f)
    p=(math.sqrt(f))
    #print(p)
    return z/p   # normalized but if same images are given not 1 so woking not properly





        
        





for i in range(np.shape(population)[0]):
    
    while True:  # for making population in range so image raken cannot be get away from pic
        population[i,0] = round((np.random.random()*np.shape(barriImage)[0]))
        if(population[i,0]+np.shape(chotiImage)[0] <= np.shape(barriImage)[0]):
            break
    population[i,0]=int(population[i,0])
    while True:
        population[i,1] = round((np.random.random()*np.shape(barriImage)[1]))
        if(population[i,1]+np.shape(chotiImage)[1] <= np.shape(barriImage)[1]):
            break
    population[i,1]=int(population[i,1])
print(population[0,2])
counter=0    
n=0
while(n<=100):
    for i in range(np.shape(population)[0]):
        x=population[i,0]
        y=population[i,1]
        x=int(x)
        y=int(y)
        
        x2 =  x+ np.shape(chotiImage)[0]
        y2 = y + np.shape(chotiImage)[1]
        pic = barriImage[x:x2,y:y2]
        #population[i,2]=normcorr(pic)
        
        mn=(normcorr(pic))
        #mn=(somcorr(pic))
        print(mn)
        
        population[i,2]=mn
        
        
        if(population[i,2]>1.90):  # if simalirty increase to 0.90 stop
            print("yes pop is")
            
            counter=counter+1
            print(population[i,2])
            print("point has found")
            print(x)
            print(y)
            n=1001
            break
    if(n<=100):
        crossover_mutate(population)   # making them sort according to similarity
        for m in range(0,np.shape(population)[0]):
            for n in range(m+1,np.shape(population)[0]):
                if(population[m,2] > population[n,2] ):
                    temp2 = population[m,2]
                    population[m,2] = population[n,2]
                    population[n,2]= temp2

                    temp1 = population[m,1]
                    population[m,1] = population[n,1]
                    population[n,1]= temp1

                    temp0 = population[m,0]
                    population[m,0] = population[n,0]
                    population[n,0]= temp0

  
    
    #print(population[0,2])
    n=n+1

if(counter<1):
    print("maximum image not found but close points are")
    print(population[0,0])
    print(population[0,1])
    print("maximum image not found but probable image is")
    print(population[0,2])
    

