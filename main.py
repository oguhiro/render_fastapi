from typing import Optional

from fastapi import FastAPI

from fastapi.responses import HTMLResponse #インポート


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "takoyaki"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
            <p>自己紹介</p>
            <p>好きな食べ物はハヤシライスです</p>
            <p>趣味はダンスです</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)