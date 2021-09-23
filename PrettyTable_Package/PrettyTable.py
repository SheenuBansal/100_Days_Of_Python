from prettytable import PrettyTable,from_csv

x = PrettyTable()
# horizontal alignment and vertical alignment
x.add_column("Country", ["Asia", "Africa"], align="l", valign="b")
x.add_column("Area", [23, 34])
print(x)


y = PrettyTable(["City", "Famous_sweet"])
y.padding_width = 1
y.add_row(["KKP", "Dhodha"])
y.add_row(["FDK", "Soan Papdi"])
print(y)


z = PrettyTable(["City 2", "Famous_item 2"])
z.align = "l"                     # Aligning to the left
z.add_row(["KKP", "Dhodha"])
z.add_rows([
    ["FDK", "Soan Papdi"],
    ["GJ", "Dhokla"],
    ["Ajmer", "Papads"]
])  # Adding Multiple Rows
z.sortby="City 2"   # Sorting the Data
print(z)


q = PrettyTable(["City 3", "Famous_sweet 3"])
# The first row containing the headings will not be printed
q.header = False
q.padding_width = 2               # width/space of 2 between column edges and contents
q.add_row(["KKP", "Dhodha"])
q.add_row(["FDK", "Soan Papdi"])
q.border = False                # Border of Table to be kept or removed.
print(q)

# Taking data from CSV File
with open("E:\\100_days_of_Python\\PrettyTable_Package\\csv_file.txt") as obj :
    req_table=from_csv(obj)
    print(req_table)

with open("E:/100_days_of_Python/PrettyTable_Package/csv_file.txt") as obj1 :
    req_table1=from_csv(obj1)
    req_table1.align="l"
    req_table1.padding_width=3

    print(req_table1)

    # If you don't want to print table, just get the format how print(x) means the table will look, use x.get_string()
    print(req_table1.get_string(fields=["Name","City"]))
    print(req_table1.get_string(start=1,end=3))
    print(req_table1.get_string(sortby="Name"))     # Sorting a table temporary

    # Setting HTML attributes
    print(req_table1.get_html_string(attributes={"name":"my_table", "class":"red_table"}))
