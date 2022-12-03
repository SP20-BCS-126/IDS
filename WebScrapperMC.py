import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='E:/Docs/PythonPJs/WebScrap SP20-BCS-126/chromedriver.exe')
driver.get('http://www.metacritic.com/browse/games/release-date/available/pc/metascore')
results = []
score_results = []
content = driver.page_source
soup = BeautifulSoup(content)
driver.quit()


for n in soup.findAll(attrs='clamp-summary-wrap'):
    name = n.find("a", class_="title")
    if name not in results:
        results.append(name.text)

for s in soup.findAll(attrs='clamp-summary-wrap'):
    score = n.find("div", class_="metascore_w large game positive")
    if score not in results:
        score_results=score.text


df = pd.DataFrame({'Names': results,'MetaScores': score_results})
df.to_csv('MetaCriticScraper.csv', index=False, encoding='utf-8')