from service.scraper import Scraper
import pandas as pd
from fastapi import FastAPI, Form
from typing import Optional

from service.news_classifier_service import NewsClassifierService

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/api")
async def handle_request(url: Optional[str] = Form(None)):
    # You can now use the 'url' variable in your function
    return {"url": url}


@app.post("/postjson")
async def return_post_json(url: str = Form(...)):

    #add scraping code
    # main.py

    text = Scraper.scrape_article_content(url)
    # print(text)
    service = NewsClassifierService()
    data = {'text': [text]}
    df = pd.DataFrame(data)
    classification_result = service.classify_news(df)
    print('Classification result:', classification_result)
    return {"Result": classification_result}