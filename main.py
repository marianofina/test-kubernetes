from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    total = 0
    for i in range(10_000_000):
        total += i*i
    return {"message": "Hello World", "total": total}

@app.get("/health")
async def health():
    return "OK"