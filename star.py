# triangle
def star(n):
    for i in range(1, n+1):
        print " "*(n-i) + "*"*i
star(5)
       

def star():
    for i in range(1, 6):
        print " "*(5-i) + "*"*i
star() 


# pyramid
def gugu(n):
    for i in range(1,n+1):
        print " "*(n-i) + "*"*(2*i-1) + " "*(n-i)

gugu(5)


def gugu(n):
    for i in range(1,n+1):
        print " "*(n-i) + "*"*(2*i-1)

gugu(5)


# wind
def gugu(n):
    for i in range(1,n+1):
        print " "*(i-1) + "*"*(n+1-i) + " "*(n-i) + "*"*(i)
    for j in range(1,n+1):   
        print "*"*(n+1-j) + " "*(j-1) + "*"*(j) + " "*(n-j)

gugu(5)


 # diamond
def gugu(n):
    for i in range(1,n+1):
        print " "*(n-i) + "*"*(2*i-1) 
    for j in range(1,n+1):   
        print " "*(j-1) + "*"*(2*n-2*j+1)
gugu(5)
    
