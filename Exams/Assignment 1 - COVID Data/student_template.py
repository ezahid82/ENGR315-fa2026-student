import sys

"""
Create a program which will provide answers to the questions posed in the assignment description.
We've provided a function which will parse the NYT covid database file (named "us-counties.csv"); 
however, its correct implementation will be up to you. DO NOT MODIFY THIS FUNCTION.
Your code needs to be successful as well as sufficiently commented/documented to receive full credit.
"""


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date,county, state, fips, cases, deaths) information

    ____________________ DO NOT MODIFY THIS FUNCTION ___________________
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, fips, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

### YOUR CODE HERE ###

data_path = "../../data/covid/us-counties.csv"  # the path exits the current location twice to reach the data file
temp_data = parse_nyt_data(data_path)           # parse the NYT COVID data file and store it in temporary variable



### Question 1: When was the first positive COVID case in Harrisonburg? 
# When was the first positive case in Rockingham County? (2 questions)

first_positive_harrisonburg = 0   # variable to store the first positive case date in Harrisonburg
first_positive_rockingham = 0     # variable to store the first positive case date in Rockingham County

# iterate through each data entry in temp_data
# then, if the county is harrisonburg, and state is VA,
# then if, there is an earlier date than the current first positive case, 
# update first_positive_harrisonburg with the new date.
for date, county, state, fips, cases, deaths in temp_data:   
    if county == "Harrisonburg city" and state == "Virginia" and cases > 0: 
        if first_positive_harrisonburg == 0 or date < first_positive_harrisonburg:
            first_positive_harrisonburg = date

# iterate through each data entry in temp_data
# then, if the county is Rockingham, and state is VA,
# then if, there is an earlier date than the current first positive case, 
# update first_positive_rockingham with the new date.
for date, county, state, fips, cases, deaths in temp_data:
    if county == "Rockingham" and state == "Virginia" and cases > 0:
        if first_positive_rockingham == 0 or date < first_positive_rockingham:
            first_positive_rockingham = date

# print the first positive case dates for Harrisonburg and Rockingham County.
print("First positive case in Harrisonburg:", first_positive_harrisonburg)
print("First positive case in Rockingham County:", first_positive_rockingham)



### Question 2: On what date was the greatest number of new cases reported in Harrisonburg? 
# What date in Rockingham County? (2 questions)


# variables to store the largest increase in new cases and their corresponding dates for Harrisonburg
largest_increase = 0
largest_increase_date = 0
previous_cases = 0

# iterate through each data entry in temp_data
# then, if the county is Harrisonburg and state is VA,
# then if, there is a greater number of new cases than the current greatest, 
# update largest_increase and largest_increase_date.
for date, county, state, fips, cases, deaths in temp_data:
    if county == "Harrisonburg city" and state == "Virginia":
        if previous_cases != 0:
            daily_increase = cases - previous_cases
            if largest_increase == 0 or daily_increase > largest_increase:
                largest_increase = daily_increase
                largest_increase_date = date
        previous_cases = cases

# print the largest increase in new cases for Harrisonburg
print(f"Largest increase in Harrisonburg was on: {largest_increase_date} with {largest_increase} cases")


# variables to store the largest increase in new cases and their corresponding dates for Rockingham County
largest_increase_rockingham = 0
largest_increase_rockingham_date = 0
previous_cases_rockingham = 0

# iterate through each data entry in temp_data
# then, if the county is Rockingham and state is VA,
# then if, there is a greater number of new cases than the current greatest, 
# update largest_increase_rockingham and largest_increase_rockingham_date.
for date, county, state, fips, cases, deaths in temp_data:
    if county == "Rockingham" and state == "Virginia":
        if previous_cases_rockingham != 0:
            daily_increase = cases - previous_cases_rockingham
            if largest_increase_rockingham == 0 or daily_increase > largest_increase_rockingham:
                largest_increase_rockingham = daily_increase
                largest_increase_rockingham_date = date
        previous_cases_rockingham = cases

# print the largest increase in new cases for Rockingham County
print(f"Largest increase in Rockingham County was on: {largest_increase_rockingham_date} with {largest_increase_rockingham} cases")




### Question 3: What was the worst seven-day period in Harrisonburg city for new COVID cases? 
# What period in Rockingham County? These are the seven-day periods when the number of new cases was maximal. (2 questions)


# list to store daily new cases for Harrisonburg city
daily_new_cases = []
previous_cases = 0

# iterate through each data entry in temp_data
# then, if the county is Harrisonburg and state is VA,
# calculate the daily new cases and append to daily_new_cases.
for date, county, state, fips, cases, deaths in temp_data:
    if county == "Harrisonburg city" and state == "Virginia":
        if previous_cases != 0:
            daily_new_cases.append((date, cases - previous_cases))
        previous_cases = cases

# variables to store the worst seven-day period for Harrisonburg city
# highest_total_cases: the maximum number of new cases in a seven-day window
# worst_start: the start date of the worst seven-day period
# worst_end: the end date of the worst seven-day period
highest_total_cases = 0
worst_start = 0
worst_end = 7

# iterate through all possible seven-day windows in daily_new_cases
# calculate the total new cases for each window
# update highest_total_cases, worst_start, and worst_end if a new maximum is found
for i in range(len(daily_new_cases) - 6):
    window = daily_new_cases[i:i+7]
    window_total = sum(value for date, value in window)

# check if the current window total is greater than the highest total found so far
    if highest_total_cases == 0 or window_total > highest_total_cases:
        highest_total_cases = window_total # update the highest total number of new cases in a seven-day window
        worst_start = window[0][0] # set the start date of the worst seven-day period
        worst_end = window[-1][0] # set the end date of the worst seven-day period

# print the worst seven-day period for Harrisonburg city
print(f"Worst seven-day period in Harrisonburg city: {worst_start} to {worst_end} with {highest_total_cases} cases")

# list to store daily new cases for Rockingham County
daily_new_cases_rockingham = []
previous_cases_rockingham = 0

# iterate through each data entry in temp_data
# then, if the county is Rockingham and state is VA,
# calculate the daily new cases and append to daily_new_cases_rockingham.
for date, county, state, fips, cases, deaths in temp_data:
    if county == "Rockingham" and state == "Virginia":
        if previous_cases_rockingham != 0:
            daily_new_cases_rockingham.append((date, cases - previous_cases_rockingham))
        previous_cases_rockingham = cases

# variables to store the worst seven-day period for Rockingham County
# highest_total_cases_rockingham: the maximum number of new cases in a seven-day window
# worst_start_rockingham: the start date of the worst seven-day period
# worst_end_rockingham: the end date of the worst seven-day period
highest_total_cases_rockingham = 0
worst_start_rockingham = 0
worst_end_rockingham = 0

# iterate through all possible seven-day windows in daily_new_cases_rockingham
# calculate the total new cases for each window
# update highest_total_cases_rockingham, worst_start_rockingham, and worst_end_rockingham if a new maximum is found
for i in range(len(daily_new_cases_rockingham) - 6):
    window = daily_new_cases_rockingham[i:i+7]
    window_total = sum(value for date, value in window)

# check if the current window total is greater than the highest total found so far
    if highest_total_cases_rockingham == 0 or window_total > highest_total_cases_rockingham:
        highest_total_cases_rockingham = window_total # update the highest total number of new cases in a seven-day window
        worst_start_rockingham = window[0][0] # set the start date of the worst seven-day period
        worst_end_rockingham = window[-1][0] # set the end date of the worst seven-day period

# print the worst seven-day period for Rockingham County
print(f"Worst seven-day period in Rockingham County: {worst_start_rockingham} to {worst_end_rockingham} with {highest_total_cases_rockingham} cases")


