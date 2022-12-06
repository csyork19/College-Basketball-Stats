import re
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Retrieve List of conferences from site
# Prompt user to select conference, and then list schools in the conference
# Prompt user to select school, and then list the roster for that school
# Prompt user to select player, and then list player statistics

# Return list of college basket ball conferences 
def get_conferences():
    conference_url = "https://www.sports-reference.com/cbb/conferences/"
    response = requests.get(conference_url).text
    soup = BeautifulSoup(response, 'html.parser')

    # Retrieve table that holds conferences and get conference names
    results = soup.find("table")
    conferences = results.find_all('a')
    list_of_conferences = []
    for row in conferences:
        list_of_conferences.append(row.text)

    print(list_of_conferences)

# Return list of teams in a single conference
# Parameter: Conference Name
# the team url is conference abr + year: /acc/2023.html
def get_team():
    team_url = "https://www.sports-reference.com/cbb/conferences/acc/2023.html"
    # team_url = "https://www.sports-reference.com/cbb/conferences/+ str(team_abbreviation) + /2023.html"
    response = requests.get(team_url).text
    soup = BeautifulSoup(response, 'html.parser')

    results = soup.find("table", attrs={'id':'standings'})
    teams = results.find_all('a')
    list_of_teams_rows = []
    list_of_teams = []
    row_num = 1
    for row in teams:
        list_of_teams.append(str(row.text))
        list_of_teams_rows.append(str(row_num) + str(row.text))
        row_num = row_num + 1
    
    print("Printing out list of teams")
    print(list_of_teams)

    num_of_teams = len(list_of_teams)



    # Prompt user to select team and get the int value of the string
    user_selection = input("Please select which team roster you want to view. \nEnter the numberic value.\n")
    converted_num = int(user_selection)

    # Get the value at index - 1 in the list of team
    user_team_selection = list_of_teams[converted_num - 1]
    print("User selected: " + str(user_team_selection))

    # add that to the url and then print html of players
    roster_url = "https://www.sports-reference.com/cbb/schools/" + str(user_team_selection).lower() + "/2023.html"
    print(roster_url)
    response_roster = requests.get(roster_url).text
    soup_roster = BeautifulSoup(response_roster, 'html.parser')
    #print(soup_roster)
    results_roster = soup_roster.find_all(id="roster")
    print(results_roster)

    column_names = ["Player", "#", "Class", "Pos", "Height", "Weight", "Hometown", "HighSchool", "Summary"]





get_team()
#get_conferences()
