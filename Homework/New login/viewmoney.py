import csv

def main():
    
    ndata=[]
    with open('friends.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            ndata.append(row)

    username=[]
    with open('login.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            username.append(row)
    print(username[0])


    for row in ndata:
        if username[0][0]==row[0]:
            a=row
            a.remove(username[0][0])
    print(a)
    
    data=[]
    with open('money.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            data.append(row)
    
    con=False
    which=input('Whose account do you want to visit: ')
    for row in a:
        if which == row:
            name=row
            con=True
    
    if con==True:
        for row in data:
            if name==row[0]:
                print(row[1])


if __name__ == '__main__':
    main()