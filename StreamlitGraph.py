#!/usr/bin/env python
# coding: utf-8

# In[139]:


import streamlit as st
import numpy as np
import pandas as pd
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt


# In[143]:


df = pd.read_excel('mothersh.xlsx', sheet_name='Sheet1')


# In[141]:


df.dropna(axis= 1, inplace = True)

print(df.head(4))


# In[142]:


df['Date']= pd.to_datetime(df['Date'])
df_subset = pd.get_dummies(df[['Date','Intensity','Frequency','Duration']],drop_first = True)
df_subset['Date']= pd.to_datetime(df_subset['Date'])
df_subset.set_index('Date', inplace=True)
#df_subset.head(5)
behavior_rolling_sum = df_subset.groupby(pd.Grouper(freq='W')).sum()

print(behavior_rolling_sum.head(9))


# In[124]:


# Multiselect widget for selecting behaviors
selected_behaviors_p = st.multiselect('Select Behaviors for pyplot:', options=behavior_rolling_sum.columns)

# Plot all selected behaviors in the same graph
if selected_behaviors_p:
    plt.figure(figsize=(10, 6))
    for behavior in selected_behaviors_p:
        plt.plot(behavior_rolling_sum.index, behavior_rolling_sum[behavior], label=behavior)

    plt.xlabel('Date')
    plt.ylabel('Occurrences')
    plt.xticks(range(len(behavior_rolling_sum.index)),rotation=45)
    plt.legend()
    st.pyplot()
else:
    st.write('Please select at least one behavior.')


# In[138]:


# Multiselect widget for selecting behaviors
selected_behaviors_b = st.multiselect('Select Behaviors Bar Chart :', options=behavior_rolling_sum.columns)

# Display bar chart for selected behaviors
if selected_behaviors_b:
    st.write('Bar Chart for Selected Behaviors:')
    
    selected_data = behavior_rolling_sum[selected_behaviors_b]  # Select only the columns for selected behaviors
    print(selected_data)   
    
    plt.xticks(range(len(selected_data.index)), selected_data.index.strftime('%Y-%m-%d'), rotation=45)
    
    st.bar_chart(selected_data)

else:
    st.write('Please select at least one behavior.')


# In[112]:


# Group by behavior and calculate rolling weekly sum
# Plot rolling weekly sum for each behavior
#for col in behavior_groups.columns:
#    st.subheader(f'Behavior: {col}')
#    st.line_chart(behavior_groups[col], use_container_width=True)
    
selected_behaviors_line = st.multiselect('Select Behaviors Line:', options=behavior_rolling_sum.columns)

# Display bar chart for selected behaviors
if selected_behaviors_line:
    st.write('Line Chart for Selected Behaviors:')
    st.line_chart(behavior_rolling_sum[selected_behaviors_line])
    
    plt.xticks(range(len(selected_data.index)), selected_data.index.strftime('%Y-%m-%d'), rotation=45)
    
else:
    st.write('Please select at least one behavior.')
    


# In[130]:


import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Assuming behavior_rolling_sum is your DataFrame and selected_behaviors_line is your list of selected behaviors
selected_behaviors_line = st.multiselect('Select Behaviors Scatter plot:', options=behavior_rolling_sum.columns)

# Display scatter plot for selected behaviors
if selected_behaviors_line:
    fig,ax = plt.subplots(figsize=(10, 6))
    for behavior in selected_behaviors_line:
        ax.scatter(behavior_rolling_sum.index, behavior_rolling_sum[behavior], label=behavior)

    ax.set_xlabel('Date')
    ax.set_ylabel('Occurrences')
    ax.set_title('Scatter Plot for Selected Behaviors')
    ax.tick_params(axis='x',rotation=45)
    ax.legend()
    st.pyplot(fig)
else:
    st.write('Please select at least one behavior.')


# In[ ]:




