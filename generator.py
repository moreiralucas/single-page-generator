import os, json
from jinja2 import Template

OPTIONAL_PARAMS = [
  "btn_size",
  "btn_color",
  "path_image",
  "footer_phrase",
  "footer",
  "path_logo_title",
]

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
  with open("templates/index.html", "r") as f:
    template_file = f.read()
    template = Template(template_file)
    return template

template = get_template()
dados = get_json()
check_data(dados)
print(template.render(dados))

