import pygsheets
import time
import requests
from bs4 import BeautifulSoup
gc = pygsheets.authorize(service_file='./google-credentials.json')


#Opening Spreadsheet
sh = gc.open('Python_Project')

wks1 = sh.worksheet_by_title('Feeds')
wks2 = sh.worksheet_by_title('From')
wks3 = sh.worksheet_by_title('To')


if __name__ == '__main__':
    home_and_away = wks1.get_all_values()

    league_name = home_and_away[0][0]

    away_team_col = home_and_away[0].index('Away Team')

    home_team_col = home_and_away[0].index('Home Team')

    home_team = home_and_away[1][home_team_col]
    away_team = home_and_away[1][away_team_col]
    print(home_team)

    for i, row in enumerate(wks2.get_all_values()):
        if row[0] == home_team and row[1] == away_team:
            home_data = wks2.get_col(i+1)
            away_data = wks2.get_col(i+2)
            time.sleep(20)
    

    #Scraping things
    # url  = 'https://oddsportal.com'
