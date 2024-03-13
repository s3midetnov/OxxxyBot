from lyricsgenius import Genius
import random
import requests
import json

where_to_go = open("/Users/artemsemidetnov/PycharmProjects/genius/names_of_songs", "r")

n = random.randint(0, 215)
sngs = where_to_go.readlines()
print(sngs[n])
def oper(w):
    u = w.split("/")
    u1 = u[2]
    le = len(u1)
    gg = u1[:le-1]
    return gg

id = oper(sngs[n])

gonogo = open("/Users/artemsemidetnov/PycharmProjects/genius/fornow.txt", "w")
gonogo.write(genius.lyrics(id))
gonogo = open("/Users/artemsemidetnov/PycharmProjects/genius/fornow.txt", "r")
lyroc = gonogo.readlines()

ans = ""

ind = 1
while ind:
    m = random.randint(2, len(lyroc)-2)
    if lyroc[m][0]!= '[':
        ind  = 0
        ans = lyroc[m]
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

do_staff(ans)