import requests
import html

response = requests.get('https://opentdb.com/api.php?amount=5')
if response.status_code != 200:
    print("Error", response.status_code)
else:
    json = response.json()
    for obj in json['results']:
        print("Q: ", html.unescape(obj['question']))
        print("\tC.A.:", html.unescape(obj['correct_answer']))
        print("\tIncorrect Answers")
        for ans in obj['incorrect_answers']:
            print("\t\t", html.unescape(ans))
