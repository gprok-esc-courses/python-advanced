import pandas as pd

df = pd.read_csv('titanic.csv')
print(df)

print("Mean survived:", df['Survived'].mean())

print("Values by age:")
print(df['Age'].value_counts())

print("Values by port embarked:")
print(df['Embarked'].value_counts())

# Group passengers by age
grouped_df = df.groupby('Age')['Name']
for key, item in grouped_df:
    print(key, ':')
    print(grouped_df.get_group(key))

fare_df = df[df['Fare'] < 8]
print(fare_df.shape)
