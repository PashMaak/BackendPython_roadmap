import csv

sales = {}
with open("/home/anush/Desktop/Zypl/BackendPython_roadmap/2.Python/Week2/CSV-Analys/sales.csv", "r") as file:
    listbek = csv.DictReader(file)

    for row in listbek:
        product = row["product"]
        cnt = int(row["amount"])

        if product in sales:
            sales[product] += cnt
        else:
            sales[product] = cnt

arr = list(sales.items())

for i in range(len(arr)):
    for j in range(len(arr) - 1):
        if arr[j][1] < arr[j + 1][1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Top 3 products:")

for i in range(min(3, len(arr))):
    print(arr[i][0], "-", arr[i][1])