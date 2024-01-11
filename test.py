from prettytable import PrettyTable

table = PrettyTable(['Name', 'Age', 'City'])
table.add_row(['Alice', 25, 'New York'])
table.add_row(['Bob', 30, 'London'])
print(table)
