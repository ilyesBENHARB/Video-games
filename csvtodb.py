import csv, sqlite3

con = sqlite3.connect("D:\\Etudes\\Fouille\\Videogames\\videogames.db")
cur = con.cursor()
cur.execute("CREATE TABLE videogames (Name,Platform,Year_of_Release,Genre,Publisher,NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales,Critic_Score,Critic_Count,User_Score,User_Count,Rating);")

with open('D:\\Etudes\\Fouille\\Videogames\\Video_Game.csv','r') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['Name'], i['Platform'], i['Year_of_Release'], i['Genre'], i['Publisher'], i['NA_Sales'], i['EU_Sales'], i['JP_Sales'], i['Other_Sales'], i['Global_Sales'], i['Critic_Score'], i['User_Score'], i['Critic_Count'], i['User_Count'], i['Rating']) for i in dr]

cur.executemany("INSERT INTO videogames (Name, Platform, Year_of_Release, Genre, Publisher, NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales, Critic_Score, Critic_Count, User_Score, User_Count, Rating) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
con.commit()
con.close()