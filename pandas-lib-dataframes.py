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

#DATA FRAME: INDEXING
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

new_df = df.rename(columns = {'LOR' : 'Letter of Recommendation', 
                             "SOP": "Statement of Purpose"}) #Function to rename a column
new_df.columns #attribute to view columns

# pass strip() function into mapper parameter strip white spaces. Very useful for accurate data cleaning
new_df = new_df.rename(mapper = str.strip, axis = "columns")

#Using the .columns attribute you can assign a list of column names which will
#-directly rename the columns. An example can be make all the column names uppercase
cols = list(df.columns)
cols = [x.upper().strip() for x in cols]
df.columns = cols
df
