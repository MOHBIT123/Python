s="[12345,232234,545454545,3333334,7776676]"
x=list(s)
l=[""]
k=0
oldl=[""]
#this section used to join dgitis with each other in one element in the list
for i in range (1,len(x)):
    if x[i].isnumeric()==True and x[i]!=",":
     l[k]+=x[i]
    elif x[i]==",":   
     l.append("")
     k+=1
#this section used to convert string numerical elements to integer
for i in range(0,len(l)):
    if (l[i].isnumeric()==True):
     l[i]=int(l[i])#to convert each element in the list or array to integer
    print(l[i]," ")
#if we want to convert back to string we use "".join(l) function
p=0
c=0
for i in range(0,len(l)*2-1):
 if c==1 :   
  oldl.insert(i+1,",")
  c=0
 elif c==0 and p!=len(l) :
  oldl.append(str(l[p]))
  p+=1
  c=1
oldl.insert(0,"[")
oldl.insert (len(oldl)+1,"]")
print("".join(oldl))#to convert back sent data to string
#so now we have our data contained in a integer list and also we can convert back this list back string  

print(l[0])
print(l[1])
print(l[4])
