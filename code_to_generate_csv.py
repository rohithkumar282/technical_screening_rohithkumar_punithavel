'''
Program Description : Generate a .csv file with data from records.log file
Input :
     records.log file
Output :
     records_csv.csv file

Author: Rohith Kumar Punithavel, rpunitha@asu.edu
'''

#import packages
import pandas as pd
import json
import os

#current directory of log file
current_directory = os.getcwd()
file_directory = current_directory+'/records.log'

#check if file exists or not
if os.path.isfile(file_directory):
  #read log file by line
  log_file = open(file_directory,'r').readlines()

  #create a dataframe with order_id,weight (lbs),volume (in3) as header
  df = pd.DataFrame(columns=['order_id','weight (lbs)','volume (in3)'])

  #process data from .log file
  for data in log_file:
    data = data.replace('\'','\"')
    temp = json.loads(data)
    weight = temp['package']['weight']
    volume  = temp['package']['volume']
    if temp['package']['imperial_unit']=='false':
      weight = round(2.20462*weight,3)
      volume = round(volume/16.387,3)
    df = df.append({'order_id': temp['order_id'] ,'weight (lbs)': weight, 'volume (in3)': volume}, ignore_index=True)
  df['order_id'] = df['order_id'].astype(int)

  #generate .csv file
  df.to_csv('records_csv.csv',index=False)

else:
  print('Log file doesnt exist')
