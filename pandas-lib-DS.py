import pandas as pd

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
