import time
import pandas as pd
import numpy as np
 
#filter Iteration Data 
CITY_DATA = { 'chicago': 'chicago.csv','new york city': 'new_york_city.csv','washington': 'washington.csv' }
MONTHS={'january' : 1,  'february' : 2,'march' : 3,  'april' : 4, 'may' : 5,  'june' : 6, 'all' : 7}
DAYS = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']
 
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
 
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print("Would you like to see data for Chicago, New York or Washington?\n")
 
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        print("Enter City To Filter :")
        city=input().lower()
        if city not in CITY_DATA.keys():
            print("Invalid City Try Again...\n")
            continue
        else:
            break
    FilterInput=input("Would you like to filter by  Month , Day or Both ?\n").lower()
    if(FilterInput=='both'):
        # TO DO: get user input for month (all, january, february, ... , june)
        while True:
            print("\nEnter Month To Filter (all, january, february, ... , june) : ")
            month = input().lower()
            if month not in MONTHS.keys():
                print("Invalid Month Try Again...\n")
                continue
            else:
                break
 
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        while True:
            print("\nEnter Week Day Name (all, monday, tuesday, ... sunday) : ")
            day = input().lower()
            if day not in DAYS:
                print("Invalid Day Name Try Again...\n")
                continue
            else:
                break
    if(FilterInput=='month'):
        # TO DO: get user input for month (all, january, february, ... , june)
        while True:
            print("\nEnter Month To Filter (all, january, february, ... , june) : ")
            month = input().lower()
            day='all'
            if month not in MONTHS.keys():
                print("Invalid Month Try Again...\n")
                continue
            else:
                break
    if(FilterInput=='day'):
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        while True:
            print("\nEnter Week Day Name (all, monday, tuesday, ... sunday) : ")
            day = input().lower()
            month='all'
            if day not in DAYS:
                print("Invalid Day Name Try Again...\n")
                continue
            else:
                break 
 
    print('-'*40)
    return city, month, day
 
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
 
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
        #Load data for city
    print("data is loading please Wait...")
    df = pd.read_csv(CITY_DATA[city])
 
    #Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
 
    #Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
 
    #Filter by month if applicable
    if month != 'all' :
        #Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
 
        #Filter by month to create the new dataframe
        df = df[df['month'] == month]
 
    #Filter by day of week if applicable
    if day != 'all':
        #Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
 
    return df
 
 
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
 
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
 
    # TO DO: display the most common month
    pop_month = df['month'].mode()[0]
    print("The Most Common Month is {} ".format(pop_month))
 
 
    # TO DO: display the most common day of week
    pop_day = df['day_of_week'].mode()[0]
    print("The Most Common Day of week is {}".format(pop_day))
 
    # TO DO: display the most common start hour
    #Hour Extraction From Start Time
    df['hour'] = df['Start Time'].dt.hour
    pop_hour = df['hour'].mode()[0]
 
    print("The Most Common Hour of week is {}".format(pop_hour))
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 
 
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
 
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
 
    # TO DO: display most commonly used start station
    pop_StartStation = df['Start Station'].mode()[0]
 
    # TO DO: display most commonly used end station
    pop_EndStation = df['End Station'].mode()[0]
 
    # TO DO: display most frequent combination of start station and end station trip
    df['Start_End'] = df['Start Station'].str.cat(df['End Station'], sep=' To ')
    frequent = df['Start_End'].mode()[0]
    print('The most Frequent Staion Path : From \033[1m{}\033[0m'.format(frequent))
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 
 
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
 
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
 
    # TO DO: display total travel time
    total_travel=df['Trip Duration'].sum()
    print("The Total Travel time ={}".format(total_travel))
 
    # TO DO: display mean travel time
    travel_mean=round(df['Trip Duration'].mean(),4)
    print("The mean Travel time ={}".format(travel_mean))
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 
 
def user_stats(df):
    """Displays statistics on bikeshare users."""
 
    print('\nCalculating User Stats...\n')
    start_time = time.time()
 
    # TO DO: Display counts of user types
    user_counter=df['User Type'].value_counts()
    print("Users Types count : \n{} \n".format(user_counter))
 
    # TO DO: Display counts of gender
    gender_counter=df['Gender'].value_counts()
    print("Users genders count : \n{}\n".format(gender_counter))
 
    # TO DO: Display earliest, most recent, and most common year of birth
    #dob is the date of birth
    earliest_dob=int(df['Birth Year'].min())
    recent_dob=int(df['Birth Year'].max())
    pop_dob=int(df['Birth Year'].mode()[0])
 
    print("The earliest Date of Birth is : {} ".format(earliest_dob))
    print("The Most recent Date of Birth is : {} ".format(recent_dob))
    print("The Most Popular Date of Birth is : {}".format(pop_dob))
 
 
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 
 
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
 
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
 
        restart = input('\nWould you like to Restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
 
 
if __name__ == "__main__":
    main()