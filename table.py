from tabulate import tabulate

table = [
["Chrizz", "Aribal"],
["Raven", "Mayol"]
]

table_ = tabulate(table, tablefmt="grid")

print(table_)