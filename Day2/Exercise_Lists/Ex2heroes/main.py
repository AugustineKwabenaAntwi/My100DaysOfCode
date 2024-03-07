heros=['spider man','thor','hulk','iron man','captain america']
len(heros)
heros.append("black panther")
print(heros)
del heros[-1]
print(heros)
heros.insert(2,"black panther")
print(heros)

heros[1:3]=["doctor strange"]
print(heros)

print(heros.sort())