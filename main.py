import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import threading
import time

MAX_THREADS = 50
PAUSE_TIME = 1
BASE_URL = "https://facebook.com"
MAX_URLS_PER_FILE = 1000

urls_set = set()
urls_list = []
urls_lock = threading.Lock()
file_lock = threading.Lock()

def scrape(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            for link in soup.find_all("a", href=True):
                href = link.get("href")
                if href.startswith("http"):
                    parsed_url = urlparse(href)
                    if parsed_url.netloc == "facebook.com":
                        continue
                    with urls_lock:
                        if href not in urls_set:
                            urls_set.add(href)
                            urls_list.append(href)
                            if len(urls_list) >= MAX_URLS_PER_FILE:
                                write_urls_to_file()
    except Exception as e:
        print(f"Error scraping {url}: {e}")

def write_urls_to_file():
    with file_lock:
        with open("urls.txt", "a") as f:
            for url in urls_list:
                f.write(url + "\n")
        urls_list.clear()

def process_urls():
    while True:
        with urls_lock:
            if urls_list:
                url = urls_list.pop(0)
                scrape(url)
            elif all(t.finished for t in threads):
                write_urls_to_file()
                break
        time.sleep(PAUSE_TIME)

threads = []
for _ in range(MAX_THREADS):
    t = threading.Thread(target=process_urls)
    t.start()
    threads.append(t)

scrape(BASE_URL)

for t in threads:
    t.join()

write_urls_to_file()
