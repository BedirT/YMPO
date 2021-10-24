# YMPO - Youtube Music Playlist Organizer
#
# Github: BedirT
# Email: tapkan@ualberta.ca
#
# This is a simple software that can be used to organize your youtube music playlists.
# Given a playlist (either your own or someone else's), the program goes through, and
# gives you the option to distribute the playlist to multiple new other playlists.
#
# Uses ytmusicapi
#
from ytmusicapi import YTMusic

def print_playlists_menu(new_playlists):
    print("\nPlaylists:")
    for i in range(len(new_playlists)):
        print(str(i) + ": " + new_playlists[i])
    print("")

def get_playlists(ytmusic):
    '''
    Gets playlist inputs and creates the playlists.

    Returns the dictionary of playlist names(key) and ids(value).
    '''
    playlist_names = []
    playlist_ids = []
    while True:
        playlist = input("Enter playlist name (empty if no more is needed): ")
        if playlist == "": break
        description = input("Enter playlist description: ")
        privacy = input("Enter playlist privacy (0 for private, 1 for public): ")
        playlist_names.append(playlist)
        playlist_ids.append(ytmusic.create_playlist(playlist, description, privacy))
    return playlist_ids, playlist_names

def main():
    ytmusic = YTMusic('headers_auth.json')

    # get playlist id to distribute
    main_playlist_id = input("Enter playlist id (to distribute): ")

    # number of songs to distribute in the playlist
    num_songs = int(input("Enter number of songs to distribute(increments of 100): "))
    
    # get new playlists to distribute to
    # playlist_ids, playlist_names = get_playlists(ytmusic)

    # parse playlist and ask user for which playlist to put the song in
    playlist_to_distribute = ytmusic.get_playlist(main_playlist_id, limit= num_songs)
    print(len(playlist_to_distribute))

    ct = 0
    for song in playlist_to_distribute['tracks']:
        print("\nSong: " + song['title'])
        ct += 1
        # get the artists
        print("Artist: ", end="")
        for artist in song['artists']:
            print(artist['name'], end=" ")
        print("")
        # display the playlist options to choose from
        # print_playlists_menu(playlist_names)

        # get user input for which playlist/s to put the song in
        # playlist_choice = input("Enter playlist id(s) to put the song in(comma seperated): ")
        # playlist_choice = playlist_choice.split(",")

        # # distribute the song to the chosen playlists
        # for choice in playlist_choice:  
        #     ytmusic.add_playlist_items(playlist_ids[int(choice)], [song['videoId']])
    print(ct)

if __name__ == "__main__":
    main()    