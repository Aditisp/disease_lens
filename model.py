# -*- coding: utf-8 -*-
"""Minor Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jfYFgAsx0Ckpq96aJNv04YnK09HPWMuR
"""

import numpy as np 
import pandas as pd 
import category_encoders as ce
import pickle
from matplotlib import pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

def disease_pred(input1):
  df1 = pd.DataFrame(pd.read_excel("D:\Sem 6\PBL\Mini project sem 6\material\dataset.xlsx"))
  df1.to_csv ("survey.csv", 
                  index = None,
                  header=True)
  df = pd.DataFrame(pd.read_csv("survey.csv"))
  pd.set_option('display.max_columns', None)
  df.head()
  encoder= ce.OrdinalEncoder(cols=['BMI Categories'],return_df=True,
                           mapping=[{'col':'BMI Categories',
  'mapping':{'Underweight':0,'Normalweight':1,'Overweight':2,'Obesity':3}}])
  df['BMI Categories'] =encoder.fit_transform(df['BMI Categories'])
  for idx, val in enumerate(df['BMI Categories']):
  #  print(idx, val)
    if val==-1.0:
      df['BMI Categories'][idx]= 1
  df['BMI Categories']
  encoder= ce.OrdinalEncoder(cols=['Gender'],return_df=True,
                           mapping=[{'col':'Gender',
  'mapping':{'Male':0,'Female':1}}])
  df['Gender'] =encoder.fit_transform(df['Gender'])
  # df['Gender']
  encoder= ce.OrdinalEncoder(cols=['At what time do you wake up?'],return_df=True,
                           mapping=[{'col':'At what time do you wake up?',
  'mapping':{'4 AM to 6 AM':0,'6 AM to 7 AM':1,'7 AM to 9 AM':2,'After 9 AM':3}}])
  df['At what time do you wake up?'] = encoder.fit_transform(df['At what time do you wake up?'])
  encoder= ce.OrdinalEncoder(cols=['Do you always have breakfast ?'],return_df=True,
                           mapping=[{'col':'Do you always have breakfast ?',
  'mapping':{'No':0,'Sometimes':1,'Yes':2}}])
  df['Do you always have breakfast ?'] = encoder.fit_transform(df['Do you always have breakfast ?'])
  encoder= ce.OrdinalEncoder(cols=['What do you usually have in breakfast ?'],return_df=True,
                           mapping=[{'col':'What do you usually have in breakfast ?',
  'mapping':{'Fast Food or Outdoor food':0,'Mix of both above mentioned options':1,'Home-made (fruits included )':2}}])
  df['What do you usually have in breakfast ?'] = encoder.fit_transform(df['What do you usually have in breakfast ?'])
  encoder= ce.OrdinalEncoder(cols=['How many times in a week do you eat outside ?'],return_df=True,
                           mapping=[{'col':'How many times in a week do you eat outside ?',
  'mapping':{'Everyday':0,'3-5 days':1,'1-2 days':2,'Once a month':3}}])
  df['How many times in a week do you eat outside ?'] = encoder.fit_transform(df['How many times in a week do you eat outside ?'])
  encoder= ce.OrdinalEncoder(cols=['Do you maintain your lunch and dinner time ?'],return_df=True,
                           mapping=[{'col':'Do you maintain your lunch and dinner time ?',
  'mapping':{'Yes':0,'No':1,'1-2 days':2}}])
  df['Do you maintain your lunch and dinner time ?'] = encoder.fit_transform(df['Do you maintain your lunch and dinner time ?'])
  encoder= ce.OrdinalEncoder(cols=['How much time do you travel in a day?'],return_df=True,
                           mapping=[{'col':'How much time do you travel in a day?',
  'mapping':{'Less than 1 hr':0,'1-2 hrs':1,'3-5 hrs':2,'More than 5 hrs':3}}])
  df['How much time do you travel in a day?'] = encoder.fit_transform(df['How much time do you travel in a day?'])
  encoder= ce.OrdinalEncoder(cols=['How many hours do you sleep ?'],return_df=True,
                           mapping=[{'col':'How many hours do you sleep ?',
  'mapping':{'less than 6':0,'6-7 hrs':1,'7-9 hrs':2,'More than 9 hrs':3}}])
  df['How many hours do you sleep ?'] = encoder.fit_transform(df['How many hours do you sleep ?'])
  encoder= ce.OrdinalEncoder(cols=['Average working hours ?'],return_df=True,
                           mapping=[{'col':'Average working hours ?',
  'mapping':{'5-7':0,'7-10':1,'More than 10':2}}])
  df['Average working hours ?'] = encoder.fit_transform(df['Average working hours ?'])
  for idx, val in enumerate(df['Average working hours ?']):
  #  print(idx, val)
    if val==-1.0:
      df['Average working hours ?'][idx]=1
  encoder= ce.OrdinalEncoder(cols=['Do you consume Alcohol?'],return_df=True,
                           mapping=[{'col':'Do you consume Alcohol?',
  'mapping':{'Daily':0,'Sometimes':1,'Never':2}}])
  df['Do you consume Alcohol?'] = encoder.fit_transform(df['Do you consume Alcohol?'])
  encoder= ce.OrdinalEncoder(cols=['Do you smoke?'],return_df=True,
                           mapping=[{'col':'Do you smoke?',
  'mapping':{'Daily':0,'Sometimes':1,'Never':2}}])
  df['Do you smoke?'] = encoder.fit_transform(df['Do you smoke?'])
  x = df.drop(['Timestamp','BMI Categories','BMI','Are you involved in any physical activities ?', 'Do you have any family history of diseases?','Diabetes', 'Blood Pressure', 'Heart related diseases',
       "Alzheimer's Disease", 'Thyroid', 'Skin related diseases',
       'Brain Stroke', 'Hairfall', 'PCOS/PCOD', 'Cancer'], axis=1)
  y = df.drop(['Timestamp', 'Gender', 'What is your Age',
       "What is your height ? (eg. 5'4)", 'What is your weight ? (in kg)',
       'BMI', 'BMI Categories', 'At what time do you wake up?',
       'Do you always have breakfast ?',
       'What do you usually have in breakfast ?',
       'How many times in a week do you eat outside ?',
       'Rate your  eating habits?',
       'Do you maintain your lunch and dinner time ?',
       'Are you involved in any physical activities ?',
       'How much time do you travel in a day?',
       'How many hours do you sleep ?', 'Do you consume Alcohol?',
       'Do you smoke?', 'Rate you stress level ?', 'Average working hours ?','Rate your hair fall level',
       'Do you have any family history of diseases?',
       'Family History Of Diabetes', 'Family History Of Blood Pressure',
       'Family History Of Heart related diseases',
       'Family History Of Alzheimer’s disease', 'Family History Of Thyroid',
       'Family History Of Skin related diseases',
       'Family History Of Brain Stroke', 'Family History Of Hairfall',
       'Family History Of PCOS / PCOD', 'Family History Of Cancer'], axis=1)
  pd.set_option('display.max_columns', None)

  from sklearn.model_selection import train_test_split
  X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size= 0.2, random_state= 3)
  print(X_train.shape, X_test.shape)
  from sklearn.tree import DecisionTreeClassifier
  DT_GINI = DecisionTreeClassifier(criterion='gini', max_depth = 5, random_state=0)
  DT_GINI.fit(X_train, Y_train)
  Y_pred_gini = DT_GINI.predict(X_test)
  from sklearn.metrics import accuracy_score
  print("Model Accuracy is : ", accuracy_score(Y_test, Y_pred_gini))
  # plt.figure(figsize=(12, 8))
  # from sklearn import tree
  # tree.plot_tree(DT_GINI.fit(X_train, Y_train))
  # pickle.dump(DT_GINI, open('model.pkl','wb'))
  # model = pickle.load(open('model.pkl','rb'))
  # input = [0 ,58,1.0, 1, 2, 2, 3,4,0, 0, 1,2,2,2,0,3,0,0,0,0,0,0,0,0,0,0,0]
  # a = np.array(input1)
  # a = a.reshape((1,-1))
  return DT_GINI.predict(input1)
  