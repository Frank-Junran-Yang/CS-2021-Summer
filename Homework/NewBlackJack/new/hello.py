import csv

class User:
    def __init__(self, username, password, first_name, last_name):
        self.username = username #username
        self.password = password # password
        self.first_name = first_name # String
        self.last_name = last_name # String

    def __str__(self):
        return 'My name is '+ self.first_name

    def __repr__(self):
        return 'My name is '+ self.first_name

    def add(self):
        #TODO: check if user in database
        with open('users.csv', 'a', newline='') as file:
            csv_writer = csv.writer(file, delimiter = ',')
            csv_writer.writerow([self.username, self.password, self.first_name, self.last_name])
        
        return 'Hello'

Frank=User(username='Frank',password=123,first_name='Junran',last_name='Yang')

print(Frank.add())

