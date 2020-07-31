import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
sns.set()

#Reading the dataset from command line
path = str(sys.argv[1])
df = pd.read_csv(path)

#Pre-processing the dataset
df = df.drop(['Email Address', 'Last Name', 'First Name', 'State', 'Course Type', 'Current Employment Status', 'Zip Code', 'Contact Number', 'Emergency Contact Number'], axis=1)
df = df.dropna(axis=1)

pp = PdfPages('visualization-output.pdf')


#Bar plot for question 2(a)
sns.set_style("darkgrid")
plt.figure(figsize=(16,8))
plt.xticks(rotation=75, fontweight='bold')
plt.xlabel('', fontsize=13, fontweight='bold')
plt.ylabel('', fontsize=13, fontweight='bold')
plt.title('Number of Students Applied to Different Technologies', fontsize=15, fontweight='bold')
sns.countplot(df['Areas of interest'])
pp.savefig()


#Pie plot for question 2(b)
ds = df[df['Areas of interest']=='Data Science ']
know_python = ds['Programming Language Known other than Java (one major)']=='Python'
other = ds['Programming Language Known other than Java (one major)']!='Python'
categories = know_python.sum(), other.sum()
lab = 'Know Python', 'Do not know Python'

plt.figure(figsize=(12,6))
plt.pie([x for x in categories], labels=lab, colors=['Lightgreen', 'Orange'], startangle=30, autopct='%.2f%%', explode=[0,0.1]) 
plt.title('Students Who Applied for Data Science', fontsize=15, fontweight='bold')
pp.savefig()


#Bar plot for question 2(c)
sns.set_style('whitegrid')
plt.figure(figsize=(16,8))
plt.xticks(rotation=60, fontweight='bold')
plt.xlabel('', fontsize=13, fontweight='bold')
plt.ylabel('', fontsize=13, fontweight='bold')
plt.title('Different Ways Students Learned About This Program', fontsize=15, fontweight='bold')
sns.countplot(df['How Did You Hear About This Internship?'])
pp.savefig()


#Bar plot for question 2(d)
df.rename(columns = {'CGPA/ percentage':'CGPA'}, inplace = True)
df.rename(columns = {'Which-year are you studying in?':'Year'}, inplace = True)

yc = df[['Year','CGPA']]
cgpa = yc.groupby(['Year'])
fy = cgpa.get_group('Fourth-year')
fourthyear = fourthyear.reset_index(drop=True)
x = []
x = fourthyear['CGPA']
greaterthan = []
for i in range(0,len(fourthyear)):
    if x[i] > 8.0:
        greaterthan.append('Have CGPA Greater than 8')
    elif x[i] < 8.0 :
        greaterthan.append('Do NOT Have CGPA Greater than 8')

sns.set_style('whitegrid')
plt.figure(figsize=(12,6))
plt.title('Students who are in the fourth year and have a CGPA greater than 8', fontsize=15, fontweight='bold')
sns.countplot(greaterthan)
pp.savefig()


#Bar plot for question 2(e)
df.rename(columns = {'Rate your written communication skills [1-10]':'Written'}, inplace = True)
df.rename(columns = {'Rate your verbal communication skills [1-10]':'Verbal'}, inplace = True)

dvw = df[['Areas of interest','Verbal','Written']]
grpdvw = dvw.groupby(['Areas of interest'])
dm = grpdvw.get_group('Digital Marketing ')
dma = dm.reset_index(drop=True)

y=dma['Verbal'].tolist()
z=dma['Written'].tolist()
grt=[]
for i in range(0,624):
    if y[i] > 8:
        if z[i]>8:
            grt.append('Have Written and Verbal Communication Skills Greater than 8')
        elif z[i]==8:
            grt.append('Others')
        else :
            grt.append('Others')
    elif y[i]==8:
        grt.append('Others')           
    else:
        grt.append('Others')      

sns.set_style('whitegrid')
plt.figure(figsize=(12,6))
plt.title('Students who are in the fourth year and have a CGPA greater than 8', fontsize=15, fontweight='bold')
sns.countplot(grt)
pp.savefig()


#Bar plots for question 2(f)
f, axes = plt.subplots(1, 2, figsize=(16, 5))
sns.countplot(df['Year'].sort_values(), ax=axes[0])
f2 = sns.countplot(df['Major/Area of Study'], ax=axes[1])
f2.set_xticklabels(labels=df['Major/Area of Study'].unique(), rotation=-10)
pp.savefig()


#Bar plots for question 2(g)
f, axes = plt.subplots(1, 2, figsize=(16, 5))
sns.countplot(df['City'], ax=axes[0])
g2 = sns.countplot(df['College name'], ax=axes[1])
g2.set_xticklabels(labels=df['College name'].unique(), rotation=-90)
pp.savefig()


#Bar plot for question 2(i)
sns.set_style("whitegrid")
plt.figure(figsize=(18,9))
plt.xticks(rotation=80, fontweight='bold')
plt.xlabel('', fontsize=13, fontweight='bold')
plt.ylabel('', fontsize=13, fontweight='bold')
plt.title('Relationship Between the Area of Interest and the Target Variable', fontsize=15, fontweight='bold')
sns.countplot(x="Areas of interest", hue='Label', data=df)
pp.savefig()


#Grouped Bar plot for question 2(j)
fe = df[(df['Year'] == 'First-year') & (df['Major/Area of Study'] == 'Electrical Engineering')].count().unique()
se = df[(df['Year'] == 'Second-year') & (df['Major/Area of Study'] == 'Electrical Engineering')].count().unique()
te = df[(df['Year'] == 'Third-year') & (df['Major/Area of Study'] == 'Electrical Engineering')].count().unique()
fie = df[(df['Year'] == 'Fourth-year') & (df['Major/Area of Study'] == 'Electrical Engineering')].count().unique()

fec = df[(df['Year'] == 'First-year') & (df['Major/Area of Study'] == 'Electronics and Telecommunication')].count().unique()
sec = df[(df['Year'] == 'Second-year') & (df['Major/Area of Study'] == 'Electronics and Telecommunication')].count().unique()
tec = df[(df['Year'] == 'Third-year') & (df['Major/Area of Study'] == 'Electronics and Telecommunication')].count().unique()
fiec = df[(df['Year'] == 'Fourth-year') & (df['Major/Area of Study'] == 'Electronics and Telecommunication')].count().unique()

fc = df[(df['Year'] == 'First-year') & (df['Major/Area of Study'] == 'Computer Engineering')].count().unique()
sc = df[(df['Year'] == 'Second-year') & (df['Major/Area of Study'] == 'Computer Engineering')].count().unique()
tc = df[(df['Year'] == 'Third-year') & (df['Major/Area of Study'] == 'Computer Engineering')].count().unique()
fic = df[(df['Year'] == 'Fourth-year') & (df['Major/Area of Study'] == 'Computer Engineering')].count().unique()

print(fe, se, te, fie, fec, sec, tec, fiec, fc, sc, tc, fic)

ce = [1470, 1536, 1449, 1516]
ee = [490, 518, 561, 464]
ece = [550, 496, 453, 497]
el_ce = [0, 274, 302, 259]
el_ee = [0, 273, 246, 275]
el_ece = [0, 818, 801, 815]
major=ce,ee,ece
barWidth = 0.1
r1 = np.arange(len(ce))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]
r6 = [x + barWidth for x in r5]

sns.set_style("whitegrid")
plt.figure(figsize=(18,9))
plt.xticks([r + barWidth for r in range(len(ce))], ['First-Year', 'Second-Year', 'Third-Year', 'Fourth-Year'], fontweight='bold')
plt.xlabel('Year of Study', fontsize=13, fontweight='bold')
plt.ylabel('Number of Students', fontsize=13, fontweight='bold')
plt.title('Relationship Between the Year of Study, Major and the Target Variable', fontsize=15, fontweight='bold')
plt.bar(r1, ce, color='crimson', width=barWidth, label = 'Computer Engineering')
plt.bar(r2, ee, color='blue', width=barWidth, label = 'Electrical Engineering')
plt.bar(r3, ece, color='green', width=barWidth, label = 'Electronics and Telecommunication')
plt.bar(r4, el_ce, color='red', width=barWidth, label = 'Eligibility for CE')
plt.bar(r5, el_ee, color='skyblue', width=barWidth, label = 'Eligibility for EE')
plt.bar(r6, el_ece, color='lightgreen', width=barWidth, label = 'Eligibility for ETC')
plt.legend()
pp.savefig()


#Stem plot for question 2(h)
Label_dict = { 'eligible' : 1, 'ineligible' : -1}
df['Label_Encoded'] = df.Label.map(Label_dict)
plt.figure(figsize=(16,8))
plt.xticks(fontweight='bold')
plt.xlabel('CGPA', fontsize=13, fontweight='bold')
plt.ylabel('Inligible, Eligible', fontsize=13, fontweight='bold')
plt.title('Relationship Between the CGPA and the Target Variable', fontsize=15, fontweight='bold')
h = plt.stem(df['CGPA'], df['Label_Encoded'], markerfmt='g_', linefmt='r--', basefmt='b', use_line_collection=True)
pp.savefig()
pp.close()

