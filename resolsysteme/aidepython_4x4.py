ListeA = [11,12,13,14,21,22,23,24,31,32,33,34,41,42,43,44]
ListeB = ["MatA","MatB","MatC","MatD","MatE","MatF","MatG","MatH","MatI","MatJ","MatK","MatL","MatM","MatN","MatO","MatP"]

def gen_coeff_inv(liste) :
    res = ""
    res += str(ListeB[ListeA.index(liste[0])])
    res += "*" + str(ListeB[ListeA.index(liste[1])])
    res += "*" + str(ListeB[ListeA.index(liste[2])])
    res += "+"
    res += str(ListeB[ListeA.index(liste[3])])
    res += "*" + str(ListeB[ListeA.index(liste[4])])
    res += "*" + str(ListeB[ListeA.index(liste[5])])
    res += "+"
    res += str(ListeB[ListeA.index(liste[6])])
    res += "*" + str(ListeB[ListeA.index(liste[7])])
    res += "*" + str(ListeB[ListeA.index(liste[8])])
    res += "-"
    res += str(ListeB[ListeA.index(liste[9])])
    res += "*" + str(ListeB[ListeA.index(liste[10])])
    res += "*" + str(ListeB[ListeA.index(liste[11])])
    res += "-"
    res += str(ListeB[ListeA.index(liste[12])])
    res += "*" + str(ListeB[ListeA.index(liste[13])])
    res += "*" + str(ListeB[ListeA.index(liste[14])])
    res += "-"
    res += str(ListeB[ListeA.index(liste[15])])
    res += "*" + str(ListeB[ListeA.index(liste[16])])
    res += "*" + str(ListeB[ListeA.index(liste[17])])
    return res