def derniereLampe(n) :
    '''
    Pour un nombre n de lampes, retourne l'insant t à partir duquel la n ième 
    lampe s'allume pour la premiere fois suivi du nombre de lampes allumées 
    à l'instant t
    '''
    t=0
    allumees = 1
    L = [0 for x in range(n)] #genere une liste representant les lampes : 0 pour eteinte, 1 pour allumee
    L[0] = 1 #a t=0, seul la 1e lampe est allumee
#    print(L)
    while L[n-1] == 0 : #derniere lampe
        for i in range(n-1,0,-1) : #rien ne sert de verifier la premiere lampe (toujours allumée)
            #il faut parcourir la liste à l'envers afin d'eviter de compter les affectations precedentes
            if L[i-1] == 1: 
                if L[i] == 1 :
                    L[i] = 0
                    allumees += -1
                else :
                    L[i] = 1
                    allumees += 1
#        if t>=n-5:
#        print(L)
        t += 1
    print(L)
    return t,allumees


