# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#path of the data file- path
data=pd.read_csv(path)
data['Gender'].replace('-','Agender',inplace=True)
#print(data.head())
gender_count=data['Gender'].value_counts()
print(gender_count)
#print(type(gender_count))
x=gender_count.index
y=gender_count[0:]
#print(y)
plt.bar(x,y)
plt.show()
#Code starts here 




# --------------
#Code starts here
alignment=data['Alignment'].value_counts()
print(alignment)
plt.title('Character Alignment')

plt.pie(alignment,labels=['good','bad','neutral'])
plt.show()


# --------------
#Code starts here
sc_df=data.iloc[:,[5,9]]
#print(sc_df.head(2))
sc_covar=sc_df.cov()
sc_covariance=617.49
#print(sc_covarinace)
sc_strength=sc_df['Strength'].std()
sc_combat=sc_df['Combat'].std()
sc_pearson=sc_covariance/(sc_strength*sc_combat)
print(sc_pearson)
ic_df=data.iloc[:,[4,9]]
ic_covar=ic_df.cov()
ic_covariance=853.42
print(ic_covariance)
ic_intelligence=ic_df['Intelligence'].std()
ic_combat=ic_df['Combat'].std()
ic_pearson=ic_covariance/(ic_intelligence*ic_combat)



# --------------
#Code starts here
total_high=data['Total'].quantile(0.99)
print(f"the 99pct of total is{total_high}")
super_best=data[data['Total'] > total_high]
print(super_best.head(1))
super_best_names=super_best['Name'].tolist()
print(f"The top superheroes/villains are{super_best_names}")


# --------------
#Code starts here
fig,(ax_1,ax_2,ax_3)=plt.subplots(1,3,figsize=(20,10))
ax_1.boxplot(data['Intelligence'])
ax_2.boxplot(data['Speed'])
ax_3.boxplot(data['Power'])
plt.show()


