import time
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
    while True:
        # Get user input for city
        city = input('Would you like to see data for Chicago, New York City, or Washington? ').lower()
        if city in CITY_DATA:
            break
        else:
            print('Invalid input. Please choose a valid city.')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Enter the name of the month to filter by (e.g., January, February, etc.) or "all" for no month filter: ').lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print('Invalid input. Please enter a valid month or "all".')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter the name of the day of the week to filter by (e.g., Monday, Tuesday, etc.) or "all" for no day filter: ').lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print('Invalid input. Please enter a valid day or "all".')

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
    # Load data file into a DataFrame
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)

    # Convert the 'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of the week from 'Start Time' to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Filter by month if applicable
    if month != 'all':
        # Use the index of the months list to get the corresponding integer
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1  # Adding 1 to match the month values in the dataframe
        df = df[df['month'] == month]
       
    # Filter by day of the week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]  # title() to ensure case-insensitive matching

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most Common Month:', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most Common Day of the Week:', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', common_hour)

    print("\nThis took {} seconds.".format(round(time.time() - start_time, 1)))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_combination = df['Combination'].mode()[0]
    print('Most Frequent Combination of Start and End Stations:', common_combination)

    print("\nThis took {} seconds.".format(round(time.time() - start_time, 1)))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time (in seconds):', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time (in seconds):', mean_travel_time)

    print("\nThis took {} seconds.".format(round(time.time() - start_time, 1)))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of User Types:\n', user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_counts = df['Gender'].value_counts()
        print('\nCounts of Gender:\n', gender_counts)
    else:
        print('\nGender information is not available for this dataset.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print('\nEarliest Birth Year:', int(earliest_birth_year))
        print('Most Recent Birth Year:', int(most_recent_birth_year))
        print('Most Common Birth Year:', int(common_birth_year))
    else:
        print('\nBirth year information is not available for this dataset.')

    print("\nThis took {} seconds.".format(round(time.time() - start_time, 1)))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
def display_raw_data(df):
    """Displays raw data in an interactive manner."""

    start_idx = 0
    end_idx = 5
    display_data = True

    while display_data:
        # Display the next 5 rows of data
        print(df.iloc[start_idx:end_idx])
        start_idx += 5
        end_idx += 5

        # Ask the user if they want to see more data
        user_input = input('Would you like to see 5 more rows of raw data? Enter yes or no: ')
        if user_input.lower() != 'yes':
            display_data = False

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # Ask the user if they want to see raw data
        raw_data_request = input('\nWould you like to see the raw data? Enter yes or no: ')
        if raw_data_request.lower() == 'yes':
            display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()