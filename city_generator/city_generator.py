import turtle
import random


class Building:
	def __init__(self, x, y):
		#Largeur du Building
		self.largeur = 140
		#Hauteur d'un étage
		self.hauteurEtage = 60
		#Hauteur du Building
		self.nbrEtage = random.randint(1, 8)
		#Couleur de l'immeuble

		self.couleur = random.choice(self.Couleurs())
		#Epaisseur contour de l'immeuble et couleur
		self.traitCouleur = "black"
		self.traitEpaisseur = 3
		self.turtle = turtle.Turtle()
		self.screen = turtle.Screen()
		self.screen.setup(width=1.0, height=1.0)
		#Suppression de la "fleche" Turtle
		self.turtle.hideturtle()
		#Vitesse de dessin maximum
		self.turtle.speed(0)

		#Initialisation des paramètres du trait
		self.turtle.pencolor(self.traitCouleur)
		self.turtle.pensize(self.traitEpaisseur)
		self.turtle.setheading(0)

		#Coordonnées du niveau 0
		self.X0 = x
		self.Y0 = y

	def ConstruireImmeuble(self):
		self.turtle.penup()
		#Initialise le curseur au centre du canvas
		self.turtle.goto(self.X0, self.Y0)
		self.turtle.pendown()
		#Couleur de fond
		self.turtle.fillcolor(self.couleur)
		self.turtle.begin_fill()
		self.turtle.forward(self.largeur)
		self.turtle.left(90)
		self.turtle.forward(self.hauteurEtage * self.nbrEtage)
		self.turtle.left(90)
		self.turtle.forward(self.largeur)
		self.turtle.left(90)
		self.turtle.forward(self.hauteurEtage * self.nbrEtage)
		self.turtle.end_fill()
		self.turtle.left(90)
		self.AjoutEtage()
		self.AjoutToit()

		self.RezDeChausse(self.X0, self.Y0)

	def AjoutEtage(self):
		if self.nbrEtage > 1:

			Y1 = self.Y0 + self.hauteurEtage

			for numEtage in range(self.nbrEtage - 1):
				self.AjoutFenetre(self.X0, Y1)
				self.turtle.penup()
				self.turtle.goto(self.X0, Y1)
				self.turtle.pendown()
				self.turtle.forward(self.largeur)
				Y1 = Y1 + self.hauteurEtage

		else:
			return

	def AjoutToit(self):
		X0 = self.X0 - 15
		Y0 = self.Y0 + (self.hauteurEtage * self.nbrEtage)
		self.turtle.penup()
		self.turtle.goto(X0, Y0)
		self.turtle.pendown()
		self.turtle.fillcolor("#000000")
		self.turtle.begin_fill()
		styleToit = random.choice(["plat", "triangle"])

		if styleToit == "plat":
			self.turtle.forward(self.largeur + 30)
			self.turtle.left(90)
			self.turtle.forward(10)
			self.turtle.left(90)
			self.turtle.forward(self.largeur + 30)
			self.turtle.left(90)
			self.turtle.forward(10)
			self.turtle.left(90)
		elif styleToit == "triangle":
			self.turtle.forward(self.largeur + 30)
			self.turtle.left(150)
			self.turtle.forward(98.15)
			self.turtle.left(60)
			self.turtle.forward(98.15)
			self.turtle.left(150)
		self.turtle.end_fill()

	def AjoutFenetre(self, x, y):
		X0 = x + 15

		for nbFenetre in range(3):
			typefenetre = random.choice(["fenetre", "portefenetre"])
			if typefenetre == "fenetre":
				Y0 = y + 20
			else:
				Y0 = y
			self.turtle.penup()
			self.turtle.goto(X0, Y0)
			self.turtle.pendown()
			self.turtle.fillcolor("#FFFFFF")
			self.turtle.begin_fill()

			for x in range(1, 5):
				hauteur = 30
				if x % 2 == 0 and typefenetre == "portefenetre":
					hauteur = 50
				self.turtle.forward(hauteur)
				self.turtle.left(90)

			self.turtle.end_fill()
			if typefenetre == "portefenetre":
				self.turtle.penup()
				self.turtle.goto(X0 - 5, Y0)
				self.turtle.pendown()
				#Cadre de la grille de la porte fenetre
				self.turtle.forward(40)
				self.turtle.left(90)
				self.turtle.forward(25)
				self.turtle.left(90)
				self.turtle.forward(40)
				self.turtle.left(90)
				self.turtle.forward(25)
				self.turtle.left(90)
				#grille
				self.turtle.penup()
				self.turtle.goto(X0, Y0)
				self.turtle.pendown()
				self.turtle.left(90)
				Xbarre = X0 + 5
				for barre in range(1, 8):

					self.turtle.penup()
					self.turtle.goto(Xbarre, Y0)
					self.turtle.pendown()
					self.turtle.forward(25)
					Xbarre = Xbarre + 5

				self.turtle.left(270)

			self.turtle.pencolor = "black"
			X0 = X0 + 40

	def Couleurs(self):
		number_of_colors = 100

		color = [
		    "#" + ''.join(
		        [random.choice('0123456789ABCDEF') for j in range(6)])
		    for i in range(number_of_colors)
		]
		return color

	def AjoutPorte(self, x, y):
		self.turtle.penup()
		self.turtle.goto(x, y)
		self.turtle.pendown()
		self.turtle.fillcolor(random.choice(self.Couleurs()))
		self.turtle.begin_fill()
		self.turtle.forward(30)
		self.turtle.left(90)
		self.turtle.forward(50)
		self.turtle.left(90)
		self.turtle.forward(30)
		self.turtle.left(90)
		self.turtle.forward(50)
		self.turtle.left(90)
		self.turtle.end_fill()

	def RezDeChausse(self, x, y):
		X0 = x + 15
		PossedePorte = False
		for nbFenetre in range(3):

			if PossedePorte == False and nbFenetre < 2:
				type = random.choice(["fenetre", "porte"])
			elif PossedePorte == False and nbFenetre == 2:
				type = "porte"
			elif PossedePorte == True:
				type = "fenetre"

			if type == "fenetre":
				Y0 = y + 20
			else:
				Y0 = y
				PossedePorte = True

			self.turtle.penup()
			self.turtle.goto(X0, Y0)
			self.turtle.pendown()
			if type == "fenetre":
				self.turtle.fillcolor("#FFFFFF")
			else:
				self.turtle.fillcolor(random.choice(self.Couleurs()))

			self.turtle.begin_fill()

			for x in range(1, 5):

				hauteur = 30
				if x % 2 == 0 and type == "porte":
					hauteur = 50
				self.turtle.forward(hauteur)
				self.turtle.left(90)

			self.turtle.end_fill()
			X0 = X0 + 40


Maison1 = Building(-380, -280)
Maison1.ConstruireImmeuble()

Maison2 = Building(-200, -280)
Maison2.ConstruireImmeuble()

Maison3 = Building(-20, -280)
Maison3.ConstruireImmeuble()

Maison4 = Building(160, -280)
Maison4.ConstruireImmeuble()
