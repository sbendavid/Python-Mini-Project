import time
import requests
from bs4 import BeautifulSoup


URL = input("Copy and paste the url you want to scrap: ")
response = requests.get(URL)

forbes_html = response.text
soup = BeautifulSoup(forbes_html, "html.parser")

time.sleep(30)
print(soup.prettify())

# print(soup.find("div", class_="Table_finalWorth__UZA6k"))

# with open("forbes.csv", "a") as file:
#     file.write("Rank, Name, NetWorth, Industry\n")
#     for i, article in enumerate(soup.find_all("div", class_="Table_tableRow__lF_cY"), 1):
#         rank = i
#         name = article.find("div", class_="Table_personName__Bus2E").text
#         net_worth = article.find("div", class_="Table_finalWorth__UZA6k").text
#         date = article.find("span", class_="c-byline__date").text
#         file.write(f"{rank},{name},{net_worth},{date}\n")

# if __name__ == "__main__":
#     main()