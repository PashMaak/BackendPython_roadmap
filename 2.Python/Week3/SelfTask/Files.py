import csv

FILE_PATH = "/home/anush/Desktop/Zypl/BackendPython_roadmap/2.Python/Week3/SelfTask/yo.csv"

with open(FILE_PATH, "r", newline="") as file:
    reader = csv.reader(file)
    dic = dict((name, int(score)) for name, score in reader)
    print(dic)
