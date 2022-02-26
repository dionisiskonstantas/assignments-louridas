import csv
import sre_yield
import string
import sys

def read_crossword(filename):
    c = {} #crosswords
    n = {} #neightbors
    e_mum = {}#οι μητρικές εκφράσεις που θα αντιστοιχούν στην κάθε λέξη
    with open(filename) as crossword_file:
        for line in crossword_file:
            parts = line.split(',')
            e_mum[int(parts[0])] = None
            c[int(parts[0])] = [None] * len(parts[1])
            for i in range(len(parts[1])):
                if parts[1][i] != ".":
                    c[int(parts[0])][i] =parts[1][i]
            n[int(parts[0])] = parts[2:len(parts)]
            n[int(parts[0])] = list(map(int, n[int(parts[0])]))
    return c,n,e_mum

#read and return the mother expressions
def read_words(filename):
    with open(filename) as words_file:
           words = words_file.read().split("\n")      
    return words

#make a dictionary with keys: the mother expressios
#and elements : the childs of every expression
def make_words(w = []):
    k = {}
    for i in range(len(w)):
        if(len(w[i]) > 0):
            b = list(sre_yield.AllStrings(w[i], max_count=5, charset=string.ascii_uppercase))
            k[w[i]] = b
    return k

def match(c,n,i,word):
    if(len(c[i]) == len(word))and (not(type(c[i]) == type("ooo"))) :
        f = 0
        for x in range(len(c[i])):
            if c[i][x] != None:
                if c[i][x] == word[x]:
                    f = f + 1
        z = {}
        num = 0
        for j in range(0,len(n[i]),2):
            other_c = n[i][j] #the other crossword 
            for k in range(0,len(n[other_c]),2):
                if(n[other_c][k] == i):
                    flag = n[other_c][k + 1] #the possision that are meeting up in the i
                    z[j]= flag
                    break
            if(c[other_c][n[i][j+1]] == None or c[other_c][n[i][j+1]] == word[flag]) and len(c[i]) - c[i].count(None) == f:
                num = num + 1 
        if (num == len(n[i])/2):
            c[i] = word
            for j in range(0,len(n[i]),2):
                if not(type(c[n[i][j]]) == type("ooo") ):
                    #βαζω στην κάθε λεξη που τέμνεται με αυτην 
                    #που ψάχνουμε τα γράμματα που πρεπει να τοποθετηθουν
                    c[n[i][j]][n[i][j+1]] = word[z[j]] 
            return True, c
        else:
            return False, c
    else:
        return False,c

def existance_none(listDict):
    tof = False
    for value in listDict:
        if  not(type(listDict[value]) == type("ooo")):
            if (None in listDict[value]):
                tof = True
                break
    return(tof)

def existance_none_in_expressions(listDict):
    tof = False
    for value in listDict:
        if (listDict[value] == None):
            tof = True
            break
    return(tof)

def deepcopy_dict(dict1):
    dict2={}
    dict2 = dict1.copy()
    for i in dict1:
	    if type(dict1[i]) != type("ooo"):
		    dict2[i]=dict1[i].copy()
    return dict2

def solve_crossword(cr, n, k, ex):

    if not(existance_none(cr)) and not(existance_none_in_expressions(ex)):
        return cr
    g= {}#will have as key the not full crossword and how much they are filled
    for x in cr:
        if  not(type(cr[x]) == type("ooo")):
            counter = cr[x].count(None)
            g[x] = counter/len(cr[x])
    sort_order = sorted(g.items(), key=lambda x: x[1])#taksinomisi
  
    for i in range(len(sort_order)):#kathe leksi poy exei mhnei me thn protaireothta poy balame
        current_crossword = sort_order[i][0]
        for keys in k: #for every mum expression
            for j in range(len(k[keys])): # for every child of the expression
                if not(k[keys][j] in cr.values()): #ckeck if the word is uniqe
                    matching, c_new = match(deepcopy_dict(cr), n, current_crossword, k[keys][j])
                    if not(existance_none(c_new)) and not(existance_none_in_expressions(ex)):
                        return c_new
                    else:
                        if matching:
                            ex[current_crossword] = keys #keep the mother expresions
                            new_k = deepcopy_dict(k)
                            new_k.pop(keys) #poping the mother expression witch child is  
                            # put in the current_crossword
                            find = solve_crossword(deepcopy_dict(c_new), n, deepcopy_dict(new_k), ex) 
                            if not(existance_none(find)) and not(existance_none_in_expressions(ex)):
                                return find
        break # if none of our expressions has a child that fit in the current_crossword we make a step back
        #because ther is no need to continue                       
    return cr                    

#main program          
cr, ne, expressions_mum= read_crossword(sys.argv[1])
words = read_words(sys.argv[2])
words_choises = make_words(words)
a = solve_crossword(cr, ne, words_choises, expressions_mum)
for i in range(len(cr)):
    print(i,expressions_mum[i],a[i], end=" ")

