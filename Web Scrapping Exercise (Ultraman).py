# from site:
#     http://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/


# Output : [{"Ultraman": {"Ultraman": {"01": "Ultraman........


# Export to JSON

# email:
#     khumaeni@purwadhika.com

import requests
from bs4 import BeautifulSoup
import json

web = requests.get('http://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/')

Out = BeautifulSoup(web.content, 'html.parser')

list1=[]
for name in Out.find_all('strong'):
    list1.append(name.text)
    
list1=list1[2:110]
ultraman=list1[:34]
monster=list1[35:]

ultraman1=[] #Buat 1 list kosong untuk menyimpan data-data ultraman
for i in ultraman: #Buat looping untuk memecah string berdasarkan spasi sebanyak 1 spasi
    ultraman1.append(i.split(' ',1))
ultraman1= {i[0]:i[1] for i in ultraman1} #Kita format tampilannya
Dict_Ultraman={'Ultraman':ultraman1} #Buat dictionary yang berisi list ultraman

monster1=[] #Buat 1 list kosong untuk menyimpan data-data monster
for i in monster: #Buat looping untuk memecah string berdasarkan spasi sebanyak 1 spasi
    monster1.append(i.split(' ',1))
monster1= {i[0]:i[1] for i in monster1} #Kita format tampilannya
Dict_Monster={'Monster':monster1} #Buat dictionary yang berisi list monster

Data_final=[{'Ultraman':Dict_Ultraman,
            'Monster':Dict_Monster}]
# print(Data_final)


'''Save to json file'''
import json
# with open('Ultraman ft Monster.json','w') as file:
#     json.dump(Data_final,file)
# print ('Data saved')


'''Open json file'''
with open('Ultraman ft Monster.json', 'r') as file:
    out=json.load(file)
print(out)
print('Data Loaded')
