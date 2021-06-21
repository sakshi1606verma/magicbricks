import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.magicbricks.com/2-bhk-flats-for-rent-in-bangalore-pppfr'

def base(url):
    response = requests.get(url)
    htmlcontent = response.content
    soup = BeautifulSoup(htmlcontent,"html.parser")
    return soup

apartments = []
society = []
price = []
tenants_preferred = []
floor = []
furnishing = []
bathrooms = []
owner = []

def AllApartments(soup):

    for a in soup.findAll('div', attrs={'class':'flex relative clearfix m-srp-card__container'}): 
        name=a.find('div',attrs={'class':'m-srp-card__desc flex__item'})
        #<<top>>
        title = name.find('div',attrs={'class':'m-srp-card__heading clearfix'})
        heading = title.find('h2')
        spann = heading.find('span',attrs={'class':'m-srp-card__title'})
        apartment = spann.find('span',attrs={'class':'m-srp-card__title__bhk'})
        apartments.append((apartment.text).strip())
        string = ' '.join((spann.text).split())
        i = string.index('in')
        society.append(string[i+2:])
        # <<between>>
        para = name.find('div',attrs={'class':'m-srp-card__collapse js-collapse'})
        para2 = para.find('div',attrs={'class':'m-srp-card__summary js-collapse__content'})

        for para21 in para2.findAll('div',attrs={'class':'m-srp-card__summary__item'}):
            hed = para21.find('div',attrs={'class':'m-srp-card__summary__title'})
            for para22 in para21.findAll('div',attrs={'class':'m-srp-card__summary__info'}):
                if hed.text == 'floor':
                    floor.append((para22.text).strip())
                if hed.text == 'furnishing':
                    furnishing.append((para22.text).strip())
                if hed.text == 'tenants preferred':
                    tenants_preferred.append((para22.text).strip())
                if hed.text == 'bathroom':
                    bathrooms.append((para22.text).strip())
        
        # <<price>>
        price_div=a.find('div',attrs={'class':'m-srp-card__info flex__item'})
        amount = price_div.find('div',attrs={'class':'m-srp-card__price'})
        if amount is not None:
            price.append(' '.join((amount.text).split()))
        else:
            price.append('NIL')
        # <<owner>>
        adname = a.find('div',attrs={'class':'m-srp-card__advertiser__name'})
        owner.append(adname.text)

  
soup = base(url)
AllApartments(soup)
for i in range(2,6):
    url = 'https://www.magicbricks.com/2-bhk-flats-for-rent-in-bangalore-pppfr' + '/page-'+str(i)
    print(url)
    soup = base(url)
    AllApartments(soup)
df = pd.DataFrame({'Apartment':apartments,'Address/Area':society, 'Price':price,'Furnishing':furnishing,'Tenants Preferred':tenants_preferred,'Owner Name':owner})
print(df)

df.to_excel("new1.xlsx", sheet_name='Sheet1')

apartments = []
society = []
price = []
tenants_preferred = []
floor = []
furnishing = []
bathrooms = []
owner = []


url = 'https://www.magicbricks.com/property-for-rent/residential-real-estate?bedroom=2,3,4&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Bangalore'
soup = base(url)
AllApartments(soup)
for i in range(2,3):
    url = 'https://www.magicbricks.com/2-bhk-flats-for-rent-in-bangalore-pppfr' + '/page-'+str(i)
    print(url)
    soup = base(url)
    AllApartments(soup)

df = pd.DataFrame({'Apartment':apartments,'Address/Area':society, 'Price':price,'Furnishing':furnishing,'Tenants Preferred':tenants_preferred,'Owner Name':owner})
print(df)

df.to_excel('new2.xlsx', sheet_name='Sheet1')




 
    


