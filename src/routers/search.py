from fastapi import APIRouter, HTTPException
from ytmusicapi import YTMusic

router = APIRouter()

@router.get("/search")
def search_default():
  raise HTTPException(
    status_code=400,
    detail="Missing required parameter"
  )

@router.get("/search/{query}")
async def search(
  query: str,
  filter: str | None = None,
  ignore_spelling: bool = False,
  limit: int = 20,
  scope: str | None = None
):
  ytmusic = YTMusic()
  search_results = ytmusic.search(
    query=query,
    filter=filter,
    ignore_spelling=ignore_spelling,
    limit=limit,
    scope=scope
  )

  return {
    "message": "OK",
    "query": query,
    "result": search_results
  }