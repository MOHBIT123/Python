def base_conversion (n="k",b="k",c="k"):
 print("this software can take input from within the function of or by entering its 3 argumnets(number,base of number,conversion base)")
 retry=""
 while True :
  if((retry=="yes") or(retry=="y") or (retry=="Y") or (retry=="") or (retry=="Yes") or (retry=="yEs") or (retry=="yeS") or(retry=="YEs")or(retry=="yES")or(retry=="YeS")or(retry=="YES")):
   import sys 
################################################################################################################variable assigning and declarations#################################################################################################################3
   letters_base={'10':'A','11':'B','12':'C','13':'D','14':'E','15':'F','16':'G','17':'H','18':'I','19':'J','20':'K','21':'L','22':'M','23':'N','24':'O','25':'P','26':'Q','27':'R','28':'S','29':'T','30':'U','31':'V','32':'W','33':'X','34':'Y','35':'Z'}                  
   d=0                                                                                                                                                                                                                                                                                     
   q=1                                                                                                                                                                                                                                                                         
   p=0
   t=""
   a=[""]
   new_val=[""]
   ff=0
   count=0
###############################################################parameters interring section#######################################################
   print("Note: In case of conversion(from d to base(n))this software can convert up to base 36 ")
   if n =="k":#this part for entering the main value and check if user did enter it from main program or didn't
    n=input("please enter a number :")

   while True:#this part for to check the base of entered number for error

    if b=="k":#this subpart to enter value of b in case user didn't in main function
      print("Note: In case of conversion(from d to base(n))this software can convert up to base 36 ") 
      b=input("please enter the base of the entered number in range of(2 to 36) and bigger than the entered number:")

    while str(b).isnumeric()== False:#this subpart to check if entered consist of only numerical values
      print("base error the entered base is not correct",b,"try again!!!") 
      b=input("please enter new valid number")

    while((int(b)<=1)or(int(b)>36)):#this subpart to enter correct value for b
      print("base error entered number out of range")  
      print("Note: In case of conversion(from d to base(n))this software can convert up to base 36 ") 
      b=input("please enter the base of the entered number in range of(2 to 36) and bigger than the entered number:")

    f1=1#when number in range f1=1

    if f1==1 and str(b).isnumeric()== True:#when entered number is correct break from loop
     break     

   while True:#this part to check if entered number is correct

      if int(b)<=10:#this subpart to check if base is smaller than or equal to 10 if yes check if any non numeric character is entered
       f=str(n).isnumeric()
       if f==False:
        print("base error the entered number is not valid in the entered base (valid digits in base",b," are from 0 to",int(b)-1,") try again!!!") 
        n=input("please enter new valid number: ")
       elif f==True:
        break

      elif int(b)>10:#this subpart to check if base is bigger than 10 if yes check if any character is out of range 
          print(max(str(n).upper()))
          #b=16
          for k,v in letters_base.items():     
            if v==max(str(n).upper()):
              o=list(letters_base.keys())[(int(k)-10)]
              break
          if (str(n).isnumeric()== True )or( int(o)<int(b)) : break
          elif int(o)>=int(b):
           print("base error the entered number is not valid in the entered base (valid digits in base",b," are from 0 to",letters_base[str(int(b)-1)],") try again!!!")
           n=input("please enter a valid number: ")
          
   while True:#this part as the b part but for conversion base

    if c=="k":
      print("Note: In case of conversion(from d to base(n))this software can convert up to base 36 ")
      c=input("please enter the base conversion base in range of (2 to 36):") 

    while str(c).isnumeric()== False:
      print("base error the entered base is not correct",c,"try again!!!") 
      c=input("please enter new valid number")

    while int(c)==b:
      print("entered base is equal to conversion base please try again!!!")
      c=input("please enter the base conversion base in range of (2 to 36):") 

    f11=1

    while((int(c)<=1)or(int(c)>36)): 
      print("base error entered number out of range")
      print("Note: In case of conversion(from d to base(n))this software can convert up to base 36 ")
      c=input("please enter the base conversion base in range of (2 to 36):") 
    f22=1

    if f11==1 and f22==1 and str(c).isnumeric()==True: 
      break
    f11=0
    f22=0

########################################this part is for base conversion##############################################
   c=int(c)
   if b == 10: n=int(n) 
   else:
     #n=str(n)
     hh=n
     n=int(str(hh),int(b))
     if c!=10 :
       print("#In decimal =",n,"\n#In base ",c,"= ")
   if c == 10: print(n)#from base(n) to d
   else:               #from d to base(n)
    while q != 0:
       #print(c) 
       q=int(n//c)
       d=(n -(q*c))
       digit= str(d)#
       #d=0
       n=q
       if d>9:
         digit=letters_base[digit]# to access the elements of dictionary with a given key
       count+=1
       if count==3:
        count=0
        t=","+t
       t= digit+ t#############
       a.insert(p,digit)   
       #digit=0
       p=p+1
   
###############################this part for displaying data###############################################################
   #for i in  range(start,end,step):

   for i in  range(0,len(t)):
      sys.stdout.write(t[i]) #used to dispay data on same line it only displays strings with the library (sys)
      sys.stdout.write(" ")
      sys.stdout.flush()
   print("\n\n")
    
   for i in  range(0,len(a)-1):
      print(c,"^",i,": ",a[i])
   print("\n")
  elif  ((retry =="no")or(retry =="NO")or(retry =="No")or(retry == "nO")or(retry=="n")or(retry=="N")):
   break
  else:
   print("invalid input please try again")
  n="k"
  b="k"
  c="k"
  retry=input("try again ?  please enter y or n : ") 
############################main program##############################
base_conversion()
#base_conversion(n=10,b=10,c=2)
