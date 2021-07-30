import random

class Card:
    def __init__(self, value, type):
        self.value = value
        self.type = type
    
    def __str__(self):
        signs = '♠♥♣♦'
        card = str(self.value)
        if self.value == 1:
            card = 'A'
        if (self.value == 13):
            card = 'K'
        if (self.value == 12):
            card = 'Q'
        if (self.value == 11):
            card = 'J'

        return card+signs[self.type]
    def __repr__(self):
        signs = '♠♥♣♦'
        card = str(self.value)
        if self.value == 1:
            card = 'A'
        if (self.value == 13):
            card = 'K'
        if (self.value == 12):
            card = 'Q'
        if (self.value == 11):
            card = 'J'

        return card+signs[self.type]

class Deck:
    def __init__(self):
        self.cards = [Card(i,j) for i in range(1,14) for j in range(0,4)]
    
    def __str__(self):
        return str(self.cards)

    def __repr__(self):
        return str(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)
        al=self.cards

    def deal(self):
        top = self.cards[0]
        self.cards.pop(0)
        return top

def decision(something):
    if choice=='Hit':
        n=d.deal()
        return n


def findv(n):
    g=str(n)
    if g[0]=='A':
        if value<=10:
            return 10
        else:
            return 1
    if g[0]=='J':
        return 10
    if g[0]=='Q':
        return 10
    if g[0]=='K':
        return 10

    b=int(g[0])
    return b


def main():
    hello=input('Do you want to start the game:')
    while hello!='yes':
        hello=input('Do you want to start the game:')
    d=Deck()
    print('original d',d)
    d.shuffle()
    print('d after shuffled',d)

    value=0

    player1=d.deal()
    dealer1=d.deal()
    player2=d.deal()
    dealer2=d.deal()

    print('Your cards: ')
    print(player1,player2)
    print('Your total value')
    value=findv(player1)+findv(player2)
    number=findv(dealer1)+findv(dealer2)
    print(value)
    print("Dealers's cards:")
    print('unknown',dealer2)
    if value==21:
        print ('You win')
        return
    else:
        choice=input('Do you want to Hit or Stick')
        if choice=='Hit':
            player3=decision(choice)
            value+findv(player3)
            print('Yours:')
            print(player1, player2, player3)
            print(value)
            print("Dealer's")
            dealer3=d.deal()
            print(dealer1,dealer2,dealer3)
            number+dealer3
            print(number)
            if number>21:
                print('You win')
                return
            if number==21:
                print('You lose')
                return
            if value==21:
                print ('You win')
        return
        if choice=='Stick':
            print('Yours:')
            print(player1, player2, player3)
            print(value)
            print("Dealer's")
            dealer3=d.deal()
            print(dealer1,dealer2,dealer3)
            number+dealer3
            print(number)
        if value==21:
            print('You win')
            return
        elif value>21:
            print('You lose')
            return
        else:
            choice=input('Do you want to Hit or Stick')
            player3=decision(choice)
            value=findv(player3)
            print(player1, player2, player3)
            print(value)

# print("Dealer's total value:")






# print('player1',player1)
# print('d after dealed',d)


# print('d after dealed again',d)
# print('e',e)



# print('Here is your card:')
# print(player1,player2)

