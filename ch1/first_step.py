"""
Hangman Solver - Greedy Strategy
Student: [Numele tău]
"""
import csv
from typing import Set, Dict, Optional, List

# Frecvențe litere în limba română
FRECVENTE = {
    'E': 11.60002, 'I': 10.22754, 'A': 10.10637, 'R': 6.577132,
    'N': 6.454273, 'U': 6.020903, 'T': 5.864385, 'C': 5.589215,
    'S': 4.291629, 'L': 4.243664, 'Ă': 4.406072, 'O': 3.897809,
    'D': 3.498098, 'M': 3.437511, 'Ș': 1.570231, 'F': 1.331246,
    'Â': 1.311892, 'Î': 1.311892, 'B': 0.983709, 'G': 0.870107,
    'Z': 0.657208, 'Ț': 1.08553, 'H': 0.386247, 'J': 0.184288,
    'X': 0.111919, 'K': 0.012622, 'Q': 0.000841, 'Y': 0.005049,
    'W': 0.007573, 'P': 2.500000, 'V': 1.800000,
}


def alege_litera(pattern: List[str], litere_folosite: Set[str], frecvente: Dict[str, float]) -> Optional[str]:
    """Alege următoarea literă pe baza frecvenței (strategie greedy)."""
    for litera in sorted(frecvente, key=frecvente.get, reverse=True):
        if litera not in litere_folosite:
            return litera
    return None


def verifica_litera(litera: str, cuvant_real: str, pattern: List[str]) -> bool:
    """Verifică dacă litera este în cuvânt și actualizează pattern-ul."""
    gasit = False
    for i, char in enumerate(cuvant_real):
        if char.upper() == litera.upper():
            pattern[i] = char.upper()
            gasit = True
    return gasit


def rezolva_joc(pattern_initial: str, cuvant_tinta: str, frecvente: Dict[str, float]) -> tuple:
    """
    Rezolvă un joc de Hangman.
    
    Returns:
        (nr_incercari, cuvant_gasit, status, secventa)
    """
    # Inițializare
    pattern = list(pattern_initial.upper())
    litere_folosite = set(x for x in pattern if x != '*')
    secventa = []
    nr_incercari = 0
    
    # Loop principal
    while '*' in pattern:
        # OPTIMIZARE: Dacă avem >= 70% din cuvânt, ghicim direct ultimele litere
        necunoscute = pattern.count('*')
        total = len(pattern)
        
        if necunoscute <= 3 and necunoscute < total * 0.3:
            # Încercăm literele rămase mai rapid
            # Prioritizăm vocalele rămase, apoi consoanele frecvente
            vocale_ramase = [l for l in 'AEIOUĂÂÎ' if l not in litere_folosite]
            consoane_frecvente = [l for l in 'RNTCSLMDȘFPBGZȚH' if l not in litere_folosite]
            
            candidati = vocale_ramase + consoane_frecvente
            
            for litera in candidati:
                if litera not in litere_folosite:
                    litere_folosite.add(litera)
                    secventa.append(litera)
                    nr_incercari += 1
                    
                    if verifica_litera(litera, cuvant_tinta.upper(), pattern):
                        if '*' not in pattern:
                            break
        else:
            # Strategie greedy normală
            litera = alege_litera(pattern, litere_folosite, frecvente)
            
            if litera is None:
                # Nu mai avem litere de încercat
                break
            
            litere_folosite.add(litera)
            secventa.append(litera)
            nr_incercari += 1
            
            # Verifică litera (simulare răspuns arbitru)
            verifica_litera(litera, cuvant_tinta.upper(), pattern)
    
    cuvant_gasit = ''.join(pattern)
    status = 'OK' if cuvant_gasit == cuvant_tinta.upper() else 'FAIL'
    
    return nr_incercari, cuvant_gasit, status, ' '.join(secventa)


def proceseaza_fisier(input_path: str, output_path: str):
    """Proceseaza fisierul CSV cu toate jocurile."""
    rezultate = []
    total_incercari = 0
    
    # Citeste CSV
    with open(input_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        
        for row in reader:
            if len(row) < 3:
                continue
            
            game_id = row[0].strip()
            pattern_initial = row[1].strip()
            cuvant_tinta = row[2].strip()
            
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
    
    print(f"\nTOTAL INCERCARI: {total_incercari}")
    print(f"Rezultate salvate in: {output_path}")
    
    return total_incercari


if __name__ == "__main__":
    import sys
    
    # Test rapid
    if len(sys.argv) < 3:
        print("Usage: python first_step.py <input.csv> <output.csv>")
        print("\n🧪 Test rapid:")
        pattern = "*A**C****"
        cuvant = "FAGOCITUL"
        nr, gasit, status, seq = rezolva_joc(pattern, cuvant, FRECVENTE)
        print(f"Pattern: {pattern} → {gasit}")
        print(f"Încercări: {nr}")
        print(f"Secvență: {seq}")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        proceseaza_fisier(input_file, output_file)