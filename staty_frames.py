import pandas
staty = pandas.read_json("staty.json")
staty = staty.set_index("name")
# print(staty.index)
print(staty.loc["Czech Republic"])
print()
print(staty.loc[["Czech Republic"], ["area", "population"]])
print()
print(staty.loc["Czech Republic":"Dominican Republic"])