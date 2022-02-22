#comparing the contents between two lists.
#1st method
list1=['cat','dog','panda','tiger'] 
list2=['tiger','lion','monkey','cat'] 
 
intersection=[i for i in list1 if i in list2] 
 
print(intersection)  

#2nd method
list_1=[10,20,30,40,10] 
list_2=[10,20,89,8,10] 
l=[] 
for i in list_1: 
    if i in list_2 and i not in l: 
        l.append(i) 
print(l) 