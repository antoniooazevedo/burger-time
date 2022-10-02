def digits_average(n):
    import math
    
    while len(str(n)) != 1:
        control = 0
        n_str = ""
        for digit in str(n):
            if control == 0:
                d1 = int(digit)
                control += 1
                continue
            else:
                d2 = int(digit)
                n_str += str(math.ceil((d1+d2) / 2))
                d1 = int(digit)

        n = int(n_str)

    return n



def budgeting(budget, products, wishlist):
    to_buy = []
    
    for prod, price in products.items():
        for item, amt in wishlist.items():
            
            if prod == item:
                to_buy.append((item, price, amt))
    
    def myfunc(e):
        return e[1]
    
    to_buy.sort(key=myfunc)
    
    def check_budget(budget, l):
        price = 0
        for el in l:
            price += el[1] * el[2]
            
        return budget - price

    control = False


    for i in range(len(to_buy)):
        tb = to_buy.copy()
        if i == 0:
            while check_budget(budget, tb) < 0:
                if tb[i][2] < 0:
                    break
                tb[i] = (tb[i][0], tb[i][1], tb[i][2] - 1)
                t1 = tb.copy()
                
                control = True
            continue
        else:
            while check_budget(budget, tb) < 0:
                if tb[i][2] < 0:
                    break
                tb[i] = (tb[i][0], tb[i][1], tb[i][2] - 1)
                t2 = tb.copy()
                
        if control == False:
            break
        elif check_budget(budget, t1) < 0 or check_budget(budget, t2) < 0:
            continue
                
        lmao = [(check_budget(budget, t1), t1),(check_budget(budget, t2), t2)]
        lmao.sort()
        
        t1 = lmao[0][1]
        
    final_dict = {}
    
    if control == False:
        t1 = to_buy
    
    for el in t1:
        if el[2] != 0:
            final_dict[el[0]] = el[2]
        
    return final_dict
        
            

def gdc_rec(n1, n2):
    if n1 % n2 != 0:
        result = gdc_rec(n2, n1 % n2)
    else:
        result = n2
        
    return result
    
    
def juggler(n,p):
    if p == 0:
        return n
    else:
        if juggler(n, p-1) % 2 == 0:
            return int(juggler(n, p-1) ** (1/2))
        else:
            return int(juggler(n, p-1) ** (3/2))
        
        
def sum_digits_rec(n):
    if len(str(n)) == 1:
        return n
    else:
        return int(str(n)[0]) + sum_digits_rec(int(str(n)[1:]))
    
def biggest_member(atuple):
    for el in atuple:
        if type(el) == tuple:
            if len(atuple) >= len(biggest_member(el)):
                return atuple
            else:
                return biggest_member(el)
        
    return atuple

def find_treasure(pos, steps):
    if len(steps) == 0:
        return pos
    else:
        if steps[0] == "up":
            l = list(pos)
            l[1] += 1
            pos = tuple(l)
            return find_treasure(pos, steps[1:])
        if steps[0] == "down":
            l = list(pos)
            l[1] -= 1
            pos = tuple(l)
            return find_treasure(pos, steps[1:])
        if steps[0] == "right":
            l = list(pos)
            l[0] += 1
            pos = tuple(l)
            return find_treasure(pos, steps[1:])
        if steps[0] == "left":
            l = list(pos)
            l[0] -= 1
            pos = tuple(l)
            return find_treasure(pos, steps[1:])
            
    return pos
            
    

def last_man_standing(alist, step):
    if len(alist) == 1:
        return alist[0]
    
    else:
        alist.pop(step - 1 % len(alist))
        step += len(alist)
        step = step % 7
        return last_man_standing(alist, step)
    
    
def to_celsius(t):
    
    return map(lambda x: round((x + 32) / 1.8, 1), t)
    
def map_filter_reduce(lst, f1, f2, f3):
    import functools
    
    r1 = filter(f1, lst)
    r2 = list(map(f2, r1))
    r3 = functools.reduce(f3, r2)
    
    return r3

def evaluate(a,x):
    
    return list(map(lambda l: l[1] * (x ** l[0]), enumerate(a)))


def rearrange(l):
    i = 0
    for el in l:
        if el <= 0:
            tmp = el
            l.remove(el)
            l.insert(i, tmp)
            i += 1
            
    return l
    
    

    
def generator(intlist):
    result = []
    for el in intlist:
        for i in range(el[0], el[1] + 1):
            result.append(i)
            yield result
    
def get_composites(n):
    primes_to_n = []
    for i in range(2, n+1):
        c = True
        for x in range(2, i):
            if i % x == 0:
                c = False
                
        if c == True:
            primes_to_n.append(i)
                
    def fu(n):
        if n not in primes_to_n:
            return n
        
    return iter(filter(fu, list(range(2, n+1))))
    


def shorten(suffixes, base):
    def shawty(n):
        
        try:
            int(n)
        except:
            return str(base)
        
        selected_suf = 0
        result = 0
        
        for suf in suffixes:
            if n / base >= 1:
                selected_suf += 1
                result = int(n / base)
                
        return "{} {}".format(result, suffixes[selected_suf])
    
    return shawty


def solve_sudoku(board):
    solved = board.copy()
    amt_of_zeros_per_row = []
    
    
    for ind, row in enumerate(board):
        flag = 0
        for index, el in enumerate(row):
            if el == 0:
                flag +=1
                
        amt_of_zeros_per_row.insert(ind, flag)
        
        
    for ind, row in enumerate(solved):
        lst = []
        lst2 = []
        for index, el in enumerate(row):
            if amt_of_zeros_per_row[ind] == 1:
                if el != 0:
                    lst.append(el)
                    continue
            elif amt_of_zeros_per_row >1:
                if el != 0:
                    lst2.append((el, index))
        
            
            
                
                    
        for i in range(1, 10):
            if i not in lst:
                num_to_add = i
                
        for index, el in enumerate(row):
            if amt_of_zeros_per_row[ind] == 1:
                if el == 0:
                    row[index] = num_to_add
                    num_to_add = 0
                    break
                
    
                
                    
                
        
                
    
    return solved
            
                
def summary_ranges(a_string):
    l_str = a_string.split(",")
    
    l_str = [int(x) for x in l_str]
    
    l_num = list(range(min(l_str), max(l_str) + 1))
    
    return l_num
    
    
    
    
    
    
    
    
    
    
    
