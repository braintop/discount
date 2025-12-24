import requests
import time
response = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = response.json()
print(posts)
dict ={}
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
    #post["title"] = "Updated title:" + str(i)
posts[0]["timestamp"] = time.time()
print(posts[0])
