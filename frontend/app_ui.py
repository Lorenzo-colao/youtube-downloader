import tkinter as tk
from tkinter import filedialog
from backend.downloader import telecharger_mp3

def lancer_app():
    
    
    root = tk.Tk()
    root.title("YouTube MP3 Downloader")
    
    largeur_fenetre = 400
    hauteur_fenetre = 200
    largeur_ecran = root.winfo_screenwidth()
    hauteur_ecran = root.winfo_screenheight()
    x = (largeur_ecran - largeur_fenetre) / 2
    y = (hauteur_ecran - hauteur_fenetre) / 2
    
    root.geometry(f"{largeur_fenetre}x{hauteur_fenetre}+{int(x)}+{int(y)}")
    
    dossier_var = tk.StringVar()
    dossier_var.set("Aucun dossier sélectionné")
    
    def on_click() : 
        url = entry.get()
        dossier_utilisateur = dossier_var.get()
        resultat = telecharger_mp3(url, dossier_utilisateur)
        print(resultat)
        
    def choisir_dossier() :
        chemin_utilisateur = filedialog.askdirectory()
        dossier_var.set(chemin_utilisateur)
        dossier_var.get()
    
    label = tk.Label(root, text="Colle ton URL YouTube ici :")
    label.pack()
    entry = tk.Entry(root, width=50)
    entry.pack(pady=5)
    button = tk.Button(root, text="Télécharger", command=on_click)
    button.pack(pady=8)
    button_dossier = tk.Button(root, text="Choisir dossier", command=choisir_dossier)
    button_dossier.pack(pady=8)
    label_chemin_utilisateur = tk.Label(root, textvariable=dossier_var)
    label_chemin_utilisateur.pack(pady=8)
    
    root.mainloop()