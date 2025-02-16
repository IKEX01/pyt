from fastapi import APIRouter, HTTPException
from ytmusicapi import YTMusic

router = APIRouter()

@router.get("/charts")
@router.get("/mood_playlists")
def explore_default():
  raise HTTPException(
    status_code=400,
    detail="Missing required parameter"
  )

@router.get("/mood_playlists/{query}")
async def search(
  query: str
):
  ytmusic = YTMusic()
  results = ytmusic.get_mood_playlists(query)

  return {
    "message": "OK",
    "query": query,
    "result": results
  }

@router.get("/charts/{country}")
async def get_search_suggestions(
  country: str = 'ZZ'
):
  ytmusic = YTMusic()
  results = ytmusic.get_charts(country)

  return {
    "message": "OK",
    "query": country,
    "result": results
  }