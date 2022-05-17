###################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet synthèse
###  Nom: Philippe Bertrand
###  Description du fichier: Programme principal
####################################################################################
#importation du module sys nécessaire à l'exécution de l'application
import sys

#Importation de jsonpickle
import jsonpickle

#Importation du fichier Qt Designer UI converti en PY
import EntrepriseInterface as F

#Importation des librairies nécessaires à QtDesigner
from PyQt5 import QtWidgets, QtCore

#Importation des classes
import cEmploye as E
import cFichePaie as P
import datetime as DT
import cTypeEmploie as T
import cAdmin as A


#Création de la liste lsEmployes
lsEmployes = []


#Instanciation d'objets
lsEmployes.append(E.Employe("H-2345","Philippe","Bertrand", "819-827-4693","Marketing", 60.00))
lsEmployes.append(E.Employe("P-2567", "Jean", "Lasalle", "819-856-4111", "Superviseur", 120.00))
lsEmployes.append(E.Employe("W-5555", "Marine", "Lepen", "819-856-0002", "Superviseur", 55.55))
lsEmployes.append(E.Employe("K-6395", "Emmanuel", "Macron", "819-427-4569", "Comptabilité", 51.99))
lsEmployes.append(E.Employe("L-2789", "Jean-Luc", "Mélenchon", "810-555-5555", "Gestion", 149.00))

#Création de la liste lsTypeEmploye

lsTypeEmploye = []

#Instanciation d'objets

lsTypeEmploye.append(T.T_TempsPartiel("", "", ""))
lsTypeEmploye.append(T.T_SurAppel("", "" , ""))
lsTypeEmploye.append(T.T_TempsPlein("", "", ""))

#Création de la liste lsFichePaie

lsFichePaie = []

#Instanciation d'objets

lsFichePaie.append(P.FichePaie(lsEmployes[0], "A1A1A1A1A1",DT.datetime.now(), 30, 900, lsTypeEmploye[0], 0.10, 810))
lsFichePaie.append(P.FichePaie(lsEmployes[1], "B2B2B2B2B2", DT.datetime.now(), 60, 7200, lsTypeEmploye[2],0.40, 4320))
lsFichePaie.append(P.FichePaie(lsEmployes[2], "C3C3C3C3C3", DT.datetime.now(), 20, 2222, lsTypeEmploye[1], 0.20, 1777.6))
lsFichePaie.append(P.FichePaie(lsEmployes[3], "D4D4D4D4D4", DT.datetime.now(), 50, 2599.5, lsTypeEmploye[2], 0.40, 1559.7 ))
lsFichePaie.append(P.FichePaie(lsEmployes[4], "E5E5E5E5E5", DT.datetime.now(), 25, 3725, lsTypeEmploye[1],0.20, 2980))

#Création de la liste lsRecherche

lsRecherche = []

#Création de la classe FenetreQt
#Héritage des librairies Qt et MainWindow
class FenetreQt(QtWidgets.QMainWindow, F.Ui_EntrepriseGestion):
    """
    Classe qui représente l'interface graphique de l'application
    """

    def __init__(self, parent = None):
        """
        Constructeur de la classe FenetreQt qui représente l'interface graphique
        :param parent:
        """
        super(FenetreQt,self).__init__(parent) #Appel du constructeur des classes parent
        self.setupUi(self)  #initialise l'interface graphique


        self.setWindowTitle("Entreprise") #Titre du form
        self.setFixedSize(400, 400) #Dimensions du form
        self.lblTitre.setText("Bienvenue sur le site de l'entreprise") #Titre du Menu
        self.gbxMenu.setGeometry(QtCore.QRect(40, 50, 331, 330)) #Visible
        self.gbxAjouterModifierSupprimer.setGeometry(QtCore.QRect(1200, 350, 120, 60)) #Caché
        self.gbxModifSupp.setGeometry(QtCore.QRect(1200, 350, 120, 60)) #Caché
        self.gbxFichePaie.setGeometry(QtCore.QRect(1200, 350, 120, 60)) #Caché
        self.gbxRecherche.setGeometry(QtCore.QRect(1200, 350, 120, 60)) #Caché
        self.gbxConnexion.setGeometry(QtCore.QRect(1200, 350, 120, 60))  # Caché



        #Alimenter le combobox des types d'emploies possible pour l'employé
        self.cboTypeEmploie.addItem("Temps plein")
        self.cboTypeEmploie.addItem("Temps partiel")
        self.cboTypeEmploie.addItem("Sur appel")
        #Alimenter le combobox des critères de recherche pour la modification ou supprimation d'un employé
        self.cboCritereRechModif.addItem("Numéro d'identification")
        self.cboCritereRechModif.addItem("Prénom")
        self.cboCritereRechModif.addItem("Nom")
        self.cboCritereRechModif.addItem("Numéro de téléphone")
        #Alimenter le combobox des critères de recherche seulement pour but de rechercher un employé
        self.cboCritereSearch.addItem("Numéro d'identification")
        self.cboCritereSearch.addItem("Prénom")
        self.cboCritereSearch.addItem("Numéro de téléphone")
        self.cboCritereSearch.addItem("Fonction")


    #Afficher la liste des employés
    @QtCore.pyqtSlot()
    def on_btnAfficher_clicked(self):
            """
            Méthode d'événement clicked sur le bouton btnAfficher du Menu
            :return:
            """

            # Configuration graphique pour l'option Afficher
            self.setFixedSize(600, 611)  # Dimensions du form pour Afficher
            self.lblTitre.setText("Liste des employés")  # Titre pour Afficher
            self.gbxMenu.setGeometry(QtCore.QRect(1200, 10, 120, 60))  # Caché
            self.txtMessage.setGeometry(QtCore.QRect(10, 70, 561, 381))  # Visible
            self.gbxAjouterModifierSupprimer.setGeometry(QtCore.QRect(1200, 150, 120, 60))  # Caché
            self.gbxModifSupp.setGeometry(QtCore.QRect(1200, 330, 120, 60))  # Caché
            self.gbxFichePaie.setGeometry(QtCore.QRect(1200, 350, 120, 60)) #Caché
            self.gbxRecherche.setGeometry(QtCore.QRect(1200, 350, 120, 60)) #Caché
            #Affichage de la chaine dans txtMessage
            Chaine = ""
            for objEmploye in lsEmployes:
                Chaine +=str(objEmploye)

            self.txtMessage.setText(Chaine)

    #Se connecter sur le site
    @QtCore.pyqtSlot()
    def on_btnConnexion_clicked(self):
        """
        Méthode d'événement clicked du bouton btnConnexion du gbxConnexion
        :return:
        """

        #Configuration graphique pour le btnConnexion

        self.setFixedSize(400, 400)  # Dimensions du form
        self.lblTitre.setText("Bienvenue sur le site de l'entreprise")  # Titre du Menu
        self.gbxConnexion.setGeometry(QtCore.QRect(40, 50, 331, 291))  # Visible
        self.gbxAjouterModifierSupprimer.setGeometry(QtCore.QRect(1200, 350, 120, 60))  # Caché
        self.gbxModifSupp.setGeometry(QtCore.QRect(1200, 350, 120, 60))  # Caché
        self.gbxFichePaie.setGeometry(QtCore.QRect(1200, 350, 120, 60))  # Caché
        self.gbxRecherche.setGeometry(QtCore.QRect(1200, 350, 120, 60))  # Caché
        self.gbxMenu.setGeometry(QtCore.QRect(1200, 350, 120, 60))  # Caché


        #Création d'un message d'erreur si la validation est invalide
        MessageErreur = ""

        #Instanciation de la classe Admin
        Admin_ = A.Admin()

        #Validation du nom d'identifiant Admin

        NomAdmin_ = self.txtNomAdmin.text()
        Admin_.NomDeAdmin = NomAdmin_
        if Admin_.NomDeAdmin != NomAdmin_:
            MessageErreur += "Le nom d'utilisateur admin est invalide !\n"
            self.txtNomAdmin.setText("")    #On efface le résultat invalide

        #Validation du mot de passe du compte Admin

        MdpAdmin_ = self.txtMdpAdmin.text()
        Admin_.AdminMdp = MdpAdmin_
        if Admin_.AdminMdp != MdpAdmin_:
            MessageErreur += "Le mot de passe admin est invalide !\n"
            self.txtMdpAdmin.setText("")    #On efface le résultat invalide

        #Si les validations sont bonnes, on affiche le menu du site et on enlève le gbxConnexion

        if MessageErreur == "":
            self.gbxMenu.setGeometry(QtCore.QRect(40, 50, 331, 291))
            self.gbxConnexion.setGeometry(QtCore.QRect(2000, 300, 120, 60))

        #Autres résultats invalides

        else:
            MessageErreur += "Veuillez rentrer les bonnes informations du compte admin"

    #Affichage des fiches de paies précédentes
    @QtCore.pyqtSlot()
    def on_btnAfficherPaie_clicked(self):
        """
        Méthode d'événement de type clicked du bouton (btnAfficherPaie)
        Affiche le txtMessage comme pour la liste des employés
        :return:
        """
        #Configuration graphique pour le btnAfficherPaie

        self.setFixedSize(600, 611)  # Dimensions du form pour Afficher
        self.lblTitre.setText("Historique des fiches de paie")  # Titre pour Afficher
        self.gbxMenu.setGeometry(QtCore.QRect(1200, 10, 120, 60))  # Caché
        self.txtMessage.setGeometry(QtCore.QRect(10, 70, 561, 381))  # Visible
        self.gbxAjouterModifierSupprimer.setGeometry(QtCore.QRect(1200, 150, 120, 60))  # Caché
        self.gbxModifSupp.setGeometry(QtCore.QRect(1200, 330, 120, 60))  # Caché
        self.gbxFichePaie.setGeometry(QtCore.QRect(1200, 350, 120, 60)) #Caché
        self.gbxRecherche.setGeometry(QtCore.QRect(1200, 350, 120, 60)) #Caché
        #Affichage de la liste des fiches de paie dans le textBrowser (txtMessage)

        Chaine = ""
        for objFichePaie in lsFichePaie:
            Chaine += str(objFichePaie)

        self.txtMessage.setText(Chaine)

    #Ajouter un employé
    @QtCore.pyqtSlot()
    def on_btnAJouter_clicked(self):
        """
        Méthode d'événement de type clicked du bouton (btnAjouter) du menu
        Affiche le gbxAjouterModifierSupprimer
        :return:
        """
        #Configuration graphique pour l'option Ajouter du menu

        self.setFixedSize(600, 650) #Dimension
        self.lblTitre.setText("Ajouter un employé") #Nom pour lblTitre
        self.gbxMenu.setGeometry(QtCore.QRect(1200,80,120,60)) #Caché
        self.gbxFichePaie.setGeometry(QtCore.QRect(1200, 80, 120, 60)) #Caché
        self.gbxModifSupp.setGeometry(QtCore.QRect(1200, 80, 120, 60)) #Caché
        self.gbxRecherche.setGeometry(QtCore.QRect(1200, 350, 120, 60)) #Caché

        self.gbxAjouterModifierSupprimer.setGeometry(QtCore.QRect(10, 70, 601, 260)) #Visible
        self.txtMessage.setText("Processus pour l'ajout d'un employé")

        #Configuration du nom du bouton dans le gbxAfficherModifierSupprimer dans le cas où on veut ajouter un employé

        self.btnAjouterModifierSupprimer.setText("Ajouter un employé")

    #Retour au menu
    @QtCore.pyqtSlot()
    def on_btnRetourMenu_clicked(self):
        """
        Méthode d'événement de type clicked du bouton (btnRetourMenu)
        Lorsqu'on appuie sur le bouton, il nous ramène au menu
        :return:
        """

        #Configuration graphique pour l'option RetourMenu

        self.setFixedSize(400, 400) #Dimensions
        self.lblTitre.setText("Bienvenue sur le site de l'entreprise") #Nom pour lblTitre
        self.gbxMenu.setGeometry(QtCore.QRect(40, 50, 331, 330)) #Visible
        self.gbxAjouterModifierSupprimer.setGeometry(QtCore.QRect(1200, 350, 120, 60)) #Caché
        self.gbxModifSupp.setGeometry(QtCore.QRect(1200, 350, 120, 60)) #Caché
        self.gbxFichePaie.setGeometry(QtCore.QRect(1200, 350, 120, 60)) #Caché
        self.gbxRecherche.setGeometry(QtCore.QRect(1200, 350, 120, 60)) #Caché
        self.txtMessage.setGeometry(QtCore.QRect(30, 510, 291, 91)) #Visible

    #Supprimer un employé
    @QtCore.pyqtSlot()
    def on_btnSupprimer_clicked(self):
        """
        Méthode d'événement de type clicked pour l'option de Supprimer un employé
        Quand on appuie sur le bouton, il nous emmène au gbxModifSupp afin de trouver l'employé
        à supprimer
        :return:
        """
        #Configuration graphique pour afficher le gbxModifSupp
        self.setFixedSize(600, 650) #Dimensions
        self.lblTitre.setText("Supprimer un employé") #Nom du lblTitre
        self.gbxMenu.setGeometry(QtCore.QRect(1200, 80, 120, 60)) #Caché
        self.gbxFichePaie.setGeometry(QtCore.QRect(1200, 80, 120, 60)) #Caché
        self.gbxAjouterModifierSupprimer.setGeometry(QtCore.QRect(1200, 80, 120, 60)) #Caché
        self.gbxRecherche.setGeometry(QtCore.QRect(1200, 350, 120, 60)) #Caché

        self.gbxModifSupp.setGeometry(QtCore.QRect(10, 70, 600, 375)) #Visible

        #Configuration des noms de bouton et labels selon le nom du titre
        if self.lblTitre.text() == "Supprimer un employé":
            self.lblModSupSearch.setText("Chercher l'employé à supprimer")
            self.lblLstModifSupp.setText("Choisir l'employé à supprimer")
            self.btnModifSuppEmp.setText("Supprimer l'employé")

        if self.lblTitre.text() == "Modifier un employé":
            self.lblModSupSearch.setText("Chercher l'employé à modifier")
            self.lblLstModifSupp.setText("Choisir l'employé à modifier")
            self.btnModifSuppEmp.setText("Modifier l'employé")
        self.txtMessage.setText("Processus pour la supprimation d'un employé")

    #Cacluler une paie
    @QtCore.pyqtSlot()
    def on_btnCalculerPaie_clicked(self):
        """
        Méthode d'événement de type clicked qui nous envoie au groupebox (gbxModifSupp grace au
        bouton (btnCalculerPaie)
        :return:
        """
        #Configuration graphique
        self.setFixedSize(600, 650)
        self.lblTitre.setText("Calculer une paie") #Nom du lblTitre
        self.gbxMenu.setGeometry(QtCore.QRect(1200, 80, 120, 60)) #Caché
        self.gbxFichePaie.setGeometry(QtCore.QRect(1200, 80, 120, 60)) #Caché
        self.gbxAjouterModifierSupprimer.setGeometry(QtCore.QRect(1200, 80, 120, 60)) #Caché
        self.gbxRecherche.setGeometry(QtCore.QRect(1200, 350, 120, 60)) #Caché

        #Affichage de ce groupebox afin de trouver l'employé pour faire la fiche de paie
        self.gbxModifSupp.setGeometry(QtCore.QRect(10, 35, 600, 400)) #Visible
        self.txtMessage.setText("Processus pour le calcul d'une fiche de paie")

        # Configuration des noms de bouton et labels selon le nom du titre
        if self.lblTitre.text() == "Supprimer un employé":
            self.lblModSupSearch.setText("Chercher l'employé à supprimer")
            self.lblLstModifSupp.setText("Choisir l'article à supprimer")
            self.btnModifSuppEmp.setText("Supprimer l'employé")
            self.txtMessage.setText("Processus pour la supprimation d'un employé")
        if self.lblTitre.text() == "Modifier un employé":
            self.lblModSupSearch.setText("Chercher l'employé à modifier")
            self.lblLstModifSupp.setText("Choisir l'employé à modifier")
            self.btnModifSuppEmp.setText("Modifier l'employé")
            self.txtMessage.setText("Processus pour la modification d'un employé")
        if self.lblTitre.text() == "Calculer une paie":
            self.lblModSupSearch.setText("Chercher l'employé pour une fiche de paie")
            self.lblLstModifSupp.setText("Choisir l'employé pour une fiche de paie")
            self.btnModifSuppEmp.setText("Calculer la paie")
            self.txtMessage.setText("Processus pour un faire une fiche de paie pour un employé")

    #Modifier un employé
    @QtCore.pyqtSlot()
    def on_btnModifier_clicked(self):
        """
        Méthode d'événement de type clicked qui nous envoie au gbxModifSupp grâce au bouton
        (btnModifier)
        :return:
        """
        #Configuration graphique
        self.setFixedSize(600, 650) #Dimensions
        self.lblTitre.setText("Modifier un employé") #Nom du lblTitre
        self.gbxMenu.setGeometry(QtCore.QRect(1200, 80, 120, 60)) #Caché
        self.gbxFichePaie.setGeometry(QtCore.QRect(1200, 80, 120, 60)) #Caché
        self.gbxAjouterModifierSupprimer.setGeometry(QtCore.QRect(1200, 80, 120, 60)) #Caché
        self.gbxRecherche.setGeometry(QtCore.QRect(1200, 350, 120, 60)) #Caché

        self.gbxModifSupp.setGeometry(QtCore.QRect(10, 70, 600, 375)) #Visible

        # Configuration des noms de bouton et labels selon le nom du titre
        if self.lblTitre.text() == "Supprimer un employé":
            self.lblModSupSearch.setText("Chercher l'employé à supprimer")
            self.lblLstModifSupp.setText("Choisir l'article à supprimer")
            self.btnModifSuppEmp.setText("Supprimer l'employé")
            self.txtMessage.setText("Processus pour la supprimation d'un employé")
        if self.lblTitre.text() == "Modifier un employé":
            self.lblModSupSearch.setText("Chercher l'employé à modifier")
            self.lblLstModifSupp.setText("Choisir l'employé à modifier")
            self.btnModifSuppEmp.setText("Modifier l'employé")
            self.txtMessage.setText("Processus pour la modification d'un employé")

    #Ajouter,Supprimer ou Modifier l'employé
    @QtCore.pyqtSlot()
    def on_btnAjouterModifierSupprimer_clicked(self):

        """
        Méthode d'événement clicked du bouton btnAjouterModifier
        Ce bouton de commande sert à 3 opérations opérations: Ajouter, Modifier ou Supprimer un employé:
        :return:
        """
        #Si le nom du bouton (btnAjouterModifierSupprimer) est (Ajouter un employé)
        if self.btnAjouterModifierSupprimer.text() == "Ajouter un employé":

            #Création d'un message d'erreur
            MessageErreur = ""

            #Instanciation d'objet
            Employe_ = E.Employe()

            #Attributs sans validation à faire
            Employe_.NomEmploye = self.txtNom.text() #Nom
            Employe_.PrenomEmploye = self.txtPrenom.text() #Prénom

            #Attributs avec de la validation à faire

            #Validation pour l'attribut NumEmploye
            NumEmp_ = self.txtNumero.text()
            Employe_.NumEmploye = NumEmp_
            if Employe_.NumEmploye != NumEmp_:
                MessageErreur += "Le numéro d'identification est invalide !\n"
                self.txtNumero.setText("")

            #Validation pour l'attribut TelEmploye
            NumTel_ = self.txtTel_2.text()
            Employe_.TelEmploye = NumTel_
            if Employe_.TelEmploye != NumTel_:
                MessageErreur += "Le numéro de téléphone est invalide !\n"
                self.txtTel_2.setText("")
                self.txtNumero.setText("")

            #Validation pour l'attribut FonctionEmploye
            Fonction_ = self.txtFonction.text()
            Employe_.FonctionEmploye = Fonction_
            if Employe_.FonctionEmploye != Fonction_:
                MessageErreur += "La fonction est invalide !\n"
                self.txtFonction.setText("")
            #Validation pour l'attribut TauxHoraire
            try:
                TauxHoraire_ = float(self.txtTauxHoraire.text())
                Employe_.TauxHoraire = TauxHoraire_
                if Employe_.TauxHoraire != TauxHoraire_:
                    MessageErreur += "Le taux horaire est invalide\n"
                    self.txtTauxHoraire.setText("")
            except:
                MessageErreur += "Une valeur numérique est obligatoire pour le taux horaire\n"
                self.txtTauxHoraire.setText("")

            #Si aucun message d'erreur est créé, on ajoute l'employé dans la liste des employés
            if MessageErreur == "":
                lsEmployes.append(Employe_)
                self.txtMessage.setText("L'employé a été ajouté à la liste des employés.")

            #Sinon, on affiche un message d'erreur qui demande de recommencez
            else:
                MessageErreur += "Veuillez modifier vos informations et re-essayez...\n"
                self.txtMessage.setText(MessageErreur)

        #Si le nom du bouton (btnAjouterModifierSupprimer) est (Modifier l'employé):
        elif self.btnAjouterModifierSupprimer.text() == "Modifier l'employé":

            #Création du message d'erreur
            MessageErreur = ""

            #Recherche de l'employé à modifier dans la liste lsEmployes
            for objEmploye in lsEmployes:
                if objEmploye.NumEmploye == self.txtNumero.text():

                    #Assignation des valeurs des txtbox à leur attribut respectif
                    #Attributs qui n'ont pas de validation d'entrée ni d'encapsulation
                    objEmploye.PrenomEmploye = self.txtPrenom.text()
                    objEmploye.NomEmploye = self.txtNom.text()

                    #Attributs avec de la validation de valeur:
                    #Attribut NumeroEmploye validation
                    NumEmp_ = self.txtNumero.text()
                    objEmploye.NumEmploye = NumEmp_
                    if objEmploye.NumEmploye != NumEmp_:
                        MessageErreur += "Le nouveau numéro de l'employé est invalide !\n"
                        self.txtNumero.setText("")

                    #Attribut FonctionEmploye validation
                    Fonction_ = self.txtFonction.text()
                    objEmploye.FonctionEmploye = Fonction_
                    if objEmploye.FonctionEmploye != Fonction_:
                        MessageErreur += "La nouvelle fonction de l'employé est invalide !\n"
                        self.txtFonction.setText("")

                    #Attribut TauxHoraire validation
                    TauxHoraire_ = float(self.txtTauxHoraire.text())
                    objEmploye.TauxHoraire = TauxHoraire_
                    if objEmploye.TauxHoraire != TauxHoraire_:
                        MessageErreur += "Le nouveau taux horaire de l'employé est invalide !\n"
                        self.txtFonction.setText("")

                    #Attribut TelEmploye validation
                    Tel_ =self.txtTel_2.text()
                    objEmploye.TelEmploye = Tel_
                    if objEmploye.TelEmploye != Tel_:
                        MessageErreur += "Le nouveau numéro de téléphone est invalide !\n"
                        self.txtTel_2.setText("")

                        # S'il n'y a pas de message d'erreur, on modifie les informations de 'employé
                    if MessageErreur == "":
                        self.txtMessage.setText("La mise à jour de l'employé a été faite avec succès.")

                        #Sinon, on demande de recommencez
                    else:
                        MessageErreur += "\nLa mise à jour n'a pu être complétée. Apportez les correctifs nécessaires et cliquez à nouveau sur le bouton - Modifier cet article -"
                        self.txtMessage.setText(MessageErreur)

        #Si le nom du bouton (btnAjouterModifierSupprimer) est (Supprimer l'employé)
        elif self.btnAjouterModifierSupprimer.text() == "Supprimer l'employé":

         for i in range(0, len(lsEmployes), 1):  # Recherche de l'employé à supprimer dans la liste
            if lsEmployes[i].NumEmploye == self.txtNumero.text():
                lsEmployes.remove(lsEmployes[i]) #Supprimation de l'employé
                break
         self.txtMessage.setText("L'employé a été retiré avec succès.")


    @QtCore.pyqtSlot()
    def on_btnModifSuppEmp_clicked(self):

        self.setFixedSize(600, 650)
        self.gbxMenu.setGeometry(QtCore.QRect(1200, 80, 120, 60))
        self.gbxFichePaie.setGeometry(QtCore.QRect(1200, 80, 120, 60))
        self.gbxModifSupp.setGeometry(QtCore.QRect(1200, 80, 120, 60))
        self.gbxRecherche.setGeometry(QtCore.QRect(1200, 350, 120, 60))


        if self.lblTitre.text() == "Supprimer un employé":
            self.btnAjouterModifierSupprimer.setText("Supprimer l'employé")
            self.gbxAjouterModifierSupprimer.setGeometry(QtCore.QRect(10, 70, 601, 301))

        elif self.lblTitre.text() == "Modifier un employé":
            self.btnAjouterModifierSupprimer.setText("Modifier l'employé")
            self.gbxAjouterModifierSupprimer.setGeometry(QtCore.QRect(10, 70, 601, 301))

        elif self.lblTitre.text() == "Calculer une paie":
            self.gbxFichePaie.setGeometry(QtCore.QRect(10, 50, 550, 400))
            ChoixEmploye = self.cboEmployeModifSupp.currentText()
            lsSplit = ChoixEmploye.split(" ;")
            EmpNoRef = lsSplit[0]

            for objEmploye in lsEmployes:
                if objEmploye.NumEmploye == EmpNoRef:
                    self.txtNumeroEmploye.setText(objEmploye.NumEmploye)
                    break

        ChoixEmploye = self.cboEmployeModifSupp.currentText()
        lsSplit = ChoixEmploye.split(" ;")
        EmpNoRef = lsSplit[0]

        for objEmploye in lsEmployes:
            if objEmploye.NumEmploye == EmpNoRef:
                self.txtNumero.setText(objEmploye.NumEmploye)
                self.txtNom.setText(objEmploye.NomEmploye)
                self.txtPrenom.setText(objEmploye.PrenomEmploye)
                self.txtTel_2.setText(objEmploye.TelEmploye)
                self.txtFonction.setText(objEmploye.FonctionEmploye)
                self.txtTauxHoraire.setText("{:.2f}".format(objEmploye.TauxHoraire))
                break

    #Affichage du gbxRecherche
    @QtCore.pyqtSlot()
    def on_btnRechercher_clicked(self):
        """
        Méthode d'événement de type clicked qui affiche le groupebox (gbxRecherche)
        Afin de rechercher un employé dans la liste des employés sans aucun autre but
        :return:
        """
        #Configuration graphique
        self.setFixedSize(600, 650) #Dimensions
        self.lblTitre.setText("Recherché un employé") #Nom du lblTitre
        self.gbxMenu.setGeometry(QtCore.QRect(1200, 80, 120, 60)) #Caché
        self.gbxFichePaie.setGeometry(QtCore.QRect(1200, 80, 120, 60)) #Caché
        self.gbxModifSupp.setGeometry(QtCore.QRect(1200, 80, 120, 60)) #Caché
        self.gbxAjouterModifierSupprimer.setGeometry(QtCore.QRect(1200, 350, 120, 60)) #Caché

        self.gbxRecherche.setGeometry(QtCore.QRect(10, 70, 601, 375)) #Visible
        self.txtMessage.setText("Les résultats de la recherche s'afficheront dans la boite de texte.")

    #Rechercher un employé sans aucun autre but
    @QtCore.pyqtSlot()
    def on_btnSearch_clicked(self):
        """
        Méthode d'événement clicked pour le bouton btnSearch
        Permet de lancer la recherche d'un employé avec le critère de recherche fourni
        :return:
        """
        #Vidage de la liste lsRecherche
        lsRecherche.clear()
        # Si le critère est le numéro d'identification
        if self.cboCritereSearch.currentText() == "Numéro d'identification":
            for objEmploye in lsEmployes: #On parcourt la liste des employés pour voir si le numéro est là
                if objEmploye.NumEmploye == self.txtValeurSearch.text().upper():
                    lsRecherche.append(objEmploye) #On ajoute le numéro de téléphone dans la liste de recherche
        # Si le critère est le numéro de téléphone
        elif self.cboCritereSearch.currentText() == "Numéro de téléphone":
            for objEmploye in lsEmployes: #On parcourt la liste des employés pour voir si le numéro de téléphone est là
                if objEmploye.TelEmploye == self.txtValeurSearch.text():
                  lsRecherche.append(objEmploye) #On ajoute le numéro de téléphone de téléphone dans la liste de recherche
        #Si le critère est le prénom
        elif self.cboCritereSearch.currentText() == "Prénom":
            for objEmploye in lsEmployes: #On parcourt la liste des employés pour voir si le prénom est là
                if objEmploye.PrenomEmploye == self.txtValeurSearch.text():
                    lsRecherche.append(objEmploye) #On ajoute le prénom dans la liste de recherche
        # Si le critère est la fonction
        elif self.cboCritereSearch.currentText() == "Fonction":
            for objEmploye in lsEmployes: #On parcourt la liste des employés pour voir si la fonction est là
                if objEmploye.FonctionEmploye == self.txtValeurSearch.text():
                    lsRecherche.append(objEmploye) #On ajoute la fonction dans la liste de recherche

        #Afficher le résultat de recherche
        Chaine = ""
        #S'il y a plusieurs résultats, les résultats obtenus ont un petit 1,2,3 au début
        cpt = 1
        for objEmploye  in lsRecherche:
            Chaine += "{}. {} / {} / {} / {} / {} $ / {} \n".format(cpt, objEmploye.NumEmploye, objEmploye.NomEmploye, objEmploye.PrenomEmploye, objEmploye.FonctionEmploye, objEmploye.TauxHoraire, objEmploye.TelEmploye)
            cpt += 1

        #Si rien n'a été ajouter dans la liste lsRecherche, un message d'erreur s'affiche
        if len(lsRecherche) == 0:
            self.txtResultSearch.setText("Aucun employé trouvé")
        else:
            self.txtResultSearch.setText(Chaine)


    @QtCore.pyqtSlot()
    def on_btnCalculerLaPaie_clicked(self):

        MessageErreur =""

        FichePaie_ = P.FichePaie()


        for objEmploye in lsEmployes:
            if self.txtNumeroEmploye.text() == objEmploye.NumEmploye:
                FichePaie_.InfEmploye = objEmploye

        NumFiche_ = self.txtFiche.text()
        FichePaie_.NumeroFiche = NumFiche_
        if FichePaie_.NumeroFiche != NumFiche_:
            MessageErreur += "Le numéro de la fiche de paie est invalide !\n"
            self.txtFiche.setText("")

        if MessageErreur == "":
          self.txtMessage.setText("Le numéro de fiche est bon ")

        else:
            MessageErreur += "Veuillez ré-essayez avec de nouvelles informations"
            self.txtMessage.setText(MessageErreur)

        NbHeures_ = int(self.txtNbHeures.text())
        FichePaie_.NombreHeures = NbHeures_
        if FichePaie_.NombreHeures != NbHeures_:
            MessageErreur += "Le nombre d'heures est invalide"
            self.txtNbHeures.setText("")
        
        if MessageErreur == "":
          self.txtMessage.setText("Le nombre d'heures est bon ")

        else:
            MessageErreur += "Veuillez ré-essayez avec de nouvelles informations"
            self.txtMessage.setText(MessageErreur)

        FichePaie_.DateFiche = DT.datetime.now()

        if self.cboTypeEmploie.currentText() == "Sur appel":
            FichePaie_.TypeEmploye = lsTypeEmploye[1]
        if self.cboTypeEmploie.currentText() == "Temps partiel":
            FichePaie_.TypeEmploye = lsTypeEmploye[0]
        if self.cboTypeEmploie.currentText() == "Temps plein":
            FichePaie_.TypeEmploye = lsTypeEmploye[2]



        FichePaie_.CalculerPaie()

        lsFichePaie.append(FichePaie_)
        self.txtMessage.setText("La fiche de paie a été ajouté à l'historique de paie")

        Chaine = ""
        Chaine += str(FichePaie_)

        self.txtAffichageFiche.setText(Chaine)

    #Rechercher un employé pour but de le modifier, supprimer ou ajouter une fiche de paie
    @QtCore.pyqtSlot()
    def on_btnRech_clicked(self):
        """
        Méthode d'événement de type clicked qui lance la recherche d'un employé selon
        le critère de recherche et la valeur donnés grâce au bouton (btnRech)
        :return:
        """
        #Vider la liste lsRecherche
        lsRecherche.clear()

        #Si le critère est le numéro d'identification
        if self.cboCritereRechModif.currentText() == "Numéro d'identification":
            for objEmploye in lsEmployes: #On parcourt la liste des employés pour voir si le numéro est là
                if objEmploye.NumEmploye == self.txtValeurRechModif.text():
                    lsRecherche.append(objEmploye) #On ajoute le numéro de l'employé dans la liste de recherche

        #Si le critère de recherche est le prénom
        elif self.cboCritereRechModif.currentText() == "Prénom":
              for objEmploye in lsEmployes: #On parcourt la liste des employés pour voir si le prénom est là
                if objEmploye.PrenomEmploye == self.txtValeurRechModif.text():
                    lsRecherche.append(objEmploye) #On ajoute le prénom dans la liste de recherche

        # Si le critère de recherche est le nom
        elif self.cboCritereRechModif.currentText() == "Nom":
            for objEmploye in lsEmployes: #On parcourt la liste des employés pour voir si le nom est là
                if objEmploye.NomEmploye == self.txtValeurRechModif.text():
                    lsRecherche.append(objEmploye) #On ajoute le nom dans la liste de recherche

        # Si le critère de recherche est le numéro de téléphone
        elif self.cboCritereRechModif.currentText() == "Numéro de téléphone":
            for objEmploye in lsEmployes: #On parcourt la liste des employés pour voir si le numro de téléphone est là
                if objEmploye.TelEmploye == self.txtValeurRechModif.text():
                    lsRecherche.append(objEmploye) #On ajoute le numéro de téléphone dans la liste de recherche

        #Vidage du comboBox ou on affiche les résultats de recherche
        self.cboEmployeModifSupp.clear()
        #Affichage des informations de l'employé trouvé dans le combobox (cboEmployeModifSupp)
        for objEmploye in lsRecherche :
            Chaine = objEmploye.NumEmploye + " ;" + objEmploye.PrenomEmploye + " ;" + objEmploye.NomEmploye + " ;" + objEmploye.TelEmploye
            self.cboEmployeModifSupp.addItem(Chaine)

    #Fermer l'application
    @QtCore.pyqtSlot()
    def on_btnFermer_clicked(self):
        """
        Méthode d'événement de type clicked qui nous envoie dans le gbxVerifQuitter
        Pour s'assurer que l'admin veut réellement quitter ou poursuivre ses activités
        :return:
        """
        #Configuration graphique
        self.setFixedSize(450, 325) #Dimensions
        self.lblTitre.setText("* Tentative de déconnection *") #Nom du lblTitre
        self.gbxMenu.setGeometry(QtCore.QRect(1200, 350, 331, 291)) #Caché
        self.gbxAjouterModifierSupprimer.setGeometry(QtCore.QRect(1200, 350, 120, 60)) #Caché
        self.gbxModifSupp.setGeometry(QtCore.QRect(1200, 350, 120, 60)) #Caché
        self.gbxFichePaie.setGeometry(QtCore.QRect(1200, 350, 120, 60)) #Caché
        self.gbxRecherche.setGeometry(QtCore.QRect(1200, 350, 120, 60)) #Caché
        self.txtMessage.setGeometry(QtCore.QRect(30, 510, 291, 91)) #Visible
        self.gbxVerifQuitter.setGeometry(QtCore.QRect(40, 50, 400, 291)) #Visible

    #Revenir au menu
    def on_btnNON_clicked(self):
        """
        Méthode d'événement de type clicked qui fait revenir au menu suite à avoir cliquer sur
        le bouton Fermer
        :return:
        """
        #Configuration graphique
        self.setFixedSize(450, 450) #Dimensions
        self.lblTitre.setText(" Bienvenue sur le site de l'entreprise ") #Nom du lblTitre
        self.gbxMenu.setGeometry(QtCore.QRect(40, 50, 331, 330)) #Visible
        self.gbxAjouterModifierSupprimer.setGeometry(QtCore.QRect(1200, 350, 120, 60)) #Caché
        self.gbxModifSupp.setGeometry(QtCore.QRect(1200, 350, 120, 60)) #Caché
        self.gbxFichePaie.setGeometry(QtCore.QRect(1200, 350, 120, 60)) #Caché
        self.gbxRecherche.setGeometry(QtCore.QRect(1200, 350, 120, 60)) #Caché
        self.txtMessage.setGeometry(QtCore.QRect(30, 510, 291, 91)) #Visible
        self.gbxVerifQuitter.setGeometry(QtCore.QRect(1200, 350, 600, 291)) #Caché

    #Quitter définitivement l'application
    @QtCore.pyqtSlot()
    def on_btnOUI_clicked(self):
        """
        Méthode d'événement de type clicked qui ferme l'application intégralement avec le bouton
        (btnOUI)
        :return:
        """

        print("Fermeture de l'application")

        # Sérialisation des objets
        #with open("fEmploye.json", "w") as fi:
            #fi.write((jsonpickle.encode(lsEmployes)))

        self.close() #Ferme l'application



def main():
    #Exécution de l'application avec l'interface graphique
    app = QtWidgets.QApplication(sys.argv)
    form = FenetreQt()
    form.show()
    app.exec()

if __name__ == "__main__":
    # Désérialisation des objets
    #with open("fEmploye.json", "r") as fi:
        #dataEmploye = fi.read()
    #lsEmployes = jsonpickle.decode(dataEmploye)


    main()


#Quelques bouts de code ont été pris de l'exercise 10.1 de Hélène Bolduc



