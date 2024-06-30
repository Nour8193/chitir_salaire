#salary_calculator.py : Logique de calcul des salaires

def calculate_salary(salaire_base, primes=0, retenues=0):
    salaire_net = salaire_base + primes - retenues
    return salaire_net