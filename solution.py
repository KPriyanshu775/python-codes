from bs4 import BeautifulSoup
from urllib.request import urlopen

doc_url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
html = urlopen(doc_url).read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

grid_data = {}
max_x, max_y = 0, 0
for tr in soup.find_all("tr")[1:]:
    tds = [td.get_text(strip=True) for td in tr.find_all("td")]
    if len(tds) == 3:
        x, char, y = int(tds[0]), tds, int(tds[2])
        grid_data[(x, y)] = char
        max_x = max(max_x, x)
        max_y = max(max_y, y)

for y in range(max_y + 1):
    print("".join(grid_data.get((x, y), " ") for x in range(max_x + 1)))


    