import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph
from reportlab.lib.pagesizes import A2
from db import Database
from salary_calculator import calculate_salary

#gui.py : Gestion de l'interface utilisateur

class SalaryApp:
    def __init__(self, root):
        self.db = Database()
        self.root = root
        self.root.title('ChitirSalaire')
        self.root.iconbitmap("C:/Users/k/Downloads/projet/icon.ico")
        self.root.geometry("1170x750")
        self.root.resizable(width=False, height=False)

        self.setup_ui()

    def setup_ui(self):

        self.frame_1 = tk.Frame(self.root, bg='#E98C34')
        self.frame_1.pack(side=tk.LEFT)
        self.frame_1.configure(width=320, height=750)
        
        self.frame_2 = tk.Frame(self.root, highlightthickness='1')
        self.frame_2.pack()
        self.frame_2.configure(width=850, height=750)
        global img
        img = ImageTk.PhotoImage(Image.open("C:/Users/k/Downloads/projet/photo_1.jpg").resize((850,750)))
        tk.Label(self.frame_2, image=img).pack()
  

        #Ajout des boutons dans le menu

        ajout = tk.Button(self.frame_1,text='Ajouter un employé',font=('Bold',14),fg='blue',bd='0',bg='#E98C34',command=lambda:indiquer(ajindic, self.ajouter_employe))
        ajout.place(x=35, y=250)
        ajindic = tk.Label(self.frame_1, text='',bg='#E98C34')
        ajindic.place(x=2, y=250, width=5, height=30)

        retirer = tk.Button(self.frame_1,text='Rerirer un employé',font=('Bold',14),fg='blue',bd='0',bg='#E98C34',command=lambda:indiquer(retindic, self.page_retirer))
        retirer.place(x=35, y=300)
        retindic = tk.Label(self.frame_1, text='',bg='#E98C34')
        retindic.place(x=2, y=300, width=5, height=30)

        calcul= tk.Button(self.frame_1,text='Calculer',font=('Bold',14),fg='blue',bd='0',bg='#E98C34',command=lambda:indiquer(calcindic, self.calculer_salaire))
        calcul.place(x=35, y=350)
        calcindic = tk.Label(self.frame_1, text='',bg='#E98C34')
        calcindic.place(x=2, y=350, width=5, height=30)

        fermer = tk.Button(self.frame_1,text='Fermer',font=('Bold',14),fg='blue',bd='0',bg='#E98C34',command=lambda:indiquer(ferindic, self.page_fermer))
        fermer.place(x=35, y=400)
        ferindic = tk.Label(self.frame_1, text='',bg='#E98C34')
        ferindic.place(x=2, y=400, width=5, height=30)
            

        def hide():
            ajindic.config(bg='#E98C34')
            retindic.config(bg='#E98C34')
            calcindic.config(bg='#E98C34')
            ferindic.config(bg='#E98C34')

        def indiquer(lab, aff):
            hide()
            lab.config(bg='blue')
            for page in self.frame_2.winfo_children():
                page.destroy()
            aff()  


    def ajouter_employe(self):
        
        tk.Label(self.frame_2, text='CNSS :', font=('Bold', 12), fg = 'green').grid(row=1, column=0, padx=10, pady=10)
        self.entry_cnss = tk.Entry(self.frame_2, borderwidth=5, font=('italic', 12),fg='brown')
        self.entry_cnss.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.frame_2, text='NOM :', font=('Bold', 12), fg='green').grid(row=2, column=0, padx=10, pady=10)
        self.entry_nom = tk.Entry(self.frame_2, borderwidth=5, font=('italic', 12),fg='brown')
        self.entry_nom.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self.frame_2, text='POSTE :', font=('Bold', 12),fg='green').grid(row=3, column=0, padx=10, pady=10)
        self.entry_poste = tk.Entry(self.frame_2, borderwidth=5, font=('italic', 12),fg='brown')
        self.entry_poste.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(self.frame_2, text='SALAIRE DE BASE :', font=('Bold', 12),fg='green').grid(row=4, column=0, padx=10, pady=10)
        self.entry_salaire_base = tk.Entry(self.frame_2, borderwidth=5, font=('italic', 12),fg='brown')
        self.entry_salaire_base.grid(row=4, column=1, padx=10, pady=10)

        tk.Label(self.frame_2, text='').grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.frame_2, text='').grid(row=19, column=0, padx=10, pady=10)
        tk.Label(self.frame_2, text='').grid(row=24, column=0, padx=10, pady=10)

        self.tree = ttk.Treeview(self.frame_2, columns=(1, 2, 3, 4), show='headings', height=10)
        self.tree.grid(row=20, column=0, columnspan=2)
        self.tree.heading(1, text='CNSS')
        self.tree.heading(2, text='Nom')
        self.tree.heading(3, text='Poste')
        self.tree.heading(4, text='Salaire de base')

        def ajouter():
            if (self.entry_cnss.get()=="" or " " in self.entry_cnss.get() and self.entry_nom.get()=="" or " " in self.entry_nom.get() and self.entry_poste.get()=="" or " " in self.entry_poste.get() and self.entry_salaire_base.get()=="" or " " in self.entry_salaire_base.get()):
                messagebox.showerror("Erreur", "Veuillez remplir les champs")
            else:
                try:
                    cnss = int(self.entry_cnss.get())
                    nom = self.entry_nom.get()
                    poste = self.entry_poste.get()
                    salaire_base = float(self.entry_salaire_base.get())

                    self.db.add_employees(cnss, nom, poste, salaire_base)
                    messagebox.showinfo('Succès', 'Employé ajouté avec succès')
                    self.clear_entries()
                except:
                    messagebox.showerror("Erreur", "Le CNSS et le SALAIRE DE BASE doivent etre des chiffres")

        tk.Button(self.frame_2, text='Ajouter', command=ajouter, font=('Bold', 15), borderwidth=5).grid(row=10, column=1, ipadx=50, ipady=3, padx=10, pady=10)

        def afficher_employes():
            for row in self.tree.get_children():
                self.tree.delete(row)
            employes = self.db.get_employees()
            for employe in employes:
                self.tree.insert('', 'end', values=employe)

        tk.Button(self.frame_2, text='Afficher la liste', command=afficher_employes, font=('Bold', 15), borderwidth=5).grid(row=25, columnspan=2, ipadx=10, ipady=3, padx=10, pady=10)

    def calculer_salaire(self):
        
        def afficher_employes():
            for row in self.tree.get_children():
                self.tree.delete(row)
            employes = self.db.get_employees()
            for employe in employes:
                self.tree.insert('', 'end', values=employe)

        tk.Label(self.frame_2, text='').grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.frame_2, text='').grid(row=9, column=0, padx=10, pady=10)
        tk.Label(self.frame_2, text='').grid(row=19, column=0, padx=10, pady=10)
        tk.Label(self.frame_2, text='').grid(row=24, column=0, padx=10, pady=10)
        tk.Label(self.frame_2, text='').grid(row=29, column=0, padx=10, pady=10)
        
        
        tk.Label(self.frame_2, text='SELECTIONNEZ UN EMPLOYE POUR LE CALCUL', fg= 'red', font=('Bold', 15)).grid(row=5, columnspan=4, padx=10, pady=10)

        tk.Button(self.frame_2, text='Afficher la liste', command=afficher_employes, font=('Bold', 15), borderwidth=5).grid(row= 8, columnspan=4, ipadx=10, ipady=3, padx=10, pady=10)

        self.tree = ttk.Treeview(self.frame_2, columns=(1, 2, 3, 4), show='headings', height=10)
        self.tree.grid(row=10, column=0, columnspan=4)
        self.tree.heading(1, text='CNSS')
        self.tree.heading(2, text='Nom')
        self.tree.heading(3, text='Poste')
        self.tree.heading(4, text='Salaire de base')

        tk.Label(self.frame_2, text='MOIS :', font=('Bold', 12),fg='green').grid(row=20, column=0, padx=5, pady=10)
        self.combo_mois = ttk.Combobox(self.frame_2, values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        self.combo_mois.grid(row=20, column=1, padx=10, pady=10)

        tk.Label(self.frame_2, text='ANNEE :', font=('Bold', 12),fg='green').grid(row=20, column=2, padx=5, pady=10)
        self.entry_annee = tk.Entry(self.frame_2, borderwidth=5, font=('italic', 12),fg='brown')
        self.entry_annee.grid(row=20, column=3, padx=10, pady=10)

        tk.Label(self.frame_2, text='PRIMES :', font=('Bold', 12),fg='green').grid(row=21, column=0, padx=5, pady=10)
        self.entry_primes = tk.Entry(self.frame_2, borderwidth=5, font=('italic', 12),fg='brown')
        self.entry_primes.grid(row=21, column=1, padx=10, pady=10)

        tk.Label(self.frame_2, text='RETENUES :', font=('Bold', 12),fg='green').grid(row=21, column=2, padx=5, pady=10)
        self.entry_retenues = tk.Entry(self.frame_2, borderwidth=5, font=('italic', 12),fg='brown')
        self.entry_retenues.grid(row=21, column=3, padx=10, pady=10)

        tk.Label(self.frame_2, text='SALAIRE NET :', fg='red', font=('Bold', 12)).grid(row=25, columnspan=2, column=1, padx=5, pady=10)

        def calculer():
            try :
                primes = float(self.entry_primes.get())
                retenues = float(self.entry_retenues.get())
            except:
                messagebox.showerror("Erreur", "Veuillez selectionner un employe et remplir les champs !")

            selected_item = self.tree.focus()
            if selected_item:
                item = self.tree.item(selected_item)
                cnss = item['values'][0]
                nom = item['values'][1]
                salaire_base = float(item['values'][3])

                salaire_net = calculate_salary(salaire_base, primes, retenues)  # Add logic for bonuses and deductions as needed

                mois = self.combo_mois.get()
                annee = self.entry_annee.get()
                                
                tk.Label(self.frame_2, text=f"{salaire_net}", font=('italic', 15), fg='red').grid(row=25, columnspan=2, column=2, padx=15, pady=10)
                
                self.db.add_payslip(cnss, nom,  mois, annee, salaire_net)

                # Détails de la fiche de paie
                payslip_data = [
                    ['Fiche de Paie', '', '', '', ''],
                    ['Periode', mois, '/', annee, ''],
                    ['Cnss', cnss, '', '', ''],
                    ['Nom de l\'employé', nom, '', '', ''],
                    ['Primes', primes, 'FCFA', '', ''],
                    ['Retenues', retenues, 'FCFA', '', ''],
                    ['Salaire de base', salaire_base, 'FCFA', '', ''],
                    ['Salaire Net', salaire_net, 'FCFA', '', '']]
                
                # Création du document PDF
                pdf_file = f"{nom}_fiche_de_paie.pdf"
                document = SimpleDocTemplate(pdf_file, pagesize=A2)

                # Table des données
                table = Table(payslip_data)

                # Ajout de la table et du titre au document
                elements = [
                    Paragraph("Fiche de Paie"),
                    table
                ]

                # Génération du PDF
                document.build(elements)

                messagebox.showinfo("Succès", f"Fiche de paie générée: {pdf_file}")

        tk.Button(self.frame_2, text='CALCULER LE SALAIRE', command=calculer, font=('Bold', 12),background='orange', borderwidth=5).grid(row=27, columnspan=2, column=2, ipadx=10, ipady=5, padx=10, pady=10)

        def liste_paye():
            lst = tk.Toplevel()
            lst.iconbitmap("C:/Users/k/Downloads/projet/icon.ico")
            tree = ttk.Treeview(lst, columns=(1, 2, 3, 4, 5), show='headings', height=10)
            tree.grid(row=1, column=0, columnspan=2)
            tree.heading(1, text='CNSS')
            tree.heading(2, text='Nom')
            tree.heading(3, text='Mois')
            tree.heading(4, text='Annee')
            tree.heading(5, text='Salaire net')

            for row in tree.get_children():
                tree.delete(row)
            for emp in self.db.get_payslip():
                tree.insert('', 'end', values=emp)
            def eff():
                for rw in tree.get_children():
                    tree.delete(rw)
                self.db.del_payslip()

            tk.Button(lst, text='EFFACER LA LISTE', command=eff, font=('Bold', 12), borderwidth=5).grid(row=5, columnspan=2, ipadx=10, ipady=5, padx=10, pady=10)

        tk.Button(self.frame_2, text='EMPLOYES PAYES', command=liste_paye, font=('Bold', 12), borderwidth=5).grid(row=27, columnspan=2, column=1, ipadx=10, ipady=5, padx=10, pady=10)

    def page_retirer(self):
        tk.Label(self.frame_2, text='CNSS EMPLOYE :', font=('Bold', 12),fg='green').grid(row=1, column=0, padx=10, pady=10)
        self.entry_id = tk.Entry(self.frame_2, borderwidth=5, font=('italic', 12),fg='brown')
        self.entry_id.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.frame_2, text='').grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.frame_2, text='').grid(row=19, column=0, padx=10, pady=10)
        tk.Label(self.frame_2, text='').grid(row=24, column=0, padx=10, pady=10)
        

        self.tree = ttk.Treeview(self.frame_2, columns=(1, 2, 3, 4), show='headings', height=10)
        self.tree.grid(row=25, column=0, columnspan=2)
        self.tree.heading(1, text='CNSS')
        self.tree.heading(2, text='Nom')
        self.tree.heading(3, text='Poste')
        self.tree.heading(4, text='Salaire de base')

        def ret():
            lste = []
            for row in self.tree.get_children():
                lste.append(int(self.tree.item(row)["values"][0]))

            try:
                
                    if  int(self.entry_id.get()) in lste: 
                        self.tree.delete(row) 
                        self.db.del_employees(int(self.entry_id.get()))
                        self.entry_id.delete(0, tk.END)
                        messagebox.showinfo("Information", "Employe retire avec succes")
                    else:
                        messagebox.showerror("Erreur", f"L'employe {self.entry_id.get()} n'est pas dans la base")
            except :
                messagebox.showerror("Erreur", "Entree invalide")

        tk.Button(self.frame_2, text='Retirer', command=ret, font=('Bold', 15), borderwidth=5).grid(row=20, column=1, ipadx=10, ipady=3, padx=10, pady=10)

        def actualiser():
            for row in self.tree.get_children():
                self.tree.delete(row)
            employes = self.db.get_employees()
            for employe in employes:
                self.tree.insert('', 'end', values=employe)

        tk.Button(self.frame_2, text='Actualiser', command=actualiser, font=('Bold', 15), borderwidth=5).grid(row=30, columnspan=2, ipadx=10, ipady=3, padx=10, pady=10)
            
    def page_fermer(self):
        global img
        img = ImageTk.PhotoImage(Image.open("C:/Users/k/Downloads/projet/photo_2.jpg").resize((850,750)))
        tk.Label(self.frame_2, image=img).pack()
        rep = messagebox.askquestion("Confirmation", "Voulez-vous vraiment quitter  ?")
        if rep == "yes":
            self.frame_2.quit()
        else:
            tk.Label(self.frame_2, image=img).pack()
            
        

    def clear_entries(self):
        self.entry_cnss.delete(0, tk.END)
        self.entry_nom.delete(0, tk.END)
        self.entry_poste.delete(0, tk.END)
        self.entry_salaire_base.delete(0, tk.END)

    def on_close(self):
        self.db.close()
        self.root.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = SalaryApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()
