import csv
import codecs

def create(reviews, filename):
    with open(filename, 'w',newline='',encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=['user', 'rating','relevant', 'developer'])
        writer.writeheader()
        for i in reviews:
            writer.writerow(i)

