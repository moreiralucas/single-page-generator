import os, json, string
from jinja2 import Template
from random import choice
from datetime import datetime
from shutil import copyfile, copytree

OPTIONAL_PARAMS = [
  "btn_size",
  "btn_color",
  "path_image",
  "footer_phrase",
  "footer",
  "path_logo_title",
]

TEMPLATE_DEFAULT = 'templates/index.html'

def check_item(items):
  for data in items:
    for key, value in data.items():
      if key in OPTIONAL_PARAMS:
        continue

      if value == "":
        raise "This param is required"

def check_data(data):
  for key, value in data.items():
    if key in OPTIONAL_PARAMS:
      continue

    if value == "":
      raise "This param is required"

    if key == "items":
      check_item(value)

def get_json():
  with open("input.json", "r") as f:
    input_file = f.read()
    return json.loads(input_file)

def get_template():
  with open(TEMPLATE_DEFAULT, "r") as f:
    template_file = f.read()
    template = Template(template_file)
    return template

def make_dirs(project_name):
  os.mkdir("output/{}".format(project_name))

def copy_files(project_name):
  dst = os.path.join("output", project_name, "static")
  copytree("static", dst)

def write_html(html, project_name=None):
  if project_name is None:
    project_name = ''.join([choice(string.ascii_letters) for _ in range(5)])
  else:
    project_name = ''.join(x if x.isalpha() else '_' for x in project_name)
  project_name += '_' + datetime.now().strftime("%d-%m-%Y")

  make_dirs(project_name)
  copy_files(project_name)

  file_path = os.path.join('output', project_name, 'index.html')
  with open(file_path, "w") as f:
    f.write(html)

template = get_template()
dados = get_json()
check_data(dados)
write_html(template.render(dados), dados['title_page'])


