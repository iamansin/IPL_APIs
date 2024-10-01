import pandas as pd 
import numpy as np
ipl = pd.read_csv('IPL_DATA.csv')

def Teams_API():
    Teams = list((pd.concat([ipl['Team1'], ipl['Team2']])).unique())
    Teams_dict = {
        'Teams': Teams
    }
    return Teams_dict


def Versus_API(Team1,Team2):
  Versus_data = ipl[((ipl['Team1'] == Team1 ) & (ipl['Team2'] == Team2)) | ((ipl['Team1'] == Team2) & (ipl['Team2'] == Team1))]
  total_matches = Versus_data.shape[0]
  Won_by_Team1 = Versus_data[Versus_data['WinningTeam'] == Team1].shape[0]
  Won_by_Team2 = Versus_data[Versus_data['WinningTeam'] == Team2].shape[0]
  Draw = total_matches - (Won_by_Team1 + Won_by_Team2)  
  Matches_dict = {
      'Total_matches':total_matches,
      Team1:Won_by_Team1,
      Team2:Won_by_Team2,
      'Draw':Draw
  }
  return Matches_dict

print(Teams_API())