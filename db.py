import sqlite3

# db.py : Gestion de la base de données
class Database:
    def __init__(self, db_name='gestion_salaires.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS employes (
                                  cnss INTEGER PRIMARY KEY,
                                  nom TEXT NOT NULL,
                                  poste TEXT NOT NULL,
                                  salaire_de_base REAL NOT NULL
                              )''')
            self.conn.execute('''CREATE TABLE IF NOT EXISTS fiches_de_paie (
                                  cnss INTEGER PRIMARY KEY,
                                  nom TEXT NOT NULL,
                                  mois INTEGER NOT NULL,
                                  annee INTEGER NOT NULL,
                                  salaire_net REAL NOT NULL,
                                  FOREIGN KEY (cnss) REFERENCES employes (cnss)
                                  )''')

    def add_employees(self, cnss, nom, poste, salaire_base):
        with self.conn:
            self.conn.execute('INSERT INTO employes (cnss, nom, poste, salaire_de_base) VALUES (?, ?, ?, ?)', 
                              (cnss, nom, poste, salaire_base))

    def del_employees(self, id):
        with self.conn:
            self.conn.execute(f"DELETE FROM employes WHERE cnss = {id}")

    def get_employees(self):
        with self.conn:
            return self.conn.execute('SELECT * FROM employes').fetchall()
    
    def get_payslip(self):
        with self.conn:
            return self.conn.execute('SELECT * FROM fiches_de_paie').fetchall()

    def add_payslip(self, cnss, nom, mois, annee, salaire_net):
        with self.conn:
            self.conn.execute('INSERT INTO fiches_de_paie (cnss, nom,  mois, annee, salaire_net) VALUES (?, ?, ?, ?, ?)', 
                              (cnss, nom, mois, annee, salaire_net))
    def del_payslip(self):
        with self.conn:
            self.conn.execute(f" DELETE FROM fiches_de_paie ")

    def close(self):
        self.conn.close()