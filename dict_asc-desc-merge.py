dict1 = {'b': 2, 'a': 1}
dict2 = {'d': 4, 'c': 3}


#ascending
sorted_asc = dict(sorted(dict1.items()))
print("Ascending:", sorted_asc)
#descending
sorted_desc = dict(sorted(dict1.items(), reverse=True))
print("Descending:", sorted_desc)


#Merge
merged_dict = {**dict1, **dict2}
print("Merged:", merged_dict)
