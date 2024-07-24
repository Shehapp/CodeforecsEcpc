import requests
from bs4 import BeautifulSoup
import get_all_users_from_codeforces, get_all_teams_from_codeforces, get_teams_from_ecpc
import save_data, get_data
import csv
import time


# 1109

def scrap_teams(url, page):
    start = time.time()
    users = get_all_users_from_codeforces.get_all_users(url, page)
    get_user = get_all_teams_from_codeforces.get_teams(users)
    save_data.write_data(get_user)
    # end timer
    end = time.time()
    print(end - start)

    return get_user


# read data from csv file
get_user = get_data.read_data()

# get data take a lot of time
# get_user = scrap_teams("https://codeforces.com/ratings/organization/336", 4)


ecpc_teams = get_teams_from_ecpc.get_ecpc_teams("https://scoreboard.acpc.global/ecpc2024/Ain%20Shams%20University%20"
                                                "-%20Faculty%20of%20Computer%20and%20Information%20Sciences.html", 11)



found = 0
for i in ecpc_teams:
    print(i[0]+" : ", end="")
    try:
        print(get_user[i[0].lower()])
        found += 1
    except:
        print("Not Found")

print("percentage of found teams: ", found/len(ecpc_teams) * 100, "%" )
