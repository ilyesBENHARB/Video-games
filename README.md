# Video-games
video game recommendations - collaborative filtering

/************** Execution **************/

1- import csvtodict					Pour generer les donnees sous le fichier games

2- import collaborative_filtering
		collaborative_filtering.coeff_correlation('user1','user2')  	Pour calculer la similarite entre user 1 et user 2
		collaborative_filtering.similarite('user')			Pour calculer la similarite entre user  et les autres utilisateurs
		collaborative_filtering.recommandations('user')			Recommander des jeux video pour user
