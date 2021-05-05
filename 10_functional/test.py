from functools import reduce

cities = ["Prague", "Athens", "New York", "Tirana", "Berlin", "Bratislava"]

sorted_cities = sorted(cities)
print(sorted_cities)
print(cities)

sorted_by_2nd_char = sorted(cities, key=lambda s: s[1:3])
print(sorted_by_2nd_char)

sorted_by_length = sorted(cities, key=lambda s: -len(s))
print(sorted_by_length)

lengths = list(map(lambda s: len(s), cities))
print(lengths)

for_csv = " # ".join(cities)
print(for_csv)

start_from_b = list(filter(lambda s: s[0]=='B', cities))
print(start_from_b)

largest = reduce(lambda a, b: a if len(a) > len(b) else b, cities)
print(largest)