from destinations import Destinations

CONTINENT = ['  1) Asia',
             '  2) Africa',
             '  3) North America',
             '  4) South America',
             '  5) Europe',
             '  6) Oceania',
             '  7) Antarctica']

MONEY = ['  $$$) No object',
         '  $$) Spendable, so long as I get value from doing so',
         '  $) Extremely important; I want to spend as little as possible']

CRIME = ['  1) Low',
         '  2) Average',
         '  3) High']

KID_FRIENDLY = ['  1) Yes',
                '  2) No']

SEASON = ['  1) Spring',
          '  2) Summer',
          '  3) Autumn',
          '  4) Winter']

CLIMATE = ['  1) Cold',
           '  2) Cool',
           '  3) Moderate',
           '  4) Warm',
           '  5) Hot']


def main():
    """

    :return:
    """
    ask_username()

    continent = ask_continent()
    cost = ask_money()
    crime = ask_crime()
    kidfriendly = ask_kidfriendly()
    season = ask_season()
    climate = ask_climate()

    interests()

    sports = float(ask_interests_sports())
    wildlife = float(ask_interests_wildlife())
    nature = float(ask_interests_nature())
    historical = float(ask_interests_historical())
    cuisine = float(ask_interests_cuisine())
    adventure = float(ask_interests_adventure())
    beach = float(ask_interests_beach())

    # Get original data from .csv file

    

    new_destination = []

    final_destination={}

    # select destinations in the selected continent
    
    for select_continent in Destinations().get_all():
        if select_continent.get_continent() == continent:
            new_destination.append(select_continent)


    # select destinations match the user cost
   
    for money_select in new_destination:

        if len(money_select.get_cost()) <= len(cost):
            continue
        else:
            new_destination.remove(money_select)
    # select destinations with selected crime rate
    



    for crime_select in new_destination:
        if crime == "high":
            continue
        elif crime == "low" and crime_select.get_crime() != "low":
            new_destination.remove(crime_select)
        elif crime == "average" and crime_select.get_crime() == "high":
            new_destination.remove(crime_select)

    for kid_select in new_destination:
        if kidfriendly == "TRUE" and kid_select.is_kid_friendly() == "FALSE":
            new_destination.remove(kid_select)

    # select destinations with certain climate

    for climate_select in new_destination:
        if climate_select.get_climate() != climate:
            new_destination.remove(climate_select)

    highest_score = -9999
    highest_score_destination = None

    for destination in new_destination:

        _sports = sports * float(destination.get_interest_score('sports'))
        _wildlife = wildlife * float(destination.get_interest_score('wildlife'))
        _nature = nature * float(destination.get_interest_score('nature'))
        _historical = historical * float(destination.get_interest_score('historical'))
        _cuisine = cuisine * float(destination.get_interest_score('cuisine'))
        _adventure = adventure * float(destination.get_interest_score('adventure'))
        _beach = beach * float(destination.get_interest_score('beach'))

        interest_score = _sports + _wildlife + _nature + _historical + _cuisine + _adventure + _beach

        score = destination.get_season_factor(season) * interest_score
        
        if score > highest_score:
           highest_score = score
           highest_score_destination = destination.get_name()

    print("Thank you for answering all our questions. Your next travel destination is:")
    print(highest_score_destination)

# Questionare design

def ask_username():
    """
    Ask user name and display on the screen.

    """
    print('Welcome to Travel Inspiration!\n')

    ask_username = input('What is your name? ')

    print('\nHi, ' + ask_username + '!\n')


def ask_continent():
    """
    Ask user to choose the continent they want to go
    :return: string
    """
    print('Which continent would you like to travel to?')

    for continent in CONTINENT:
        print(continent)
    answer_continent = input('> ')
    print("")

    if answer_continent == "1":
        answer_continent = "asia"
    elif answer_continent == "2":
        answer_continent = "africa"
    elif answer_continent == "3":
        answer_continent = "north america"
    elif answer_continent == "4":
        answer_continent = "south america"
    elif answer_continent == "5":
        answer_continent = "europe"
    elif answer_continent == "6":
        answer_continent = "oceania"
    elif answer_continent == "7":
        answer_continent = "antarctica"
    else:
        print("I'm sorry, but", answer_continent, "is not a valid choice, Please try again.")
        answer_continent = ask_continent()

    return answer_continent
    

def ask_money():
    """
    Ask user to choose the cost they want to spend
    :return: string
    """
    print('What is money to you?')
    for money in MONEY:
        print(money)

    answer_money = input('> ')
    print("")

    if answer_money not in ["$", "$$", "$$$"]:
        print("I'm sorry, but", answer_money, "is not a valid choice, Please try again.")
        answer_money = ask_money()
    return answer_money
   

def ask_crime():
    """
    Ask user to choose the crime rate
    :return: string
    """
    print('How much crime is acceptable when you travel?')
    for crime in CRIME:
        print(crime)

    answer_crime = input('> ')
    print("")

    if answer_crime == "1":
        answer_crime = "low"
    elif answer_crime == "2":
        answer_crime = "average"
    elif answer_crime == "3":
        answer_crime = "high"
    else:
        print("I'm sorry, but", answer_crime, "is not a valid choice. Please try again.\n")
        answer_crime = ask_crime()

    return answer_crime
    

def ask_kidfriendly():
    """
    Ask user to choose if kid friendly or not
    :return: string
    """
    print('Will you be travelling with children?')

    for kidfriendly in KID_FRIENDLY:
        print(kidfriendly)

    answer_kidfriendly = input('> ')
    print("")


    if answer_kidfriendly == "1":
        answer_kidfriendly = "TRUE"
    elif answer_kidfriendly == "2":
        answer_kidfriendly = "FALSE"
    else:
        print("I'm sorry, but", answer_kidfriendly, "is not a valid choice, Please try again.")
        answer_kidfriendly = ask_kidfriendly()

    return answer_kidfriendly
  

def ask_season():
    """
    Ask user to choose the season they want
    :return: string
    """
    print('Which season do you plan to travel in?')
    for season in SEASON:
        print(season)

    answer_season = input('> ')
    print("")

    if answer_season == "1":
        answer_season = "spring"
    elif answer_season == "2":
        answer_season = "summer"
    elif answer_season == "3":
        answer_season = "autumn"
    elif answer_season == "4":
        answer_season = "winter"
    else:
        print("I'm sorry, but", answer_season, "is not a valid choice, Please try again.")
        answer_season = ask_season()

    return answer_season


def ask_climate():
    """
    Ask user to choose the climate
    :return: string
    """

    print('What climate do you prefer?')
    for climate in CLIMATE:
        print(climate)

    answer_climate = input('> ')
    print("")

    if answer_climate == "1":
        answer_climate = "cold"
    elif answer_climate == "2":
        answer_climate = "cool"
    elif answer_climate == "3":
        answer_climate = "moderate"
    elif answer_climate == "4":
        answer_climate = "warm"
    elif answer_climate == "5":
        answer_climate = "hot"
    else:
        print("I'm sorry, but", answer_climate, "is not a valid choice, Please try again.")
        answer_climate = ask_climate()

    return answer_climate


def interests():
    """
    A reminder to display the next section
    :return: None
    """
    print(
        "Now we would like to ask you some questions about your interests, on a scale of -5 to 5. -5 indicates strong dislike, whereas 5 indicates strong interest, and 0 indicates indifference."
    )
    print("")

def ask_interests_sports():
    """
    Ask user about the how they are interested in sports
    :return: string
    """
    print('How much do you like sports? (-5 to 5)')
    answer_interests_sports = input('> ')
    print("")
    if answer_interests_sports not in ["-1", "-2", "-3", "-4", "-5", "0", "1", "2", "3", "4", "5"]:
        print("I'm sorry, but", answer_interests_sports, "is not a valid choice, Please try again.")
        answer_interests_sports = ask_interests_sports()
    return answer_interests_sports


def ask_interests_wildlife():
    """
    Ask user about the how they are interested in wildlife
    :return: string
    """
    print('How much do you like wildlife? (-5 to 5)')
    answer_interests_wildlife = input('> ')
    print("")
    if answer_interests_wildlife not in ["-1", "-2", "-3", "-4", "-5", "0", "1", "2", "3", "4", "5"]:
        print("I'm sorry, but", answer_interests_wildlife, "is not a valid choice, Please try again.")
        answer_interests_wildlife = ask_interests_wildlife()
    return answer_interests_wildlife


def ask_interests_nature():
    """
    Ask user about the how they are interested in nature
    :return: string
    """
    print('How much do you like nature? (-5 to 5)')
    answer_interests_nature = input('> ')
    print("")
    if answer_interests_nature not in ["-1", "-2", "-3", "-4", "-5", "0", "1", "2", "3", "4", "5"]:
        print("I'm sorry, but", answer_interests_nature, "is not a valid choice, Please try again.")
        answer_interests_nature = ask_interests_nature()
    return answer_interests_nature


def ask_interests_historical():
    """
    Ask user about the how they are interested in historical
    :return: string
    """
    print('How much do you like historical sites? (-5 to 5)')
    answer_interests_historical = input('> ')
    print("")
   
    if answer_interests_historical not in ["-1", "-2", "-3", "-4", "-5", "0", "1", "2", "3", "4", "5"]:
        print("I'm sorry, but", answer_interests_historical, "is not a valid choice, Please try again.")
        answer_interests_historical = ask_interests_historical()
    return answer_interests_historical


def ask_interests_cuisine():
    """
    Ask user about the how they are interested in cuisine
    :return: string
    """
    print('How much do you like fine dining? (-5 to 5)')
    answer_interests_cuisine = input('> ')
    print("")
    if answer_interests_cuisine not in ["-1", "-2", "-3", "-4", "-5", "0", "1", "2", "3", "4", "5"]:
        print("I'm sorry, but", answer_interests_cuisine, "is not a valid choice, Please try again.")
        answer_interests_cuisine = ask_interests_cuisine()
    return answer_interests_cuisine


def ask_interests_adventure():
    """
    Ask user about the how they are interested in adventure
    :return: string
    """
    print('How much do you like adventure activities? (-5 to 5)')
    answer_interests_adventure = input('> ')
    print("")
    if answer_interests_adventure not in ["-1", "-2", "-3", "-4", "-5", "0", "1", "2", "3", "4", "5"]:
        print("I'm sorry, but", answer_interests_adventure, "is not a valid choice, Please try again.")
        answer_interests_adventure = ask_interests_adventure()
    return answer_interests_adventure


def ask_interests_beach():
    """
    Ask user about the how they are interested in beach
    :return: string
    """
    print('How much do you like the beach? (-5 to 5)')
    answer_interests_beach = input('> ')
    print("")
    if answer_interests_beach not in ["-1", "-2", "-3", "-4", "-5", "0", "1", "2", "3", "4", "5"]:
        print("I'm sorry, but", answer_interests_beach, "is not a valid choice, Please try again.")
        answer_interests_beach = ask_interests_beach()
    return answer_interests_beach


if __name__ == "__main__":
    main()
