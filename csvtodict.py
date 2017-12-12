from pprint import pprint
import csv
import random 
import pandas as pd
import json

data = {}

video_games = pd.read_csv("C://Users//ILYES//Documents//GitHub//Video-games//Video_Game.csv",sep=",")
nom_video_games = video_games[video_games.columns[0]].tolist()

colonnes = ['user_id', 'nom_jeux', 'rating'] # colonnes du nouveau fichier csv temporaire

with open('temp.csv', "w") as fichier1: 

    write = csv.DictWriter(fichier1, delimiter = ',', fieldnames = colonnes)    
    write.writeheader()    
    
    for x in range(1, 20): #19 utilisateurs 
        items = random.sample(nom_video_games,500)    #500 jeux video
        random.randint(1,5) # rating de 1 à 5 
        for item in items:        
            write.writerow({'user_id': x, 'nom_jeux': item, 'rating': random.randint(1, 5)})
        
		
with open('temp.csv') as fichier2:     

    reader = csv.DictReader(fichier2, delimiter=',')    
    i = 0    
    for line in reader:            
        i += 1
        if (i == 1):
            continue    
        
        if (int(line['user_id']) not in data):
            data[int(line['user_id'])] = {}
            
        data[int(line['user_id'])][str(line['nom_jeux'])] = float(line['rating'])

		
with open('C://Users//ILYES//Documents//GitHub//Video-games//games.py', 'w') as fichier3:
    fichier3.write("data = ")
    json.dump(data, fichier3)

