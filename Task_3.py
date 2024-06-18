#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt

file_path = 'householdtask3.csv'
df = pd.read_csv(file_path)

print(df.head())

plt.figure(figsize=(12, 6))
plt.bar(df['year'], df['tot_hhs'], color='blue', label='Total Households')
plt.bar(df['year'], df['own'], color='green', label='Owned Households', alpha=0.7)
plt.title('Total Households and Owned Households Over Years')
plt.xlabel('Year')
plt.ylabel('Number of Households')
plt.legend()
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(df['year'], df['income'], marker='o', color='blue', label='Income')
plt.plot(df['year'], df['expenditure'], marker='o', color='red', label='Expenditure')
plt.title('Average Income and Expenditure Over Years')
plt.xlabel('Year')
plt.ylabel('Amount ($)')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:




