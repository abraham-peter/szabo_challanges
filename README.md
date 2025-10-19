# Hangman Solver - Proiect Algoritmică

**Student**: [Numele tău]  
**Data**: Octombrie 2025

## 📋 Descriere

Aplicație Python care rezolvă automat jocuri de tip Hangman folosind o strategie greedy bazată pe frecvența literelor în limba română.

## 🚀 Instalare și Rulare

### Cerințe
- Python 3.8+
- Toate dependențele sunt din biblioteca standard Python

### Instalare
```bash
# Clonează repository-ul
git clone [URL_REPOSITORY]
cd szabo_challanges

# Nu sunt necesare dependențe externe
# Toate bibliotecile folosite sunt din Python standard library
```

### Rulare
```bash
# Navighează în directorul src
cd src

# Rulează programul
python solve_hangman.py <input_file> <output_file>

# Exemplu
python solve_hangman.py cuvinte_de_verificat.txt rezultate.csv
```

### Verificare dependențe (opțional)
```bash
# Verifică versiunea Python
python --version

# Verifică că toate modulele sunt disponibile
python -c "import csv, os, sys, typing; print('OK: All modules available')"
```

**Exemplu**:
```bash
python first_step.py test_input.csv rezultate.csv
```

## 📁 Structură Repository

```
szabo_challanges/
├── src/                           # Codul sursă
│   └── solve_hangman.py          # Script principal
├── data/                         # Fișiere de intrare
│   └── cuvinte_de_verificat.txt  # Dataset de test
├── results/                      # Rezultate generate
│   └── rezultate_final.csv       # Output exemple
├── docs/                         # Documentație
├── requirements.txt              # Dependențe (doar Python standard)
└── README.md                     # Acest fișier
```

## 📊 Format Date

### Input (CSV)
```csv
game_id,pattern_initial,cuvant_tinta
1,st****t,student
2,*a***ă,cărare
```

### Output (CSV)
```csv
game_id,total_incercari,cuvant_gasit,status,secventa_incercari
1,11,STUDENT,OK,E I R N U D T S L O A
2,14,CĂRARE,OK,E I A R N U C Ă T S L O D M
```

## 🧠 Strategie Implementată

**Algoritm**: Greedy pe baza frecvenței

1. Sortează literele după frecvența în limba română
2. La fiecare pas, alege cea mai frecventă literă neîncercată
3. Verifică litera și actualizează pattern-ul
4. Repetă până când cuvântul este complet

**Frecvențe folosite** (top 10):
- E: 11.6%
- I: 10.2%
- A: 10.1%
- R: 6.6%
- N: 6.5%
- U: 6.0%
- T: 5.9%
- C: 5.6%
- S: 4.3%
- L: 4.2%

## 📈 Performanță

- **Cerință**: < 1200 încercări totale pe fișierul de test
- **Rezultat**: [COMPLETEAZĂ DUPĂ RULARE]
- **Medie**: ~[X] încercări/joc
- **Rată succes**: [Y]%

## 🔧 Funcții Principale

### `alege_litera(pattern, litere_folosite, frecvente)`
Selectează următoarea literă folosind strategia greedy.

### `verifica_litera(litera, cuvant_real, pattern)`
Verifică dacă litera există în cuvânt și actualizează pattern-ul.

### `rezolva_joc(pattern_initial, cuvant_tinta, frecvente)`
Orchestrează rezolvarea unui singur joc.

### `proceseaza_fisier(input_path, output_path)`
Procesează fișierul CSV complet.

## ⚠️ Limitări

- Strategie greedy simplă fără optimizări avansate
- Nu folosește dicționar de cuvinte românești
- Nu detectează pattern-uri comune (sufixe, prefixe)
- Case-insensitive, dar suportă diacritice

## 🚀 Îmbunătățiri Posibile

1. **Dicționar**: Filtrare cuvinte pe baza pattern-ului
2. **Pattern matching**: Detecție sufixe (-UL, -ARE, -EȘTE)
3. **Probabilități**: Bayesian pentru alegere literă
4. **Optimizare**: Ghicire directă cuvânt când e evident

## 📚 Referințe

- Frecvența literelor: Wikipedia - Cifrul Cezar
- Dataset: [cuvinte_de_verificat.txt]


