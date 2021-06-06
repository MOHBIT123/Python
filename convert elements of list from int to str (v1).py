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
     l.append(",")   
     l.append("")
     k+=2
#this section used to convert string numerical elements to integer
l.insert(0,"[")
l.insert (len(l)+1,"]")
for i in range(0,len(l)):
    if (l[i].isnumeric()==True):
     l[i]=int(l[i])#to convert each element in the list or array to integer
    print(l[i])
#if we want to convert back to string we use "".join(l) function
for i in range(0,len(l)):
 #if str(l[i]).isnumeric()==True:
  oldl.append(str(l[i]))
 #oldl[i]=str(l[i])
olds="".join(oldl)#to convert back sent data to string
print(olds)
#so now we have our data contained in a integer list and also we can convert back this list back string  
