import csv
from blackjack import Card, Deck, Player, Game


def main():
    n=[]
    with open('login.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            n.append(row)
    data = []
    with open('money.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            data.append(row)


    for row in data:
        if row[0]==n[0][0]:
            print('You have',row[1],'$ in your account')

    add=input('Do you want to deposit or withdraw money: ')
    if add=='deposit':
        ammount=input('How much do you want to deposit: ')
        for row in data:
            if row[0]==n[0][0]:
                print(row[1])
                print(ammount)
                row[1]=int(row[1])+int(ammount)
                print('Now you have',row[1],'$ in your account')
                with open('money.csv', 'w',newline='') as file:
                    csv_writer = csv.writer(file, delimiter =',')
                    for row in data:
                        csv_writer.writerow(row)
    
    if add=='withdraw':
        ammount=input('How much do you want to withdraw: ')
        for row in data:
            if row[0]==n[0][0]:
                print(row[1])
                print(ammount)
                row[1]=int(row[1])-int(ammount)
                print(row[1])
                print('Now you have',row[1],'$ in your account')
                with open('money.csv', 'w',newline='') as file:
                    csv_writer = csv.writer(file, delimiter =',')
                    for row in data:
                        csv_writer.writerow(row)
                
        






if __name__ == '__main__':
    main()