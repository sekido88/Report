import requests
import pandas as pd
from bs4 import BeautifulSoup
def function (url) : 
  
    page = requests.get(url) 
    soup = BeautifulSoup(page.text , "html.parser")
    title = soup.find_all('div',{'class' : 'info'})
    arr_titles = []
    arr_prices = []
    mer = []
    for i in title :
        if (i.a) :
            arr_tmp = []
            arr_tmp.append(i.a.get('title'))
            arr_tmp.append(i.strong.text )
            mer.append(arr_tmp)  
    columns = ['Name' , 'Price']
    excel = pd.DataFrame(mer,columns = columns)
    excel.to_excel('data.xlsx', index=False)
    print(excel)
url = "https://hoanghamobile.com/dien-thoai-di-dong?p=5#page_5"
function(url)
