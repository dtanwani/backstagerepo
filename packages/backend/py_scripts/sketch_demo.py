#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system(' pip install sketch')
get_ipython().system(' pip install lambdaprompt')


# In[1]:


import sketch
import pandas as pd


# In[2]:


sales_data = pd.read_csv("https://gist.githubusercontent.com/bluecoconut/9ce2135aafb5c6ab2dc1d60ac595646e/raw/c93c3500a1f7fae469cba716f09358cfddea6343/sales_demo_with_pii_and_all_states.csv")


# In[3]:


sales_data.sketch.howto("Create some friendly names for each column? (output as an HTML list)")


# In[6]:


sales_data.sketch.ask("Can you give me descriptions for each column?(output as an HTML list)")


# In[7]:


sales_data.sketch.ask("What columns might have PII information in them?")


# In[9]:


sales_data.sketch.ask("Can you tell if there is any PII information for each column in form of flag Yes/No (output as an HTML list)?")


# In[10]:


sales_data.sketch.ask("Can you tell if there is any PII information for each column in form of flag Yes/No (output as JSON)?")


# In[5]:


sales_data.sketch.ask("Can you give me friendly names for each column? (output as an HTML list)")


# In[11]:


sales_data.sketch.ask("Can you give me friendly names for each column? (output as JSON)")


# In[14]:


sales_data.sketch.ask("Can you give me friendly names, Business descriptions, and flag (Yes/No) tell if there is any PII information for each column? (output as JSON)")


# In[6]:


sales_data.sketch.howto("Create some derived features from the address")


# In[7]:



# Create a new column for the city
sales_data['City'] = sales_data['Purchase Address'].apply(lambda x: x.split(',')[1])

# Create a new column for the state
sales_data['State'] = sales_data['Purchase Address'].apply(lambda x: x.split(',')[2].split(' ')[1])

# Create a new column for the zipcode
sales_data['Zipcode'] = sales_data['Purchase Address'].apply(lambda x: x.split(',')[2].split(' ')[2])


# In[8]:


sales_data.sketch.howto("Get the top 5 grossing states")


# In[9]:



# Get the top 5 grossing states

# Calculate total sales per state
state_sales = sales_data.groupby('State')['Price Each'].sum().reset_index()

# Sort the dataframe by total sales in descending order
state_sales = state_sales.sort_values(by='Price Each', ascending=False)

# Get the top 5 grossing states
top_5_states = state_sales.head(5)

# Print the results
print(top_5_states)


# In[ ]:




