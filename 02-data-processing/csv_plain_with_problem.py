titanic_list = []

with open('titanic.csv', 'r') as titanic_data:

    # Skip the first row with headers
    next(titanic_data)

    for line in titanic_data:
        line_data = line.split(',')
        titanic_list.append(line_data)

    for record in titanic_list:
        print(record, len(record))

    print("See the problem?")
    print("Names containing commas are separated, too.")

