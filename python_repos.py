import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Faz uma chamada de API e armazena a resposta
url = 'https://api.github.com/search/repositories?q=language:javascript&sort=stars'
r = requests.get(url)
print('Status Code:', r.status_code)


# Armazena a resposta da API em uma variável
reponse_dict = r.json()
print('Total repositories:', reponse_dict['total_count'])

# Explora informações sobre os repositórios
repo_dicts = reponse_dict['items']
print('Repositories returned:', len(repo_dicts))


# repo_dict = repo_dicts[0]
# for keys in sorted(repo_dict.keys()):
#     print(keys)

# Analisa o primeiro repositório

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    
    if repo_dict['description']:
        desc = repo_dict['description']
    else:
        desc = 'No description'

    plot_dict = {
    'value': repo_dict['stargazers_count'],
    'label': desc,
    'xlink': repo_dict['html_url'],      
    }
    plot_dicts.append(plot_dict)

my_style = LS('#336699', base_style=LCS)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config,style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('',plot_dicts)
chart.render_to_file('js_repos.svg')