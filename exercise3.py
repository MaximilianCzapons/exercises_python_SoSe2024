def steigung_funktion(meine_liste):
    
    x1 = meine_liste[0]
    y1 = meine_liste[1]
    x2 = meine_liste [2]
    y2 = meine_liste [3]
   
    x = x2 - x1
    y = y2 - y1
    
    
    if x==0:
        print("Die Steigung ist nicht definiert") 
    else: 
        steigung = y / x
        print(steigung)

steigung_funktion([8,4,8,4])


