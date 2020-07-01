string = input()
print("".join(["_" + i if i != i.lower() else i for i in string]))
