from tkinter import * # La syntaxe "from [module] import *" évite d'avoir à écrire "[module].[fonction]" chaque fois que l'on utilise une fonction du module
from random import *
from tkinter.messagebox import *

Fenetre = Tk() # Création de la fenêtre
Fenetre.title("Mastermind") # Définition du titre de la fenêtre

# Création de listes vides qui accueilleront les scores et les pseudos
Noms_Joueurs = [] 
Scores_Joueurs = []

def Mastermind(): # Fonction mère qui affiche les widgets (éléments de la fenêtre) pour le pseudo et les paramètres et qui contient également les autres fonctions
	
	for widget in Fenetre.winfo_children(): # "Fenetre.winfo_children" est la liste de tous les widgets de la fenêtre
		widget.destroy() # D'abord suppression tous les widgets pour (re)commencer une partie
	
	try: # On utilise "try" pour cette suppression de variable car il est normal que ce paramètre ne soit pas encore défini au début de la première partie
		global Nb_Essais_Max # "global" définit la variable comme locale aussi à cette fonction et non locale seulement à la fonction où elle est définie
		del Nb_Essais_Max # Suppression de ce paramètre pour que le "try" de la fonction Recuperation_Parametres fonctionne lors de parties successives
	except:
		pass

	Label_Pseudo = Label(Fenetre, text="Entrez votre pseudo pour enregistrer votre score en cas de victoire :") # Un "Label" est un widget affichant du texte
	Entree_Pseudo = Entry(Fenetre, textvariable=StringVar()) # Une "Entry" est un widget permettant au joueur de rentrer qqch dans un champ de saisie
	
	Label_Pseudo.grid(row=1, column=1) # La méthode "grid" permet d'organiser les widgets en tableau (lignes et colonnes)
	Entree_Pseudo.grid(row=1, column=2)

	def Recuperation_Pseudo(): # Fonction récupérant et vérifiant le pseudo du joueur dans le champ de saisie dédié

		Pseudo = Entree_Pseudo.get() # ".get()" récupère le contenu d'une entrée sous forme de chaîne de caractères 
	
		if Pseudo == "": # On vérifie que le joueur a bien entré un pseudo
			showwarning("Erreur de syntaxe", "Vous n'avez pas entré de pseudo.") # Un "showwarning" est une fenêtre pop-up utilisée pour afficher un message d'avertissement, c'est la seule fonction du module "tkinter.messagebox" qui est utilisée
			pass
		else:
			Noms_Joueurs.append(Pseudo)
		
			# Suppression des widgets (devenus obsolètes) qui ont permis au joueur d'entrer son pseudo
			Label_Pseudo.destroy()
			Entree_Pseudo.destroy()
			Bouton_Entrer.destroy()
		
			Label_Chance = Label(Fenetre, text="Bonne chance "+str(Pseudo)+" !", fg="green")
			Label_Chance.grid(row=1, column=1)

	Bouton_Entrer = Button(Fenetre, text="Entrer", command=Recuperation_Pseudo) # Un "Button" est un widget affichant un bouton dont on exécute la commande par un clic gauche dessus
	Bouton_Entrer.grid(row=1, column=3)
			
	def Recuperation_Parametres(): # Fonction récupèrant les paramètres de jeu dans les widgets dédiés
		
		global Code, Code2, Nb_Essais_Max, Longueur_Code, Chiffres_Admis, Choix_Code, Nb_Essais
		
		try: # Ce "try" vérifie si les paramètres ont déjà été définis si on rappelle plus tard cette fontion si la syntaxe du code s'il est défini manuellement est incorrecte
			a = int(Nb_Essais_Max) # La vérification de seulement un seul paramètre est nécessaire
		except:
			# Récupération des paramètres
			Nb_Essais_Max = Entree_Parametre_1.get() 
			Longueur_Code = Entree_Parametre_2.get()
			Chiffres_Admis = VariableParametre3.get()
			Choix_Code = VariableParametre4.get()
			
			# Les boucles "if" et les "try" qui vont suivre vérifient la syntaxe des paramètres récupérés, et rappelle la fonction Mastermind en cas d'erreur pour que le joueur les redéfinisse correctement

			try:
				a = int(Nb_Essais_Max)
			except:
				showwarning("Erreur de syntaxe", "Le nombre d'essais maximum doit être un nombre entier positif.")
				pass
				return # "return" stoppe l'exécution de la fonction dans laquelle il se trouve (comme un "break" dans une boucle while), ici on retourne uniquement à la fonction Mastermind
			if int(Nb_Essais_Max) < 1:
				showwarning("Erreur de syntaxe", "Le nombre d'essais maximum doit être un nombre entier positif.")
				pass
				return
			
			try:
				a = int(Longueur_Code)
			except:
				showwarning("Erreur de syntaxe", "La longueur du code doit être un nombre entier positif.")
				pass
				return
			if int(Longueur_Code) < 1:
				showwarning("Erreur de syntaxe", "La longueur du code doit être un nombre entier positif.")
				pass
				return
				
			if Chiffres_Admis == "Choisissez une valeur":
				showwarning("Erreur de syntaxe", "Veuillez définir les chiffres admis dans le code.")
				pass
				return
				
			if Choix_Code == "Choisissez comment":
				showwarning("Erreur de syntaxe", "Veuillez définir un méthode de génération du code.")
				pass
				return
			
			Liste_Widgets = [Label_Pseudo, Entree_Pseudo, Bouton_Entrer, Label_Parametres, Entree_Parametre_1, Entree_Parametre_2, Menu_Parametre_3, Menu_Parametre_4, Bouton_Jouer]
			for widget in Liste_Widgets:			 
				widget.destroy() # Suppression des widgets qui ont permis au joueur de définir les paramètres
			
			# On les remplace par des labels (fixes, donc) pour que les paramètres ne puissent plus être changés, mais restent quand même visibles
			
			Label_Parametre_1 = Label(Fenetre, text=Nb_Essais_Max, fg="orange")
			Label_Parametre_2 = Label(Fenetre, text=Longueur_Code, fg="orange")
			Label_Parametre_3 = Label(Fenetre, text=Chiffres_Admis, fg="orange")
			Label_Parametre_4 = Label(Fenetre, text=Choix_Code, fg="orange")
			
			Label_Parametre_1.grid(row=3, column=2)
			Label_Parametre_2.grid(row=3, column=3)
			Label_Parametre_3.grid(row=3, column=4)
			Label_Parametre_4.grid(row=3, column=5)
			
			# Changement du type des variables des paramètres pour qu'ils soient des nombres entiers utilisables mathématiquement dans les fonctions suivantes
			
			Nb_Essais_Max = int(Nb_Essais_Max)
			Longueur_Code = int(Longueur_Code)
			Chiffres_Admis = int(Chiffres_Admis)

		def Preparation_Essai(): # Fonction affichant les widgets dédiés à la saisie de l'essai par le joueur
			
			global Nb_Essais_Max, Nb_Essais
			
			if Nb_Essais < Nb_Essais_Max+1:	# On vérifie qu'il reste des essais au joueur
				Label_Essai = Label(Fenetre, text="Essai n°" + str(Nb_Essais) + " sur "+str(Nb_Essais_Max)+" :", fg="blue")
				Entree_Essai = Entry(Fenetre, textvariable=StringVar(), width=Longueur_Code)
			
				Label_Essai.grid(row=Nb_Essais+4, column=1)
				Entree_Essai.grid(row=Nb_Essais+4, column=2)
			
				def Diagnostic(): # Fonction établissant le diagnostic de l'essai rentré
					
					Essai = Entree_Essai.get() # On récupère l'essai du joueur
					
					Code = Code2[:] # Le code récupère sa valeur initiale
					Bien, Mal, j = 0, 0, 0 # On réinitialise les variables du diagnostic
					global Nb_Essais
					
					if len(Essai) != Longueur_Code: # Cette boucle "if" vérifie la syntaxe de l'essai
						showwarning("Erreur de syntaxe", "Un essai doit respecter les parametres.")
						pass
						return
					else:
						for i in range(Chiffres_Admis + 1, 10):
							if str(i) in Essai:
								showwarning("Erreur de syntaxe", "Un essai doit respecter les parametres.")
								pass
								return
						try:
							a = int(Essai)
						except:
							showwarning("Erreur de syntaxe", "Un essai doit respecter les parametres.")
							pass
							return	
					
					# On supprime ces boutons car ils seront réaffichés pour l'essai suivant
					
					Bouton_Diagnostiquer.destroy()
					Bouton_Abandonner.destroy()
					
					Essai = list(Essai) # Changement du type de variable de l'essai en "liste" pour diagnostiquer individuellement chaque chiffre
					EssaiAux = Essai[:] # Définition d'une variable égale à l'essai pour garder sa valeur initiale qui sera réutilisée car certains chiffres de l'essai pourront être supprimés lors du diagnostic
					
					while j < len(Code): # Diagnostic des chiffres de l'essai présents à la même place dans le code, ce sont des chiffres "bien placés"
						if Essai[j] == Code[j]:
							Bien += 1
							# Suppression des chiffres identiques pour la boucle suivante
							Code.remove(Code[j])
							Essai.remove(Essai[j])
							continue
						else:
							j += 1
					
					for i in range(len(Essai)): # Cette boucle "for" diagnostique si des chiffres restants dans l'essai sont aussi présents dans le code, ils y seront obligatoirement à des places différentes, ce seront des chiffres "mal placés"
						if Essai[i] in Code:
							Mal += 1
							for k in range(len(Code)):
								if Essai[i] == Code[k]:
									Position = k
									break
							Code.remove(Code[k]) # Suppression des chiffres "mal placés" dans le code au fur et à mesure pour ne pas compter plusieurs fois les mêmes
							
					if Bien == Longueur_Code: # S'il y a autant de chiffres "bien placés" que de chiffres dans le code, la partie est terminée, c'est une victoire
						Entree_Essai.destroy()
						
						try: # Ce "try" essaie de jouer un son en cas de victoire, et ignore toute erreur en cas d'erreur d'importation préalable
							Son_Victoire = "Son_Victoire.wav" # "Son_Victoire.wav" est un des fichiers audio téléchargés avec le programme
							winsound.PlaySound(Son_Victoire, winsound.SND_NOWAIT)
						except:
							pass
						
						Label_Essai_Correct = Label(Fenetre, text=EssaiAux, fg="red")
						Label_Gagne = Label(Fenetre, text="Gagné ! Vous avez trouvé le code en "+str(Nb_Essais)+" essai(s).", fg="green")
					
						Label_Essai_Correct.grid(row=Nb_Essais+4, column=2)
						Label_Gagne.grid(row=Nb_Essais+5, column=1)
					
						Rejouer() # La partie est finie, on exécute la fonction "Rejouer"
					else: # Si l'essai n'est pas identique au code, on affiche le diagnostic"
						Entree_Essai.destroy()
					
						Label_Verification = Label(Fenetre, text=str(Bien)+" chiffre(s) bien placé(s) & "+str(Mal)+ " chiffre(s) mal placé(s).")
						Label_Essai_Fixe = Label(Fenetre, text=EssaiAux)
					
						Label_Verification.grid(row=Nb_Essais+4, column=4)
						Label_Essai_Fixe.grid(row=Nb_Essais+4, column=2)
					
						Nb_Essais += 1
						Preparation_Essai() # On réexécute la fonction Preparation_Essai pour préparer le diagnostic de l'essai suivant
				
				global Rejouer
				def Rejouer(): # Fonction permettant au joueur de rejouer directement
			
					global Pseudo, Label_Chance
			
					Liste = [Label_Essai, Entree_Essai, Bouton_Diagnostiquer, Bouton_Abandonner] # En cas d'abandon, on supprime les widgets du dernier essai qui n'ont pas été supprimés par la fonction Diagnostic 
					for widget in Liste:
						widget.destroy()
					
					try:
						Label_Chance.destroy()
					except:
						pass
					
					try:
						del Pseudo
					except:
						pass
			
					if len(Noms_Joueurs) != len(Scores_Joueurs): # On vérifie si le joueur a entré un pseudo
						if Nb_Essais <= Nb_Essais_Max: # Si le joueur a gagné, on ajoute son score à son pseudo
							Ajout_Score = str(Nb_Essais)+" essai(s) utilisé(s) sur "+str(Nb_Essais_Max)+" maximum pour un code à "+str(Longueur_Code)+" chiffre(s)."
							Scores_Joueurs.append(Ajout_Score)
						else: # Sinon, on supprime son pseudo
							del Noms_Joueurs[-1]
				
					def Afficher_Scores(): # Fonction affichant les scores précédents
			
						Bouton_Aff_Scores.destroy()
				
						Label_Nom = Label(Fenetre, text="Pseudo", fg="blue")
						Label_Score = Label(Fenetre, text="Score", fg="blue")
				
						Label_Nom.grid(row=Nb_Essais+6, column=1)
						Label_Score.grid(row=Nb_Essais+6, column=2)
						
						for i in range(len(Noms_Joueurs)):
							Label_Joueurs = Label(Fenetre, text=Noms_Joueurs[i])
							Label_Scores_Joueurs = Label(Fenetre, text=Scores_Joueurs[i])
					
							Label_Joueurs.grid(row=Nb_Essais+7+i, column=1)
							Label_Scores_Joueurs.grid(row=Nb_Essais+7+i, column=2)
					
					Bouton_Rejouer = Button(Fenetre, text="Rejouer", fg="green", command=Mastermind)
					Bouton_Rejouer.grid(row=Nb_Essais+5, column=2)	
			
					if Noms_Joueurs != []:
						Bouton_Aff_Scores = Button(Fenetre, text="Afficher les scores", command=Afficher_Scores)
						Bouton_Aff_Scores.grid(row=Nb_Essais+5, column=3)
			
					Bouton_Quitter = Button(Fenetre, text="Quitter", fg="red", command=exit)
					Bouton_Quitter.grid(row=Nb_Essais+5, column=4)
				
				Bouton_Diagnostiquer = Button(Fenetre, text="Diagnostiquer", command=Diagnostic)
				Bouton_Diagnostiquer.grid(row=Nb_Essais+4, column=3)
				
				Bouton_Abandonner = Button(Fenetre, text="Abandonner", command=Rejouer, fg="red")
				Bouton_Abandonner.grid(row=Nb_Essais+4, column=4)
			else:
				try:
					Son_Défaite = "Son_Défaite.wav" # "Son_Défaite.wav" est un des fichiers audio téléchargés avec le programme
					winsound.PlaySound(Son_Défaite, winsound.SND_NOWAIT)
				except:
					pass
				
				Label_Perdu = Label(Fenetre, text="Perdu ! Vous avez utilisé votre(vos) "+str(Nb_Essais_Max)+" essai(s). Le code était "+"".join(Code2), fg="red")
				Label_Perdu.grid(row=Nb_Essais+5, column=1)
				
				Rejouer()
		
		if Choix_Code == "...aléatoirement par l'ordinateur":
			global Code, Code2
			Code = []
			for i in range(Longueur_Code):
				Code.append(str(randint(0,Chiffres_Admis))) # "randit" est la seule fonction du module "random" que l'on importe, elle choisit un entier aléatoire entre 2 arguments a et b entiers inclus
			print(Code)												# À SUPPRIMER
			Code2 = Code[:]
			Nb_Essais = 1
			try: # Le module "winsound" n'est pas disponible sur Mac, on utilise "try" pour essayer de l'importer
				import winsound 
				showwarning("Avertissement", "Un son sera joué à la fin de la partie.\nActivez et/ou augmentez le volume de votre ordinateur pour l'entendre.")
			except: # Exécute quelque chose en cas d'erreur
				pass # "pass" n'exécute rien, mais "except" est obligatoire s'il y a un "try" avant (ici, on ignore une erreur d'importation)
			
			Preparation_Essai()
		else:
			def Recuperation_Code(): # Fonction récupérant le code s'il est défini manuellement
				
				global Code, Code2, Nb_Essais
			
				Code = Entree_Code.get() # On récupère le code proposé par le second joueur
				
				Label_Code.destroy()
				Entree_Code.destroy()
				Bouton_Code.destroy()
				
				try:
					a = int(Code)
				except:
					showwarning("Erreur de syntaxe", "Le code doit respecter les paramètres.")
					pass
					return
				if len(Code) != Longueur_Code:
					showwarning("Erreur de syntaxe", "Le code doit respecter les paramètres.")
					pass
					return
				else:
					for i in range(Chiffres_Admis + 1, 10):
						if str(i) in Code:
							showwarning("Erreur de syntaxe", "Le code doit respecter les paramètres.")
							pass
							return
							
				Code = list(Code)
				print(Code) 										# À SUPPRIMER
				Code2 = Code[:]
				Nb_Essais = 1
				try:
					import winsound
					showwarning("Avertissement", "Un son sera joué à la fin de la partie.\nActivez et/ou augmentez le volume de votre ordinateur pour l'entendre.")
				except:
					pass
				
				Preparation_Essai()
			
			Bouton_Jouer.destroy()
			
			# Les widgets suivants sont ceux relatifs à la définition du code par le second joueur
			
			Label_Code = Label(Fenetre, text="Définissez un code pour l'autre joueur :")
			Entree_Code = Entry(Fenetre, textvariable=StringVar(), width=Longueur_Code)
			Bouton_Code = Button(Fenetre, text="Définir", command=Recuperation_Code)
				
			Label_Code.grid(row=4, column=1)
			Entree_Code.grid(row=4, column=2)
			Bouton_Code.grid(row=4, column=3)
	
	# Les derniers widgets sont ceux relatifs à la définition des paramètres par le joueur
	
	Label_Parametres = Label(Fenetre, text="Choisissez vos paramètres de jeu :")
	Label_Parametre_1 = Label(Fenetre, text="Nombre d'essais maximum", fg="blue")
	Label_Parametre_2 = Label(Fenetre, text="Longueur du code", fg="purple")
	Label_Parametre_3 = Label(Fenetre, text="Chiffres admis dans le code, de 0 à (votre valeur)", fg="brown")
	Label_Parametre_4 = Label(Fenetre, text="Code généré...")
	
	Entree_Parametre_1 = Entry(Fenetre, textvariable=StringVar())
	Entree_Parametre_2 = Entry(Fenetre, textvariable=StringVar())
	
	VariableParametre3 = StringVar()
	VariableParametre3.set("Choisissez une valeur")
	Menu_Parametre_3 = OptionMenu(Fenetre, VariableParametre3, "1", "2", "3", "4", "5", "6", "7", "8", "9")
	VariableParametre4 = StringVar()
	VariableParametre4.set("Choisissez comment")
	Menu_Parametre_4 = OptionMenu(Fenetre, VariableParametre4, "...aléatoirement par l'ordinateur", "...manuellement par un autre joueur")
	
	Label_Parametres.grid(row=2, column=1)
	Label_Parametre_1.grid(row=2, column=2)
	Label_Parametre_2.grid(row=2, column=3)
	Label_Parametre_3.grid(row=2, column=4)
	Label_Parametre_4.grid(row=2, column=5)
	Entree_Parametre_1.grid(row=3, column=2)
	Entree_Parametre_2.grid(row=3, column=3)
	Menu_Parametre_3.grid(row=3, column=4)
	Menu_Parametre_4.grid(row=3, column=5)

	Bouton_Jouer = Button(Fenetre, text="Jouer", command=Recuperation_Parametres, fg="red")
	Bouton_Jouer.grid(row=4, column=1)
	
Mastermind() # La première exécution de la fonction Mastermind

Fenetre.mainloop() # On lance la boucle qui affiche la fenêtre