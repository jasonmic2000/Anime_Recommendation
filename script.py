from data import *
from linked_list import LinkedList

# Code to insert anime genres into a data structure (LinkedList)
def insert_anime_genres():
    anime_genre_list = LinkedList()
    for genre in genres:
        anime_genre_list.insert_beginning(genre)
    return anime_genre_list

# Code to insert anime data into a data structure (LinkedList of LinkedLists)
def insert_anime_data():
    anime_data_list = LinkedList()
    for genre in genres:
        anime_sublist = LinkedList()
        for anime in anime_data:
            if anime[0] == genre:
                anime_sublist.insert_beginning(anime)
        anime_data_list.insert_beginning(anime_sublist)
    return anime_data_list

my_genre_list = insert_anime_genres()
my_anime_list = insert_anime_data()

selected_genre = ""

# Code for user interaction
while len(selected_genre) == 0:
    user_input = str(input(
        f"\nWhat genre of anime would you like to watch?\n{my_genre_list.stringify_list()}\n"
        "Enter the first letter(s) of the genre\n"
    )).lower()

    # Search for user_input in genres data structure
    matching_genres = []
    genre_list_head = my_genre_list.get_head_node()
    while genre_list_head is not None:
        if str(genre_list_head.get_value()).startswith(user_input):
            matching_genres.append(genre_list_head.get_value())
        genre_list_head = genre_list_head.get_next_node()

    # print list of matching genres
    for genre in matching_genres:
        print(genre)

    select_genre = str(input(
        f"Would you like to look at {matching_genres[0]} animes? Enter y for yes and n for no\n"
    )).lower()

    if select_genre == 'y':
        selected_genre = matching_genres[0]
        print(f"Selected Genre: {selected_genre}")
        anime_list_head = my_anime_list.get_head_node()

        while anime_list_head.get_next_node() is not None:
            sublist_head = anime_list_head.get_value().get_head_node()
            if sublist_head.get_value()[0] == selected_genre:
                while sublist_head.get_next_node() is not None:
                    # print("--------------------------")
                    print(sublist_head.get_value()[1] + "\n")
                    # print("--------------------------")
                    sublist_head = sublist_head.get_next_node()
            anime_list_head = anime_list_head.get_next_node()

        # # Ask user if they would like to search for other genres of anime
        # repeat_loop = str(input("Do you want to find other animes? Enter y for yes and n for no")).lower()
        # if repeat_loop == 'y':
        #     selected_food_type = ""