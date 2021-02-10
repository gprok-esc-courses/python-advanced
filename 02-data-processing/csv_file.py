import csv

with open('titanic.csv', 'r') as csv_titanic:
    csv_reader = csv.reader(csv_titanic)

    # Skip the first row with headers
    next(csv_reader)

    for line in csv_reader:
        print(line)

# Lets find how many survived
with open('titanic.csv', 'r') as csv_titanic:
    survived = 0
    died = 0
    csv_reader = csv.reader(csv_titanic)
    for line in csv_reader:
        if line[1] == '1':
            survived += 1
        else:
            died += 1

    print("Survived:", survived)
    print("Died:", died)