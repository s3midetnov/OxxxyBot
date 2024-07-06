# from lyricsgenius import Genius
import random
# import requests
import json

songs_path = "names_of_songs"
songs_file = open(songs_path, "r")
number_of_songs = len(songs_file.readlines())


currentsong_path = ""

# this is a description of lines that are "good" to use
def admissible_line(w : str) -> bool: 
    if w[0] == '[' or w[0] == ' ' or w == "\n" or w[0:19] == "You might also like":
        return False
    return True


def parse_id(w : str):
    split_hyphen = w.split("/")[2]
    split_hyphen = split_hyphen[:len(split_hyphen)-1]
    return split_hyphen

def fetch_line() : 
    # take an id of a random song
    song_to_send = random.randint(0, number_of_songs)
    id_of_song = parse_id(songs_file[song_to_send])

    # fetch the random song and write it into currentsong.txt
    currentsong = open(currentsong_path, "w")
    # currentsong.write(genius.lyrics(id_of_song))

    # prepare choose a random line
    currentsong.close()
    currentsong = open(currentsong_path, "r")
    number_of_lines = len(currentsong.readlines())
    ans = ""

    # choose a line and make sure that it belongs to the song lyrics and not some info
    while True :
        line_num = random.randint(2, number_of_lines - 2)
        ans = currentsong[line_num]
        if admissible_line(ans):
            return ans




def send_message(msg, mass):

    for x in mass:
        compose = ''
        requests.get(compose)

def do_staff(msg):
    uRLs = open("/Users/artemsemidetnov/PycharmProjects/genius/urls.txt", "r")
    mass = []
    mass1 = uRLs.readlines()
    for x in mass1:
        if x[len(x)-1:] == '\n':
            print("ZHOPA")
            print("ZHOPA")
            mass.append(x[0:len(x)-1])
    print(mass)

    link = ''
    f = requests.get(link)

    g = f.text
    d = json.loads(g)

    arr = d['result']
    for x in arr:
        if 'message' in x:
            idx = x['message']['from']['id']
            print(idx)
            if str(idx) not in mass:
                print("AZAZAZA")
                mass.append(str(idx))
    print(mass)
    send_message(msg ,mass)
    uRLs = open("/Users/artemsemidetnov/PycharmProjects/genius/urls.txt", "w")
    for x in mass:
        uRLs.write(x+"\n")

def main() : 
    # checks:
    print(admissible_line("You might also like[Припев]"))
    print(admissible_line("\n"))
    print(admissible_line("[Куплет 2]"))
    print(parse_id("/songs/116335\n"))
    w = "You might also like[Припев]"
    

main()