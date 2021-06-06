def sprd(n=0):
 l=0
 digit =[]
 while n !=0:
     digit.insert(l,n%10)
     n//=10
     l +=1
 digit=list(reversed(digit))#we use the list() to convert back reversed data to list
 print(digit)
 return digit



x=sprd(23545458697888888888888888888888888877985879574387757435783457835789349758378493)
print(x)


