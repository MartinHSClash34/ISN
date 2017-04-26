from tkinter import *
from random import *
from tkinter.messagebox import *
from winsound import *

Fenetre = Tk()
Fenetre.title("Mastermind")

Noms_Joueurs = []
Scores_Joueurs = []

def Mastermind():
	
	for widget in Fenetre.winfo_children():
		widget.destroy()
		
	try:
		del Nb_Essais_Max
		del Choix_Code
	except:
		pass

	Label_Pseudo = Label(Fenetre, text="Entrez votre pseudo pour enregistrer votre score en cas de victoire :")
	Label_Pseudo.grid(row=1, column=1)
		
	Entree_Pseudo = Entry(Fenetre, textvariable=StringVar())
	Entree_Pseudo.grid(row=1, column=2)
	
	def Recup_Pseudo():
	
		Pseudo = Entree_Pseudo.get()
		if Pseudo == "":
			showwarning("Erreur de syntaxe", "Vous n'avez pas entré de pseudo.")
			Mastermind()
		else:
			Noms_Joueurs.append(Pseudo)
			
			Label_Pseudo.destroy()
			Entree_Pseudo.destroy()
			Bouton_Entrer.destroy()
			
			global Label_Chance
			Label_Chance = Label(Fenetre, text="Bonne chance "+str(Pseudo)+" !", fg="green")
			Label_Chance.grid(row=1, column=1)

	Bouton_Entrer = Button(Fenetre, text="Entrer", command=Recup_Pseudo)
	Bouton_Entrer.grid(row=1, column=3)
			
	def Preparation_Partie():
		
		global Code, Code_Aux, Nb_Essais_Max, Longueur_Code, Chiffres_Acceptees, Choix_Code
		
		try:
			a = int(Nb_Essais_Max)
		except:
			Nb_Essais_Max = Entree_Parametre_1.get()
			Longueur_Code = Entree_Parametre_2.get()
			Chiffres_Acceptees = VariableParametre3.get()
			Choix_Code = VariableParametre4.get()
			
			try:
				a = int(Nb_Essais_Max)
			except:
				showwarning("Erreur de syntaxe", "Le nombre d'essais maximum doit être un nombre entier positif.")
				Mastermind()
				return
			if int(Nb_Essais_Max) < 1:
				showwarning("Erreur de syntaxe", "Le nombre d'essais maximum doit être un nombre entier positif.")
				Mastermind()
				return
			
			try:
				a = int(Longueur_Code)
			except:
				showwarning("Erreur de syntaxe", "La longueur du code doit être un nombre entier positif.")
				Mastermind()
				return
			if int(Longueur_Code) < 1:
				showwarning("Erreur de syntaxe", "La longueur du code doit être un nombre entier positif.")
				Mastermind()
				return
				
			if Chiffres_Acceptees == "Choisissez une valeur":
				showwarning("Erreur de syntaxe", "Veuillez définir les chiffres acceptees.")
				Mastermind()
				return
				
			if Choix_Code == "Choisissez comment":
				showwarning("Erreur de syntaxe", "Veuillez définir un méthode de génération du code.")
				Mastermind()
				return
				
			showwarning("Avertissement", "Un son sera joué à la fin de la partie.\nAugmentez le volume de votre ordinateur pour l'entendre.")
			
			Liste_Widgets = [Label_Pseudo, Entree_Pseudo, Bouton_Entrer, Label_Parametres, Entree_Parametre_1, Entree_Parametre_2, Menu_Parametre_3, Menu_Parametre_4, Bouton_Jouer]
			for widget in Liste_Widgets:
				widget.destroy()
			
			Label_Parametre_1 = Label(Fenetre, text=Nb_Essais_Max, fg="orange")
			Label_Parametre_2 = Label(Fenetre, text=Longueur_Code, fg="orange")
			Label_Parametre_3 = Label(Fenetre, text=Chiffres_Acceptees, fg="orange")
			Label_Parametre_4 = Label(Fenetre, text=Choix_Code, fg="orange")
			
			Label_Parametre_1.grid(row=3, column=2)
			Label_Parametre_2.grid(row=3, column=3)
			Label_Parametre_3.grid(row=3, column=4)
			Label_Parametre_4.grid(row=3, column=5)
			
			Nb_Essais_Max = int(Nb_Essais_Max)
			Longueur_Code = int(Longueur_Code)
			Chiffres_Acceptees = int(Chiffres_Acceptees)

		def Preparation_Essai():
		
			if Nb_Essais < Nb_Essais_Max+1:
				Label_Essai = Label(Fenetre, text="Essai n°" + str(Nb_Essais) + " sur "+str(Nb_Essais_Max)+" :", fg="blue")
				Entree_Essai = Entry(Fenetre, textvariable=StringVar(), width=Longueur_Code)
			
				Label_Essai.grid(row=Nb_Essais+4, column=1)
				Entree_Essai.grid(row=Nb_Essais+4, column=2)
			
				def Verification():
				
					Bouton_Verifier.destroy()
					Essai = Entree_Essai.get()
					Code = Code_Aux[:]
					Bien, Mal, j = 0, 0, 0
					global Nb_Essais
				
					if len(Essai) != Longueur_Code:
						showwarning("Erreur de syntaxe", "Un essai doit respecter les parametres.")
						Preparation_Essai()
						return
					else:
						for i in range(Chiffres_Acceptees + 1, 10):
							if str(i) in Essai:
								showwarning("Erreur de syntaxe", "Un essai doit respecter les parametres.")
								Preparation_Essai()
								return
						try:
							a = int(Essai)
						except:
							showwarning("Erreur de syntaxe", "Un essai doit respecter les parametres.")
							Preparation_Essai()
							return	
							
					Essai = list(Essai)
					EssaiAux = Essai[:]

					while j < len(Code):
						if Essai[j] == Code[j]:
							Bien += 1
							Code.remove(Code[j])
							Essai.remove(Essai[j])
							continue
						else:
							j += 1
					for i in range(len(Essai)):
						if Essai[i] in Code:
							Mal += 1
							for k in range(len(Code)):
								if Essai[i] == Code[k]:
									Position = k
									break
							Code.remove(Code[k])
							
					if Bien == Longueur_Code:
						Entree_Essai.destroy()
						
						Son_Victoire = "Son_Victoire.wav"
						PlaySound(Son_Victoire, SND_NOWAIT)
						
						Label_Essai_Correct = Label(Fenetre, text=EssaiAux, fg="red")
						Label_Gagne = Label(Fenetre, text="Gagné ! Vous avez trouvé le code en "+str(Nb_Essais)+" essai(s).", fg="green")
					
						Label_Essai_Correct.grid(row=Nb_Essais+4, column=2)
						Label_Gagne.grid(row=Nb_Essais+5, column=1)
					
						Rejouer()
					else:
						Entree_Essai.destroy()
					
						Label_Verification = Label(Fenetre, text=str(Bien)+" chiffre(s) bien placé(s) & "+str(Mal)+ " chiffre(s) mal placé(s).")
						Label_Essai_Fixe = Label(Fenetre, text=EssaiAux)
					
						Label_Verification.grid(row=Nb_Essais+4, column=4)
						Label_Essai_Fixe.grid(row=Nb_Essais+4, column=2)
					
						Nb_Essais += 1
						Preparation_Essai()
			
				Bouton_Verifier = Button(Fenetre, text="Vérifier", command=Verification)
				Bouton_Verifier.grid(row=Nb_Essais+4, column=3)
			else:
				Code = Code_Aux[:]
				
				Son_Défaite = "Son_Défaite.wav"
				PlaySound(Son_Défaite, SND_NOWAIT)
				
				Label_Perdu = Label(Fenetre, text="Perdu ! Vous avez utilisé vos "+str(Nb_Essais_Max)+" essais. Le code était "+"".join(Code), fg="red")
				Label_Perdu.grid(row=Nb_Essais+5, column=1)
			
				Rejouer()
		
		if Choix_Code == "...aléatoirement par l'ordinateur":
			global Code, Code_Aux, Nb_Essais
			Code = []
			for i in range(Longueur_Code):
				Code.append(str(randint(0,Chiffres_Acceptees)))
			print(Code)												# À SUPPRIMER
			Code_Aux = Code[:]
			Nb_Essais = 1
			Preparation_Essai()
		else:
			def Recup_Code():
				
				global Code, Code_Aux, Nb_Essais
				Code = Entree_Code.get()
				
				Label_Code.destroy()
				Entree_Code.destroy()
				Bouton_Def_Code.destroy()
				
				try:
					a = int(Code)
				except:
					showwarning("Erreur de syntaxe", "Le code doit respecter les paramètres.")
					Preparation_Partie()
					return
				if len(Code) != Longueur_Code:
					showwarning("Erreur de syntaxe", "Le code doit respecter les paramètres.")
					Preparation_Partie()
					return
				else:
					for i in range(Chiffres_Acceptees + 1, 10):
						if str(i) in Code:
							showwarning("Erreur de syntaxe", "Le code doit respecter les paramètres.")
							Preparation_Partie()
							return
				Code = list(Code)
				print(Code) 										# À SUPPRIMER
				Code_Aux = Code[:]
				Nb_Essais = 1
				
				Preparation_Essai()
			
			Bouton_Jouer.destroy()
			
			Label_Code = Label(Fenetre, text="Définissez un code pour l'autre joueur :")
			Entree_Code = Entry(Fenetre, textvariable=StringVar(), width=Longueur_Code)
			Bouton_Def_Code = Button(Fenetre, text="Définir", command=Recup_Code)
				
			Label_Code.grid(row=4, column=1)
			Entree_Code.grid(row=4, column=2)
			Bouton_Def_Code.grid(row=4, column=3)

		def Rejouer():
			
			global Label_Chance, Pseudo
			
			try:
				Label_Chance.destroy()
				del Label_Chance
			except:
				pass
			
			try:
				del Pseudo
			except:
				pass
			
			if len(Noms_Joueurs) != len(Scores_Joueurs):
				if Nb_Essais <= Nb_Essais_Max:
					Ajout_Score = str(Nb_Essais)+" essai(s) utilisé(s) sur "+str(Nb_Essais_Max)+" maximum pour un code à "+str(Longueur_Code)+" chiffre(s)."
					Scores_Joueurs.append(Ajout_Score)
				else:
					del Noms_Joueurs[-1]
				
			def Aff_Scores():
			
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
				Bouton_Aff_Scores = Button(Fenetre, text="Afficher les scores", command=Aff_Scores)
				Bouton_Aff_Scores.grid(row=Nb_Essais+5, column=3)
			
			Bouton_Quitter = Button(Fenetre, text="Quitter", fg="red", command=exit)
			Bouton_Quitter.grid(row=Nb_Essais+5, column=4)
	
	Label_Parametres = Label(Fenetre, text="Choisissez vos paramètres de jeu :")
	Label_Parametre_1 = Label(Fenetre, text="Nombre d'essais maximum", fg="blue")
	Label_Parametre_2 = Label(Fenetre, text="Longueur du code", fg="purple")
	Label_Parametre_3 = Label(Fenetre, text="Chiffres acceptées, de 0 à (votre valeur)", fg="brown")
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

	Bouton_Jouer = Button(Fenetre, text="Jouer", command=Preparation_Partie, fg="red")
	Bouton_Jouer.grid(row=4, column=1)
			
Mastermind()

Fenetre.mainloop()