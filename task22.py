def count_names(names: list[str]) -> dict[str, int] :
    result = {}
    
    for name in names:
        if name not in result.keys():
            result[name] = names.count(name)

    return result

names = ['ali', 'vali', 'sami', 'gani', 'vali', 'vali', 'sami', 'ali']
result = count_names (names=names)
print(result)