import requests

api_key='f6847aeb-cadd-4129-a674-1ad287027c07'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definitions)

