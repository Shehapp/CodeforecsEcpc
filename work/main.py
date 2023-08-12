import requests
from bs4 import BeautifulSoup
import get_all_users_from_codeforces,get_all_teams_from_codeforces
import save_data,get_data
import csv


#948

# read data from csv file
get_user = get_data.read_data()

# # get data take a lot of time
# users = get_all_users_from_codeforces.get_all_users("https://codeforces.com/ratings/organization/336",4)
# get_user = get_all_teams_from_codeforces.get_teams(users)
# save_data.write_data(get_user)

while True:
    name = str(input("enter a team: "))
    try:
        print(get_user[name])
    except:
        print("Not Found")