from bs4 import BeautifulSoup
import openpyxl
import requests

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Tech News'
headers = ['Headline','Link','Source','Time']
sheet.append(headers)

source = requests.get('https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGRqTVhZU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen')
source.raise_for_status()
soup = BeautifulSoup(source.text,'html.parser')

tag1 = soup.find('div',class_='T4LgNb').find('div',class_='fe4pJf')
tag2 = tag1.find('div',class_='lBwEZb BL5WZb GndZbb')
for tag3 in tag2.findAll('div',jscontroller="MRcHif"):
    Headline = tag3.find('h3').text
    rawlink = tag3.find('a',href = True)['href'].split('.')[1]
    link = "https://news.google.com"+rawlink
    Source = tag3.find('div',class_='QmrVtf RD0gLb kybdz').find('a',class_='wEwyrc AVN2gc uQIVzc Sksgp').text
    time = tag3.find('div',class_='QmrVtf RD0gLb kybdz').find('time',class_='WW6dff uQIVzc Sksgp').text
    print (Headline,link,Source,time)
    list=[Headline,link,Source,time]
    sheet.append(list)

excel.save('GoogleTechNews.xlsx')
file = pd.read_excel('GoogleTechNews.xlsx',sheet_name='Tech News',usecols='A:C')
file.to_html("GoogleTechNews.html",index=False)

