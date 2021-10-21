import json
from jinja2 import Environment, FileSystemLoader

with open("Sample_data.json","r") as d:
    sampleData = json.load(d)

fileLoader = FileSystemLoader("templates")
env = Environment(loader=fileLoader)

stars = {
        '1.0':'https://cdn.tripadvisor.com/img2/email/rex/ratingstar1.0.png',
        '1.5':'https://cdn.tripadvisor.com/img2/email/rex/ratingstar1.5.png',
        '2.0':'https://cdn.tripadvisor.com/img2/email/rex/ratingstar2.0.png',
        '2.5':'https://cdn.tripadvisor.com/img2/email/rex/ratingstar2.5.png',
        '3.0':'https://cdn.tripadvisor.com/img2/email/rex/ratingstar3.0.png',
        '3.5':'https://cdn.tripadvisor.com/img2/email/rex/ratingstar3.5.png',
        '4.0':'https://cdn.tripadvisor.com/img2/email/rex/ratingstar4.0.png',
        '4.5':'https://cdn.tripadvisor.com/img2/email/rex/ratingstar4.5.png',
        '5.0':'https://cdn.tripadvisor.com/img2/email/rex/ratingstar5.0.png'
        }

rendered = env.get_template("template.html").render(jsonData=sampleData, stars=stars)

# Write HTML to a file - index2.html

fileName = "index2.html"

with open(f"./site/{fileName}","w") as f:
    f.write(rendered)