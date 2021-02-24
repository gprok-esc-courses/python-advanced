import mysql.connector
import pandas as pd

db = mysql.connector.connect(
    host="localhost", user="test", password="test", database="python_simple"
)

query = pd.read_sql_query("SELECT * FROM client", db)
df = pd.DataFrame(query, columns=['client_id','birth_number','district_id'])
print(df)



