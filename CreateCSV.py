import csv

def create(reviews):
    with open('Reviews.csv', 'w',newline='') as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=['user', 'relevant', 'developer'])
        writer.writeheader()
        for i in reviews:
            writer.writerow(i)

