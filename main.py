from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def 테스트():
    return 'hello'