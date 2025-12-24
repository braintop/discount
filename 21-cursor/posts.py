import requests
class Posts:
    url = "https://jsonplaceholder.typicode.com/posts"
    @staticmethod
    def get_posts():
        response = requests.get(Posts.url)
        posts = response.json()
        return posts

    @staticmethod
    def get_post(id):
        response = requests.get(f"{Posts.url}/{id}")
        post = response.json()
        return post

    @staticmethod
    def create_post(title, body, userId):
            response = requests.post(Posts.url, json={"title": title, "body": body, "userId": userId})
        post = response.json()
        return post