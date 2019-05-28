
import pandas as pd

data = pd.read_csv('training_titanic.csv')

data.shape

data.info()

data.head(10)
#survived people coloumn
data['Survived'].value_counts()

#people survived
survived = data['Survived'].value_counts()[1]
#people died
died = data['Survived'].value_counts()[0]
#survived people in percentage
survived_percentage = data['Survived'].value_counts(normalize=True)[1]
#died people in percentage
died_percentage = data['Survived'].value_counts(normalize=True)[0]

male_survived = data['Survived'][data['Sex'] == 'male'].value_counts(normalize=True)[1]
male_died =  data['Survived'][data['Sex'] == 'male'].value_counts(normalize=True)[0]

female_survived = data['Survived'][data['Sex'] == 'female'].value_counts(normalize=True)[1]
female_died =  data['Survived'][data['Sex'] == 'female'].value_counts(normalize=True)[0]


print ("disaster_survived : "+str(survived))
print ("disaster_died : "+str(died))
print ("disaster_survived_percentage : "+str(round(survived_percentage*100,2))+"%")
print ("disaster_died_percentage : "+str(round(died_percentage*100,2))+"%")
print ("male_survived : "+str(round(male_survived*100,2))+"%")
print ("male_passed_away : "+str(round(male_died*100,2))+"%")
print ("female_survived : "+str(round(female_survived*100,2))+"%")
print ("female_passed_away : "+str(round(female_died*100,2))+"%")

#saving childs first 
data['Child'] = 0
data['Child'][data['Age'] < 18] = 1
c =  data['Survived'][data['Child'] == 1].value_counts(normalize=True)
print ("Child Survived : "+str(round(c[1]*100, 2))+"%")






