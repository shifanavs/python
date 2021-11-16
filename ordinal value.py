

list1=['aravind','aparna']
print("the original list:\n"+str(list1))
res=[ord(ele)for sub in list1 for ele in sub]
print("the ASCII list is:\n"+str(res))







output

the original list:
['aravind', 'aparna']
the ASCII list is:
[97, 114, 97, 118, 105, 110, 100, 97, 112, 97, 114, 110, 97]
>>> 

