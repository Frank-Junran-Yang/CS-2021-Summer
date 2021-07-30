import csv
import register
import login
import dashboard
import blackmain
import blackjack
import friends
import viewmoney
import money

def main():
    name='username'
    choice=input('Do you want to login or register: ')
    if choice=='register':
        print('hello')
        register.main()
        hi=input('')
    elif choice=='login':
        if login.main():
            print('Choices:')
            print('Blackjack','Friends','Check Account','View Users and Change Password',"Check Friends' Money")
            hello=input('What do you want to do next: ')
            if hello=='Blackjack':
                blackmain.main()
            elif hello=='Friends':
                friends.main()
            elif hello=='Check Account':
                money.main()
            elif hello=='View Users and Change Password':
                dashboard.main()
            elif hello=="Check Friends' Money":
                viewmoney.main()
            else:
                print('You did not follow the instructions, so you need to go over through all these things again!')
    else:
        print('You lost your chance!')

    # hello=input('Do you want to register: ')
    # if hello=='yes':
    #     print('hello')
    #     register.main()
    # hi=input('Do you want to login: ')
    # if hi=='yes':
    #     if login.main():
    #         dashboard.main()
    #         play=input('Do you want to play blackjack: ')
    #         if play=='yes':
    #             blackmain.main()

    #         view=input('Do you want to check your account')
    #         if view=='yes':
    #             money.main()

    #         addfriend=input('Do you want add friends: ')
    #         if addfriend=='yes':
    #             friends.main()

                
    #         checkmoney=input('Do you want to see your friends money: ')
    #         if checkmoney=='yes':
    #             viewmoney.main()
        

if __name__ == '__main__':
    main()