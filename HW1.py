#HW1
from numpy import *

!pip install brewer2mpl

%matplotlib inline
from urllib import urlopen

import brewer2mpl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('bank-data.csv',sep=',', error_bad_lines=False)
df.head()

print "AGE Stat"
print "min: ", min(df['age'])
print "median: ", df['age'].median()
print "max: ", max(df['age'])
print "avg: ", df['age'].mean()
print "mode: ", df['age'].mode()
print "std: ", df['age'].std()
print " "
print "INCOME Stat"
print "min: ", min(df['income'])
print "median: ", df['income'].median()
print "max: ", max(df['income'])
print "avg: ", df['income'].mean()
print "mode: ", df['income'].mode()
print "std: ", df['income'].std()
print " "
print "CHILDREN Stat"
print "min: ", min(df['children'])
print "median: ", df['children'].median()
print "max: ", max(df['children'])
print "avg: ", df['children'].mean()
print "mode: ", df['children'].mode()
print "std: ", df['children'].std()
print " "

print "SEX distribution"
sex_groupby = df.groupby('sex')
for key, value in sex_groupby:
    print key, ",", len(value)
    v=value
print " "
print "REGION distribution"
region_groupby = df.groupby('region')
for key, value in region_groupby:
    print key, ",", len(value)
    v=value
print " "
print "MARRIED distribution"
married_groupby = df.groupby('married')
for key, value in married_groupby:
    print key, ",", len(value)
    v=value
print " "
print "CAR distribution"
car_groupby = df.groupby('car')
for key, value in car_groupby:
    print key, ",", len(value)
    v=value
print " "
print "SAVING ACCT distribution"
saveaccount_groupby = df.groupby('save_act')
for key, value in saveaccount_groupby:
    print key, ",", len(value)
    v=value
print " "
print "CURRENT ACCT distribution"
currentacct_groupby = df.groupby('current_act')
for key, value in currentacct_groupby:
    print key, ",", len(value)
    v=value
print " "
print "MORTGAGE distribution"
mortgage_groupby = df.groupby('mortgage')
for key, value in mortgage_groupby:
    print key, ",", len(value)
    v=value
print " "
print "PEP distribution"
pep_groupby = df.groupby('pep')
for key, value in pep_groupby:
    print key, ",", len(value)
    v=value
print " "

#2
pep_df = pep_groupby['age','income','children'].describe()
print type(pep_df)
pep_df.head(20)
#People who buy PEP have higher income on average, and they also have less kids in comparison to people who don't buy PEP

#3
Young=0
Mid_age=0
Old=0

for x in df['age']:
    if x<30:
        Young+=1
    elif x>=30 and x<60:
        Mid_age+=1
    elif x>=60:
        Old+=1

print("# of Young people (less than 30): ", Young)
print("# of Mid_age people (between 30 and 60): ", Mid_age)
print("# of Old people (60 and older): ", Old)

#4
N=500
x=df['age']
y=df['income']
colors=(0,0,0)
area=np.pi*3

plt.scatter(x,y,s=area,c=colors,alpha=0.5)
plt.title('Income and Age Correlation')
plt.xlabel("age")
plt.ylabel("income")
plt.show()

#age and income has a positive correlations; as age increases, income increases

#5
x=df['age']
num_bins=15
n,bins,patches=plt.hist(x,num_bins,facecolor='blue',alpha=0.5)
plt.title('Age Histogram')
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

x=df['income']
num_bins=9
n,bins,patches=plt.hist(x,num_bins,facecolor='blue',alpha=0.5)
plt.title('Income Histograma')
plt.xlabel("Income")
plt.ylabel("Frequency")
plt.show()
