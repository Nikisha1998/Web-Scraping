import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.imdb.com/chart/top/"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
print("Status Code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

movies = []
# Select all h3 titles with the new class
rows = soup.select("h3.ipc-title__text.ipc-title__text--reduced")

for row in rows:
    title = row.get_text(strip=True)

    # Skip the header row if it appears as "IMDb Top 250 Movies"
    if "IMDb Top 250" in title:
        continue

    movies.append({"Title": title})

# Save CSV
df = pd.DataFrame(movies)
df.to_csv("imdb_top_movies.csv", index=False, encoding="utf-8")
print(f"Scraped {len(df)} movies!")
