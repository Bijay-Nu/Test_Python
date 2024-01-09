names = {
    'name':'Bijay',
    'age':18,
    'address':'ktm,lalitpur'
}
lists=[18,24,6,7,12,34,4,6,720,19,23]
for i in names.values():
    lists.append(i)
rm_dup = list(tuple(set(lists)))
print(rm_dup)