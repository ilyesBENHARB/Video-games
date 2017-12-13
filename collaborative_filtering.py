from math import sqrt
from pprint import pprint
import csv
import random
from games import data

 
def coeff_correlation(user1,user2):

        jeux_video = {} # jeux video en commun
        for i in data[user1]:
                if i in data[user2]:
                        jeux_video[i] = 1

        nb_jeux = len(jeux_video)               
        if nb_jeux == 0:
                return 0

        #https://stackoverflow.com/questions/3949226/calculating-pearson-correlation-and-significance-in-python
        sum_user1 = sum([data[user1][i] for i in jeux_video])
        sum_user2 = sum([data[user2][i] for i in jeux_video])
        
        sum_user1_sq = sum([pow(data[user1][i],2) for i in jeux_video])
        sum_user2_sq = sum([pow(data[user2][i],2) for i in jeux_video])

        p_sum = sum([data[user1][i] * data[user2][i] for i in jeux_video])

        num = p_sum - (sum_user1*sum_user2/nb_jeux)
        den = sqrt((sum_user1_sq - pow(sum_user1,2)/nb_jeux) * (sum_user2_sq -pow(sum_user2,2)/nb_jeux))
        
        if den == 0:
                return 0
        else:
                r = num/den
                return r 

def similarite(user):
        #calculer similarite entre user et les autres utilisateurs
        sim = [(coeff_correlation(user,autre),autre) for autre in data if  autre != user ]
        sim.sort(reverse=True)#trier la liste de plus similaire vers le moins similaire
        return sim

def recommandations(user):

        totale = {}
        somme_coeff = {}
        classement =[]
        for autre in data:
                
                if autre == user:
                        continue
                sim = coeff_correlation(user,autre) #calculer similarite entre user et les autres utilisateurs
                if sim <=0: 
                        continue

                for i in data[autre]:

                    if i not in data[user] or data[user][i] == 0:
                        totale.setdefault(i,0)
                        totale[i] += data[autre][i]* sim # rating * similarite
                        somme_coeff.setdefault(i,0)
                        somme_coeff[i]+= sim #somme des similarites

        classement = [(total/somme_coeff[i],i) for i,total in totale.items()] #divisier le totale par la somme des similarites
        classement.sort(reverse=True) #trier la liste de plus recommendé vers le moins recommandé
		
        recommandations_list = [i for rating,i in classement] # extraire les nom des jeux video  de la liste classement
        return recommandations_list
                
