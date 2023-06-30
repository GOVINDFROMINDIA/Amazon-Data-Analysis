import requests
from bs4 import BeautifulSoup

# URL of the Amazon product reviews page
url = "https://www.amazon.in/Apple-iPhone-128GB-Space-Black/product-reviews/B0BDJ22G36/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
elements = soup.find_all(class_="a-fixed-right-grid-col a-col-left")
text_content = [element.get_text(strip=True) for element in elements]
with open("reviews1.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(text_content))

print("Reviews saved to 'reviews1.txt'.")
