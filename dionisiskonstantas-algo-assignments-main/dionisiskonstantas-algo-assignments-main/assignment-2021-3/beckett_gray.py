import sys


def Flip(m_x,m_i):
    s = list(m_x)
    if s[m_i]=="1":
        s[m_i] = '0'
    elif s[m_i] == '0':
        s[m_i] = "1"
    string1=""
    for i in s:
        string1=string1+i
    m_x = string1
    return m_x

def make_x(n):
    first_bits = ""
    for i in range(n):
        first_bits = first_bits + "0"
    return first_bits

def all_bits(n,j,y):
    if n == j:
        return y
    else:
        k = 0
        z = ["-1"] * (pow(2,j+1))
        for i in range(len(y)):
            z[k] = '0' + y[i]
            k = k + 1
        for i in range(len(y)-1,-1,-1):
            z[k] = '1' + y[i]
            k = k + 1
        j = j+1
        the_bits = all_bits(n,j,z).copy()
    return the_bits


def make_visited(a):
    vis = {}
    for i in range(len(a)):
        vis[a[i]] = False
    return vis
   

def isIsomorphic(str1, str2):          
    dict_str1 = {}
    dict_str2 = {}
    for i, value in enumerate(str1):
        dict_str1[value] = dict_str1.get(value, []) + [i]    
            
    for j, value in enumerate(str2):
        dict_str2[value] = dict_str2.get(value, []) + [j]
    if sorted(dict_str1.values()) == sorted(dict_str2.values()):
        return True
    else:
        return False
    

def reverse_string(string):
	if len(string) == 0:
		return string
	else:
		return reverse_string(string[1:]) + string[0]


def reversed_isIsomorphic(str1, str2):
    reverse_str1 = reverse_string(str1)
    return isIsomorphic(reverse_str1,str2)


def fun_a(n,w1,w2,argument2):
    lis = []
    for i in range(len(w1)):
        if len(w1[i]) == pow(2,n):
            x = "C"
            print("C",w1[i])
            if argument2 == "-m":
                fun_m(n,i,w2)
            if argument2 == "-f":
                fun_f(n,i,w2,x)
            lis.append(w1[i])
        else:
            x = "P"
            print("P",w1[i])
            if argument2 == "-m":
                fun_m(n,i,w2)
            if argument2 == "-f":
                fun_f(n,i,w2,x)
            lis.append(w1[i])
    return lis
def fun_c(n,w1,w2,argument2):
    x = "C"
    lis = []
    for i in range(len(w1)):
        if len(w1[i]) == pow(2,n):
            print("C",w1[i])
            if argument2 == "-m":
                fun_m(n,i,w2)
            if argument2 == "-f":
                fun_f(n,i,w2,x)
            lis.append(w1[i])
    return lis

def fun_p(n,w1,w2,argument2):
    x = "P"
    lis = []
    for i in range(len(w1)):
        if len(w1[i]) != pow(2,n):
            print("P",w1[i])
            if argument2 == "-m":
                fun_m(n,i,w2)
            if argument2 == "-f":
                fun_f(n,i,w2,x)
            lis.append(w1[i])
    return lis

def fun_b(n,w1,w2,argument2):
    lis = []
    count = 0 
    for i in range(len(w1)):
        if len(w1[i]) == pow(2,n):
            x = "B"
            count+=1
            print("B",w1[i])
            if argument2 == "-m":
                fun_m(n,i,w2)  
            if argument2 == "-f":
                fun_f(n,i,w2,x)
            lis.append(w1[i])
    if count == 0:
        for i in range(len(w1)):
            if len(w1[i]) != pow(2,n):
                x = "U"
                print("U",w1[i])
                if argument2 == "-m":
                    fun_m(n,i,w2)
                if argument2 == "-f":
                    fun_f(n,i,w2,x)
                lis.append(w1[i])
    return lis            
def fun_u(n,w1,w2,argument2): 
    x = "U"             
    lis = []
    for i in range(0,len(w1)):
        if len(w1[i]) != pow(2,n):
            print("U",w1[i])
            if argument2 == "-m":
                fun_m(n,i,w2)
            if argument2 == "-f":
                fun_f(n,i,w2,x) 
            lis.append(w1[i])
    return lis

def fun_r(w):
    for i in range(len(w)-1):
        for j in range(i+1,len(w)):
            if reversed_isIsomorphic(w[i], w[j]):
                print(w[i],"<=>",w[j])

def fun_m(n,ii,w2):
    for k in range(n):
        for j in range(len(w2[ii])):
            print(w2[ii][j][k], end = " ")
        print("")

def fun_f(n,ii,w2,letter):
    print(letter,end = " ")
    for j in range(len(w2[ii])):
            print(reverse_string(w2[ii][j]), end = " ")
    print("")  


def GC_DFS(d, x, max_coord, n, gc,delta):
    if d == pow(2,n) -1:
        all_codes.append(gc.copy())
        count = 0
        flag = -1
        for i in range(len(gc[len(gc)-1])):
            if gc[len(gc)-1][i] == "1":
                count = count + 1
                if count == 1:
                    flag = str(i)
        if count == 1:
            delta = delta + flag
        all_delta.append(delta)
        return 

    for i in range(0, min(n,max_coord +1)):
        x = Flip(x,i)
        if not visited[x]:
            visited[x] = True
            gc.append(x)
            delta = delta + str(i)
            GC_DFS(d+1, x, max(i+1,max_coord), n, gc,delta)
            visited[x]= False
            gc.pop()
            l = len(delta)
            delta = delta[:l-1]
        x = Flip(x,i)
    return all_codes,all_delta


def BE_GC_DFS(d, x, max_coord, n, gc,delta,Q):
    if d == pow(2,n) -1:
        all_codes.append(gc.copy())
        count = 0
        flag = -1
        for i in range(len(gc[len(gc)-1])):
            if gc[len(gc)-1][i] == "1":
                count = count + 1
                if count == 1:
                    flag = str(i)
        if count == 1:
            delta = delta + flag
        all_delta.append(delta)
        return 

    for i in range(0, min(n,max_coord +1)):        
        x = Flip(x,i)
        if not visited[x] :
            if x[i] == '0':
                if Q[0] == i:
                    Q.pop(0)
                    visited[x] = True
                    gc.append(x)
                    delta = delta + str(i)
                    BE_GC_DFS(d+1, x, max(i+1,max_coord), n, gc,delta,Q)
                    Q.insert(0,i)            
                    visited[x]= False
                    gc.pop()
                    l = len(delta)
                    delta = delta[:l-1]
            else:
                if not i in Q:
                    Q.append(i)
                visited[x] = True
                gc.append(x)
                delta = delta + str(i)
                BE_GC_DFS(d+1, x, max(i+1,max_coord), n, gc,delta,Q)
                visited[x]= False
                if len(Q) != 0:
                    Q.pop(len(Q)-1)
                gc.pop()
                l = len(delta)
                delta = delta[:l-1]
       
        x = Flip(x,i)

    return all_codes,all_delta

#------main--------------------

#passing arguments

correct_inputs = True
if len(sys.argv) == 2:
    arg1 = "null"
    arg2 = "null"
    try:
        n = int(sys.argv[1])
    except:
        correct_inputs = False
elif len(sys.argv) == 3:
    if sys.argv[1] == "-r" or sys.argv[1] == "-m" or sys.argv[1] == "-f":
        arg2 = sys.argv[1]
        arg1 = "null"
        try:
            n = int(sys.argv[2])
        except:
            correct_inputs = False

    elif sys.argv[2] == "-r" or sys.argv[2] == "-m" or sys.argv[2] == "-f":
        arg2 = sys.argv[2]
        try:
            n = int(sys.argv[1])
            arg1 = "null"
        except:
            correct_inputs = False 

    else:
        arg1 = sys.argv[1]
        arg2 = "null"
        try:
            n = int(sys.argv[2])
        except:
            correct_inputs = False 
elif len(sys.argv) == 4:
    arg1 = sys.argv[1]
    if sys.argv[2] == "-r" or sys.argv[2] == "-m" or sys.argv[2] == "-f":
        arg2 = sys.argv[2]
        try:
            n = int(sys.argv[3])
        except:
            correct_inputs = False
    
    elif  sys.argv[3] == "-r" or sys.argv[3] == "-m" or sys.argv[3] == "-f":
        arg2 = sys.argv[3]
        try:
            n = int(sys.argv[2])
        except:
            correct_inputs = False
    else:
        correct_inputs = False

else:
    correct_inputs = False


if correct_inputs:
    if arg1 != "-a" and arg1 != "-b" and arg1 != "-u" and arg1 != "-c" and arg1 != "-p" and arg1 != "null":
        correct_inputs = False
    if arg2 != "-r" and arg2 != "-m" and arg2 != "-f" and arg2 != "null":
        correct_inputs = False





if correct_inputs:
    #initializations

    Q= []  #for a queue
    Q.append(0)
    all_codes = []
    delta=""
    all_delta = []
    j = 1
    the_bits = []
    y = ['0','1']
    visited = make_visited(all_bits(n,j,y))
    gc = []
    lista = []
    x = make_x(n)
    visited[x]= True
    gc.append(x)

    #make_results
    if arg1 == "-a" or arg1 == "null":
        GC_DFS(0,x,0 ,n, gc,delta)
        lista_delta = fun_a(n,all_delta,all_codes,arg2)
    if arg1 == "-b":
        BE_GC_DFS(0,x,0 ,n, gc,delta,Q)
        lista_delta = fun_b(n,all_delta,all_codes,arg2)
    if arg1 == "-u":
        BE_GC_DFS(0,x,0 ,n, gc,delta,Q)
        lista_delta = fun_u(n,all_delta,all_codes,arg2)
    if arg1 == "-c":
        GC_DFS(0,x,0 ,n, gc,delta)
        lista_delta = fun_c(n,all_delta,all_codes,arg2)
    if arg1 == "-p":
        GC_DFS(0,x,0 ,n, gc,delta)
        lista_delta = fun_p(n,all_delta,all_codes,arg2)
    if arg2 == "-r":
        fun_r(lista_delta)
else:
    print("Incorrect inputs")