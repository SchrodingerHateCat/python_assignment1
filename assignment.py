"""
Template for the COMP1730/6730 project assignment, S2 2021.
The assignment specification is available on the course web
site, at https://cs.anu.edu.au/courses/comp1730/assessment/project/


The assignment is due 25/10/2021 at 9:00 am, Canberra time

Collaborators: <list the UIDs of ALL members of your project group here>
"""
import os
import csv
from datetime import datetime

def analyse(path_to_files):
    question_1(path_to_files)


def question_1(path_to_files):
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

    print('Question 1:')
    print('Most recent data is in file \'' + recent_file + '\'')
    print('Last updated at ' + last_update)
    print('Total worldwide cases: ' ,total_cases,', Total worldwide deaths: ' ,total_deaths)




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

# The section below will be executed when you run this file.
# Use it to run tests of your analysis function on the data
# files provided.

if __name__ == '__main__':
    # test on folder containg all CSV files
    analyse('./covid-data')
