import marcpy as mp
list = [5,2,6,3,7,8,3,2]
list2 = []
# list2 = list
for i in list:
    list2.append(i)
list2.sort()

# print(list)
# print(list2)

print("abs:", mp.abs_haeufigkeit(list))
print("rel:", mp.rel_haeufigkeit(list))
print("cum:", mp.kum_haeufigkeit(list))