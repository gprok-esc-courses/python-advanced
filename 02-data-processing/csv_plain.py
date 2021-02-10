import re


class Passenger:
    def __init__(self, line_data):
        self.id = line_data[0]
        self.survived = line_data[1]
        self.pclass = line_data[2]
        self.name = line_data[3]
        self.sex = line_data[4]
        self.age = line_data[5]
        self.siblings_spouse = line_data[6]
        self.parents_children = line_data[7]
        self.ticket_no = line_data[8]
        self.fare = line_data[9]
        self.cabin = line_data[10]
        self.embarked = line_data[11]

    def __str__(self):
        return self.name + ": " + ('S' if self.survived == 0 else 'D')


titanic_list = []
titanic_dict = {}

with open('titanic.csv', 'r') as titanic_data:

    # Skip the first row with headers
    next(titanic_data)

    for line in titanic_data:
        line = line.rstrip('\n')
        comma_matcher = re.compile(r",(?=(?:[^\"]*[\"][^\"]*[\"])*[^\"]*$)")
        line_data = comma_matcher.split(line)
        line_data[3] = line_data[3].replace('"', '')
        titanic_list.append(line_data)
        if len(line_data) == 12:
            titanic_dict[line_data[0]] = Passenger(line_data)

    for record in titanic_list:
        print(record, len(record))

    for pid, passenger in titanic_dict.items():
        print(passenger)

