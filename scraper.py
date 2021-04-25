import requests
r = requests.get ('https://www.ceneo.pl/72542823#tab=reviews')

print(r.text)