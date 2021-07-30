from blackjack import Card, Deck, Player, Game
import csv

# player pays $100 to play a game
# they get $500 if sum = 21
# they get $300 if sum = 20
# they get $200 if sum = 19
# they get $150 if sum = 18
# they get $50 if sum = 17
# they get $10 if sum = 16



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
    # print(data)
    # print(n[0][0])
    for row in data:
        # print(row)
        # print(row[0])
        if n[0][0]==row[0]:
            ammount=int(row[1])
            break
    player = Player(name=n[0][0],money=ammount)
    print(player.name)
    print(player.money)
    new_game = True

    while (new_game):
        game = Game(player)
        next_card = True
        while (next_card):
            game_continue = game.turn()
            if (not game_continue):
                break


            x = input('Do you want to take a card (y/n): ')
            if (x == 'n' or x=='N' or x=='no' or x=='NO'):
                next_card = False
    
        payoff = game.stop()
        print('You won: $' + str(payoff))
        print('You know have $' + str(player.money))
        
        x = input('do you want to play another game (y/n): ')
        if (x == 'n' or x=='N' or x=='no' or x=='NO'):
            new_game = False

    print('Thank you for visiting 4Schoolers BlackJack')
    print('You now have: $' + str(player.money))
    print(player.money)
    ndata=[]
    with open('money.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            ndata.append(row)

    for row in ndata:
        if player.name==row[0]:
            row[1]=player.money

    with open('money.csv', 'w',newline='') as file:
        csv_writer = csv.writer(file, delimiter =',')
        for row in ndata:
            csv_writer.writerow(row)



if __name__ == '__main__':
    main()