# A simple static page generator for one specific purpose

## Requirements

We recomend installing Python's venv:
```
sudo apt install python3-venv
```

Then, create and activate a venv:
```
python3 -m venv env
source env/bin/activate
```
In this project, the python version is 3.6.9

Install the requirements:
```
pip install -r requirements.txt
```

## How to use

Após a instalação, altere o arquivo ```input.json```, inserindo os dados a serem exibidos na página html.

## Summary

-  title_body: A title of your content. this will be displayed below the header image   
-  title_page: A title of your page html  
-  path_logo_title: The path to header image  
-  items: The list of items to display (this will be described below)   
-  footer_phrase: A phrase to be displayed below the listed items.   
-  footer: Your page footer message   
**The list of items**
-  description: The item description
-  description_foot: The complement of description
-  total_price: The price of item
-  path_image: The path of image of the item
-  link_pagseguro: Link to the payment service (PagSeguro)
-  btn_size: The size of button of payment service
-  btn_color: The color of button of payment service



## License
See the [LICENSE](LICENSE) file for details.
