class User:
    def __init__ (self,fname,lname,email,password):
        self.fname=fname
        self.lname=lname
        self.email=email
        self.password=password
    
    def __str__(self):
        return 'First Name:{}, Last Name: {}, Email: {}, Password: {}'.format(self.fname,self.lname,self.email,self.password)

    def __repr__(self):
        return 'First Name:{}, Last Name: {}, Email: {}, Password: {}'.format(self.fname,self.lname,self.email,self.password)