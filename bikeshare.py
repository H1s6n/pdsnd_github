import time
import datetime
import statistics as st
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
#part1    
    city = input ('\nWhat city data would you like to see? please write one of these cities Chicago, New York City or Washington\n').lower() #The user can write the name of the city in either small or capital letters
    
    while True:
        if (city == 'chicago' or city == 'new york city' or city == 'washington'):
            break
        else:
            city = input('Error, write a correct city\n').lower()
    ###month###
    
    month = input ('\nWhich month? January, February, March, April, May, or June\n').lower()
    
    while True :
        if (month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june'):
            break
        else:
            month = input('Error, write a correct month\n').lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    ###day###
    
    day = input ('\nWhich day? Sunday, Monday, Tuesday, Wednesday, Thursday, Firday or Saturday\n').lower()
    
    while True :
        if (day == 'sunday' or day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday'):
            break
        else:
            day = input ('Error, write a correct day\n')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day

#part2
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
    df = pd.read_csv(CITY_DATA[city])
    ###by month###
    df['Start Time'] = pd.to_datetime(df['Start Time']) #to_datetime is to converting from date to date format
    df['End Time'] = pd.to_datetime(df['End Time'])
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1       
    
    df = df[df['Start Time'].dt.month == month]
    ###by day###
    if day != 'all':
        df = df[df['Start Time'].dt.weekday_name == day.title()]
    print(df.head())
    return df

#part3
def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if(month == 'all'):
        most_common_month = df['Start Time'].dt.month.value_counts().idxmax()
        print('Most common month is ' + str(most_common_month))

    # TO DO: display the most common day of week
    if(day == 'all'):
        most_common_day = df['Start Time'].dt.weekday_name.value_counts().idxmax()
        print('Most common day is ' + str(most_common_day))
        
    # TO DO: display the most common start hour
    most_common_hour = df['Start Time'].dt.hour.value_counts().idxmax()
    print('Most popular hour is ' + str(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#part4
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = st.mode(df['Start Station'])
    print('\nMost Popular Start Station is {}'.format(most_common_start_station))
    
    # TO DO: display most commonly used end station
    most_common_end_station = st.mode(df['End Station'])
    print('\nMost Popular End Station is {}'.format(most_common_end_station))
    
    # TO DO: display most frequent combination of start station and end station trip
    combination_trip = df['Start Station'].astype(str) + df['End Station']
    most_frequent_trip = combination_trip.value_counts().idxmax()
    print('\nMost popular trip is from {}'.format(most_frequent_trip))

    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#part5
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    time1 = total_travel_time
    day = time1 // (24 * 3600)
    time1 = time1 % (24 * 3600)
    hour = time1 // 3600
    time1 %= 3600
    minutes = time1 // 60
    time1 %= 60
    print('\nThe Total travel time is {} days {} hours {} minutes'.format(day, hour, minutes))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    time2 = mean_travel_time
    day2 = time2 // (24 * 3600)
    time2 = time2 % (24 * 3600)
    hour2 = time2 // 3600
    time2 %= 3600
    minutes2 = time2 // 60
    time2 %= 60
    print('The Mean travel time is {} hours {} minutes'.format(hour2, minutes2))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#part6
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    no_of_subscribers = df['User Type'].str.count('Subscriber').sum()
    no_of_customers = df['User Type'].str.count('Customer').sum()
    print('Number of subscribers are {}\n'.format(int(no_of_subscribers)))
    print('Number of customers are {}\n'.format(int(no_of_customers)))

    # TO DO: Display counts of gender
    if('Gender' in df):
        male_count = df['Gender'].str.count('Male').sum()
        female_count = df['Gender'].str.count('Female').sum()
        print('Number of Male users are {}\n'.format(int(male_count)))
        print('Number of Female users are {}\n'.format(int(female_count)))

    # TO DO: Display earliest, most recent, and most common year of birth
    if('Birth Year' in df):
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()
    
    try:
        print('\nOldest Birth Year is {}\nYoungest Birth Year is {}\nMost popular Birth Year is {}'.format(int(earliest_year), int(recent_year), int(most_common_birth_year)))
    
    except TypeError:
        print("\nOldest Birth Year is {}\nYoungest Birth Year is {}\nMost popular Birth Year is {}".format(int(earliest_year), int(recent_year), most_common_birth_year))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        while True :
            test = input ('\nDo you want to view some data? Enter yes or no\n')
            if test.lower() == 'yes':
                print (df.head)
            else:
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()