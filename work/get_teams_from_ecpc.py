
import requests
from bs4 import BeautifulSoup





def get_ecpc_teams(url,remove_last):
        page = requests.get(url)
        src = page.content
        soup = BeautifulSoup(src, 'lxml')
        table = soup.find_all('table')
        table = table[2].find_all('tr')
        table = table[2:]
        # print(table)
        teams = []
        print("\n")
        for i in range(0,len(table)-3):
            table[i] = table[i].find_all('td')
            # ex erase from end this " (CU-FCAI)"
            table[i] = [table[i][1].text[:-remove_last]]
            teams.append(table[i])

        return teams
