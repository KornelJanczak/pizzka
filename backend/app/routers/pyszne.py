from typing import Any

from fastapi import APIRouter
from pydantic import BaseModel

from app.services.pyszne_pl_scraper import PysznePlScraper


class PyszneScrapeResponse(BaseModel):
    content: Any


router = APIRouter(prefix="/scraper", tags=["scraper"])
scraper = PysznePlScraper()


@router.get("/pyszne", response_model=PyszneScrapeResponse)
async def scrape_pyszne() -> PyszneScrapeResponse:
    content = await scraper.scraper_page()
    return PyszneScrapeResponse(content=content)
