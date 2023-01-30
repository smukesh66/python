s="I AM A PYTHON PROGRAMMER!"
words=s.split()
l1=list(words)
l2=[]
for i in l1[::-1]:
    l2.append(i)
print(l2)
print("converting of string!")
strc=" "
for x in l2:
    strc+=' '+x
print(strc)
