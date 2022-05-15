###################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet synthèse
###  Nom: Philippe Bertrand
###  Description du fichier: Programme principal
####################################################################################
#importation du module sys nécessaire à l'exécution de l'application
import sys

#Importation du fichier Qt Designer UI converti en PY
import EntrepriseInterface as F

#Importation des librairies nécessaires à QtDesigner
from PyQt5 import QtWidgets, QtCore

#Importation des classes
import cEmploye as E
import cFichePaie as P
import datetime as DT
import cTypeEmploie as T


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
        self.gbxConnexion.setGeometry(QtCore.QRect(40, 50, 331, 291)) #Visible
        self.gbxAjouterModifierSupprimer.setGeometry(QtCore.QRect(1200, 350, 120, 60)) #Caché
        self.gbxModifSupp.setGeometry(QtCore.QRect(1200, 350, 120, 60)) #Caché
        self.gbxFichePaie.setGeometry(QtCore.QRect(1200, 350, 120, 60)) #Caché
        self.gbxRecherche.setGeometry(QtCore.QRect(1200, 350, 120, 60)) #Caché
        self.gbxMenu.setGeometry(QtCore.QRect(1200, 350, 120, 60))  # Caché



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
            self.gbxFichePaie.setGeometry(QtCore.QRect(1200, 350, 120, 60))
            self.gbxRecherche.setGeometry(QtCore.QRect(1200, 350, 120, 60))
            Chaine = ""
            for objEmploye in lsEmployes:
                Chaine +=str(objEmploye)

            self.txtMessage.setText(Chaine)

    @QtCore.pyqtSlot()
    def on_btnAfficherPaie_clicked(self):
        self.setFixedSize(600, 611)  # Dimensions du form pour Afficher
        self.lblTitre.setText("Historique des fiches de paie")  # Titre pour Afficher
        self.gbxMenu.setGeometry(QtCore.QRect(1200, 10, 120, 60))  # Caché
        self.txtMessage.setGeometry(QtCore.QRect(10, 70, 561, 381))  # Visible
        self.gbxAjouterModifierSupprimer.setGeometry(QtCore.QRect(1200, 150, 120, 60))  # Caché
        self.gbxModifSupp.setGeometry(QtCore.QRect(1200, 330, 120, 60))  # Caché
        self.gbxFichePaie.setGeometry(QtCore.QRect(1200, 350, 120, 60))
        self.gbxRecherche.setGeometry(QtCore.QRect(1200, 350, 120, 60))

        Chaine = ""
        for objFichePaie in lsFichePaie:
            Chaine += str(objFichePaie)

        self.txtMessage.setText(Chaine)


    @QtCore.pyqtSlot()
    def on_btnAJouter_clicked(self):

        self.setFixedSize(600, 650)
        self.lblTitre.setText("Ajouter un employé")
        self.gbxMenu.setGeometry(QtCore.QRect(1200,80,120,60))
        self.gbxFichePaie.setGeometry(QtCore.QRect(1200, 80, 120, 60))
        self.gbxModifSupp.setGeometry(QtCore.QRect(1200, 80, 120, 60))
        self.gbxRecherche.setGeometry(QtCore.QRect(1200, 350, 120, 60))

        self.gbxAjouterModifierSupprimer.setGeometry(QtCore.QRect(10, 70, 601, 260))
        self.txtMessage.setText("Processus pour l'ajout d'un employé")
        self.btnAjouterModifierSupprimer.setText("Ajouter un employé")

    @QtCore.pyqtSlot()
    def on_btnRetourMenu_clicked(self):

        self.setFixedSize(400, 400)
        self.lblTitre.setText("Bienvenue sur le site de l'entreprise")
        self.gbxMenu.setGeometry(QtCore.QRect(40, 50, 331, 291))
        self.gbxAjouterModifierSupprimer.setGeometry(QtCore.QRect(1200, 350, 120, 60))
        self.gbxModifSupp.setGeometry(QtCore.QRect(1200, 350, 120, 60))
        self.gbxFichePaie.setGeometry(QtCore.QRect(1200, 350, 120, 60))
        self.gbxRecherche.setGeometry(QtCore.QRect(1200, 350, 120, 60))
        self.txtMessage.setGeometry(QtCore.QRect(30, 510, 291, 91))



    @QtCore.pyqtSlot()
    def on_btnSupprimer_clicked(self):

        self.setFixedSize(600, 650)
        self.lblTitre.setText("Supprimer un employé")
        self.gbxMenu.setGeometry(QtCore.QRect(1200, 80, 120, 60))
        self.gbxFichePaie.setGeometry(QtCore.QRect(1200, 80, 120, 60))
        self.gbxAjouterModifierSupprimer.setGeometry(QtCore.QRect(1200, 80, 120, 60))
        self.gbxRecherche.setGeometry(QtCore.QRect(1200, 350, 120, 60))

        self.gbxModifSupp.setGeometry(QtCore.QRect(10, 70, 600, 375))

        if self.lblTitre.text() == "Supprimer un employé":
            self.lblModSupSearch.setText("Chercher l'employé à supprimer")
            self.lblLstModifSupp.setText("Choisir l'employé à supprimer")
            self.btnModifSuppEmp.setText("Supprimer l'employé")

        if self.lblTitre.text() == "Modifier un employé":
            self.lblModSupSearch.setText("Chercher l'employé à modifier")
            self.lblLstModifSupp.setText("Choisir l'employé à modifier")
            self.btnModifSuppEmp.setText("Modifier l'employé")
        self.txtMessage.setText("Processus pour la supprimation d'un employé")

    @QtCore.pyqtSlot()
    def on_btnCalculerPaie_clicked(self):
        self.setFixedSize(600, 650)
        self.lblTitre.setText("Calculer une paie")
        self.gbxMenu.setGeometry(QtCore.QRect(1200, 80, 120, 60))
        self.gbxFichePaie.setGeometry(QtCore.QRect(1200, 80, 120, 60))
        self.gbxAjouterModifierSupprimer.setGeometry(QtCore.QRect(1200, 80, 120, 60))
        self.gbxRecherche.setGeometry(QtCore.QRect(1200, 350, 120, 60))

        self.gbxModifSupp.setGeometry(QtCore.QRect(10, 35, 600, 400))
        self.txtMessage.setText("Processus pour le calcul d'une fiche de paie")
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

    @QtCore.pyqtSlot()
    def on_btnModifier_clicked(self):
        self.setFixedSize(600, 650)
        self.lblTitre.setText("Modifier un employé")
        self.gbxMenu.setGeometry(QtCore.QRect(1200, 80, 120, 60))
        self.gbxFichePaie.setGeometry(QtCore.QRect(1200, 80, 120, 60))
        self.gbxAjouterModifierSupprimer.setGeometry(QtCore.QRect(1200, 80, 120, 60))
        self.gbxRecherche.setGeometry(QtCore.QRect(1200, 350, 120, 60))

        self.gbxModifSupp.setGeometry(QtCore.QRect(10, 70, 600, 375))
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


    @QtCore.pyqtSlot()
    def on_btnAjouterModifierSupprimer_clicked(self):

        """
        Méthode d'événement clicked du bouton btnAjouterModifier
        Ce bouton de commande sert à 2 opérations opérations: Ajouter ou modifier un employé:
        :return:
        """

        if self.btnAjouterModifierSupprimer.text() == "Ajouter un employé":

            MessageErreur = ""

            Employe_ = E.Employe()

            Employe_.NomEmploye = self.txtNom.text()
            Employe_.PrenomEmploye = self.txtPrenom.text()

            NumEmp_ = self.txtNumero.text().upper()
            Employe_.NumEmploye = NumEmp_
            if Employe_.NumEmploye != NumEmp_:
                MessageErreur += "Le numéro d'identification est invalide !\n"
                self.txtNumero.setText("")

            NumTel_ = self.txtTel_2.text()
            Employe_.TelEmploye = NumTel_
            if Employe_.TelEmploye != NumTel_:
                MessageErreur += "Le numéro de téléphone est invalide !\n"
                self.txtNumero.setText("")

            Fonction_ = self.txtFonction.text()
            Employe_.FonctionEmploye = Fonction_
            if Employe_.FonctionEmploye != Fonction_:
                MessageErreur += "La fonction est invalide !\n"
                self.txtFonction.setText("")

            try:
                TauxHoraire_ = float(self.txtTauxHoraire.text())
                Employe_.TauxHoraire = TauxHoraire_
                if Employe_.TauxHoraire != TauxHoraire_:
                    MessageErreur += "Le taux horaire est invalide\n"
            except:
                MessageErreur += "Une valeur numérique est obligatoire\n"
                self.txtTauxHoraire.setText("")

            if MessageErreur == "":
                lsEmployes.append(Employe_)
                self.txtMessage.setText("L'employé a été ajouté à la liste des employés.")
            else:
                MessageErreur += "Veuillez modifier vos informations et re-essayez...\n"
                self.txtMessage.setText(MessageErreur)


        elif self.btnAjouterModifierSupprimer.text() == "Modifier l'employé":
            self.txtMessage.setText("Test")


        elif self.btnAjouterModifierSupprimer.text() == "Supprimer l'employé":
         for i in range(0, len(lsEmployes), 1):  # Recherche de l'article à supprimer dans la liste
            if lsEmployes[i].NumEmploye == self.txtNumero.text():
                lsEmployes.remove(lsEmployes[i])
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
                self.txtNumero.setText(objEmploye.NumEmploye)
                self.txtNom.setText(objEmploye.NomEmploye)
                self.txtPrenom.setText(objEmploye.PrenomEmploye)
                self.txtTel_2.setText(objEmploye.TelEmploye)
                self.txtFonction.setText(objEmploye.FonctionEmploye)
                self.txtTauxHoraire.setText("{:.2f}".format(objEmploye.TauxHoraire))
                break


    @QtCore.pyqtSlot()
    def on_btnRechercher_clicked(self):
        self.setFixedSize(600, 650)
        self.lblTitre.setText("Recherché un employé")
        self.gbxMenu.setGeometry(QtCore.QRect(1200, 80, 120, 60))
        self.gbxFichePaie.setGeometry(QtCore.QRect(1200, 80, 120, 60))
        self.gbxModifSupp.setGeometry(QtCore.QRect(1200, 80, 120, 60))
        self.gbxAjouterModifierSupprimer.setGeometry(QtCore.QRect(1200, 350, 120, 60))

        self.gbxRecherche.setGeometry(QtCore.QRect(10, 70, 601, 375))
        self.txtMessage.setText("Les résultats de la recherche s'afficheront dans la boite de texte.")


    @QtCore.pyqtSlot()
    def on_btnSearch_clicked(self):
        """
        Méthode d'événement clicked pour le bouton btnSearch
        Permet de lancer la recherche d'un employé avec le critère de recherche fourni
        :return:
        """

        lsRecherche.clear()
        if self.cboCritereSearch.currentText() == "Numéro d'identification":
            for objEmploye in lsEmployes:
                if objEmploye.NumEmploye == self.txtValeurSearch.text().upper():
                    lsRecherche.append(objEmploye)
        elif self.cboCritereSearch.currentText() == "Numéro de téléphone":
            for objEmploye in lsEmployes:
                if objEmploye.TelEmploye == self.txtValeurSearch.text():
                    lsRecherche.append(objEmploye)
        elif self.cboCritereSearch.currentText() == "Prénom":
            for objEmploye in lsEmployes:
                if objEmploye.PrenomEmploye == self.txtValeurSearch.text():
                    lsRecherche.append(objEmploye)
        elif self.cboCritereSearch.currentText() == "Fonction":
            for objEmploye in lsEmployes:
                if objEmploye.FonctionEmploye == self.txtValeurSearch.text():
                    lsRecherche.append(objEmploye)
        Chaine = ""
        cpt = 1
        for objEmploye  in lsRecherche:
            Chaine += "{}. {} / {} / {} / {} / {} $ / {} \n".format(cpt, objEmploye.NumEmploye, objEmploye.NomEmploye, objEmploye.PrenomEmploye, objEmploye.FonctionEmploye, objEmploye.TauxHoraire, objEmploye.TelEmploye)
            cpt += 1

        if len(lsRecherche) == 0:
            self.txtResultSearch.setText("Aucun employé trouvé")
        else:
            self.txtResultSearch.setText(Chaine)


    @QtCore.pyqtSlot()
    def on_btnCalculerLaPaie_clicked(self):

        MessageErreur =""

        FichePaie_ = P.FichePaie()


        NumFiche_ = self.txtFiche.text().upper()
        FichePaie_.NumeroFiche = NumFiche_
        if FichePaie_.NumeroFiche != NumFiche_:
            MessageErreur += "Le numéro de la fiche de paie est invalide !\n"
            self.txtFiche.setText("")

        if MessageErreur == "":
          self.txtMessage.setText("Le numéro de fiche est bon ")

        else:
            MessageErreur += "Veuillez ré-essayez avec de nouvelles informations"
            self.txtMessage.setText(MessageErreur)




    @QtCore.pyqtSlot()
    def on_btnRech_clicked(self):

        lsRecherche.clear()

        if self.cboCritereSearch.currentText() == "Numéro d'identification":
            for objEmploye in lsEmployes:
                if objEmploye.NumEmploye == self.txtValeurRechModif.text():
                    lsRecherche.append(objEmploye)
        elif self.cboCritereSearch.currentText() == "Prénom":
              for objEmploye in lsEmployes:
                if objEmploye.PrenomEmploye == self.txtValeurRechModif.text():
                    lsRecherche.append(objEmploye)
        elif self.cboCritereSearch.currentText() == "Nom":
            for objEmploye in lsEmployes:
                if objEmploye.NomEmploye == self.txtValeurRechModif.text():
                    lsRecherche.append(objEmploye)
        elif self.cboCritereSearch.currentText() == "Numéro de téléphone":
            for objEmploye in lsEmployes:
                if objEmploye.TelEmploye == self.txtValeurRechModif.text():
                    lsRecherche.append(objEmploye)

        self.cboEmployeModifSupp.clear()
        for objEmploye in lsRecherche :
            Chaine = objEmploye.NumEmploye + " ;" + objEmploye.PrenomEmploye + " ;" + objEmploye.NomEmploye + " ;" + objEmploye.TelEmploye
            self.cboEmployeModifSupp.addItem(Chaine)

    @QtCore.pyqtSlot()
    def on_btnFermer_clicked(self):

        print("Fermeture de l'application")
        self.close()



def main():
    #Exécution de l'application avec l'interface graphique
    app = QtWidgets.QApplication(sys.argv)
    form = FenetreQt()
    form.show()
    app.exec()

if __name__ == "__main__":
    main()






