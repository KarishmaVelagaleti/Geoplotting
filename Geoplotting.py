
# coding: utf-8

# ## GEO PLOTTING

# In[1]:


import plotly as py


# In[2]:


from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot


# In[5]:


init_notebook_mode(connected=True)


# In[12]:


data = dict(type='choropleth', locations=['AZ', 'CA', 'NY'], locationmode='USA-states', colorscale='Portland', text=['Arizona', 'California', 'New York'], z=[1.0, 2.0, 3.0], colorbar = {'title':'Colorbar Title Goes Here'})


# In[13]:


data


# In[14]:


layout = dict(geo={'scope':'usa'})


# In[15]:


import plotly.graph_objs as go


# In[16]:


choromap = go.Figure(data= [data],layout=layout)


# In[17]:


iplot(choromap)


# In[19]:


import pandas as pd 
import numpy as np
df= pd.read_csv('2011_US_AGRI_Exports')


# In[20]:


df.head()


# In[33]:


data= dict(type='choropleth',
          colorscale='Portland', 
          locations = df['code'], 
          locationmode='USA-states',
          z= df['total exports'],
          text= df['text'],
           marker = dict(line= dict(color= 'rgb(255,255,255)', width=2)),
          colorbar = {'title': 'Millions USD'})


# In[22]:


layout=dict(title = '2011 US Agriculture Exports by State', 
           geo = dict(scope='usa', showlakes=True, lakecolor='rgb(85,173,240)'))


# In[23]:


layout


# In[34]:


choromap2 = go.Figure(data=[data], layout=layout)


# In[28]:


iplot(choromap2)


# ### World Plots

# In[2]:


import plotly as py


# In[5]:


from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot


# In[6]:


init_notebook_mode(connected=True)


# In[13]:


import plotly.graph_objs as go


# In[8]:


import pandas as pd
import numpy as np
df = pd.read_csv('2014_World_GDP')


# In[9]:


df.head()


# In[10]:


data = dict(type = 'choropleth',
           locations = df['CODE'],
           z = df['GDP (BILLIONS)'],
           colorbar = {'title': 'GDP in Billions USD'})


# In[17]:


layout = dict(title = '2014 Global GDP', 
             geo = dict(showframe=False,
                       projection= {'type':'mercator'}))


# In[18]:


choromap3 = go.Figure(data=[data], layout = layout)


# In[19]:


iplot(choromap3)


# In[20]:


layout = dict(title = '2014 Global GDP', 
             geo = dict(showframe=False,
                       projection= {'type':'natural earth'}))


# In[21]:


choromap3 = go.Figure(data=[data], layout = layout)
iplot(choromap3)

