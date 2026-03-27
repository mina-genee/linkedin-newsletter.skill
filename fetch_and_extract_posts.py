import os
import sys
import time
import json
import re
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def main():
    if len(sys.argv) < 2:
        print("Usage: python fetch_and_extract_posts.py <browser_data_dir>")
        sys.exit(1)
        
    data_dir = sys.argv[1]
    os.makedirs(data_dir, exist_ok=True)
    
    with sync_playwright() as pw:
        context = pw.chromium.launch_persistent_context(
            data_dir,
            headless=False,
            args=["--disable-blink-features=AutomationControlled"],
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 900},
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto("https://www.linkedin.com/my-items/saved-posts/", wait_until="domcontentloaded", timeout=60000)
        
        print("Checking login status...")
        if "login" in page.url or "signup" in page.url or "session_redirect" in page.url:
            print("Please log in... waiting up to 5 mins.")
            try:
                page.wait_for_url("**/my-items/saved-posts/**", timeout=300000)
            except Exception as e:
                print("Login failed or timed out.")
                return
        
        time.sleep(5)
        # Scroll to load elements
        for _ in range(5):
            page.mouse.wheel(0, 1000)
            time.sleep(1.5)
            
        html_content = page.content()
        soup = BeautifulSoup(html_content, "html.parser")
        
        posts = []
        results = soup.find_all(class_=re.compile(r"entity-result__item|reusable-search__result-container"))
        
        if results:
            for res in results:
                link_el = res.find("a", class_=re.compile(r"app-aware-link"))
                link = link_el["href"].split("?")[0] if link_el else None
                
                summary_el = res.find(class_=re.compile(r"entity-result__summary|entity-result__content-summary|update-components-text"))
                text = summary_el.get_text(separator=" ", strip=True) if summary_el else ""
                if not text:
                    text = res.get_text(separator=" ", strip=True)
                    
                if link and ("linkedin.com/posts/" in link or "linkedin.com/feed/update/" in link or "urn:li:activity" in link):
                    if not any(p["link"] == link for p in posts):
                        posts.append({"link": link, "text": text[:300] + "..." if len(text) > 300 else text})
                        
        if not posts:
            links = soup.find_all("a", href=re.compile(r"linkedin\.com/posts/|linkedin\.com/feed/update/|urn:li:activity"))
            for link in links:
                url = link["href"].split("?")[0]
                container = link.find_parent("li") or link.find_parent("div", class_=re.compile(r"card|feed"))
                if container:
                    text = container.get_text(separator=" ", strip=True)
                    if text and len(text) > 50 and not any(p["link"] == url for p in posts):
                        posts.append({"link": url, "text": text[:300] + "..." if len(text) > 300 else text})

        with open("extracted_linkedin_posts.json", "w", encoding="utf-8") as f:
            json.dump(posts, f, indent=2)
            
        print(f"Extracted {len(posts)} posts and saved to extracted_linkedin_posts.json.")

if __name__ == "__main__":
    main()
