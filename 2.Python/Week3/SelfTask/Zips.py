from zipfile import ZipFile

# myzip = ZipFile("test.zip", "w")
FILE_PATH_1 = "home/anush/Desktop/Zypl/BackendPython_roadmap/2.Python/Week3/SelfTask/1.txt"
FILE_PATH_2 = "home/anush/Desktop/Zypl/BackendPython_roadmap/2.Python/Week3/SelfTask/2.txt"
ZIP_PATH = "/home/anush/Desktop/Zypl/BackendPython_roadmap/2.Python/Week3/SelfTask/test.zip"

with ZipFile(ZIP_PATH, "r") as myzip:
    print(myzip.namelist())
    print(myzip.read(FILE_PATH_1).decode("utf-8"))
    myzip.extractall("2.Python/Week3/SelfTask/")


'''
1)
from zipfile import ZipFile

# myzip = ZipFile("test.zip", "w")
FILE_PATH_1 = "/home/anush/Desktop/Zypl/BackendPython_roadmap/2.Python/Week3/SelfTask/1.txt"
FILE_PATH_2 = "/home/anush/Desktop/Zypl/BackendPython_roadmap/2.Python/Week3/SelfTask/2.txt"
ZIP_PATH = "/home/anush/Desktop/Zypl/BackendPython_roadmap/2.Python/Week3/SelfTask/2.txt"

with ZipFile("ZIP_PATH", "w") as myzip:
    myzip.write(FILE_PATH_1)
    myzip.write(FILE_PATH_2)

    print(str(myzip.namelist()))

2)
from zipfile import ZipFile

# myzip = ZipFile("test.zip", "w")
FILE_PATH_1 = "home/anush/Desktop/Zypl/BackendPython_roadmap/2.Python/Week3/SelfTask/1.txt"
FILE_PATH_2 = "home/anush/Desktop/Zypl/BackendPython_roadmap/2.Python/Week3/SelfTask/2.txt"
ZIP_PATH = "/home/anush/Desktop/Zypl/BackendPython_roadmap/2.Python/Week3/SelfTask/test.zip"

with ZipFile(ZIP_PATH, "r") as myzip:
    print(myzip.namelist())
    print(myzip.read(FILE_PATH_1).decode("utf-8"))

3)

from zipfile import ZipFile

# myzip = ZipFile("test.zip", "w")
FILE_PATH_1 = "home/anush/Desktop/Zypl/BackendPython_roadmap/2.Python/Week3/SelfTask/1.txt"
FILE_PATH_2 = "home/anush/Desktop/Zypl/BackendPython_roadmap/2.Python/Week3/SelfTask/2.txt"
ZIP_PATH = "/home/anush/Desktop/Zypl/BackendPython_roadmap/2.Python/Week3/SelfTask/test.zip"

with ZipFile(ZIP_PATH, "r") as myzip:
    print(myzip.namelist())
    print(myzip.read(FILE_PATH_1).decode("utf-8"))
    myzip.extract(FILE_PATH_1, "2.Python/Week3/SelfTask/")

4)

from zipfile import ZipFile

# myzip = ZipFile("test.zip", "w")
FILE_PATH_1 = "home/anush/Desktop/Zypl/BackendPython_roadmap/2.Python/Week3/SelfTask/1.txt"
FILE_PATH_2 = "home/anush/Desktop/Zypl/BackendPython_roadmap/2.Python/Week3/SelfTask/2.txt"
ZIP_PATH = "/home/anush/Desktop/Zypl/BackendPython_roadmap/2.Python/Week3/SelfTask/test.zip"

with ZipFile(ZIP_PATH, "r") as myzip:
    print(myzip.namelist())
    print(myzip.read(FILE_PATH_1).decode("utf-8"))
    myzip.extractall("2.Python/Week3/SelfTask/")

'''