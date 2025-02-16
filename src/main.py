from fastapi import FastAPI
from src.routers import search, browsing, explore, watch

app = FastAPI()
app.include_router(search.router)
app.include_router(browsing.router)
app.include_router(explore.router)
app.include_router(watch.router)

@app.get("/")
def root():
  return {"message": "Hello YT Music API!"}

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="0.0.0.0")