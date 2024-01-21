from pprint import pprint
import json

points = 0

with open('quiz.json') as json_file:
    questions = json.loads(json_file.read().encode('UTF-8'))
    print(questions)
    pprint(questions)
    print('ść')