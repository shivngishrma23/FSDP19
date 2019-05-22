import pandas as pd

df = pd.read_csv('training_titanic.csv')

print(df)

df1 = df['Survived'].value_counts().tolist()
print(df1)

df['Survived'].value_counts(normalize = True)

df2 = df['Survived'][df['Sex']=='male'].value_counts(normalize = True)[1]
print(df2)

df3 = df['Survived'][df['Sex'] == 'female'].value_counts(normalize = True)[1]
print(df3)

df4 = df['Survived'][df['Sex'] == 'female'].value_counts(normalize = True)[0]
print(df4)

df["child"] = df["Age"].map(lambda x: 0 if x > 18 else 1 )

