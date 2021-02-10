import pandas as pd


df = pd.read_json('quiz.json')
print(df.head())

print(df['quiz']['maths']['q1'])