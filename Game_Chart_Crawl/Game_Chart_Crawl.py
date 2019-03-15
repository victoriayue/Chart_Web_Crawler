# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import os.path


dir = os.path.dirname(os.path.realpath(__file__))
print(dir)

"""
Apple App Store Chart Crawl:
"""


"""
find game which inside Word genre,
if true, return the text inside page
"""
def A_find_game_with_word_category(target):
    if __name__ == '__main__':
        req = requests.get(url=target) # get all from target
        html = req.text
        bf = BeautifulSoup(html)
        check_genre = bf.find_all("li", "inline-list__item") # find_all（标签名，标签属性）
        check_genre = check_genre[0].string
        if check_genre != None and "Word" in check_genre:
            return bf

"""
inside bf text, find the game name and company name
"""
def A_get_game_info(bf):
    title = bf.find_all("h1", "product-header__title app-header__title")
    title = title[0].contents[0].strip()
    game = "Game:\t\t" + title + "\n"
    company = bf.find("h2", "product-header__identity app-header__identity")
    company = "Company:\t" + company.a.string + "\n"
    text = game + company
    return text

def A_get_update_content(bf):
    class__ = bf.find("section", 'l-content-width section section--bordered whats-new')
    ti = class__.find("time") # update time
    contents = class__.find_all('p')
    content = ""
    for a in contents[1].contents:
        if a.string != None:
            content += a.string

    return "Update Time: \t" + ti.string + "\n" + content + "\n"

def A_startPrinting(target):
    bf = A_find_game_with_word_category(target)
    if bf != None:
        txt = ""
        txt = txt + A_get_game_info(bf)
        txt = txt + A_get_update_content(bf)
        f = open("Apple_Top_Game_Chart.txt", "a")
        f.write(txt.encode('utf-8') + "\n")

def Apple_Chart_Crawl():
    fName = os.path.join(dir, "Apple_Top_Game_Chart.txt")
    f = open(fName, "w+")
    target = 'https://itunes.apple.com/us/genre/ios-games-word/id7019?mt=8'

    if __name__ == '__main__':
            req = requests.get(url=target)
            html = req.text
            bf = BeautifulSoup(html)
            game_details = bf.find_all(id="selectedcontent")
            #print(game_details)
            for game_detail in game_details:
                for game in game_detail.find_all('a'):
                    s = game.contents[0] + "\n"
                    li = game['href'] #link
                    A_startPrinting(li)
            print("the result is in Apple_Top_Game_Chart.txt")

"""
Google Play Chart Crawl:
"""
"""
find game which inside Word genre,
if true, return the text inside page
"""
def G_find_game_with_word_category(target):
    if __name__ == '__main__':
        req = requests.get(url=target)
        html = req.text
        bf = BeautifulSoup(html)
        check_genre = bf.find_all("a", itemprop="genre")
        if check_genre == None:
            return None
        if check_genre[0].string == "Word":
            return bf

"""
inside bf text, find the game name and company name
"""
def G_get_game_info(bf):
    title = bf.find("h1", "AHFaub", itemprop="name")
    txt = "Game:\t\t" + title.string + "\n"
    company = bf.find("a", "hrTbp R8zArc")
    txt += "Company:\t" + company.string + "\n"
    return txt.encode('utf-8')

"""
inside bf text, find the latest update content
"""
def G_get_update_content(bf):
    updates = bf.find_all("div", jscontroller="IsfMIf", jsaction="rcuQ6b:npT2md")
    txt = ""
    if len(updates) > 1:
        update_content = updates[1].find("div", jsname="bN97Pc", itemprop="description")
        update_content = update_content.find("content").string
        if update_content != None:
            txt = "Update Content:\t" + update_content + "\n"
            txt = txt.encode('utf-8')
    return txt

"""
inside bf text, find the latest update date and time
"""
def G_get_update_time(bf):
    updates1 = bf.find("span", "htlgb")
    updates2 = updates1.find("div", "IQ1z0d")
    txt = "Update Time:\t" + updates2.string + "\n"
    return txt.encode('utf-8')

"""
start crawl for every game info webpage
"""
def G_startPrinting(target, rank):
    bf = G_find_game_with_word_category(target)
    if bf != None:
        txt = ""
        txt += rank + "\n"
        txt = txt + G_get_game_info(bf)
        txt = txt + G_get_update_content(bf)
        txt = txt + G_get_update_time(bf)
        f = open("Google_Top_Game_Chart.txt", "a")
        f.write(txt)

"""
search game in chart webpage
"""
def Google_Chart_Crawl():
    target = 'https://play.google.com/store/apps/category/GAME/collection/topselling_free'
    fName = os.path.join(dir, "Google_Top_Game_Chart.txt")
    f = open(fName, "w+")

    if __name__ == '__main__':
        req = requests.get(url=target)
        html = req.text
        bf = BeautifulSoup(html)
        for game_details in bf.find_all("div", "details"):
            for game_content in game_details.find_all("a", "title"):
                rank = game_content.contents[0].encode('utf-8')
                game_target = 'https://play.google.com' + game_content['href']    #get html of game
                G_startPrinting(game_target, rank)
        print("the result is in Google_Top_Game_Chart.txt")

"""
main
"""

print("The chart result is in progress ...... ")

try:
    Apple_Chart_Crawl()
    Google_Chart_Crawl()
except requests.ConnectionError:
    print("connection error")
