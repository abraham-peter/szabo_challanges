from typing import Set,Dict,Optional,List
frecvente= {
    'E': 11.60002,
    'I': 10.22754,
    'A': 10.10637,
    'R': 6.577132,
    'N': 6.454273,
    'U': 6.020903,
    'T': 5.864385,
    'C': 5.589215,
    'S': 4.291629,
    'L': 4.243664,
    'Ă': 4.406072,
    'O': 3.897809,
    'D': 3.498098,
    'M': 3.437511,
    'Ș': 1.570231,
    'F': 1.331246,
    'Â': 1.311892,
    'Î': 1.311892,
    'B': 0.983709,
    'G': 0.870107,
    'Z': 0.657208,
    'Ț': 1.08553,
    'H': 0.386247,
    'J': 0.184288,
    'X': 0.111919,
    'K': 0.012622,
    'Q': 0.000841,
    'Y': 0.005049,
    'W': 0.007573,
    'P': 0.500000,
}
codat="*A**C****"
pattern=list(codat)
cuvant_de_ghicit='FAGOCITUL'
litere_folosite=set(x for i,x in enumerate(pattern)if x!='*' )
def alege_litera(pattern:List[str],litere_folosite:Set[str],frecvente:Dict[str,float])-> Optional[str]:
    for litera in sorted(frecvente,key=frecvente.get,reverse=True): 
        if litera not in litere_folosite:
            return litera
def verifica_litera(litera:str,cuvant_real:str,pattern:List[str])->Optional[bool]:
    for i,char in enumerate(cuvant_real):

    pass

if __name__=="__main__":
    print("\n=== Ordine sortată după frecvență ===")
    for litera in sorted(frecvente, key=frecvente.get, reverse=True): 
        print(f"{litera}: {frecvente[litera]}")
        #alege_litera(pattern,litere_folosite,frecvente)
        pass


