import json


with open('test.json') as file:
    data = json.load(file)
    for item in data:
        print(item['questions'])
        for idx, answer in enumerate(item['answers']):
            print(f'{idx + 1} : {answer}')
        answer = input('Write answer:\n')
        if str(answer) == str(item['right answers']):
            print('You have right')
        else:
            print('It is not right answer')

# print(data[0]['answers'][1])