from fastapi import FastAPI
import file_operations
import requests

app = FastAPI()
account_id = "123456789005"

@app.get("/")
def read_root():
    return {"Hello": "World"}
