import requests
from bs4 import BeautifulSoup
import get_all_users_from_codeforces,get_all_teams_from_codeforces
import save_data,get_data
import csv


def get_all_users(url,pages):
    users = []
    # FCIS Ain Shams University, 614  page [1 :4]
    for i in range(1, pages+1):

        page = requests.get(f"{url}/page/{i}")

        src = page.content
        soup = BeautifulSoup(src, 'lxml')
        table = soup.find_all('div', {'class': 'datatable'})
        table = table[0].find_all('tr')
        table = table[1:]


        for i in range(len(table)):
            table[i] = table[i].find_all('td')
            table[i] = [table[i][1].text]
            users.append(table[i][0].strip())

    return users

