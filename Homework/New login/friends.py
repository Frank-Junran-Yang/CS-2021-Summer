import csv

def friendslist(username,ndata):
    for row in ndata:
        if username[0][0]==row[0]:
            a=row
            a.remove(username[0][0])
    return a
def main():
    ndata=[]
    with open('friends.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            ndata.append(row)
    print(ndata)
    username=[]
    with open('login.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            username.append(row)
    print(username[0])
    print('Here is all users:')
    for pair in ndata:
        print(pair[0])
    
    new=input('Which user do you want to add: ')
    hello=False
    hi=True
    for row in ndata:
        if new==row[0]:
            hello=True
            # for row in ndata:
            #     if username[0][0]==row[0]:
            #         for jk in row:
            #             if new==jk:
            #                 print('Already have this friend')
            #                 break
                    # for kj in ndata:
                    #     if username[0][0]==kj[0]:
                    #         a=kj
                    #         a.remove(username[0][0])
                    # for ii in a:
                    #     if new ==ii:
                    #         hi=False
                    # if hi:
                        
                        # row.append(new)
                        # with open('friends.csv', 'w',newline='') as file:
                        #     csv_writer = csv.writer(file, delimiter =',')
                        #     for row in ndata:
                        #         csv_writer.writerow(row)
                    # else:
                    #     print('Already have this friend')
                    #     break
    already=True
    if hello:
        for row in ndata:
            if username[0][0]==row[0]:
                for jk in row:
                    if new==jk:
                        print('Already have this friend')
                        already=False
                        break
        if already:
            for row in ndata:
                if username[0][0]==row[0]:
                    row.append(new)
                    with open('friends.csv', 'w',newline='') as file:
                        csv_writer = csv.writer(file, delimiter =',')
                        for row in ndata:
                            csv_writer.writerow(row)
    if hello==False:
        print('The user does not exist')    
    for row in ndata:
        if username[0][0]==row[0]:
            a=row
            a.remove(username[0][0])
    # print(a)
    view=input('Do you want to view all your friends: ')
    if view=='yes':
        print(a)




if __name__ == '__main__':
    main()