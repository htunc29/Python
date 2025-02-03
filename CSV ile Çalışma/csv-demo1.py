#user.csv
import csv

def add_user(firstname,lastname):
    with open("user.csv","a",encoding="utf-8",newline="") as file:
        csv_write=csv.writer(file)
        csv_write.writerow([firstname,lastname])
def get_users():
    with open("user.csv",encoding="utf-8") as file:
        csv_reader=csv.DictReader(file)
        for p in csv_reader:
            print(p)
add_user("Hüseyin","Tunç")
add_user("Bedirhan","Tunç")
def find_user(firstname,lastname):
    with open("user.csv") as file:
        csv_reader=csv.reader(file)
        for (index,row) in enumerate(csv_reader):
            if(row[0]==firstname and row[1]==lastname):
                print(index)
