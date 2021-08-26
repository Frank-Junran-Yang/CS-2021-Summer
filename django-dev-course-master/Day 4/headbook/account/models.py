from django.db import models


class Account(models.Model):
    name = models.CharField(max_length  = 30)
    login = models.CharField(max_length  = 30)
    password = models.CharField(max_length  = 30)
    picture = models.ImageField(upload_to = 'profile_pictures/', null = True, blank = True)
    def __str__(self):
        return self.login
    def __repr__(self):
        return self.login

class Friendship(models.Model):
    person = models.ForeignKey(Account, on_delete = models.CASCADE)
    friends = models.ManyToManyField(Account, related_name = 'friendship_friends')
    def __str__(self):
        return '{}: {}'.format(str(self.person), ','.join([str(e) for e in (self.friends.all())]))
    def __repr__(self):
        return '{}: {}'.format(str(self.person), ','.join([str(e) for e in (self.friends.all())]))