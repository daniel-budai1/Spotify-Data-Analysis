import os
import pandas as pd
import matplotlib.pyplot as plt

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "Spotify Most Streamed Songs.csv") #line 5 and 6 make the path based on where the python file is, making it portable
try: #try and except for providing user with info as to why the script won't run
    df = pd.read_csv(csv_path)
except FileNotFoundError:
    print(f"Could not find the CSV file at: {csv_path}")
    print("Make sure the provided CSV file is in the same folder as the script/python file.")
    exit()
pd.set_option("display.float_format", lambda x: "%.2f" % x) #formats numbers to 2 decimal places)
df["streams"] = pd.to_numeric(df["streams"], errors='coerce') #read csv file and convert streams column to numeric while dropping rows with missing values (NaN)
df = df.dropna(subset=["streams"])


#function for menu and user input
def user_input():
    flag = True
    while flag:
        print("\n=========================================================")
        print("Welcome to the Spotify Most Streamed Songs Data Analysis.")
        print("=========================================================")
        print("\nPlease select an option:")
        print("\n1. View the top 10 most streamed songs")
        print("2. View the top 10 artists with the most streams")
        print("3. View the top 10 most saved songs in spotify playlists")
        print("4. View the top 10 most saved songs in apple music playlists")
        choice = (input("\nEnter your choice (1-4): "))
        try:
            choice = int(choice)
        except ValueError:
            print("Choice must be numeric, please try again.")
        else:
            if 1 <= choice <= 4:
                flag = False
            else:
                print("Please enter a number between 1-4.")
    return choice
        

#function for getting top 10 streamed songs and displaying them on a bar chart
def view_top_streamed_songs():
    top10 = df[["track_name", "released_year", "released_month", "released_day", "artist(s)_name", "streams"]].sort_values(by="streams", ascending=False).head(10)
    print(top10.to_string(index=False))

    plt.bar(top10["track_name"], top10["streams"], color="blue")
    plt.title("Top 10 Most Streamed Songs")
    plt.xlabel("Song Name")
    plt.ylabel("Streams")
    plt.xticks(rotation=45)
    plt.ticklabel_format(style="plain", axis="y") #makes y-axis numbers easier to read by showing them as whole numbers instead of scientific notation
    plt.show()

#function for showing top 10 artists with most streams and displaying them on a graph
def view_top_artists():
    top10_artists = df[["artist(s)_name", "streams"]].groupby("artist(s)_name").sum().sort_values(by="streams", ascending=False).head(10)
    print(top10_artists.to_string())

    plt.bar(top10_artists.index, top10_artists["streams"], color="Yellow") #matches the order of the graph is meant to be displayed like in the previous function using "index" to get the artist names
    plt.title("Top 10 Artists With The Most Streams")
    plt.xlabel("Artist Name")
    plt.ylabel("Streams")
    plt.xticks(rotation=45)
    plt.ticklabel_format(style="plain", axis="y")
    plt.show()

#function for showing top 10 saved songs in spotify playlists
def view_top_saved_songs_spotify():
    top10_saved_spotify = df[["track_name", "artist(s)_name", "in_spotify_playlists"]].sort_values(by="in_spotify_playlists", ascending=False).head(10)
    print(top10_saved_spotify.to_string(index=False))

    plt.bar(top10_saved_spotify["track_name"], top10_saved_spotify["in_spotify_playlists"], color="red")
    plt.title("Top 10 Most Saved Songs In Spotify Playlists")
    plt.ylabel("Spotify Playlists")
    plt.xlabel("Song Name")
    plt.xticks(rotation=45)
    plt.ticklabel_format(style="plain", axis="y")
    plt.show()

#function for showing top 10 saved songs in apple music playlists
def view_top_saved_songs_AM():
    top10_saved_AM = df[["track_name", "artist(s)_name", "in_apple_playlists"]].sort_values(by="in_apple_playlists", ascending=False).head(10)
    print(top10_saved_AM.to_string(index=False))

    plt.bar(top10_saved_AM["track_name"], top10_saved_AM["in_apple_playlists"], color="green")
    plt.title("Top 10 Most Saved Songs In Apple Music Playlists")
    plt.xlabel("Song Name")
    plt.ylabel("Apple Music Playlists")
    plt.xticks(rotation=45)
    plt.ticklabel_format(style="plain", axis="y")
    plt.show()

#allowing user options to be accepted       
user_choice = user_input()
if user_choice == 1:
    view_top_streamed_songs()
elif user_choice == 2:
    view_top_artists()
elif user_choice == 3:
    view_top_saved_songs_spotify()
elif user_choice == 4:
    view_top_saved_songs_AM()
