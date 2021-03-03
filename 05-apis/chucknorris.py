import requests

"""
Retrieves a Chuck Norris joke from an API
"""

response = requests.get('https://api.chucknorris.io/jokes/random')
if response.status_code != 200:
    print('Error', response.status_code)
else:
    joke = response.json()
    print(joke['value'])