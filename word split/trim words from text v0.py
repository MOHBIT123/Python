#bilo milo siko
#0123456789abcd
t=input("please enter a text to display each word seperated")
t=t.strip()
c=t.count(" ")
old=0
s=0
x=0
for i in range(0,c+1):
 s=t.find(" ")
 if s==-1:
  print(t[old:])
  break
 w_1=t[old:s]
 w_1.strip()
 print(w_1)
 #w_2=w_1+"*"
 #w_11=w_1+" "
 t=t.replace(w_1+" ",w_1+"*",1)
 old=s+1
