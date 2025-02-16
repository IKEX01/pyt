from fastapi import FastAPI
from src.routers import search

app = FastAPI()
app.include_router(search.router)

@app.get("/")
def root():
  return {"message": "Hello YT Music API!"}

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="0.0.0.0", port=8000)