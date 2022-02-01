from bs4 import BeautifulSoup
from requests_html import HTMLSession
import pandas as pd

def shopping_data(url):

    from requests_html import HTMLSession
    session = HTMLSession()
    data_list = []
    
    for number in range(1,5):
       loop_url = url + "&tbs=vw:d,ss:44&tbm=shop&start="+str(number - 1) *60
       r = session.get(loop_url)
       r.html.render(sleep=5, timeout=5000)
       soup = BeautifulSoup(r.html.html, 'html.parser')
       sp_data = soup.findAll('div', class_='sh-dgr__content')
       for data in sp_data:
            title = data.find('h4', class_='Xjkr3b')
            title = title.text
            price = data.find('span', class_='a8Pemb OFFNJ')
            price = price.text
            supplier = data.find('div', class_='aULzUe IuHnof')
            supplier = supplier.text
            data_results = {
                "Title": title,
                "Price": price,
                "Supplier": supplier,
            }
            data_list.append(data_results)
    return data_list

def results(data_list):
    dataResult = pd.DataFrame(data_list)
    dataResult.to_csv('google_shopping_v1.csv', index=False)
    print('done')


search = 'illuma'
url = f"https://www.google.com/search?q={search}"
data = shopping_data(url)
Result = results(data)
