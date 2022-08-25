#-----------------------------------------------------------------------Import from Library -----------------------------
from PokemonLib import all_Types_Eng
from PokemonLib import Weakdic
from PokemonLib import Resdic
from PokemonLib import Nothdic

#-----------------------------------------------------------------------Calculator------------------------------------

Type_Comp_Eng = ([[a,b] for a in all_Types_Eng for b in all_Types_Eng if b != a ]) #create List of TypeComps
#for Carmesin/Purpur: Type_Comp_Eng = ([[a,b,c] for a in all_Types_Eng for b in all_Types_Eng if b != a for c in all_Types_Eng if c != a and c != b])    
             
for comps in Type_Comp_Eng:
    if [comps[1],comps[0]] in Type_Comp_Eng:# remove dublicates
        Type_Comp_Eng.remove(comps)  

for t in Type_Comp_Eng: #create Weakness, Resistenz and Negates
    weak = []
    res = []
    noth = []
    for def_type in t:
        for Atk in all_Types_Eng:
            if def_type in Weakdic[Atk]:
                weak.append(Atk)
            if def_type in Resdic[Atk]:
                res.append(Atk)
            if def_type in Nothdic[Atk]:
                noth.append(Atk)
                
    for i in weak: #clear negates
        if i in noth:
            weak.remove(i)
        if weak in res:
            weak.remove(i)
            res.remove(i)
            
        
    print ("Typ:" + str(t))
    print ("Weakness: " + str(weak))
    print ("Resistent: " + str(res))
    print ("Doesn't Effect: " + str(noth))
    print ("")
    
