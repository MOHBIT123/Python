
t=input("please enter a text to display each word seperated:")
t=t.strip()
copy =t
t2=list(t)
k=0
f=False
for i in range(0,len(t2)):
 if t2[i]!=" ":
   k=0
 if t2[i]==" ":
   k+=1
 if k>1:
   t2[i]=""
   f=True
t="".join(t2)
if f==True:
 print("corrected text:\n",t)
 
c=t.count(" ")
old=0
s=0
for i in range(0,c+1):
 s=t.find(" ")
 if s==-1:
  print(t[old:])
  break
 w_1=t[old:s]
 w_1= w_1.strip()
 print(w_1)
 t=t.replace(w_1+" ","",1)
