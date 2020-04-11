from bs4 import BeautifulSoup
from selenium import webdriver
from requests import get
from time import sleep
import xlsxwriter

search = input("Wonach soll ich suchen ")
filename = input("Wie soll die Excel heißen: ")
pages = int(input("Wie viele Seiten soll ich durchsuchen: "))

driver = webdriver.Chrome(executable_path=r"C:\Users\dross\Documents\GitHub\PyTh0n\chromedriver.exe")

driver.maximize_window()
driver.get("https://www.spreadshirt.de/")

driver.find_element_by_xpath("//input[@id='header-search-input']").send_keys(f"{search}")
input("Sind wir soweit? ")
driver.find_element_by_xpath("//div[@id='header-search-submit']").click()
sleep(2)

pagesscrapped = 1

alldescriptions = []
alltags = []

newlink = driver.current_url

while (pagesscrapped<=pages):
    sleep(4)
    
    try:
        driver.execute_script("document.getElementsByClassName('promo-popup__close lightbox__close js-promo-layer-close')[0].click();")
    except:
        pass
    
    try:
        soup = BeautifulSoup(driver.page_source, "html.parser")
        alllinks = []
        allcards = soup.find("div", id="articleTileList")
        for alllinksinallcards in allcards.find_all("a", class_="article thumb-font", href=True):
            alllinks.append(f"https:{alllinksinallcards['href']}")

        for i in range(len(alllinks)):
            soup(3)
            req = get(alllinks[i])
            soup = BeautifulSoup(req.text, "html.parser")
            all = soup.find("div", id="design-info")
            description = all.find("div", class_="designer-info__description").get_text()
            tags = all.find("div", class_="designer-info__tags small-font").get_text()
            alldescriptions.append(description)
            alltags.append(tags)
            print(description)
            print(tags)
        
    except:
        alldescriptions.append("No description")
        alltags.append("No tags")
    
    pagesscrapped += 1

    driver.get(f"{newlink}?page={pagesscrapped}")



workBook = xlsxwriter.Workbook(f"{filename}.xlsx")
workSheet = workBook.add_worksheet()

for j in range(len(alldescriptions)):
    workSheet.write(j, 0, alldescriptions[j])
    workSheet.write(j, 1, alltags[j])

workBook.close()
driver.quit()

input("Press enter to exit...")
