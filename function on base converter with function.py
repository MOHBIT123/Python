import sys 
def base_conversion (n=0,b=0,c=0):
   letters_base={'10':'A','11':'B','12':'C','13':'D','14':'E','15':'F','16':'G','17':'H','18':'I','19':'J','20':'K','21':'L','22':'M','23':'N','24':'O','25':'P','26':'Q','27':'R','28':'S','29':'T','30':'U','31':'V','32':'W','33':'X','34':'Y','35':'Z'}
   d=0
   q=1
   p=0
   t=""
   a=[""]
   new_val=[""]
   print("Note: In case of conversion(from d to base(n))this software can convert up to base 36 ")
   n=input("please enter a number :")
   while (b<=1)or(b>36)or(b==0):#to enter correct value or(b<=k)
     b=input("please enter the base of the entered number in range of(2 to 36) and bigger than the entered number:")
     b=int(b)
   while (c<=1)or(c>36)or(c==0): 
     c=input("please enter the base conversion base in range of (2 to 36):") 
     c=int(c)
   if b == 10: n=int(n) 
   else:
     n=str(n)
     n=int(n,b)
     if c!=10 :
       print("#In decimal =",n,"\n#In base ",b,"= ")
   if c == 10: print(n)#from base(n) to d
   else:               #from d to base(n)
    while q != 0: 
       q=int(n/c)
       d=(n -(q*c))
       digit= str(d)
       n=q
       if d>9:
        digit=letters_base[digit]# to access the elements of dictionary with a given key    
       t= digit+ t
       a.insert(p,digit)   
       p=p+1
   print("\n\n")
   for i in  range(0,len(a)-1):
      sys.stdout.write(t[i]) #used to dispay data on same line it only displays strings with the library (sys)
      sys.stdout.write(" ")
      sys.stdout.flush()
   print("\n\n")
#for i in  range(start,end,step): 
   for i in  range(0,len(a)-1):
      print(c,"^",i,": ",a[i])
   print("\n")

############################main program##############################
retry=""
while ((retry=="yes") or(retry=="y") or (retry=="Y") or (retry=="") or (retry=="Yes") or (retry=="yEs") or (retry=="yeS") or(retry=="YEs")or(retry=="yES")or(retry=="YeS")or(retry=="YES"))and((retry !="no")or(retry !="NO")or(retry !="No")or(retry != "nO")):
  base_conversion()
  retry=input("try again ?  please enter y or n : ")
else:
 print("invalid input please try again")
 
