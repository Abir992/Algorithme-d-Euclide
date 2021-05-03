############### QUESTION 1
def pgcd(a,b):
    
    while a%b != 0:
        a,b = b , a%b
    return "le pgcd c'est :",b
    
pgcd(2322,654)

Affichage :
("le pgcd c'est :", 6)

############### QUESTION 2
def bezout(a,b):
    r1 = a 
    r2 = b 
    u1 = 1
    v1 = 0
    u2 = 0
    v2 = 1
    while r1%r2 != 0 :
        q = r1//r2
        r1 , r2 = r2 , r1%r2
        u1 , v1 , u2 , v2 = u2 , v2 , u1 - q*u2 , v1-q*v2
    print("Bezout",(a,b),"#PGCD:",r2,"(u=" , u2 ,") *",b,"+ (v=" ,v2,") *",a," = ",r2)

bezout(2016,1600)

Affichage :

Bezout (2016, 1600) #PGCD: 32 (u= -23 ) * 1600 + (v= 29 ) * 2016  =  32
