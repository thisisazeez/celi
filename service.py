import pygsheets
import time
import requests
from bs4 import BeautifulSoup
gc = pygsheets.authorize(service_file='./google-credentials.json')


#Opening Spreadsheet
sh = gc.open('Python_Project')

wks1 = sh.worksheet_by_title('Test')
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
            # time.sleep(20)
    

    #Scraping things
    # url  = 'https://oddsportal.com'

    # Get all the values from the worksheet
    data = wks1.get_all_values()

    # Extract the league name from the first row
    league_name = data[1][0]
    country = data[0][0]

    # Construct the URL for the league's page on the website
    url = f"https://www.oddsportal.com/football/{country}/{league_name}/"

    # Use requests to check if the page exists
    response = requests.get(url)

    if response.status_code == 404:
        print(f"Page not found for league {league_name}")
    else:
        # If the page exists, use BeautifulSoup to scrape the page and extract the odds data
        soup = BeautifulSoup(response.content, 'html.parser')

        home_odds = soup.find('div', {'class': 'table-container'}).find_all('tr')[1].find_all('td')[2].text
        away_odds = soup.find('div', {'class': 'table-container'}).find_all('tr')[1].find_all('td')[3].text

