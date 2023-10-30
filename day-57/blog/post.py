import requests


class Post:
    def __init__(self):
        self.posts = []
        self.get_posts()

    def get_posts(self):
        response = requests.get("https://api.npoint.io/79033b02e537403ed53d")
        self.posts = response.json()
