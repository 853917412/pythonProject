# x = (2, 1, 0)
# print("".join('%s' %id for id in x))


x = [3,'a', 'b', 'c',True,True,False]
for i in range(len(x)):
    if type(x[i]) == bool:
        if x[i] is True:
            print(i)


