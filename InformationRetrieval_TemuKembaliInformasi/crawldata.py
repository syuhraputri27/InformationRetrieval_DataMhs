import requests
from bs4 import BeautifulSoup
from csv import writer

with open('crawlDataMhs.csv', 'w', encoding='utf8', newline= '') as f:
    thewriter = writer(f)
    header = ['Nama','NIM','Organisasi/UKM & Periode','Foto']
    thewriter.writerow(header)

    nim = ['A11.2020.12457','A11.2020.12590','A15.2020.01760','A11.2020.12720','A11.2020.12953','A15.2021.02136','A11.2021.13249','A15.2021.01986','A11.2021.13462',
       'A11.2020.12460','A14.2020.03420','A15.2021.02040','A11.2021.13252','A15.2021.02021','A11.2020.12417','A11.2021.13221','A11.2020.12490','A11.2021.13909',
       'A11.2021.13676','A11.2021.13579','A14.2020.03323','A14.2020.03494','A14.2020.03552','A11.2021.13498','A11.2020.12770','A15.2021.02239','A15.2020.01815',
       'A15.2021.02005','A11.2021.13250','A12.2020.06531','A22.2021.02875','A14.2020.03589','A11.2019.11827','B11.2020.06653','A11.2020.12444','A12.2020.06538',
       'A11.2020.12468','A12.2020.06372','A14.2020.03403','A15.2020.01890','A12.2020.06535','A11.2019.11725','A15.2020.01903'] 

    idx = 0
    while idx < len(nim) :
        url = 'https://dinus.ac.id/mahasiswa/{}'.format(nim[idx])
        #print(url)

        #membuat request
        r = requests.get(url)
        #hasil response
        request = r.content

        soup=BeautifulSoup(request, 'html.parser')

        #extract element
        nama = soup.find('table',attrs={'class':'table'}).find('td',{'style' : None}).get_text().replace('\n',' ')
        org = soup.find('div',attrs={'class':'row organisasi'}).find('tbody').get_text().replace('\n',' ').replace('  1','').replace('  2',',').replace('  3',',').replace('  4',',').replace('  5',',').replace('  6',',').replace('  7',',')
        foto = soup.find('a',attrs={'class':'fotonews'}).find('img')
        
        #lower case
        namaL = nama.lower()
        orgL = org.lower()

        data = [namaL,nim[idx],orgL,foto['src']]
        thewriter.writerow(data)

        # data = [nama,nim[idx],org,foto['src']]
        # thewriter.writerow(data)

        idx = idx + 1