# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import os.path


dir = os.path.dirname(os.path.realpath(__file__))
print(dir)

"""
Google Play Chart Crawl:
"""

"""
find game category
"""
def G_find_game_category(bf):
        genre = bf.find("a", class_="hrTbp R8zArc", itemprop="genre")
        if genre == None:
            return None
        return genre

"""
inside bf text, find the game name and company name
"""
def G_get_game_info(bf):
    title = bf.find("h1", class_="AHFaub", itemprop="name")
    txt = "Game:\t\t" + title.string + "\n"
    company = bf.find("a", "hrTbp R8zArc")
    txt += "Company:\t" + company.string + "\n"
    return txt

"""
inside bf text, find the latest update content
"""
def G_get_update_content(bf):
    updates = bf.find_all("div", jscontroller="IsfMIf", jsaction="rcuQ6b:npT2md")
    txt = ""
    if len(updates) > 1:
        update_content = updates[1].find("div", jsname="bN97Pc", itemprop="description")
        update_content = update_content.find("content")
        if update_content != None:
            txt = "Update Content:\t" + update_content.string + "\n"
            txt = txt.encode('utf-8')
    return txt

"""
inside bf text, find the latest update date and time
"""
def G_get_update_time(bf):
    updates1 = bf.find("span", "htlgb")
    updates2 = updates1.find("div", "IQ1z0d")
    txt = "Update Time:\t" + updates2.string + "\n"
    return txt

"""
start crawl for every game info webpage
"""
def G_startPrinting(target, idx):
    req = requests.get(url=target)
    html = req.text
    bf = BeautifulSoup(html, "html.parser")

    category = G_find_game_category(bf)
    if bf != None:
        txt = ""
        txt += str(idx) + " "+category.string+ " Game\n"
        txt = txt + G_get_game_info(bf)
        txt = txt + G_get_update_content(bf)
        txt = txt + G_get_update_time(bf)
        txt = txt + "\n"
        f = open("Google_Top_Game_Chart.txt", "a")
        f.write(txt)

"""
search game in chart webpage
"""
def Google_Chart_Crawl():
    # Google Play Top free game chart.
    target = 'https://play.google.com/store/apps/collection/cluster?clp=0g4cChoKFHRvcHNlbGxpbmdfZnJlZV9HQU1FEAcYAw%3D%3D:S:ANO1ljJ_Y5U&gsr=Ch_SDhwKGgoUdG9wc2VsbGluZ19mcmVlX0dBTUUQBxgD:S:ANO1ljL4b8c'
    fName = os.path.join(dir, "Google_Top_Game_Chart.txt")
    f = open(fName, "w+")

    if __name__ == '__main__':
        req = requests.get(url=target)
        html = req.text
        bf = BeautifulSoup(html, "html.parser")
        idx = 1
        # for each game info
        for game_details in bf.find_all("div", "ImZGtf mpg5gc"):
            for game_content in game_details.find_all("a", "JC71ub"):
                game_url = 'https://play.google.com' + game_content['href']    #get html of game
                print (game_url)
                G_startPrinting(game_url, idx)
                idx += 1
        print("the result is in Google_Top_Game_Chart.txt")

"""
main
"""

print("The chart result is in progress ...... ")

try:
    Google_Chart_Crawl()
except requests.ConnectionError:
    print("connection error")
