"""
DOCSTRING
"""
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    """
    METHOD DOCSTRING
    """
    return {"message": "Hello World", "source": "Undisclosed"}
