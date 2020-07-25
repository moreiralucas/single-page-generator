import os
from jinja2 import Template

template = Template('Hello {{ name }}!')
template.render(name='John Doe')

itens = []

template = env.get_templates(os.path.join('templates','index.html'))

print(template.render(itens=itens))


