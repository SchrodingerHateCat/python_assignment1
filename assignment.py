"""
Template for the COMP1730/6730 project assignment, S2 2021.
The assignment specification is available on the course web
site, at https://cs.anu.edu.au/courses/comp1730/assessment/project/


The assignment is due 25/10/2021 at 9:00 am, Canberra time

Collaborators: <list the UIDs of ALL members of your project group here>
"""
import os
import csv
from datetime import datetime,timedelta

def analyse(path_to_files):
    print('Analysing data from folder \'' + path_to_files + '\'\n')
    recent_file = question_1(path_to_files)
    question_2(path_to_files,recent_file)


def question_1(path_to_files):
    print('Question 1:')
    dirs = os.listdir(path_to_files)
    file_format = '%m-%d-%Y'
    date_format = '%Y-%m-%d %H:%M:%S'
    recent_date = datetime.min.strftime(file_format)
    recent_file = ''
    last_update = datetime.min.strftime(date_format)
    total_cases = 0
    total_deaths = 0
    for file in dirs:
        if file.endswith('.csv'):
            file_name = file.split('.')[0]
            if compare_date(file_format,file_name,recent_date):
                recent_date = file_name
                recent_file = file
    
    with open(path_to_files+'/'+recent_file , 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if compare_date(date_format,row['Last_Update'],last_update):
                last_update = row['Last_Update']
            total_cases += int(row['Confirmed'])
            total_deaths += int(row['Deaths'])

    print('Most recent data is in file \'' + recent_file + '\'')
    print('Last updated at ' + last_update)
    print('Total worldwide cases: ',total_cases,', Total worldwide deaths: ',total_deaths,'\n')
    return recent_file

def question_2(path_to_files,recent_file):
    print('Question 2:')
    file_format = '%m-%d-%Y'
    country_cases = {}
    country_deaths = {}
    country_lastdate = {}
    country_news = {}
    with open(path_to_files+'/'+recent_file , 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Country_Region'] in country_cases.keys():
                country_cases[row['Country_Region']] += int(row['Confirmed'])
                country_deaths[row['Country_Region']] += int(row['Deaths'])
            else:
                country_cases[row['Country_Region']] = int(row['Confirmed'])
                country_deaths[row['Country_Region']] = int(row['Deaths'])
    
    file_name = recent_file.split('.')[0]
    last_day_file = get_yesterday(file_format,file_name)
    with open(path_to_files+'/'+last_day_file+'.csv' , 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Country_Region'] in country_lastdate.keys():
                country_lastdate[row['Country_Region']] += int(row['Confirmed'])
            else:
                country_lastdate[row['Country_Region']] = int(row['Confirmed'])
    for k,v in country_cases.items():
        country_news[k] = v - country_lastdate[k]
    temp = sorted(country_cases.items(), key = lambda v:(v[1],v[0]),reverse=True)
    for i in range(10):
        print('{0:20} - total cases: {1:10} -deaths: {2:10} -new: {3:10}'.format(temp[i][0],temp[i][1],country_deaths[temp[i][0]],country_news[temp[i][0]]))
    print()
        




def question_3(path_to_files):
    pass

def question_4(recent_file):
    pass




def compare_date(format_pattern,time1,time2):
    '''
    description: check between time1 and time2, return true if time1 is later
                 than time2
    param {string}format_pattern: given the format of the date
          {string}time1 
          {string}time2
    return {boolean} True or False
    '''    
    different = (datetime.strptime(time1,format_pattern) - datetime.strptime(time2,format_pattern))
    return different.days > 0


def get_yesterday(format_pattern,date):
    '''
    description: return the last day of input parameter date
    param {string}date: flag date
          {string}format_pattern: date format
    return {string}lastday
    '''    
    this_day = datetime.strptime(date,format_pattern)
    last_day = this_day - timedelta(days = 1)
    return last_day.strftime(format_pattern)

# The section below will be executed when you run this file.
# Use it to run tests of your analysis function on the data
# files provided.

if __name__ == '__main__':
    # test on folder containg all CSV files
    analyse('./covid-data')
