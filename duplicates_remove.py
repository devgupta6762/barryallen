numbers=[3,4,3,5]
new=[]
for x in numbers:
    if x not in new:
        new.append(x)
print(new)
