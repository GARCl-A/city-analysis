"""
Using Wyscout 
=====================

Getting familiar with Wyscout data
"""
#importing necessary libraries
import pathlib
import os
import pandas as pd
import json


##############################################################################
# Competition data
# ----------------------------
# In this dataframe you will find information about the id of a competition and available competitions.
# If you are trying it locally, comment  ..... active lines (put # in front lines path = ...) and comment out (delete #).

#path to data
path = os.path.join(str(pathlib.Path().resolve()), 'data', 'Wyscout', 'competitions.json') # put # in front if used locally
#path = os.path.join(str(pathlib.Path().resolve()), 'Wyscout', 'competitions.json') # delete #

#open data 
with open(path) as f:
    data = json.load(f)
    #save it in dataframe 
df_competitions = pd.DataFrame(data)
#structure of data
df_competitions.info()


##############################################################################
# Match data
# ----------------------------
# In this dataframe you can find information about all games that were played in Premier League 2017/18 season.
# *wyId* is the unique id in the Wyscout database. 

#path to data 
path = os.path.join(str(pathlib.Path().resolve()), 'data', 'Wyscout', 'matches_England.json') # put # in front if used locally
#path = os.path.join(str(pathlib.Path().resolve()), 'data', 'Wyscout', 'matches_England.json') # delete #
with open(path) as f:
    data = json.load(f)
#save it in a dataframe  
df_matches = pd.DataFrame(data)
#structure of data
df_matches.info()


##############################################################################
# Player data
# ----------------------------
# In this dataframe you can find information about all players available for Wyscout public dataset. *wyId* is 
# the player id in the Wyscout database. In the *currentTeamId* you can find the id of a team that the player plays form.
# *shortName* is an important column for vizualisations and rankings since player's name is written in a shorter way.

#path to data
path = os.path.join(str(pathlib.Path().resolve()), 'data', 'Wyscout', 'players.json') # put # in front if used locally
#path = os.path.join(str(pathlib.Path().resolve()), 'data', 'Wyscout', 'players.json')  
#open data
with open(path) as f:
    data = json.load(f)
#save it in a dataframe  
df_players = pd.DataFrame(data)
#structure of data
df_players.info()


##############################################################################
# Event data
# ----------------------------
# In this dataframe you can find information about all events that occured in all the games during 2017/18 Premier League
# season. *matchId* matches the wyId from *df_matches*, *playerId* matches *wyId* from *df_players*.*tags* provide information on additional characteristics of an event, for example
# if the pass was accurate. The location on the pass can be found in *positions*, but remeber, that the data are collected
# on 100x100 square with reverted y-axis. In the *eventName* you will find the basic name of an event, whereas *subEventName*
# provide more information. *eventSec* is the time of an event.
# 
# If you want to learn more about Wyscout data, you can explore 
# `WyScout API <https://apidocs.wyscout.com/>`_, but remember to switch the version to 2.0 at the top of the page.
# 
# This code is adjusted to the webpage with file size limit. If you want to open the data that is stored in the working
# directory, comment (put '#') before the following code and comment out the lines below them (delete '#').

#prepare empty dataframe
df_events = pd.DataFrame() # put # in front if used locally
for i in range(13): # put # in front if used locally
    #get file name and path to it
    file_name = 'events_England_' + str(i+1) + '.json' # put # in front if used locally
    path = os.path.join(str(pathlib.Path().resolve()), 'data', 'Wyscout', file_name) # put # in front if used locally
    #open data
    with open(path) as f: # put # in front if used locally
        data = json.load(f) # put # in front if used locally
    #append data to the dataframe
    df_events = pd.concat([df_events, pd.DataFrame(data)]) # put # in front if used locally


#path = os.path.join(str(pathlib.Path().resolve()), 'Wyscout', 'events_England_.json') # delete #
#with open(path) as f: # delete #
    #data = json.load(f) # delete #
#df_events = pd.DataFrame(data) # delete #

#structure of data
df_events.info()


##############################################################################
# Before you start
# ----------------------------
# Run these lines in Spyder/Jupyter notebook and explore dataframes 
# to get more familiar before you start working on the course.