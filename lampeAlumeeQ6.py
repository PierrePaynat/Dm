def lampeAllumees(n) :
    '''
    retourne le nombre de lampes allumées au temps t = n-1
    '''
    S=0
    base = bin(n-1)
    a = len(base)
    for i in range(2,a) :  #le  debut 2 permier de retirer le 0b présent au debut de l'ecriture binaire de n-1
        S += int(base[i])  #on convertit le string du bit en integer
    return 2**S
