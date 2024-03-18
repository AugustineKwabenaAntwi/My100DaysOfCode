heros=['spider man','thor','hulk','iron man','captain america']

print(len(heros))

heros.append("black panther")
print(heros)

del heros[-1]
heros.insert(3,"black panther")
print(heros)

heros[1:3]=["doctor strange"]
print(heros)

heros.sort()
print(heros)
