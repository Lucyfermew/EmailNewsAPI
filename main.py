from pydoc_data.topics import topics
import requests
from send_email import send_email
from email.message import EmailMessage
# RAN DAILY ON PYTHON ANYWHERE, if you hardcode your password and don't take it from os

# topic = "tech-news" - u can add with an f string and not hardcore the topic in the url

api_key = "YOUR_API_CODE"
url = "LINK_FOR_AN_API_SITE"

# make a request
request = requests.get(url)

# get a dict with data
content = request.json()

# access the article titles and description
news_body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        # body = "Subject: Today's news" + "\n" + body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n"
        news_body += f"{article['title']}\n{article['description']}\n{article['url']}\n\n"

# body = body.encode("utf-8")
email = EmailMessage()
email["Subject"] = "Today's TechCrunch News"
email["From"] = "your_own_email"
email["To"] = "your_own_email"
email.set_content(news_body)

send_email(email)
# server.send_message(email)
