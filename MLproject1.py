#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
iris=pd.read_csv("convert.csv")
iris.head(150)


# In[2]:


iris.sample(10)


# In[3]:


iris.iloc[:,0:4].apply(np.mean)


# In[4]:


iris.apply(np.min)


# In[5]:


iris.apply(np.max)


# In[6]:


iris.iloc[:,0:4].apply(np.std)


# In[7]:


class_correlation = {
    "Iris-setosa - Iris-versicolor" : iris[iris["species"].isin(["Iris-setosa", "Iris-versicolor"])][["sepal.Length", "petal.Length"]].corr().iloc[0,1],
    "Iris-versicolor - Iris-virginica" : iris[iris["species"].isin(["Iris-versicolor", "Iris-virginica"])][["sepal.Length", "petal.Length"]].corr().iloc[0,1],
    "Iris-virginica - Iris-setosa" : iris[iris["species"].isin(["Iris-virgina", "Iris-virginica"])][["sepal.Length", "petal.Length"]].corr().iloc[0,1]
}

print("Class Correlations:")
for correlation, value in class_correlation.items():
    print(f"{correlation}:{value}")


# In[ ]:




