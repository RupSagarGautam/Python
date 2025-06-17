# list

list = ["Hello","World","Python","Programming",1,2,3, True,False,2.4]
# print(list[:4])

list.append("HelloWorld")
# print(list)

# for item in list:
#     print(item,end=" ")
    
list.reverse()
# print(list,end=" ")
list2 = []
list2.insert(1,4)
list2.sort(reverse=True)
print(list2)

list3 =list + list2
print(f"list3 contains: {list3}")