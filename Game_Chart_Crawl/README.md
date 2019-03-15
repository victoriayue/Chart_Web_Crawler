# Top Game Chart Crawl
A small project to crawl the info of word games on App Store chart and Google play chart.

## General info
Using Requests to get the link of game from two website.
Then get into the link one by one.


### Google Play
* [Top Selling Free Game Chart](https://play.google.com/store/apps/category/GAME/collection/topselling_free)
* [Top Selling Paid Game Chart](https://play.google.com/store/apps/category/GAME/collection/topselling_paid)
* [Top Grossing Game Chart](https://play.google.com/store/apps/category/GAME/collection/topgrossing)
* Google Play doesn't have chart for subcategories like Word category. So, I use the two top selling chart and one top growing chart.

### Apple App Store
* [App Store Word Chart](https://itunes.apple.com/us/genre/ios-games-word/id7019?mt=8)
* Since App Store doesn't have chart for word game on their website, it only have subcategories chart on their App. I use word game category page which most game are on the word game rank chart.

## Technologies
Project is created with:
* Python        version: 2.7.13
* Requests      version: 2.21.0
* BeautifulSoup version: 4.0.0

## Features

Finished:
* Finding the game from Google Play Game Top Chart. 
* Getting the info of Word games from Apple App Store chart.
* Storing the game name, company name, latest update time and contents in two file called "Apple_Top_Game_Chart.txt" and "Google_Play_Game_Chart.txt"

In Progress:
* Get the info of pop-up window
* Get the games of Google Play Chart over 60 rank. It need the dynamic page Crawling skill. 
* Auto-refresh
* The executable may not work. 
