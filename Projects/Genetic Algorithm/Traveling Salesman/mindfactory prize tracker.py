import urllib.request

import re

url = "https://www.mindfactory.de/shopping_cart.php/basket_action/load_basket_extern/id/b8980422109c30ef52b0089aa8b160c9487961cbc2a84570de4"
data = urllib.request.urlopen(url).read()
print(data)
