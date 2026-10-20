from typing import Any
from playwright.async_api import async_playwright


class PysznePlScraper:
    pysznepl_url = ''

    async def scraper_page(self) -> Any:
        async with async_playwright() as plawyright:
            browser = await plawyright.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto("https://www.pyszne.pl/en/delivery/food/50-148?utm_source=google&utm_medium=cpc&utm_campaign=CM_S_G_POL_[BRAND]_[ENGM]_Pyszne.pl_Wroclaw_1011243&utm_campaignid=24100530141&gad_source=1&gad_campaignid=24100530141&gbraid=0AAAAAD3ULIWD1v0cTsJ6i0c0ov_Mf0xFy&gclid=CjwKCAjwuczWBhA9EiwAYGgEoYqDHnvlZMaU7cyHAvGMO2hVEJW0KZRXqpaRF7I7-sA2os4DMMkOoxoChGcQAvD_BwE", wait_until="domcontentloaded")

            content = await page.content()

            print(content)

            await browser.close()
            return content
