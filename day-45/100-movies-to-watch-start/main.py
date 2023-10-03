import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
best_movies_page = response.text
soup = BeautifulSoup(best_movies_page, "html.parser")
movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in movies]
movies_text = "\n".join(movie_titles[::-1])

with open("./movies.txt", mode="w") as file:
    file.write(f"{movies_text}")

# movies_list = []

# for movie in movies:
#     title = movie.getText()
#     movies_list[:0] = [title]
