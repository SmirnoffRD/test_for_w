def min_count_of_symbol(number_of_symbols, file_name):
    symbols = []
    rdy_list = []
    with open(file_name, "r") as file:
        # for line in file:
        symbols.append(file.read())
    dict_of_symbols = {}
    list_of_symbols = list(symbols[0])
    set_of_simbols = set(list_of_symbols)

    for symbol in set_of_simbols:
        dict_of_symbols.update({symbol: symbols[0].count(symbol)})

    while len(dict_of_symbols) > number_of_symbols:
        largest_k = ''
        largest = 0
        for key, value in dict_of_symbols.items():
            if value > largest:
                largest_k = key
                largest = value
        del dict_of_symbols[largest_k]
    for key in dict_of_symbols: 
        rdy_list.append(key)
    return rdy_list

print(min_count_of_symbol(8, 'symbols.txt'))
