# JOB 1
def job1() :
    fruits = ['pomme', 'cerise', 'orange']
    return fruits

# JOB 2
def job2() :
    fruits = ['pomme', 'cerise', 'orange']
    return fruits[1]

# JOB 3
def job3() :
    fruits = ['pomme', 'cerise', 'orange']
    fruits = fruits + ['Melon']
    return fruits

# JOB 4
def job4() :
    fruits = ['pomme', 'cerise', 'orange', 'melon']
    fruits.insert(2, 'mangue')
    return fruits

# JOB 5
def job5() :
    L = [1,2,3,4,5]
    print(L)
    print(L[1])
    L[3] = L[2]+L[4]
    print(L)
    print(L[-1])

# JOB 6
def job6() :
    L = [1,2,3,4,5]
    print(L)
    first = L[0]
    last = L[-1]
    L[-1] = first
    L[0] = last

    return L

# JOB 7
def job7() :
    L = [8,24,48,2,16]
    total = 0
    for x in L :
        if (x%3 == 0) :
            total += 1
    return total

# JOB 8
def job8() :
    L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
    somme = 0
    for x in L :
        if (x%2==0) :
            somme += x
    
    return somme

# JOB 9
def job9() :
    L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
    min = L[0]
    max = L[0]
    for x in L :
        if (x>=max) :
            max = x
        if (x<=min) :
            min = x
    
    print("La valeur max est : " + str(max))
    print("La valeur min est : " + str(min))

# JOB 10
def job10() :
    L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
    produit = 1
    for x in L :
        if x>=25 and x<= 90 :
            produit = produit * x
    return produit

# JOB 11
def job11() :
    L = [7, 11, 42, 39, 2]
    for i in range(len(L)) :
        L[i] += 1
    return L
        
# JOB 12
def min(List) :
    min = List[0]
    for x in List :
        if (x<=min) :
            min = x
    return min

def trieur(L) :
    base = L
    Lsort = []
    while len(base)>0 :
        Lsort.append(min(base))
        base.remove(min(base))

    return Lsort
    
def job12() :
    L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
    print(trieur(L))

# JOB 13
def deleteDoubles(L) :
    res = L
    a = []
    for j in range(len(L)-1) :
        for x in range(len(L)-1) :
            if L[x]==a[j] :
                print("Supprimé")
            else :
                a.append(L[x])
    
    
        
    return a
                

def job13() :
    L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
    return deleteDoubles(L)



#############################################
print(job13())