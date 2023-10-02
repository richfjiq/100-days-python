import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_texts = []
article_links = []
# article_tag = soup.select_one(".title span a")
# article_text = article_tag.getText()
# article_link = article_tag.get("href")
# print(article_text)
# print(article_link)
# article_upvote = soup.select_one(".score")
# article_votes = article_upvote.getText()
# print(article_votes)

articles = soup.find_all("span", class_="titleline")
for article in articles:
    article_tag = article.find("a")
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [
    int(score.getText().split(" ")[0])
    for score in soup.find_all(name="span", class_="score")
]

# index_max_votes = 0
# max_votes = 0
# index = 0

# for vote in article_upvotes:
#     if vote > max_votes:
#         max_votes = vote
#         index_max_votes = index
#     index += 1

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(f"Title: {article_texts[largest_index]}")
print(f"Link: {article_links[largest_index]}")
print(f"Votes: {largest_number}")
