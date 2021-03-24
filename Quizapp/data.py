from quiz.models import quiz
import json
with open('quiz_data.json', 'r') as data_file:
    json_data = data_file.read()


data = json.loads(json_data)

for i in data:
    q=quiz(question=i['question'],a=i['a'],b=i['b'],c=i['c'],d=i['d'],correct=i['correct'])
    q.save()