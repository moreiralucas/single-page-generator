# A simple static page generator for one specific purpose   
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=4PKKLTZXPF9LS&currency_code=BRL&source=url)


The purpose of this project was to create a static html page generator for support a virtual [Baby Shower](https://en.wikipedia.org/wiki/Baby_shower) party.

Despite this event being held in person, due to the context in which we are quarantined due to the pandemic caused by the coronavirus (COVID-19), there was a need to perform it in a virtual way to maintain the tradition.


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

After installation, change the ```input.json``` file, inserting the data to be displayed on the html page.

## Summary


**Tags of page**
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
-  link_pagseguro: Link to the payment service ([PagSeguro](https://pagseguro.uol.com.br/))
-  btn_size: The size of button of payment service
-  btn_color: The color of button of payment service

## Donation
If this project help you reduce time to develop, you can give me a cup of coffee :) 

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=4PKKLTZXPF9LS&currency_code=BRL&source=url)


## License
See the [LICENSE](LICENSE) file for details.
