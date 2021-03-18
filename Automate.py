#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.getcwd()
os.chdir(r'D:\Python Training\ML\Dataset') # r - raw
os.getcwd()


# In[6]:


from datetime import datetime as dt
dts = dt.now().strftime('%Y-%m-%d')
dts


# In[7]:


inputfile = "logsqlinj_"+dts+'.csv'
inputfile


# In[2]:


f = open('mtcars.csv','r')

fout = open('hpgreater200_2021-03-18.csv','w')

for line in f:
    #print(type(line),line)
    recordlist = line.split(',')
    print(type(recordlist),recordlist,"--hp----",recordlist[4])
    
    if (recordlist[4]=='hp'):   # This is a header, simply write it
        outline = ','.join(recordlist)
        fout.write(outline)
    else:     # Not a header, check the value > 200 before writing it
        if (int(recordlist[4]) > 200):
            outline = ','.join(recordlist)
            fout.write(outline)

f.close()
fout.close()

