import pandas as pd

#DATA FRAMES 
students = ["Justin", "Siroun", "Addison"]
pd.Series(students)

#1st method: Create 3 different series and read them into the data frame 
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

#2nd method: An alternative method is using a list of dictionaries NOTE: Each dictionary represents a row of data
students = [{'Name': 'Justin',
       'Class': 'Data Engineering',
       'Score' : 89}, 
      {'Name': "Siroun",
       'Class': 'Artifical Inteligence',
        'Score': 92},
      {'Name': "Addison",
       'Class': 'Automation',
       'Score': 85}]
df = pd.DataFrame(students, index = ['school1', 'school2','school3'])     

df.head()

df.loc["school2"]  #Returns a tubular display with data that is indexed as 'school1'
df.loc['school1', 'Name'] #Returns only the names of records with a index of 'school1'

type(df.loc['school2']) #Check the data type of the the return using the type function in python
#OUTPUT" 'pandas.core.series.Series

df.T #Displays the transpose of the table. Making the column headers the indexes and viceverse

df.T.loc["Name"] 

df.loc[:, ['Name','Score']] #The colon means we want to get all the rows, and the columns in the second 
#parameter means we want to get only those select columns

copy_df = df.copy() #Makes a copy of a dataframe

#Dropping columns:
#1st method
copy_df.drop("Name", inplace = True, axis =1) 

#2nd method
del copy_df['Class']

df['ClassRanking'] = None #Initializing a new column with no values

