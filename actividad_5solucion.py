#!/usr/bin/env python
# coding: utf-8

# # Welcome to Jupyter!

# In[1]:


#Este es el script para la actividad 5


# In[2]:


# Importo las bibliotecas necesarias
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats as st


# In[3]:


# Leo los datos del archivo csv que está en linea
url = 'https://raw.githubusercontent.com/ohjerez/zoom/main/Museos_vs_EdadVisitantes_enteros.csv'
data = pd.read_csv(url)
print(data)


# In[4]:


edadDeLosVisitantes = data["EdadVisitantes"]


# In[5]:


#Hago un print de la Variable
print("Print de la edad de los visitantes:")
print(edadDeLosVisitantes)


# In[6]:


# para cada visitante imprimo su edad.
# si la edad es mayor de 40 imprime "You rock!"


# In[7]:


for edad in edadDeLosVisitantes:
    if edad > 40:
        print("Edad : ", edad)
        print("You rock!")


# In[8]:


# 1. Modifica el script anterior para indicar si el visitante tiene menos de 21 años.


# In[9]:


for edad in edadDeLosVisitantes:
    if edad < 21:
        print("Edad : ", edad)
        print("Menos de 21 años")


# In[10]:


# 2. Modifica el programa anterior para encontrar franja de edad entre 17 y 25 años.


# In[11]:


for edad in edadDeLosVisitantes:
    if 17<edad < 25:
        print("Edad : ", edad)
        print("Se encuentra entre 17 y 25 años")


# In[12]:


print("Programa terminado")


# In[ ]:





# This repo contains an introduction to [Jupyter](https://jupyter.org) and [IPython](https://ipython.org).
# 
# Outline of some basics:
# 
# * [Notebook Basics](../examples/Notebook/Notebook%20Basics.ipynb)
# * [IPython - beyond plain python](../examples/IPython%20Kernel/Beyond%20Plain%20Python.ipynb)
# * [Markdown Cells](../examples/Notebook/Working%20With%20Markdown%20Cells.ipynb)
# * [Rich Display System](../examples/IPython%20Kernel/Rich%20Output.ipynb)
# * [Custom Display logic](../examples/IPython%20Kernel/Custom%20Display%20Logic.ipynb)
# * [Running a Secure Public Notebook Server](../examples/Notebook/Running%20the%20Notebook%20Server.ipynb#Securing-the-notebook-server)
# * [How Jupyter works](../examples/Notebook/Multiple%20Languages%2C%20Frontends.ipynb) to run code in different languages.

# You can also get this tutorial and run it on your laptop:
# 
#     git clone https://github.com/ipython/ipython-in-depth
# 
# Install IPython and Jupyter:
# 
# with [conda](https://www.anaconda.com/download):
# 
#     conda install ipython jupyter
# 
# with pip:
# 
#     # first, always upgrade pip!
#     pip install --upgrade pip
#     pip install --upgrade ipython jupyter
# 
# Start the notebook in the tutorial directory:
# 
#     cd ipython-in-depth
#     jupyter notebook
