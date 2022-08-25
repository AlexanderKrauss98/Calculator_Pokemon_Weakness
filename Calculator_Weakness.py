#--------------------------------------------------------------------------------------------------------Pokemon library----------------------------
all_Types_Eng = {"Normal","Fighting","Flying","Poison","Ground","Rock","Bug",
                 "Ghost","Steel","Fire","Water","Grass","Electric",
                 "Psychic","Ice","Dragon","Dark","Fairy"} #check

Weakdic = {
        "Normal" : [],
        "Psychic":["Fighting", "Poison"],
        "Bug":["Psychic","Dark","Grass"],
        "Fighting":["Normal","Rock","Steel","Ice","Dark"],
        "Ice":["Flying","Ground","Grass","Dragon"],
        "Fairy":["Fighting","Dragon","Dark"],
        "Poison":["Grass","Fairy"],
        "Ghost":["Ghost","Psychic"],
        "Grass":["Ground","Rock","Water"],
        "Dark":["Ghost","Psychic"],
        "Rock":["Flying","Bug","Fire","Ice"],
        "Fire":["Bug","Steel","Grass","Ice"],
        "Flying":["Fighting","Bug","Grass"],
        "Dragon":["Dragon"],
        "Ground":["Poison", "Rock","Steel","Fire","Electric"],
        "Electric":["Flying","Water"],
        "Steel":["Rock","Ice","Fairy"],
        "Water":["Ground","Rock","Fire"],
        }
        
Resdic = {
        "Normal" : ["Rock","Steel"],
        "Psychic":["Psychic","Steel"],
        "Bug":["Fire","Fighting","Poison","Flying","Ghost","Steel"],
        "Fighting":["Poison","Flying","Psychic","Bug","Fairy","Ghost"],
        "Ice":["Fire","Water","Ice","Steel"],
        "Fairy":["Fire","Fighting","Steel"],
        "Poison":["Poison","Ground","Rock","Ghost","Steel"],
        "Ghost":["Normal","Steel"],
        "Grass":["Fire","Grass","Poison","Flying","Bug","Dragon"],
        "Dark":["Fighting","Dark","Fairy"],
        "Rock":["Fighting","Ground","Steel"],
        "Fire":["Fire","Water","Rock","Dragon"],
        "Flying":["Electric","Rock","Steel"],
        "Dragon":["Steel","Fairy"],
        "Ground":["Grass","Flying","Bug"],
        "Electric":["Grass","Electric","Ground","Dragon"],
        "Steel":["Fire","Water","Electric","Steel"],
        "Water":["Water","Grass","Dragon"],
        }
Nothdic = {
    "Normal":["Ghost"],
    "Psychic":["Dark"],
    "Bug":[],
    "Fighting":["Ghost"],
    "Ice":[],
    "Fairy":[],
    "Poison":["Steel"],
    "Ghost":["Normal"],
    "Grass":[],
    "Dark":[],
    "Rock":[],
    "Fire":[],
    "Flying":[],
    "Dragon":["Fairy"],
    "Ground":["Flying"],
    "Electric":["Ground"],
    "Steel":[],
    "Water":[],
    }
    
#---------------------------------------------------------------------------------------------------------------Type Calculator--------------------

#Type_Comp_Eng = ([[a,b,c] for a in all_Types_Eng for b in all_Types_Eng if b != a for c in all_Types_Eng if c != a and c != b]) 
Type_Comp_Eng = ([[a,b] for a in all_Types_Eng for b in all_Types_Eng if b != a ]) 
    
             
for comps in Type_Comp_Eng:
    if [comps[1],comps[0]] in Type_Comp_Eng:# remove dublicates #check 
        Type_Comp_Eng.remove(comps)  

for t in Type_Comp_Eng: #create Weakness, Resistent and Negates
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
