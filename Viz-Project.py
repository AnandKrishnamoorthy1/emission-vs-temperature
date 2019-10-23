
# coding: utf-8
# Analyzing Carbon dioxide emission VS Temperature 

# Problem Statement-
# How has the increase in the human emission of Carbon dioxide affect the temperature change over the last few years?
# Temperature and Carbon dioxide emission data: 
#https://ourworldindata.org/grapher/temperature-anomaly?time=1850..2017
#https://ourworldindata.org/grapher/cumulative-co-emissions?tab=chart&time=1751..2016


"""
The chart attached shows the median temperature rise from the year 1985. The dashed blue line represent the median average temperature change across the globe, and grey lines represent the upper and lower 95% confidence intervals. The region between the upper and lower 95% confidence intervals are shaded to provide better clarity to the image. The red dotted lines shows the human carbon dioxide emission for the same duration.
There has been a steady increase in the carbon dioxide emissions. So as postulated by scientists all over the world, the increase in global temperature could indeed have been due to the increase in carbon dioxide emissions.

Cairo’s principles of charting applied!
"""
# In[1]:

import pandas as pd


# In[2]:
#Read Data
temp_dat=pd.read_csv(r'Assn Data/temperature-anomaly.csv')
temp_dat=temp_dat[(temp_dat.Year>1984) & (temp_dat.Entity=='Global')]
temp_dat.tail(2)


# In[3]:
#Read Data
emission_dat=pd.read_csv('Assn Data/cumulative-co-emissions.csv')
emission_dat=emission_dat[emission_dat.Year>1984]
emission_dat=emission_dat.groupby(['Year'])['Cumulative CO₂ emissions by nation (tonnes)'].sum()/10**11
emission_dat.tail(2)


# In[4]:
#Import libraries
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib notebook')


# In[5]:
#Create figure object
fig, ax1 = plt.subplots()


# In[6]:

p1=ax1.plot(temp_dat['Year'],temp_dat['Upper (℃)'], '-',alpha=0.5,color='gray', label='Upper Anomaly')
p2=ax1.plot(temp_dat['Year'],temp_dat['Median (℃)'], '--',color='b', label='Median Anomaly')
p3=ax1.plot(temp_dat['Year'],temp_dat['Lower (℃)'], '-',alpha=0.5,color='gray', label='Lower Anomaly')
ax1.set_xlabel('Calendar Year',fontweight='bold')


# In[7]:

_=plt.gca().fill_between(temp_dat['Year'],temp_dat['Lower (℃)'],temp_dat['Upper (℃)'],facecolor='gray',alpha=0.3)


# In[8]:

# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('Temperature anomaly, (Global)', color='b',fontweight='bold')
ax1.tick_params('y', colors='b')


# In[9]:

ax2 = ax1.twinx()
p4=ax2.plot(emission_dat.index, emission_dat.values, 'r.',color='r', label='CO₂ emission')
ax2.set_ylabel('Global CO₂ emission 10$^{11}$ tonnes', color='r',fontweight='bold')
ax2.tick_params('y', colors='r')


# In[10]:

box = ax1.get_position()
ax1.set_position([box.x0, box.y0, box.width * 1, box.height])
ax2.set_position([box.x0, box.y0, box.width * 1, box.height])


# In[11]:

from matplotlib.font_manager import FontProperties
fontP = FontProperties()
fontP.set_size('small')


# In[12]:

plots = p1+p2+p3+p4
labs = [p.get_label() for p in plots]
_=ax1.legend(plots, labs,loc='2',title="$\\bf{Legend}$", frameon=False,prop={'size':8})


# In[13]:

_=plt.title('Global CO₂ emission v/s temerature rise',fontweight='bold')


# In[14]:

_=ax1.tick_params(left='off', bottom='off',right='off', labelbottom='on')
_=ax2.tick_params(left='off', bottom='off',right='off', labelbottom='on')


# In[ ]:



