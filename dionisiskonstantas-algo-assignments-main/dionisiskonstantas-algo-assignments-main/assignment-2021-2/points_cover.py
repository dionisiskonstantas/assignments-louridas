import itertools
import sys

def read_filename(filename):
    po = {} #points [x,y]
    i = -1 
    with open(filename) as points_file:
        for line in points_file:
            i = i + 1
            parts = line.split(' ')
            po[i] = [int(parts[0]), int(parts[1])]
    min_val = 10000000000
    min_posision = -1
    for i in range(len(po)):
        min_val = po[i][0]
        min_posision = i
        for j in range(i+1,len(po)):
            if po[j][0] < min_val:
                min_val = po[j][0]
                min_posision = j
        temp = po[i]
        po[i] = po[min_posision]
        po[min_posision] = temp
    return po

#making the possible lines
def make_S(points,ar2):
    #ftiaxnoyme oles tis pithanes dyades shmeion
    #kai meta tha tis syblirosoyme peretero
    c = make_allfirst_combinations(points)
    s = [None] * len(c)
    if ar2 == "-g": #making orizodies kai kathetes grammes
        k = -1
        for i in  range(len(c)):
            x1 = points[c[i][0]][0]
            y1 = points[c[i][0]][1]
            x2 = points[c[i][1]][0]
            y2 = points[c[i][1]][1]
            if x1 == x2 or y1 ==y2:
                k = k+1
                s[k]= [c[i][0], c[i][1]] 
                for key in points:
                    if (key != c[i][0]  and key !=c[i][1]):
                        x3 = points[key][0]
                        y3 = points[key][1]   
                        if (x1 == x2 and x2 == x3)or (y1==y2 and y2==y3):
                            s[k].append(key)    
                s[k].sort(reverse= False)
                for j in range(k):
                    if  s[k] == s[j]:
                        del s[k]
                        k = k -1
                        break
        res = list(filter(None, s))
        s = res
        z=[]
        #if (x,y) is alone
        #make a line with (x,y) , (x+1,y)
        for item in s:
            for j in range(len(item)):
                z.append(item[j])
        for i in points:
            if i in z:
                pass
            else:
                s.append([i])

        #for i in s
    else:#making all lines
        k = -1
        for i in  range(len(c)):
            k = k + 1
            s[k]= [c[i][0], c[i][1]]
    
            x1 = points[c[i][0]][0]
            y1 = points[c[i][0]][1]
            x2 = points[c[i][1]][0]
            y2 = points[c[i][1]][1]
            if x2-x1 != 0:
                #grammiki eksisosh y = a*x +b
                a = (y2 - y1)/(x2-x1)
                b = (x2 * y1 - x1*y2)/(x2-x1)
            for key in points:
                if (key != c[i][0]  and key !=c[i][1]):
                    x3 = points[key][0]
                    y3 = points[key][1]
                    if x2-x1 != 0:
                        if y3 ==a * x3 + b:
                            s[k].append(key)
                    elif x2-x1 == 0:
                        if x3 == x2:
                            s[k].append(key)
            s[k].sort(reverse= False)
            for j in range(k):
                if  s[k] == s[j]:
                    del s[k]
                    k = k -1
                    break
    return s #epistrefei mia alhlouxia shmeion poy theoroyde os mia gramh

#making all the diferent combinations beetwin tow points 
def make_allfirst_combinations(e):
    lis = []
    for i in e:
        lis.append(i)
    comb = list(itertools.combinations(lis,2))
    return comb

def covering(s,points,ar1):
    sol = {}#solusion
    a = []#to synolo U
    for i in points:
            a.append(i) 
    a.sort(reverse = False)
    if ar1 == "-f":
        r = {}
        m = -1
        for i in range(1,len(points)):
            g = list(itertools.combinations(s,i))
            for val in g:
                z2= []
                for item in val:
                    for j in range(len(item)):
                        z2.append(item[j])
                if len(z2) == len(a) and len(set(z2.copy())) == len(z2):
                    m = m + 1
                    r[m] = val  
        min_value = 10000000000
        for val in r:
            b = []
            for item in r[val] :
                for i in range(len(item)):
                    b.append(item[i])
            b.sort(reverse = False)
            if b == a and len(r[val])< min_value:
                min_value = len(r[val])
                sol = r[val]
     
    else:
        visited = [False] * len(points)
        b = []#ena yposynolo toy S
        k = -1
        prev = None
        while b != a:
            max_value = None
            for val in s:
                check = True
                for i in range(len(val)):
                    if visited[val[i]] == True:
                        check = False

               
                #evala >= gia na piasei thn teleytaia timh oste na vgazei akrivos 
                # ta idia apotelesmata me toy paradeigmatos
                if ((max_value is None or len(val) > max_value)and check == True):
                    max_value = len(val)
                    max_sequence = val.copy()


            

            k = k + 1
            sol[k] = max_sequence.copy()
            if sol[k]== prev:
                del sol[k]
                break
            prev = sol[k].copy()
            for i in range(len(max_sequence)):
                visited[max_sequence[i]] = True
                b.append(max_sequence[i])
            b.sort(reverse=False)
            
        #to fill the alone points
        if a != b:
            while a != b:
                max_non_visited = None
                for val in s:
                    j = 0
                    for i in range(len(val)):
                        if visited[val[i]] == False:
                            j = j+1

                    if (max_non_visited is None or j > max_non_visited):
                        max_non_visited = j
                        max_sequence = val.copy()
            
                k = k + 1
                sol[k] = max_sequence.copy()
                for i in range(len(max_sequence)):
                    if visited[max_sequence[i]] == False:
                        visited[max_sequence[i]] = True
                        b.append(max_sequence[i])
                b.sort(reverse=False)
    #convert tuple solusion to dictionary
    if type(sol) == tuple:
        m = -1
        dic = {}
        for val in sol:
            m = m + 1
            dic[m] = val
        sol = dic.copy()               
    return sol


#main programm
#checking if the parammetres are correct
f = None
if len(sys.argv) == 2 and (sys.argv[1]!= "-f" and sys.argv[1]!= "-g") :
    a = None
    b = None 
    f = sys.argv[1] 
if len(sys.argv)== 3 and (sys.argv[2]!= "-f" and sys.argv[2]!= "-g"):
    if sys.argv[1] == "-g":
        a = None
        b = "-g"
        f = sys.argv[2]  
    if sys.argv[1] == "-f":
        a = "-f"
        b = None
        f = sys.argv[2]
if len(sys.argv) == 4:
    a = "-f"
    b = "-g"
    f = sys.argv[3]

if f != None:
    points_matrix = read_filename(f)
    sum_s = make_S(points_matrix,b)
    solusion = covering(sum_s,points_matrix,a)
    #making the solusion in a correct order
    visited = {}
    for i in solusion:
        visited[i] = False
    for i in solusion:
        visited[i] = True
        maxmin_len = len(solusion[i])
        maxmin_val = solusion[i]
        maxmin_posision = i
        for j in solusion:
            if len(solusion[j]) > maxmin_len and visited[j] == False:
                maxmin_len = len(solusion[j])
                maxmin_val = solusion[j]
                maxmin_posision = j
            elif len(solusion[j]) == maxmin_len and visited[j]==False:
                for k in range(len(solusion[j])):
                    if solusion[j][k] < maxmin_val[k]:
                        maxmin_val = solusion[j]
                        break
        temp = solusion[i].copy()
        solusion[i] = maxmin_val.copy()
        solusion[maxmin_posision] = temp.copy()
    for i in solusion:   
        for j in range(len(solusion[i])):
            if len(solusion[i])==1:
                #printig to make exactly the same result
                print("(",end = "")
                print(points_matrix[solusion[i][j]][0],end = "")
                print(",",end = " ")
                print(points_matrix[solusion[i][j]][1],end = "")
                print(")", end =" ")
                print("(",end = "")
                print(points_matrix[solusion[i][j]][0] + 1,end = "")
                print(",",end = " ")
                print(points_matrix[solusion[i][j]][1],end = "")
                print(")", end =" ")
            else:
                #printig to make exactly the same result
                print("(",end = "")
                print(points_matrix[solusion[i][j]][0],end = "")
                print(",",end = " ")
                print(points_matrix[solusion[i][j]][1],end = "")
                if j < len(solusion[i])- 1:
                    print(")", end = " ")
                else:
                    print(")", end = "")
        print("")
else:
    print("incorect inputs")