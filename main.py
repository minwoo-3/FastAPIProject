from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root_handler():
    return {"message": "Hello, FastAPI!"}

@app.get("/login")
def root_handler():
    return {"message": "로그인 페이지에 오신 것을 환영합니다"}