import requests

"""
Retrieves a list of todo items from an API.
Asks for user-id and displays the tasks of the respective user.
"""

class Task:
    def __init__(self, id, user_id, title, completed):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.completed = completed

    def __str__(self):
        return 'id:' + str(self.id) + ' ' + self.title + (' -DONE' if self.completed is False else '')


class Tasks:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        uid = task.user_id
        if uid in self.tasks:
            self.tasks[uid].append(task)
        else:
            self.tasks[uid] = [task]

    def get_user_tasks(self, uid):
        if uid in self.tasks:
            return self.tasks[uid]
        else:
            return None

    def load(self):
        response = requests.get('https://jsonplaceholder.typicode.com/todos')
        if response.status_code != 200:
            print('Error', response.status_code)
        else:
            data = response.json()
            for row in data:
                task = Task(row['id'], row['userId'], row['title'], row['completed'])
                self.add_task(task)


if __name__ == '__main__':
    tasks = Tasks()
    tasks.load()
    while True:
        print('=================')
        id = int(input("User ID (0 to exit): "))
        if id == 0:
            break
        user_tasks = tasks.get_user_tasks(id)
        if user_tasks is None:
            print('User not found')
            continue
        for task in user_tasks:
            print(task)
