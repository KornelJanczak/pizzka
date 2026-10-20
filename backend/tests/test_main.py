from fastapi.testclient import TestClient

from app.main import app
from app.routers import pyszne


client = TestClient(app)


def test_read_root() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Pizzka API is running"}


def test_read_health() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_scrape_pyszne(monkeypatch) -> None:
    async def fake_scraper_page() -> str:
        return "<html>scraped content</html>"

    monkeypatch.setattr(pyszne.scraper, "scraper_page", fake_scraper_page)

    response = client.get("/scraper/pyszne")

    assert response.status_code == 200
    assert response.json() == {"content": "<html>scraped content</html>"}
