from lyricsgenius import Genius
import random
import requests
import json

def get_token(file):
    token_file = open(file, "r")
    return token_file.readline()

token = get_token("token.txt")
genius = Genius(token)

bot_token = get_token("bot_token.txt")

songs_path = "names_of_songs"
songs_file = open(songs_path, "r")
songs_array = songs_file.readlines()
number_of_songs = len(songs_array)


currentsong_path = "currentsong.txt"

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
    id_of_song = parse_id(songs_array[song_to_send])

    # fetch the random song and write it into currentsong.txt
    currentsong = open(currentsong_path, "w")
    currentsong.write(genius.lyrics(id_of_song))

    # prepare choose a random line
    currentsong.close()
    currentsong = open(currentsong_path, "r")
    currentsong_array = currentsong.readlines()
    number_of_lines = len(currentsong_array)
    ans = ""

    # choose a line and make sure that it belongs to the song lyrics and not some info
    while True :
        line_num = random.randint(2, number_of_lines - 2)
        ans = currentsong_array[line_num]
        if admissible_line(ans):
            return ans



def send_message(msg, array_ids):
    for id in array_ids:
        url = ('https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + str(id) +  '&text={}').format(
        msg)
        requests.get(url)

def do_staff(msg):
    urls_to_send_to = open("testurls.txt", "r")
    send_to_array = [] #mass
    mass1 = urls_to_send_to.readlines()
    for x in mass1:
        if x[len(x)-1:] == '\n':
            send_to_array.append(x[0:len(x)-1])
    # print(send_to_array)

    link = ''
    f = requests.get(link)

    g = f.text
    d = json.loads(g)

    arr = d['result']
    print(arr)
    # for x in arr:
    #     if 'message' in x:
    #         idx = x['message']['from']['id']
    #         print(idx)
    #         if str(idx) not in mass:
    #             print("AZAZAZA")
    #             mass.append(str(idx))
    # print(mass)
    # send_message(msg ,mass)
    # uRLs = open("/Users/artemsemidetnov/PycharmProjects/genius/urls.txt", "w")
    # for x in mass:
    #     uRLs.write(x+"\n")

def main() : 
    urls_to_send_to = open("urls.txt", "r")
    urls = urls_to_send_to.readlines()
    msg = fetch_line()
    send_message(msg, urls)

main()