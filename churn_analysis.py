import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('data/telecom_churn.csv')
print('Total Customers:',len(df))
print('Churn Rate:',round((df['Churn']=='Yes').mean()*100,2),'%')

region=df.groupby('Contract')['CustomerID'].count()
region.plot(kind='bar',title='Customers by Contract')
plt.tight_layout()
plt.savefig('images/contract_distribution.png')
