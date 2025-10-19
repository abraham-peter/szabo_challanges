"""
Hangman Solver - Versiune Finală
Structură: /src pentru cod, /data pentru input, /results pentru output
"""
import csv
import os
import sys
from typing import Set, Dict, Optional, List

# Frecvențe litere în limba română
FRECVENTE = {
    'E': 11.60002, 'I': 10.22754, 'A': 10.10637, 'R': 6.577132,
    'N': 6.454273, 'U': 6.020903, 'T': 5.864385, 'C': 5.589215,
    'S': 4.291629, 'L': 4.243664, 'O': 3.897809, 'D': 3.498098,
    'M': 3.437511, 'F': 1.331246, 'P': 2.500000, 'V': 1.800000,
    'B': 0.983709, 'G': 0.870107, 'Z': 0.657208, 'H': 0.386247,
    'J': 0.184288, 'X': 0.111919, 'K': 0.012622, 'Q': 0.000841,
    'Y': 0.005049, 'W': 0.007573, 'Ă': 4.406072, 'Â': 1.311892,
    'Î': 1.311892, 'Ș': 1.570231, 'Ț': 1.08553,
}

def alege_litera(pattern: List[str], litere_folosite: Set[str], frecvente: Dict[str, float]) -> Optional[str]:
    """Alege urmatoarea litera pe baza frecventei."""
    for litera in sorted(frecvente, key=frecvente.get, reverse=True):
        if litera not in litere_folosite:
            return litera
    return None

def verifica_litera(litera: str, cuvant_real: str, pattern: List[str]) -> bool:
    """Verifica daca litera este in cuvant si actualizeaza pattern-ul."""
    gasit = False
    for i, char in enumerate(cuvant_real):
        if char.upper() == litera.upper():
            pattern[i] = char.upper()
            gasit = True
    return gasit

def rezolva_joc(pattern_initial: str, cuvant_tinta: str, frecvente: Dict[str, float]) -> tuple:
    """Rezolva un joc de Hangman."""
    pattern = list(pattern_initial.upper())
    litere_folosite = set(x for x in pattern if x != '*')
    secventa = []
    nr_incercari = 0
    
    while '*' in pattern:
        litera = alege_litera(pattern, litere_folosite, frecvente)
        
        if litera is None:
            break
        
        litere_folosite.add(litera)
        secventa.append(litera)
        nr_incercari += 1
        
        verifica_litera(litera, cuvant_tinta.upper(), pattern)
    
    cuvant_gasit = ''.join(pattern)
    status = 'OK' if cuvant_gasit == cuvant_tinta.upper() else 'FAIL'
    
    return nr_incercari, cuvant_gasit, status, ' '.join(secventa)

def get_project_paths():
    """Determina caile proiectului relativ la fisierul curent."""
    # Calea catre root-ul proiectului (parent al directorului src)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    
    data_dir = os.path.join(project_root, 'data')
    results_dir = os.path.join(project_root, 'results')
    
    # Creează directorul results dacă nu există
    os.makedirs(results_dir, exist_ok=True)
    
    return data_dir, results_dir

def proceseaza_fisier(input_filename: str, output_filename: str):
    """Proceseaza fisierul cu toate jocurile."""
    data_dir, results_dir = get_project_paths()
    
    input_path = os.path.join(data_dir, input_filename)
    output_path = os.path.join(results_dir, output_filename)
    
    if not os.path.exists(input_path):
        print(f"EROARE: Fisierul {input_path} nu exista!")
        return
    
    rezultate = []
    total_incercari = 0
    
    print(f"Procesez: {input_path}")
    
    # Citeste fisierul txt si converteste
    with open(input_path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            
            parts = line.split(';')
            if len(parts) < 3:
                continue
                
            game_id = parts[0]
            pattern_initial = parts[1]
            cuvant_tinta = parts[2]
            
            # Validare
            if len(pattern_initial) != len(cuvant_tinta):
                continue
            
            # Rezolva
            nr_inc, cuv_gasit, status, secventa = rezolva_joc(
                pattern_initial, cuvant_tinta, FRECVENTE
            )
            
            rezultate.append({
                'game_id': game_id,
                'total_incercari': nr_inc,
                'cuvant_gasit': cuv_gasit,
                'status': status,
                'secventa_incercari': secventa
            })
            
            total_incercari += nr_inc
    
    # Scrie rezultate
    with open(output_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=[
            'game_id', 'total_incercari', 'cuvant_gasit', 'status', 'secventa_incercari'
        ])
        writer.writeheader()
        writer.writerows(rezultate)
    
    print(f"Rezultate salvate in: {output_path}")
    return total_incercari, len(rezultate)

def main():
    """Functia principala."""
    if len(sys.argv) < 3:
        print("Usage: python solve_hangman.py <input_file> <output_file>")
        print("Exemplu: python solve_hangman.py cuvinte_de_verificat.txt rezultate.csv")
        print("")
        print("Fisierul de input trebuie sa fie in /data")
        print("Rezultatele vor fi salvate in /results")
        return
    
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    
    result = proceseaza_fisier(input_filename, output_filename)
    
    if result is None:
        return
    
    total, nr_jocuri = result
    
    print("\n" + "="*50)
    print(f"REZULTATE FINALE:")
    print(f"Total incercari: {total}")
    print(f"Numar jocuri: {nr_jocuri}")
    print(f"Media incercari/joc: {total/nr_jocuri:.1f}")
    print(f"Cerinta (<1200): {'PASS' if total < 1200 else 'FAIL'}")
    print("="*50)

if __name__ == "__main__":
    main()