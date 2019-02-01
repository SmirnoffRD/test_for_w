symbols = []
with open("symbols.txt", "r") as file:
    # for line in file:
    symbols.append(file.read())
    print(type(symbols[0]))

list_of_symbols = list(symbols[0])
set_of_simbols = set(list_of_symbols)
print(set_of_simbols)
# for symbol in 