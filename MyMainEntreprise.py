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

#Importation de la classe Employe
import cEmploye as E



#Création de la liste lsEmployes
lsEmployes = []

#Instanciation d'objets
lsEmployes.append(E.Employe("H-2345","Philippe","Bertrand", "819-827-4693","Marketing", 60.00))
lsEmployes.append(E.Employe("P-2567", "Jean", "Lasalle", "819-856-4111", "Superviseur", 120.00))
lsEmployes.append(E.Employe("W-5555", "Marine", "Lepen", "819-856-0002", "Directeur", 55.55))
lsEmployes.append(E.Employe("K-6395", "Emmanuel", "Macron", "819-427-4569", "Comptabilité", 51.99))
lsEmployes.append(E.Employe("L-2789", "Jean-Luc", "Mélenchon", "810-555-5555", "Gestion", 149.00))

lsRecherche = []

class FenetreQt(QtWidgets.QMainWindow, F.Ui_EntrepriseGestion):
    """
    Classe qui représente l'interface graphique de l'application
    """

    def __init__(self, parent = None):
        """
        Constructeur de la classe FenetreQt qui représente l'interface graphique
        :param parent:
        """
        super(FenetreQt,self).__init__(parent)
        self.setupUi(self)


        self.setWindowTitle("Entreprise")
        self.setFixedSize(400, 400)
        self.lblTitre.setText("Bienvenue sur le site de l'entreprise")
        self.gbxMenu.setGeometry(QtCore.QRect(40, 50, 331, 291))
        self.gbxAjouterModifier.setGeometry(QtCore.QRect(1200, 350, 120, 60))
        self.gbxModifSupp.setGeometry(QtCore.QRect(1200, 350, 120, 60))
        self.gbxFichePaie.setGeometry(QtCore.QRect(1200, 350, 120, 60))
        self.gbxRecherche.setGeometry(QtCore.QRect(1200, 350, 120, 60))




        self.cboTypeEmploie.addItem("Temps plein")
        self.cboTypeEmploie.addItem("Temps partiel")
        self.cboTypeEmploie.addItem("Sur appel")

        self.cboCritereRechModif.addItem("Numéro d'identification")
        self.cboCritereRechModif.addItem("Prénom")
        self.cboCritereRechModif.addItem("Nom")
        self.cboCritereRechModif.addItem("Numéro de téléphone")

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
            self.gbxAjouterModifier.setGeometry(QtCore.QRect(1200, 150, 120, 60))  # Caché
            self.gbxModifSupp.setGeometry(QtCore.QRect(1200, 330, 120, 60))  # Caché
            self.gbxFichePaie.setGeometry(QtCore.QRect(1200, 350, 120, 60))
            self.gbxRecherche.setGeometry(QtCore.QRect(1200, 350, 120, 60))
            Chaine = ""
            for objEmploye in lsEmployes:
                Chaine +=str(objEmploye)

            self.txtMessage.setText(Chaine)

    @QtCore.pyqtSlot()
    def on_btnAJouter_clicked(self):

        self.setFixedSize(600, 650)
        self.lblTitre.setText("Ajouter un employé")
        self.gbxMenu.setGeometry(QtCore.QRect(1200,80,120,60))
        self.gbxFichePaie.setGeometry(QtCore.QRect(1200, 80, 120, 60))
        self.gbxModifSupp.setGeometry(QtCore.QRect(1200, 80, 120, 60))
        self.gbxRecherche.setGeometry(QtCore.QRect(1200, 350, 120, 60))

        self.gbxAjouterModifier.setGeometry(QtCore.QRect(10, 70, 601, 260))
        self.txtMessage.setText("Processus pour l'ajout d'un employé")
        if self.lblTitre.text() == "Ajouter un employé":
            self.btnAjouterModifierSupprimer.setText("Ajouter un employé")
        elif self.lblTitre.text() == "Modifier un employé":
            self.btnAjouterModifierSupprimer.setText("Modifier l'employé")

    @QtCore.pyqtSlot()
    def on_btnRetourMenu_clicked(self):

        self.setFixedSize(400, 400)
        self.lblTitre.setText("Bienvenue sur le site de l'entreprise")
        self.gbxMenu.setGeometry(QtCore.QRect(40, 50, 331, 291))
        self.gbxAjouterModifier.setGeometry(QtCore.QRect(1200, 350, 120, 60))
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
        self.gbxAjouterModifier.setGeometry(QtCore.QRect(1200, 80, 120, 60))
        self.gbxRecherche.setGeometry(QtCore.QRect(1200, 350, 120, 60))

        self.gbxModifSupp.setGeometry(QtCore.QRect(10, 70, 600, 375))

        if self.lblTitre.text() == "Supprimer un employé":
            self.lblModSupSearch.setText("Chercher l'employé à supprimer")
            self.lblLstModifSupp.setText("Choisir l'article à supprimer")
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
        self.gbxModifSupp.setGeometry(QtCore.QRect(1200, 80, 120, 60))
        self.gbxAjouterModifier.setGeometry(QtCore.QRect(1200, 80, 120, 60))
        self.gbxRecherche.setGeometry(QtCore.QRect(1200, 350, 120, 60))

        self.gbxFichePaie.setGeometry(QtCore.QRect(10, 35, 600, 400))
        self.txtMessage.setText("Processus pour le calcul d'une fiche de paie")

    @QtCore.pyqtSlot()
    def on_btnModifier_clicked(self):
        self.setFixedSize(600, 650)
        self.lblTitre.setText("Modifier un employé")
        self.gbxMenu.setGeometry(QtCore.QRect(1200, 80, 120, 60))
        self.gbxFichePaie.setGeometry(QtCore.QRect(1200, 80, 120, 60))
        self.gbxAjouterModifier.setGeometry(QtCore.QRect(1200, 80, 120, 60))
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

            Employe_.NomEmploye = self.txtNom()
            Employe_.PrenomEmploye = self.txtPrenom()

            NumEmp_ = self.txtNumero.text().upper()
            Employe_.NumEmploye = NumEmp_
            if Employe_.NumEmploye != NumEmp_:
                MessageErreur += "Le numéro d'identification est invalide !"
                self.txtNumero.setText("")

            NumTel_ = self.txtTel_2
            Employe_.TelEmploye = NumTel_
            if Employe_.TelEmploye != NumTel_:
                MessageErreur += "Le numéro de téléphone est invalide !"
                self.txtNumero.setText("")

            Fonction_ = self.txtFonction.text()
            Employe_.FonctionEmploye = Fonction_
            if Employe_.FonctionEmploye != Fonction_:
                MessageErreur += "La fonction est invalide !"
                self.txtFonction.setText("")

            try:
                TauxHoraire_ = float(self.txtTauxHoraire.text())
                Employe_.TauxHoraire = TauxHoraire_
                if Employe_.TauxHoraire != TauxHoraire_:
                    MessageErreur += "Le taux horaire est invalide"
            except:
                MessageErreur += "Une valeur numérique est obligatoire"
                self.txtTauxHoraire.setText("")

            if MessageErreur == "":
                lsEmployes.append(Employe_)
                self.txtMessage.setText("L'employé a été ajouté à la liste des employés.")
            else:
                MessageErreur += "Veuillez modifier vos informations et re-essayez..."
                self.txtMessage.setText(MessageErreur)


        elif self.btnAjouterModifierSupprimer.text() == "Modifier l'employé":
            self.txtMessage.setText("Test")


        elif self.btnAjouterModifierSupprimer.text() == "Supprimer l'employé":
            self.txtMessage.setText("Wesh la famille")



    @QtCore.pyqtSlot()
    def on_btnModifSuppEmp_clicked(self):

        self.setFixedSize(600, 650)
        self.gbxMenu.setGeometry(QtCore.QRect(1200, 80, 120, 60))
        self.gbxFichePaie.setGeometry(QtCore.QRect(1200, 80, 120, 60))
        self.gbxModifSupp.setGeometry(QtCore.QRect(1200, 80, 120, 60))
        self.gbxRecherche.setGeometry(QtCore.QRect(1200, 350, 120, 60))

        self.gbxAjouterModifier.setGeometry(QtCore.QRect(10, 70, 601, 301))
        if self.lblTitre.text() == "Supprimer un employé":
            self.btnAjouterModifierSupprimer.setText("Supprimer l'employé")

        elif self.lblTitre.text() == "Modifier un employé":
            self.btnAjouterModifierSupprimer.setText("Modifier l'employé")

    @QtCore.pyqtSlot()
    def on_btnRechercher_clicked(self):
        self.setFixedSize(600, 650)
        self.lblTitre.setText("Recherché un employé")
        self.gbxMenu.setGeometry(QtCore.QRect(1200, 80, 120, 60))
        self.gbxFichePaie.setGeometry(QtCore.QRect(1200, 80, 120, 60))
        self.gbxModifSupp.setGeometry(QtCore.QRect(1200, 80, 120, 60))
        self.gbxAjouterModifier.setGeometry(QtCore.QRect(1200, 350, 120, 60))

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
        if self.cboCritereSearch.text() == "Numéro d'identification":
            for objEmploye in lsEmployes:
                if objEmploye.NumEmploye == self.txtValeurSearch.text().upper():
                    lsRecherche.append(objEmploye)
        elif self.cboCritereSearch.text() == "Nom":
            for objEmploye in lsEmployes:
                if objEmploye.NomEmploye == self.txtValeurSearch.text().upper():
                    lsRecherche.append(objEmploye)
        elif self.cboCritereSearch.text() == "Prénom":
            for objEmploye in lsEmployes:
                if objEmploye.PrenomEmploye == self.txtValeurSearch.text().upper():
                    lsRecherche.append(objEmploye)
        elif self.cboCritereSearch.text() == "Fonction":
            for objEmploye in lsEmployes:
                if objEmploye.FonctionEmploye == self.txtValeurSearch.text().upper():
                    lsRecherche.append(objEmploye)
        Chaine = ""
        cpt = 1
        for objEmploye  in lsRecherche:
            Chaine += "{}. {} / {} / {} /{}\n".format(cpt, objEmploye.NumEmploye, objEmploye.NomEmploye, objEmploye.PrenomEmploye, objEmploye.FonctionEmploye)
            cpt += 1

        if len(lsRecherche) == 0:
            self.txtResultSearch.setText("Aucun article trouvé")
        else:
            self.txtResultSearch.setText(Chaine)


    @QtCore.pyqtSlot()
    def on_btnCalculerLaPaie_clicked(self):
        self.txtMessage.setText("Test du bon fonctionnement du bouton pour calculer une paie")

    @QtCore.pyqtSlot()
    def on_btnRech_clicked(self):

        lsRecherche.clear()

        if self.cboCritereSearch.currentText() == "Numéro d'identification":
            for objEmploye in lsEmployes:
                if objEmploye.NumEmploye == self.txtValeurRechModif.text().upper():
                    lsRecherche.append(objEmploye)
        if self.cboCritereSearch.currentText() == "Prénom":
              for objEmploye in lsEmployes:
                if objEmploye.PrenomEmploye == self.txtValeurRechModif.text().upper():
                    lsRecherche.append(objEmploye)
        if self.cboCritereSearch.currentText() == "Nom":
            for objEmploye in lsEmployes:
                if objEmploye.NomEmploye == self.txtValeurRechModif.text().upper():
                    lsRecherche.append(objEmploye)
        if self.cboCritereSearch.currentText() == "Numéro de téléphone":
            for objEmploye in lsEmployes:
                if objEmploye.TelEmploye == self.txtValeurRechModif.text().upper():
                    lsRecherche.append(objEmploye)

        self.cboEmployeModifSupp.clear()
        for objEmploye in lsRecherche:
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






