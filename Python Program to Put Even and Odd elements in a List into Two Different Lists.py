odd = []
even = []
originallist = [1,2,3,4,5,6,7,8,9,10,11,11]
for i in originallist:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print(odd)
print(even)