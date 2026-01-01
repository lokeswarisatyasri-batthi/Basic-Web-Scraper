import requests
from bs4 import BeautifulSoup

print("Fetching latest news headlines...\n")

try:
    url = "https://www.bbc.com/news"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to retrieve the webpage.")
    else:
        soup = BeautifulSoup(response.text, "html.parser")

        headlines = soup.find_all("h2")

        if not headlines:
            print("No headlines found.")
        else:
            print("Top News Headlines:\n")
            count = 1
            for headline in headlines[:10]:
                text = headline.get_text().strip()
                if text:
                    print(f"{count}. {text}")
                    count += 1

except requests.exceptions.RequestException:
    print("Network error. Please check your internet connection.")

except Exception as e:
    print("An unexpected error occurred:", e)

