import csv
with open('movie.csv','w',newline='')as file:
    writer=csv.writer(file)
    writer.writerow(["SN","Movie","Rating"])
    writer.writerow([1,"got",5])
    writer.writerow([2,"friends",6])
with open('movie.csv')as csvfile:
    data=csv.reader(csvfile)
    for row in data:
        print(','.join(row))