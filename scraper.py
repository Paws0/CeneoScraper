import requests
from bs4 import BeautifulSoup
r = requests.get ('https://www.ceneo.pl/72542823#tab=reviews')


page_dom = BeautifulSoup(respons.text,"html.parser")

opinions = page_dom.select("div.js_product-review")
# print (type(opinions))
opinion = opinions.pop(0)
# print (type(opinion))
  
opinion_id = opinion["data-entry-id"]
author = opinion.select_one("span.user-post__author-name").text.strip()
recomm = opinion.select_one(
    "span.user-post__author-recomendation").text.strip()
stars = opinion.select_one("span.user-post__score-count").text.strip()
content = opinion.select_one("div.user-post__text").text.strip()
pros = opinion.select("div.review-feature__title--positives ~ review-feature__item")
cons = opinion.select("div.review-feature__title--negatives ~ review-feature__item")
useful = opinion.select_one("button.vote-yes > span").text.strip()
useless = opinion.select_one("button.vote-no > span").text.strip()
purchased = opinion.select_one("div.review-pz").text.strip()
publish_date = opinion.select_one(
    "span.user-post__published > time:nth-child(1)")["datetime"]
purchase_date = opinion.select_one(
    "span.user-post__published > time:nth-child(2)")["datetime"]

print(opinion_id, author, recomm, stars, content, pros, cons, useful, useless, purchased, publish_date, purchase_date)

# print(page_dom.prettify())