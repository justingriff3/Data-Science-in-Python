import pandas as pd
import numpy as np

numbers = [1,2,3]

pd.Series[numbers]


#NAN VALUES (NUMPY)
np.nan = None
np.nan == np.nan  #Returns false be cause NaN does equate to none

np.isnan(np.nan)  #isnan is a special function to test for the presence of not a number, useful for querying a Series/Dataframe

#Creating a series from dictionary data. Note: The index will auto assign to the keys of the dict
student_scores = {'Justin' : 'Astrophysics',
                   'Siroun' : 'Microbiology',
                   'Addison' : 'Neuroscience'}

s = pd.Series(student_scores)
s 

s.index #Displays all indexes in the form of a list

students = [("Justin", 'Griffin'),('Siroun', 'Elliot'), ('Addison', 'Ruffin')] 
ss = pd.Series(students)   #Create a series from a list of tuples. Note: Index is still int from 0-N

ss = pd.Series(students, index = [333, 454, 782])







#DATA FRAMES 
students = ["Justin", "Siroun", "Addison"]
pd.Series(students)

record1 = pd.Series({'Name': "Justin",
                    'Class': 'Data Engineering',
                    'Score': 89})

record2 = pd.Series({'Name': "Siroun",
                    'Class': 'Artifical Inteligence',
                    'Score': 92})

record3 = pd.Series({'Name': "Addison",
                    'Class': 'Automation',
                    'Score': 85})

df = pd.DataFrame([record1, record2, record3],
                 index = ['school1', 'school2', 'school1'])

df.head()

df.loc["school1"]

df.T.loc["Name"]

