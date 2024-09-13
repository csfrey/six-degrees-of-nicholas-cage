from fastapi import FastAPI
from imdb import Cinemagoer
from requests import Response

app = FastAPI()
ia = Cinemagoer()

# @app.get("/hello")
# def hello_world():
#     return {"Hello": "World"}

@app.get("/api/search/{name}")
def search(name: str):
  people = []
  search_results = ia.search_person(name)
  for r in search_results:
    people.append(r.data)
  
  return {
    "data": people
  }