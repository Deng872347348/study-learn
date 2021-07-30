import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

i = 1

while i >= 1:
    url = "https://store.steampowered.com/search/?filter=globaltopsellers&page=" + str(i) + "&os=win"
    s = requests.session()
    res = s.get(url).text
    soup = BeautifulSoup(res, "html.parser")
    contents = soup.find(id="search_result_container").find_all('a')

    for content in contents:
        try:
            gamename = content.find(class_="title").string.strip()
            date = content.find("div", class_="col search_released responsive_secondrow").string.strip()
            price = content.find("div", class_="col search_price responsive_secondrow").string.strip()
            img_src = content.find("div", class_="col search_capsule").find('img').get("src")
            href = content.get("href")
            title =[gamename, href, date, price, img_src]
            ws.append(title)
            print(title)
            #print(gamename, href, date, price, img_src)
        except :
           print('error')

    i = i + 1
    wb.save("Steam热销.xlsx")
