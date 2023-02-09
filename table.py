from tabulate import tabulate

table = [
["Chrizz", "Aribal", 18],
["Raven", "Mayol", 19]
]

head = ["First Name", "Lastname", "Age"]
table_ = tabulate(table, headers = head, tablefmt = "grid")

print(table_)