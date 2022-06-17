mport pandas as pd
import numpy as np

numbers = [1,2,3]

pd.Series(numbers)


#NAN VALUES (NUMPY)
np.nan = None
np.nan == np.nan  #Returns false be cause NaN does equate to none

np.isnan(np.nan)  #isnan is a special function to test for the presence of not a number, useful for querying a Series/Dataframe
#^^^  might throw an error

#Creating a series from dictionary data. Note: The index will auto assign to the keys of the dict
student_scores = {'Justin' : 'Astrophysics',
                   'Siroun' : 'Microbiology',
                   'Addison' : 'Neuroscience'}

s = pd.Series(student_scores)
s 

s.index #Displays all indexes in the form of a list

student_classes = pd.Series({'Xander' : 'iOS development',
                              'Keianna' : 'Machine Learning',
                              'Joseph' : 'Cyber Secuirty',
                              'Michael' : 'Data Analytics'})
mia_classes = pd.Series(['Team coordination',  'Consulting', 'Tech strategies'], index = 'Mia', 'Mia', 'Mia')
student_classes = student_classes.append(mia_classes)  #append() adds data to the end of a series
print(student_classes)

print(student_classes.loc['Mia']) #prints only Mia's classes 

students = [("Justin", 'Griffin'),('Siroun', 'Elliot'), ('Addison', 'Ruffin')] 
ss = pd.Series(students)   #Create a series from a list of tuples. Note: Index is still int from 0-N

ss = pd.Series(students, index = [333, 454, 782]) #Sets the indexes of the series as these values 

s.iloc[2] #OR
s[2]      # BOTH returns 'neuroscience'

s.loc['Justin'] #OR
s['Justin'] #BOTH returns 'Astrophysics'

ss.loc[543] = 'Mariam' #.loc aslso lets you add new values, index is string

#NOTE: IF YOUR INDEX IS A LIST OF INTEGERS YOU MUST BE CAREFUL BECAUSE PANDAS CANNOT DETERMINE IF YOU ARE QUERYING BY INDEX POSITION OR INDEX LABEL

#Methodization for finding a certain number, summarizing or transforming data within the series
grades = pd.Series([95, 75, 85]) 
total = 0
for grade in grades:       #Iteration
    total += grades
print(total/len(grades))   #Returns the average of grades


numbers = pd.Series(np.random.randint(o, 1000, 10000)) #random int generator from 0 - 1000 with 10000 elements

#Cellular magic function (timeit) will run our code a few times to determine on average how long it takes (100). by default it runs 1000
%%timeit -n 100
total = 0
for number in numbers:
    total += numbers

print(total/len(numbers)

%%timeit -n 100
total = np.sum(numbers)
print(total/len(numbers))  #Computation method; Vectorization with numpy function sum is exponentially faster
#vectorization = the ability for a computer to execture mutliple instructions at once, with the right computer specs you can get dramatic speed ups

#For many data structures like stacks, queues or linked list, you must iterate over the entire structure to increment all elements, such as below;
#for label, value in numbers.iteritems():
    #numbers.set_value(label, value+2)

#but pandas makes it easy
numbers.head() #displays first five entries within any pandas data structure 
numbers += 2 #adds to all 10000 values in numbers
