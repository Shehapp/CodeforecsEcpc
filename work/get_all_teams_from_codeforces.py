import requests
from bs4 import BeautifulSoup
import get_all_users_from_codeforces,get_all_teams_from_codeforces
import save_data,get_data
import csv

get_user = {}

def get_teams(users):
    for i in range(len(users)):
        get_team(users[i])
    return get_user

def get_team(name):
    page = requests.get(f"https://codeforces.com/teams/with/{name}")
    src = page.content
    soup = BeautifulSoup(src, 'lxml')
    table = soup.find_all('div', {'class': 'datatable'})
    table = table[0].find_all('tr')
    table = table[1:]
    for i in range(len(table)):
        table[i] = table[i].find_all('td')
        table[i] = [table[i][0].text]
        table[i][0] = table[i][0].strip()


    for i in range(len(table)):
        get_user[table[i][0].lower()] = name
