tmp = ([5], 11)
print(id(tmp[0]))

try:
    tmp[0].append(11)
except:
    print(tmp)



print(tmp)


print(False == False in [])


import dis

print(dis.dis("print(False == False in [])"))