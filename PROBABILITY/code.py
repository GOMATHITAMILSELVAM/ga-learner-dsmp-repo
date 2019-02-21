# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# code starts here
df=pd.read_csv(path)
df_fico=df[df['fico']>700]
p_a=len(df_fico)/len(df)
print(f"PROB THAT FICO CREDIT SCORE IS GREATER THAN 700 IS {p_a}")
df_purpose=df[df['purpose']=='debt_consolidation']
p_b=len(df_purpose)/len(df)
print(f"PROB THAT THE PURPOSE IS DEBT CONSOLIDATION IS {p_b}")
df1=df[df['purpose']=='debt_consolidation']
#df1_fico=df1[df1['fico']>700]
#p_fico=len(df1_fico)/len(df1)
p_a_b=p_b/p_a
print(f"PROB THAT THE PURPOSE IS DEBT CONSOL PROVIDED THE FICO IS GREATER THAN 700 IS {p_a_b}")
p=p_a/p_b
result=(p==p_a)
print(result)
# code ends here


# --------------
# code starts here
df_lp=df[df['paid.back.loan'] == 'Yes']
prob_lp=len(df_lp)/len(df)
#print(prob_lp)
prob_cs=len(df[df['credit.policy'] == 'Yes'])/len(df)
#print(prob_cs)
new_df=df[df['paid.back.loan']=='Yes']
prob_pd_cs=new_df[new_df['credit.policy']=='Yes'].shape[0]/new_df.shape[0]
bayes=(prob_pd_cs*prob_lp)/(prob_cs)
#print(f"using bayes theorem prob is {bayes}")
# code ends here


# --------------
# code starts here
df1=df[df['paid.back.loan']=='No']
#print(df1.head())
Height=df1['purpose'].value_counts()
print(Height)
plt.bar(Height.index,height=Height.values)

# code ends here


# --------------
# code starts here
inst_median=df['installment'].median()
inst_mean=df['installment'].mean()
plt.hist(df['installment'],bins=300)
plt.hist(df['log.annual.inc'],bins=300)
plt.show()
# code ends here


