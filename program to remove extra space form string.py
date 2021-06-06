#bilo milo siko
#0123456789abcd
t=input("please enter a text to display each word seperated")
t=t.strip()
copy =t
t2=list(t)
k=0
for i in range(0,len(t2)):
 if t2[i]!=" ":
   k=0
 if t2[i]==" ":
   k+=1
 if k>1:
   t2[i]=""
   #k=1
print(t2)
l="".join(t2)
print(l)

