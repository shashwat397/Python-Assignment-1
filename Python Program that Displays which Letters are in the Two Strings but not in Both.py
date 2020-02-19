from collections import Counter
str1 = list(input("Please enter the first string"))
str2 = list(input("Please enter the second string"))
dict1 = Counter(str1)
dict2 = Counter(str2)
dictcommon = dict1&dict2
commonlist = list(dictcommon.elements())
print("The common element in the two string ",commonlist)
for i in commonlist:
    str1.remove(i)
    str2.remove(i)
print("First string after the removal of the common string",str1)
print("Second string after the removal of the common string",str2)