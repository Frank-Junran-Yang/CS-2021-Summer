from blackjack import Card, Deck, Player, Game
import csv

class Hello:
    def __init__(self,deck,name):
        self.deck=deck
        self.name=name
        
    def __str__(self):
        return self.deck + self.name
    
    def __repr__(self):
        return self.deck + self.name

def main():
    user=Player('Frank')
    game=Game(user)
    game.turn()
    d=Deck()
    print(d.cards)
    d.shuffle()
    a=d.cards
    b=[]
    for i in a:
        b.append(i)
    print(b)
    print(type(b))
    with open('cards.csv', 'w',newline='',encoding="utf-8") as file:
        csv_writer = csv.writer(file, delimiter =',')
        csv_writer.writerow(['5♦'])
    
    data = []
    with open('cards.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            data.append(row)
    game=Hello(name='Frank',deck=data)
    print(game())


    # player = Player('Daniyar')
    # new_game = True

    # while (new_game):
    #     game = Game(player)
    #     next_card = True
    #     while (next_card):
    #         print('test')
    #         game_continue = game.turn()
    #         print('test')
    #         if (not game_continue):
    #             break


    #         x = input('Do you want to take a card (y/n): ')
    #         if (x == 'n' or x=='N' or x=='no' or x=='NO'):
    #             next_card = False
    
    #     payoff = game.stop()
    #     print('You won: $' + str(payoff))
    #     print('You know have $' + str(player.money))
        
    #     x = input('do you want to play another game (y/n): ')
    #     if (x == 'n' or x=='N' or x=='no' or x=='NO'):
    #         new_game = False

    # print('Thank you for visiting 4Schoolers BlackJack')
    # print('You now have: $' + str(player.money))


if __name__ == '__main__':
    main()