import requests
from bs4 import BeautifulSoup
from random import randint
from time import sleep

file = open('Swoop.csv', 'w+', encoding='utf-8_sig')
header = "კომპანია,მომსახურეობა,ფასი,ლინკი\n"
file.write(header)
page = 1
while page < 6:
    link = 'https://www.swoop.ge/category/23/?page='+str(page)
    r = requests.get(link)
    content = r.text
    soup = BeautifulSoup(content,'html.parser')
    block = soup.find('div',{'class':'items'})
    movies = block.find_all('div',{'class':'special-offer'})
    for each in movies:
        company = each.find('div',{'class':'special-offer-title'}).text.strip()
        price = each.find('div',{'class':'special-offer-installment'}).text.strip().split()[0]
        text = each.find('div',{'class':'special-offer-text'}).text.strip()
        link = 'https://www.swoop.ge'+each.a['href']
        file.write(company+','+text+','+price+','+link+'\n')
    page += 1
    sleep(randint(15,20))

###ჩემს პროგრამას სილამაზის სექციიდან მოაქვს 5 გვერდიდან ინფორმაცია





