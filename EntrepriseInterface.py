# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmEntreprise.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EntrepriseGestion(object):
    def setupUi(self, EntrepriseGestion):
        EntrepriseGestion.setObjectName("EntrepriseGestion")
        EntrepriseGestion.resize(2336, 850)
        font = QtGui.QFont()
        font.setPointSize(12)
        EntrepriseGestion.setFont(font)
        self.centralwidget = QtWidgets.QWidget(EntrepriseGestion)
        self.centralwidget.setObjectName("centralwidget")
        self.gbxMenu = QtWidgets.QGroupBox(self.centralwidget)
        self.gbxMenu.setGeometry(QtCore.QRect(40, 50, 331, 331))
        self.gbxMenu.setTitle("")
        self.gbxMenu.setFlat(False)
        self.gbxMenu.setObjectName("gbxMenu")
        self.btnAfficher = QtWidgets.QPushButton(self.gbxMenu)
        self.btnAfficher.setGeometry(QtCore.QRect(10, 10, 311, 31))
        self.btnAfficher.setObjectName("btnAfficher")
        self.btnAJouter = QtWidgets.QPushButton(self.gbxMenu)
        self.btnAJouter.setGeometry(QtCore.QRect(10, 50, 311, 31))
        self.btnAJouter.setObjectName("btnAJouter")
        self.btnSupprimer = QtWidgets.QPushButton(self.gbxMenu)
        self.btnSupprimer.setGeometry(QtCore.QRect(10, 90, 311, 31))
        self.btnSupprimer.setObjectName("btnSupprimer")
        self.btnModifier = QtWidgets.QPushButton(self.gbxMenu)
        self.btnModifier.setGeometry(QtCore.QRect(10, 130, 311, 31))
        self.btnModifier.setObjectName("btnModifier")
        self.btnRechercher = QtWidgets.QPushButton(self.gbxMenu)
        self.btnRechercher.setGeometry(QtCore.QRect(10, 170, 311, 31))
        self.btnRechercher.setObjectName("btnRechercher")
        self.btnFermer = QtWidgets.QPushButton(self.gbxMenu)
        self.btnFermer.setGeometry(QtCore.QRect(10, 290, 311, 31))
        self.btnFermer.setObjectName("btnFermer")
        self.btnCalculerPaie = QtWidgets.QPushButton(self.gbxMenu)
        self.btnCalculerPaie.setGeometry(QtCore.QRect(10, 210, 311, 31))
        self.btnCalculerPaie.setObjectName("btnCalculerPaie")
        self.btnAfficherPaie = QtWidgets.QPushButton(self.gbxMenu)
        self.btnAfficherPaie.setGeometry(QtCore.QRect(10, 250, 311, 31))
        self.btnAfficherPaie.setObjectName("btnAfficherPaie")
        self.gbxAjouterModifierSupprimer = QtWidgets.QGroupBox(self.centralwidget)
        self.gbxAjouterModifierSupprimer.setGeometry(QtCore.QRect(450, 0, 601, 301))
        self.gbxAjouterModifierSupprimer.setTitle("")
        self.gbxAjouterModifierSupprimer.setObjectName("gbxAjouterModifierSupprimer")
        self.txtNumero = QtWidgets.QLineEdit(self.gbxAjouterModifierSupprimer)
        self.txtNumero.setGeometry(QtCore.QRect(30, 40, 191, 20))
        self.txtNumero.setObjectName("txtNumero")
        self.txtNom = QtWidgets.QLineEdit(self.gbxAjouterModifierSupprimer)
        self.txtNom.setGeometry(QtCore.QRect(30, 110, 191, 20))
        self.txtNom.setObjectName("txtNom")
        self.lblNumero = QtWidgets.QLabel(self.gbxAjouterModifierSupprimer)
        self.lblNumero.setGeometry(QtCore.QRect(30, 20, 171, 16))
        self.lblNumero.setObjectName("lblNumero")
        self.lblNom = QtWidgets.QLabel(self.gbxAjouterModifierSupprimer)
        self.lblNom.setGeometry(QtCore.QRect(30, 80, 131, 21))
        self.lblNom.setObjectName("lblNom")
        self.lblPrenom = QtWidgets.QLabel(self.gbxAjouterModifierSupprimer)
        self.lblPrenom.setGeometry(QtCore.QRect(30, 150, 201, 21))
        self.lblPrenom.setObjectName("lblPrenom")
        self.txtPrenom = QtWidgets.QLineEdit(self.gbxAjouterModifierSupprimer)
        self.txtPrenom.setGeometry(QtCore.QRect(30, 170, 191, 20))
        self.txtPrenom.setObjectName("txtPrenom")
        self.txtTel_2 = QtWidgets.QLineEdit(self.gbxAjouterModifierSupprimer)
        self.txtTel_2.setGeometry(QtCore.QRect(30, 220, 191, 20))
        self.txtTel_2.setObjectName("txtTel_2")
        self.lblTel = QtWidgets.QLabel(self.gbxAjouterModifierSupprimer)
        self.lblTel.setGeometry(QtCore.QRect(30, 200, 191, 21))
        self.lblTel.setObjectName("lblTel")
        self.lblFonction = QtWidgets.QLabel(self.gbxAjouterModifierSupprimer)
        self.lblFonction.setGeometry(QtCore.QRect(360, 20, 191, 21))
        self.lblFonction.setObjectName("lblFonction")
        self.txtTauxHoraire = QtWidgets.QLineEdit(self.gbxAjouterModifierSupprimer)
        self.txtTauxHoraire.setGeometry(QtCore.QRect(360, 110, 191, 20))
        self.txtTauxHoraire.setObjectName("txtTauxHoraire")
        self.lblTauxHoraire = QtWidgets.QLabel(self.gbxAjouterModifierSupprimer)
        self.lblTauxHoraire.setGeometry(QtCore.QRect(360, 90, 191, 16))
        self.lblTauxHoraire.setObjectName("lblTauxHoraire")
        self.btnAjouterModifierSupprimer = QtWidgets.QPushButton(self.gbxAjouterModifierSupprimer)
        self.btnAjouterModifierSupprimer.setGeometry(QtCore.QRect(320, 170, 231, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnAjouterModifierSupprimer.setFont(font)
        self.btnAjouterModifierSupprimer.setObjectName("btnAjouterModifierSupprimer")
        self.txtFonction = QtWidgets.QLineEdit(self.gbxAjouterModifierSupprimer)
        self.txtFonction.setGeometry(QtCore.QRect(360, 40, 191, 20))
        self.txtFonction.setObjectName("txtFonction")
        self.btnRetourMenu = QtWidgets.QPushButton(self.centralwidget)
        self.btnRetourMenu.setGeometry(QtCore.QRect(30, 460, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.btnRetourMenu.setFont(font)
        self.btnRetourMenu.setObjectName("btnRetourMenu")
        self.txtMessage = QtWidgets.QTextBrowser(self.centralwidget)
        self.txtMessage.setGeometry(QtCore.QRect(30, 510, 321, 91))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.txtMessage.setFont(font)
        self.txtMessage.setObjectName("txtMessage")
        self.lblTitre = QtWidgets.QLabel(self.centralwidget)
        self.lblTitre.setGeometry(QtCore.QRect(50, 0, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitre.setFont(font)
        self.lblTitre.setObjectName("lblTitre")
        self.gbxFichePaie = QtWidgets.QGroupBox(self.centralwidget)
        self.gbxFichePaie.setGeometry(QtCore.QRect(550, 320, 501, 421))
        self.gbxFichePaie.setTitle("")
        self.gbxFichePaie.setObjectName("gbxFichePaie")
        self.cboTypeEmploie = QtWidgets.QComboBox(self.gbxFichePaie)
        self.cboTypeEmploie.setGeometry(QtCore.QRect(30, 70, 201, 31))
        self.cboTypeEmploie.setObjectName("cboTypeEmploie")
        self.lblTypeEmploie = QtWidgets.QLabel(self.gbxFichePaie)
        self.lblTypeEmploie.setGeometry(QtCore.QRect(30, 50, 201, 21))
        self.lblTypeEmploie.setObjectName("lblTypeEmploie")
        self.txtNbHeures = QtWidgets.QLineEdit(self.gbxFichePaie)
        self.txtNbHeures.setGeometry(QtCore.QRect(30, 130, 201, 22))
        self.txtNbHeures.setObjectName("txtNbHeures")
        self.lblNbHeures = QtWidgets.QLabel(self.gbxFichePaie)
        self.lblNbHeures.setGeometry(QtCore.QRect(30, 110, 201, 16))
        self.lblNbHeures.setObjectName("lblNbHeures")
        self.txtAffichageFiche = QtWidgets.QTextBrowser(self.gbxFichePaie)
        self.txtAffichageFiche.setGeometry(QtCore.QRect(30, 200, 451, 192))
        self.txtAffichageFiche.setObjectName("txtAffichageFiche")
        self.lblFichePaie = QtWidgets.QLabel(self.gbxFichePaie)
        self.lblFichePaie.setGeometry(QtCore.QRect(180, 160, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lblFichePaie.setFont(font)
        self.lblFichePaie.setObjectName("lblFichePaie")
        self.btnCalculerLaPaie = QtWidgets.QPushButton(self.gbxFichePaie)
        self.btnCalculerLaPaie.setGeometry(QtCore.QRect(290, 100, 191, 61))
        self.btnCalculerLaPaie.setObjectName("btnCalculerLaPaie")
        self.txtNumeroEmploye = QtWidgets.QLineEdit(self.gbxFichePaie)
        self.txtNumeroEmploye.setGeometry(QtCore.QRect(290, 60, 191, 20))
        self.txtNumeroEmploye.setObjectName("txtNumeroEmploye")
        self.lblNumeroEmploye = QtWidgets.QLabel(self.gbxFichePaie)
        self.lblNumeroEmploye.setGeometry(QtCore.QRect(290, 40, 201, 21))
        self.lblNumeroEmploye.setObjectName("lblNumeroEmploye")
        self.txtFiche = QtWidgets.QLineEdit(self.gbxFichePaie)
        self.txtFiche.setGeometry(QtCore.QRect(30, 30, 201, 20))
        self.txtFiche.setObjectName("txtFiche")
        self.lblNumeroFiche = QtWidgets.QLabel(self.gbxFichePaie)
        self.lblNumeroFiche.setGeometry(QtCore.QRect(30, 10, 201, 21))
        self.lblNumeroFiche.setObjectName("lblNumeroFiche")
        self.gbxRecherche = QtWidgets.QGroupBox(self.centralwidget)
        self.gbxRecherche.setGeometry(QtCore.QRect(1060, 0, 591, 391))
        self.gbxRecherche.setTitle("")
        self.gbxRecherche.setObjectName("gbxRecherche")
        self.cboCritereSearch = QtWidgets.QComboBox(self.gbxRecherche)
        self.cboCritereSearch.setGeometry(QtCore.QRect(10, 40, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.cboCritereSearch.setFont(font)
        self.cboCritereSearch.setCurrentText("")
        self.cboCritereSearch.setObjectName("cboCritereSearch")
        self.lblCritereSearch = QtWidgets.QLabel(self.gbxRecherche)
        self.lblCritereSearch.setGeometry(QtCore.QRect(10, 10, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.lblCritereSearch.setFont(font)
        self.lblCritereSearch.setObjectName("lblCritereSearch")
        self.lblValeurSearch = QtWidgets.QLabel(self.gbxRecherche)
        self.lblValeurSearch.setGeometry(QtCore.QRect(10, 80, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.lblValeurSearch.setFont(font)
        self.lblValeurSearch.setObjectName("lblValeurSearch")
        self.txtValeurSearch = QtWidgets.QLineEdit(self.gbxRecherche)
        self.txtValeurSearch.setGeometry(QtCore.QRect(10, 110, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.txtValeurSearch.setFont(font)
        self.txtValeurSearch.setObjectName("txtValeurSearch")
        self.lblResultSearch = QtWidgets.QLabel(self.gbxRecherche)
        self.lblResultSearch.setGeometry(QtCore.QRect(10, 150, 281, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.lblResultSearch.setFont(font)
        self.lblResultSearch.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblResultSearch.setObjectName("lblResultSearch")
        self.txtResultSearch = QtWidgets.QTextBrowser(self.gbxRecherche)
        self.txtResultSearch.setGeometry(QtCore.QRect(10, 180, 541, 192))
        self.txtResultSearch.setObjectName("txtResultSearch")
        self.btnSearch = QtWidgets.QPushButton(self.gbxRecherche)
        self.btnSearch.setGeometry(QtCore.QRect(330, 110, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.btnSearch.setFont(font)
        self.btnSearch.setObjectName("btnSearch")
        self.gbxModifSupp = QtWidgets.QGroupBox(self.centralwidget)
        self.gbxModifSupp.setGeometry(QtCore.QRect(1100, 310, 561, 371))
        self.gbxModifSupp.setTitle("")
        self.gbxModifSupp.setObjectName("gbxModifSupp")
        self.cboCritereRechModif = QtWidgets.QComboBox(self.gbxModifSupp)
        self.cboCritereRechModif.setGeometry(QtCore.QRect(10, 80, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.cboCritereRechModif.setFont(font)
        self.cboCritereRechModif.setCurrentText("")
        self.cboCritereRechModif.setObjectName("cboCritereRechModif")
        self.lblCritereRechModif = QtWidgets.QLabel(self.gbxModifSupp)
        self.lblCritereRechModif.setGeometry(QtCore.QRect(10, 50, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.lblCritereRechModif.setFont(font)
        self.lblCritereRechModif.setObjectName("lblCritereRechModif")
        self.lblValeurRechModif = QtWidgets.QLabel(self.gbxModifSupp)
        self.lblValeurRechModif.setGeometry(QtCore.QRect(10, 120, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.lblValeurRechModif.setFont(font)
        self.lblValeurRechModif.setObjectName("lblValeurRechModif")
        self.txtValeurRechModif = QtWidgets.QLineEdit(self.gbxModifSupp)
        self.txtValeurRechModif.setGeometry(QtCore.QRect(10, 150, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.txtValeurRechModif.setFont(font)
        self.txtValeurRechModif.setObjectName("txtValeurRechModif")
        self.btnRech = QtWidgets.QPushButton(self.gbxModifSupp)
        self.btnRech.setGeometry(QtCore.QRect(330, 150, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.btnRech.setFont(font)
        self.btnRech.setObjectName("btnRech")
        self.lblLstModifSupp = QtWidgets.QLabel(self.gbxModifSupp)
        self.lblLstModifSupp.setGeometry(QtCore.QRect(10, 240, 421, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblLstModifSupp.setFont(font)
        self.lblLstModifSupp.setObjectName("lblLstModifSupp")
        self.cboEmployeModifSupp = QtWidgets.QComboBox(self.gbxModifSupp)
        self.cboEmployeModifSupp.setGeometry(QtCore.QRect(10, 270, 541, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.cboEmployeModifSupp.setFont(font)
        self.cboEmployeModifSupp.setCurrentText("")
        self.cboEmployeModifSupp.setObjectName("cboEmployeModifSupp")
        self.btnModifSuppEmp = QtWidgets.QPushButton(self.gbxModifSupp)
        self.btnModifSuppEmp.setGeometry(QtCore.QRect(150, 310, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.btnModifSuppEmp.setFont(font)
        self.btnModifSuppEmp.setObjectName("btnModifSuppEmp")
        self.lblModSupSearch = QtWidgets.QLabel(self.gbxModifSupp)
        self.lblModSupSearch.setGeometry(QtCore.QRect(10, 20, 421, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblModSupSearch.setFont(font)
        self.lblModSupSearch.setObjectName("lblModSupSearch")
        self.line = QtWidgets.QFrame(self.gbxModifSupp)
        self.line.setGeometry(QtCore.QRect(70, 200, 421, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gbxConnexion = QtWidgets.QGroupBox(self.centralwidget)
        self.gbxConnexion.setGeometry(QtCore.QRect(1640, 10, 331, 301))
        self.gbxConnexion.setTitle("")
        self.gbxConnexion.setObjectName("gbxConnexion")
        self.txtNomAdmin = QtWidgets.QLineEdit(self.gbxConnexion)
        self.txtNomAdmin.setGeometry(QtCore.QRect(10, 70, 301, 51))
        self.txtNomAdmin.setObjectName("txtNomAdmin")
        self.txtMdpAdmin = QtWidgets.QLineEdit(self.gbxConnexion)
        self.txtMdpAdmin.setGeometry(QtCore.QRect(10, 180, 301, 51))
        self.txtMdpAdmin.setObjectName("txtMdpAdmin")
        self.btnConnexion = QtWidgets.QPushButton(self.gbxConnexion)
        self.btnConnexion.setGeometry(QtCore.QRect(70, 240, 171, 51))
        self.btnConnexion.setObjectName("btnConnexion")
        self.lblNomAdmin = QtWidgets.QLabel(self.gbxConnexion)
        self.lblNomAdmin.setGeometry(QtCore.QRect(40, 30, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblNomAdmin.setFont(font)
        self.lblNomAdmin.setObjectName("lblNomAdmin")
        self.lblMdpAdmin = QtWidgets.QLabel(self.gbxConnexion)
        self.lblMdpAdmin.setGeometry(QtCore.QRect(40, 140, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblMdpAdmin.setFont(font)
        self.lblMdpAdmin.setObjectName("lblMdpAdmin")
        self.gbxVerifQuitter = QtWidgets.QGroupBox(self.centralwidget)
        self.gbxVerifQuitter.setGeometry(QtCore.QRect(1660, 470, 381, 231))
        self.gbxVerifQuitter.setTitle("")
        self.gbxVerifQuitter.setObjectName("gbxVerifQuitter")
        self.lblVerifQuitter = QtWidgets.QLabel(self.gbxVerifQuitter)
        self.lblVerifQuitter.setGeometry(QtCore.QRect(10, 50, 361, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lblVerifQuitter.setFont(font)
        self.lblVerifQuitter.setObjectName("lblVerifQuitter")
        self.btnOUI = QtWidgets.QPushButton(self.gbxVerifQuitter)
        self.btnOUI.setGeometry(QtCore.QRect(40, 130, 121, 61))
        self.btnOUI.setObjectName("btnOUI")
        self.btnNON = QtWidgets.QPushButton(self.gbxVerifQuitter)
        self.btnNON.setGeometry(QtCore.QRect(210, 130, 121, 61))
        self.btnNON.setObjectName("btnNON")
        EntrepriseGestion.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EntrepriseGestion)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 2336, 21))
        self.menubar.setObjectName("menubar")
        EntrepriseGestion.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EntrepriseGestion)
        self.statusbar.setObjectName("statusbar")
        EntrepriseGestion.setStatusBar(self.statusbar)

        self.retranslateUi(EntrepriseGestion)
        QtCore.QMetaObject.connectSlotsByName(EntrepriseGestion)

    def retranslateUi(self, EntrepriseGestion):
        _translate = QtCore.QCoreApplication.translate
        EntrepriseGestion.setWindowTitle(_translate("EntrepriseGestion", "MainWindow"))
        self.btnAfficher.setText(_translate("EntrepriseGestion", "Afficher la liste des employ??s"))
        self.btnAJouter.setText(_translate("EntrepriseGestion", "Ajouter un employ??"))
        self.btnSupprimer.setText(_translate("EntrepriseGestion", "Supprimer un employ??"))
        self.btnModifier.setText(_translate("EntrepriseGestion", "Modifier un employ??"))
        self.btnRechercher.setText(_translate("EntrepriseGestion", "Rechercher un employ??"))
        self.btnFermer.setText(_translate("EntrepriseGestion", "Fermer l\'application"))
        self.btnCalculerPaie.setText(_translate("EntrepriseGestion", "Calculer un paie"))
        self.btnAfficherPaie.setText(_translate("EntrepriseGestion", "Afficher l\'historique des fiches de paie"))
        self.lblNumero.setText(_translate("EntrepriseGestion", "Num??ro d\'identification"))
        self.lblNom.setText(_translate("EntrepriseGestion", "Nom de l\'employ??"))
        self.lblPrenom.setText(_translate("EntrepriseGestion", "Pr??nom de l\'employ??"))
        self.lblTel.setText(_translate("EntrepriseGestion", "Num??ro de t??l??phone"))
        self.lblFonction.setText(_translate("EntrepriseGestion", "Fonction occup??e"))
        self.lblTauxHoraire.setText(_translate("EntrepriseGestion", "Taux horaire"))
        self.btnAjouterModifierSupprimer.setText(_translate("EntrepriseGestion", "Ajouter l\'employ??"))
        self.btnRetourMenu.setText(_translate("EntrepriseGestion", "Retour au menu"))
        self.lblTitre.setText(_translate("EntrepriseGestion", "Bienvenue sur le site de l\'entreprise"))
        self.lblTypeEmploie.setText(_translate("EntrepriseGestion", "Type d\'emploie"))
        self.lblNbHeures.setText(_translate("EntrepriseGestion", "Nombre d\'heures travaill??es"))
        self.lblFichePaie.setText(_translate("EntrepriseGestion", "Fiche de paie"))
        self.btnCalculerLaPaie.setText(_translate("EntrepriseGestion", "Calculer la paie"))
        self.lblNumeroEmploye.setText(_translate("EntrepriseGestion", "Num??ro de l\'employ??"))
        self.lblNumeroFiche.setText(_translate("EntrepriseGestion", "Num??ro de la fiche"))
        self.lblCritereSearch.setText(_translate("EntrepriseGestion", "Crit??re de recherche"))
        self.lblValeurSearch.setText(_translate("EntrepriseGestion", "Valeur ?? chercher"))
        self.lblResultSearch.setText(_translate("EntrepriseGestion", "R??sultat(s) de recherche"))
        self.btnSearch.setText(_translate("EntrepriseGestion", "Lancer la recherche"))
        self.lblCritereRechModif.setText(_translate("EntrepriseGestion", "Crit??re de recherche"))
        self.lblValeurRechModif.setText(_translate("EntrepriseGestion", "Valeur ?? chercher"))
        self.btnRech.setText(_translate("EntrepriseGestion", "Lancer la recherche"))
        self.lblLstModifSupp.setText(_translate("EntrepriseGestion", "Choisir l\'employ?? ?? modifier"))
        self.btnModifSuppEmp.setText(_translate("EntrepriseGestion", "Modifier l\'employ??"))
        self.lblModSupSearch.setText(_translate("EntrepriseGestion", "Chercher l\'employ?? ?? modifier"))
        self.btnConnexion.setText(_translate("EntrepriseGestion", "Se connecter"))
        self.lblNomAdmin.setText(_translate("EntrepriseGestion", "Nom d\'utilisateur admin:"))
        self.lblMdpAdmin.setText(_translate("EntrepriseGestion", "Mot de passe admin:"))
        self.lblVerifQuitter.setText(_translate("EntrepriseGestion", "Voulez-vous vraiment quitter ?"))
        self.btnOUI.setText(_translate("EntrepriseGestion", "OUI"))
        self.btnNON.setText(_translate("EntrepriseGestion", "NON"))
