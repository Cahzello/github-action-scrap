from playwright.sync_api import Playwright, sync_playwright
import numpy as np
import datetime 
import re

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.scrapethissite.com/")
    page.get_by_role("link", name=" Sandbox").click()
    page.get_by_role("link", name="Countries of the World: A").click()
    page.get_by_role("heading", name="Countries of the World: A").click()
    # pageTitle = page.locator(".col-md-12").locator("h1").all_inner_texts()
    # print(pageTitle)
    
    currentTime = datetime.datetime.now().strftime("%X")
    currentTime = re.sub(":", "-", currentTime)
    np.savetxt(f"countries-{currentTime}.csv", page.locator(".country").all_inner_texts(), delimiter=",", fmt="%s")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
