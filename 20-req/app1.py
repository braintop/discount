import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = response.json()
for i, post in enumerate(posts):
    print(i, post["title"])
    # print(post["body"])
    # print(post["userId"])
    # print(post["id"])
    # print(post["title"])
    # print(post["body"])
    # print(post["userId"])
    # print(post["id"])
    # print(post["title"])
    # print(post["body"])
    # print(post["userId"])
    # print(post["id"])