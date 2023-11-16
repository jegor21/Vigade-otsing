import math #oli parandatud
print("Ruudu karakteristikud")
a=int(input("Sisesta ruudu külje pikkus => ")) #oli parandatud
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P) #oli parandatud 
di=a*math.sqrt(2) #oli parandatud 
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud") #oli parandatud 
b=int(input("Sisesta ristküliku 1. külje pikkus => ")) #oli parandatud 
c=int(input("Sisesta ristküliku 2. külje pikkus => ")) #oli parandatud 
S=b*c
print("Ristküliku pindala", S) #oli parandatud 
P=2*(b+c) #oli parandatud 
print("Ristküliku ümbermõõt", P)
di=math.sqrt(b*2+c*2)  
print("Ristküliku diagonaal", round(di)) #oli parandatud 
print()
print("Ringi karakteristikud")
r=int(input("Sisesta ringi raadiusi pikkus => ")) #oli parandatud 
d=2*r #oli parandatud 
print("Ringi läbimõõt", d)
S=math.pi*r**2 #oli parandatud 
print("Ringi pindala", round(S))
C=2*math.pi*r #oli parandatud 
print("Ringjoone pikkus", round(C)) #oli parandatud 
