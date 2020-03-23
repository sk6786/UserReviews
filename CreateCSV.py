import csv
import codecs

def create(reviews):
    with open('Reviews3.csv', 'w',newline='',encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=['user', 'relevant', 'developer'])
        writer.writeheader()
        for i in reviews:
            writer.writerow(i)

