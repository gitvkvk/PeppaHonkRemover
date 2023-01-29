import audioread
import os
import matplotlib.pyplot as plt


directory = r"C:\Users\kvk19\Projects\PeppaHonkRemover\SamplesOriginal\Honks"
directory2 = r"C:\Users\kvk19\Projects\PeppaHonkRemover\SamplesOriginal\NotHonks"

data = []

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)

    if os.path.isfile(f):
        g = audioread.audio_open(f)
        totalsec = g.duration
    
        #print(totalsec)
        data.append(totalsec)

data.sort()
print("\n")
print(data[0])
print( sum(data)/len(data))

#plt.hist(data, 100)
#plt.show()


#smallest sample size is 0.08
#using a sampling size of 1/3 the sample size
#this ensures only a maximum of 1/3 of 0.08 is removed from each sample when normalizing lengths



remainders = []

for points in data:
    g = points % 0.027
    remainders.append(g)

print("\n")
print(len(remainders))
plt.hist(remainders, 100)
plt.show()





for filename in os.listdir(directory2):
    f = os.path.join(directory2, filename)
    if os.path.isfile(f):
        g = audioread.audio_open(f)
        totalsec = g.duration
        print(totalsec)





  


        




        
