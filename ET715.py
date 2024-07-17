#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import numpy as np 
import pandas as pd 
import time

import shap
import joblib

from sklearn.ensemble import ExtraTreesRegressor
from sklearn.preprocessing import StandardScaler

# In[2]:





# In[3]:





# In[4]:




# In[5]:


st.markdown("<h1 style='text-align: center; color: black;'>围术期心脏移植受者他克莫司日剂量预测</h1>", unsafe_allow_html=True)


# In[ ]:


# side-bar 
def user_input_features():
    st.sidebar.header('参数选择面板')
    st.sidebar.write('输入参数如下 ⬇️')
    a1 = st.sidebar.selectbox("CYP3A5(rs776746_3)", ('TT/TC','CC'))
    a2 = st.sidebar.number_input("上一次的日剂量/past_1")
    a3 = st.sidebar.number_input("上一次TDM浓度/dv")
    a4 = st.sidebar.number_input("他克莫司服用时间/time")   
    a5 =  st.sidebar.selectbox("是否服用伏立康唑/VOR", ('是/YES', '否/NO'))  
    a6 = st.sidebar.number_input("体重/weight（kg）")
    a7 = st.sidebar.number_input("每搏输出量/SV")
    a8 = st.sidebar.number_input("身高/height（cm）")


    
    output = [a1,a2,a3,a4,a5,a6,a7,a8]
    return output

outputdf = user_input_features()


# In[ ]:


# If button is pressed
if st.button("提交/Submit"):
    
    # Unpickle classifier
    et= joblib.load("et715.pkl")
    
    # Store inputs into dataframe
    X0 = pd.DataFrame([outputdf], columns= ["rs776746_3","past_1","dv","time","FLKZ","weight","SV","height"])
    X0 = X0.replace(["是/YES", "否/NO"], [1, 0])
    X0 = X0.replace(["TT/TC","CC"], [0,1])
    
    
    
    
    

   
    p1=et.predict(X0)
    st.write(f'预测结果为: {p1}mg/day')
    
    

