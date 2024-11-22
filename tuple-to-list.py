tuple1 = ('apple', 'banana', 'orange', 'mango', 'guava', 'grapes', 'pineapple', 'papaya', 'dragonfruit')
print("This is a tuple:",tuple1)
print(len(tuple1))
i = 0
lst = []
while i < len(tuple1):
    lst.append(tuple1[i])
    i = i + 1
print("The tuple has converted to a list:",lst)
