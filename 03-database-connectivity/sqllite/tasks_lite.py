import sqlite3

db = sqlite3.connect('tasks.db')

db.execute('''CREATE TABLE tasks
         (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
         task TEXT NOT NULL);''')

db.execute("INSERT INTO tasks (task) VALUES ('Reply to customer')");
db.execute("INSERT INTO tasks (task) VALUES ('Repair motorcycle')");
db.commit()

cursor = db.cursor()
result = cursor.execute("SELECT * FROM tasks")
for row in result:
    print(row)

