from fastapi import FastAPI,HTTPException
from schemas import Postcreate,Postresponds
app=FastAPI()
text_posts={1: {"text": "hello", "content": "hello to anybody, I am Zeina"},
    2: {"text": "python", "content": "Python is my favorite programming language"},
    3: {"text": "weather", "content": "Today is sunny and warm"},
    4: {"text": "database", "content": "I am learning PostgreSQL and SQL"},
    5: {"text": "food", "content": "I had pizza for dinner"},
    6: {"text": "python", "content": "I built a small Python project today"},
    7: {"text": "travel", "content": "I want to visit Italy someday"},
    8: {"text": "books", "content": "I am reading a book about software engineering"},
    9: {"text": "coffee", "content": "Coffee helps me focus while coding"},
    10: {"text": "api", "content": "I am learning how APIs communicate with applications"},
    11: {"text": "music", "content": "I listen to music while studying"},
    12: {"text": "django", "content": "Django can be used to build web applications"},
    13: {"text": "exercise", "content": "I went for a walk this morning"},
    14: {"text": "school", "content": "Learning new skills takes consistent practice"},
    15: {"text": "python", "content": "I need more practice with Python classes"}
}
# @app.get("/home")
# def home():
#     return{"message":"hello FastApi"}
@app.get("/posts")
def get_all_posts(limit: int=None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts
@app.get("/posts/{id}")
def get_post(id:int):
    if id not in text_posts:
        raise HTTPException(status_code=404,detail="Post Not found")
    return text_posts.get(id)
@app.post("/posts")
def Create_posts(post:Postcreate) -> Postresponds :
    new_post={"text":post.text,"content":post.content}
    text_posts[max(text_posts.keys())+1]=new_post
    return new_post
