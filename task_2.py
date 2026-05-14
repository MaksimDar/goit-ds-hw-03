import json
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from pymongo.server_api import ServerApi


command = 'poetry run python3 task_2.py'

url = 'http://quotes.toscrape.com'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
data = []
authors = []

qoutes = soup.find_all('div', class_= 'quote')

for qoute in qoutes:
    tags_list = []

    # Find the author
    author = qoute.find('small', class_ = 'author')
    author_text = author.text

    # Find the quote
    quote = qoute.find('span', class_ = 'text')
    quote_text = quote.text

    # find all tags that relate to this quote
    for tag in qoute.find_all('a', class_='tag'):
        tag_text = tag.get_text()
        tags_list.append(tag_text)

    data.append({
        'tags': tags_list,
        'author': author_text,
        "quote": quote_text
    })

    author_link = author.find_next_sibling('a')

    author_link_href = author_link['href'] # url to the author's biography
    response_biography = requests.get(url+author_link_href)
    biography_soup = BeautifulSoup(response_biography.text, 'lxml')

    # Find the author
    author_title = biography_soup.find('h3', class_='author-title')
    author_title_text = author_title.text

    #Find birth details
    born_info = author_title.find_next_sibling()
    born_date = born_info.find('span', class_='author-born-date')
    born_date_text = born_date.text
    born_place = born_info.find('span', class_='author-born-location')
    born_place_text = born_place.text

    #Find description
    description = biography_soup.find('div', class_='author-description')
    description_text = description.text
    
    authors.append({"fullname": author_title_text, "born_date": born_date_text,
    "born_location": born_place_text,"description": description_text.strip()})




with open('qoutes.json','w',encoding='utf-8') as file:
    json.dump(data,file,indent=4)

with open('authors.json', 'w',encoding='utf-8') as file:
    json.dump(authors,file,indent=4)

######### Import qoutes.json and authors.json to relative collections of the database

mongo_connection = MongoClient('mongodb+srv://maksym_learner:ssXumE4galkz66sP@maksympractise.jz4oll5.mongodb.net/', server_api=ServerApi('1'))
db = mongo_connection.task_2
collection_authors = db.authors
collection_qoutes = db.qoutes

### Insert data from qoutes.json into mongodb database task_2, quotes collection
with open('qoutes.json', 'r', encoding='utf-8') as file:
    quotes = json.load(file)

for quote in quotes:
    collection_qoutes.insert_one(quote)

### Insert data from authors.json into mongodb database task_2, authors collection

with open('authors.json', 'r', encoding='utf-8') as file:
    authors = json.load(file)

for author in authors:
    collection_authors.insert_one(author)





