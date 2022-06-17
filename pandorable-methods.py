import pandas as pd 
import numpy as np
import timeit

df = pd.DataFrame([{'COA': 0.92,
       'GRE Score': 337,
       'SOP' : 4.5, 
        'Research' : 1,
        "Serial Number" : 1,
        "CGPA": 9.65,
         "LOR": 4.5,
         "University Rating": 4,
           "TOEFL": 118},
        {'COA': 0.76,
       'GRE Score': 324,
       'SOP' : 4.0, 
        'Research' : 1,
        "Serial Number" : 2,
        "CGPA": 8.87,
         "LOR": 4.5,
         "University Rating": 4,
           "TOEFL": 107},
           {'COA': 0.72,
       'GRE Score': 316,
       'SOP' : 3.0, 
        'Research' : 1,
        "Serial Number" : 3,
        "CGPA": 8.00,
         "LOR": 3.5,
         "University Rating": 3,
           "TOEFL": 104},
           {'COA': 0.80,
       'GRE Score': 322,
       'SOP' : 3.5, 
        'Research' : 0,
        "Serial Number" : 4,
        "CGPA": 8.67,
         "LOR": 2.5,
         "University Rating": 3,
           "TOEFL": 110},
           {'COA': 0.65,
       'GRE Score': 314,
       'SOP' : 2.0, 
        'Research' : 0,
        "Serial Number" : 5,
        "CGPA": 8.21,
         "LOR": 3.0,
         "University Rating": 2,
           "TOEFL": 103}])

#Pandorable method
(df.where(df['SOP'] > 3.0)   
    .dropna()
    .set_index(['Serial Number', 'University Rating'])
    .rename(columns = {'LOR' : 'Letter of Recommendation'}))
