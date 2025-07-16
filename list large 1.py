l=[]
print("Enter integer to the list:")
while True:
    ele=int(input())
    l.append(ele)
    print("Is this the last element?(y/n):")
    flag=input()
    if flag=="y":
        break
print("List:",l)
print("Largest value in list l is:",max(l))
