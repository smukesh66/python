def length(str):
    lis=list(str.split(" "))
    return len(lis[-1])
str=input("Enter the string to find the last word count")
print("The length of last word is",length(str))
