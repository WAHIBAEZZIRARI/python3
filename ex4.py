n=int(input("entre un nombre entie possitif"))
if n<0: 
    print("veuilley entre un nombre entier possitif")
else:
    resultat=1
    for i in range (1,n+1):
        resultat*=i
    print("la factrielle de",n, "=", resultat)

