import requests

from operator import itemgetter

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print('Status Code:', r.status_code)

submissions_ids = r.json()
submissions_dicts = []

for submissions_id in submissions_ids[:30]:
# Cria uma chamada de API separada para cada artigo submetido
    url = ('https://hacker-news.firebaseio.com/v0/item/' + 
    str(submissions_id) + '.json')
    submissions_r = requests.get(url)
    response_dict = submissions_r.json()

    submissions_dict = { 
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + 
        str(submissions_id),
        'comments': response_dict.get('descendants', 0)
    }
    submissions_dicts.append(submissions_dict)

submissions_dicts = sorted(submissions_dicts, key=itemgetter('comments'),
reverse=True)

for submission_dict in submissions_dicts:
    print("\nTitle:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])

