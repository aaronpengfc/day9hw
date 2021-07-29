
dic = {"A001":["gummy bear", 20],"A002":["ice bar" , 25],"A004":["instant noodles" , 10],"A006":["soda" , 30]}
def sel_2(code):
    h = input("your objects name:")
    n = int(input("your objects price:"))
    print(h)
    print(n)
    dic[code] = [h,n]
while True:
    print(dic)
    a = int(input("the items code:1\nstop:2\nyour number:"))
    print(a)
    if a==1:
        q = input("code:")
        print(q)
        if q in dic:
            print(dic[q])
        else:
            print("there isn't this object")
            x = sel_2(q)
            print(x)
    elif a==2:
        break
        
            
            